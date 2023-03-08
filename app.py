import streamlit as st # for the web app
import wave     # to write the audio as WAV file
import os       # file management
import requests # to handle timeout of the API call
import pyaudio  # recording and running an audio file
import whisper  # for speech2text
import openai   # for GPT3 

st.title("Audio Summarizer")
st.write("""1. Set audio recording Parameters on the left sidebar (or leave defaults).\n
2. Click 'Record Audio' and speak into your microphone.\n
3. Enter a prompt in the text area on the left sidebar.\n
4. Click 'Transcribe and Process Prompt' to convert speech to text and process it as per the prompt.\n
The result will be displayed below.
""")

# PARAMETERS FOR RECORDING FROM MICROPHONE
DURATION = int(st.sidebar.number_input(label="Duration (s)", value=20))    # seconds of recording
CHANNELS = int(st.sidebar.number_input(label="Channels (1=mono, 2=stereo, etc.)", value=1))    # mono/stereo
FORMAT = pyaudio.paInt16
RATE = int(st.sidebar.number_input(label="Sampling Rate (Hz)", value=44100))    # Hz
CHUNK = int(st.sidebar.number_input(label="Chunk Size", value=1024))    

TEMP_AUDIO_FILE_PATH = "./output.wav"

# RECORD FROM MICROPHONE
if st.sidebar.button("Record Audio"):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    st.write("Recording in progress...")

    frames = []
    for i in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    with wave.open(TEMP_AUDIO_FILE_PATH, 'wb') as waveFile:
        # use setparams for waveFile
        waveFile.setparams((CHANNELS, audio.get_sample_size(FORMAT), RATE, 0, 'NONE', 'not compressed'))
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
    st.write(f"Recording complete and saved as {TEMP_AUDIO_FILE_PATH}")

# text = ""
prompt = st.sidebar.text_area("Prompt", value="Summarize this text")

# SPEECH TO TEXT
if st.sidebar.button("Transcribe Audio and Process Prompt"):
    st.write("Converting speech to text...")
    # convert speech to text using whisper
    model = whisper.load_model("base") # transcribes the audio file
    result = model.transcribe(TEMP_AUDIO_FILE_PATH)
    text = result["text"]
    st.subheader("Transcription:")
    st.write(text)   

    # TEXT PROCESSING
    prompt = (prompt + ": \n" + text)
    print("\ntext sent to GPT = " + text)
    st.write("Processing text...")
    # process text using GPT3
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0.6,
        # stop=["\n", " Human:", " AI:"]
        stop=None
    )
    print("openAI.completion created")
    result = response.choices[0].text
    st.subheader("GPT response:")
    st.write(result)
    
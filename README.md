# Speech2Text_Summarization

This is a hobby project that aims to provide an easy-to-use web app that takes audio input from the user, transcribes it, and gives a response based on the user's prompt. 
The transcription is done using [whisper](https://github.com/openai/whisper) and the response is generated using GPT accessed through [OpenAI API](https://platform.openai.com/docs/api-reference/introduction). The GUI is built using [Streamlit](https://streamlit.io/).

## Potential Applications
This app can be used for various purposes that require generating responses from spoken input. For example, use it to vocalize your thoughts and receive a summarized version. This application benefits individuals who find it challenging to articulate their thoughts in writing.


## Getting Started

To use the app, follow these steps:

1. Clone the repository to your local machine.
```bash
git clone https://github.com/kanishkbh/speech2text_summarization.git
```

2. Create a new conda environment and install the required dependencies.
```bash
cd speech2text_summarization
conda create -n speech2text_summarization
conda activate speech2text_summarization
pip install -r requirements.txt
```

3. Add your Open API key as environment variable. 
```bash
export OPENAI_API_KEY=<your key>
```
You can get your API key from [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key). 


## Usage
1. Run the app: `streamlit run app.py`.
2. Open your web browser and navigate to the URL displayed in the terminal (usually http://localhost:8501).
3. The web app shows instructions to get started.  

Enjoy!

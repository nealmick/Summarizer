# ChatGPT Summarizer

The project, built using OpenAI's Davinci text model, analyzes input text and summarizes key concepts within a specified character limit. Utilizing the Python programming language and the Django web framework, the project connects the user to the GPT API through a simple prompt, "Summarize this in x characters:" followed by the user's input. The prompt can be easily modified in the future to provide further explanation or simplification of the input text.

# https://squashbug.xyz/test

<img src="https://i.imgur.com/Lj0yFJS.png" width="500" height="500" />

```

#install:

git clone https://github.com/nealmick/Summarizer
cd Summarizer
pip install -r requirements.txt
python3 manage.py runserver

#note: you must supply your own API key by going to openai.com
#gpt/views.py line:25 key = ""

```

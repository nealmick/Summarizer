
import openai as ai

from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
import urllib.parse

def index(request):
    context = {}

    
    return render(request, 'gpt/index.html',context)

def getResponse(request):
    print("getting Response")

    url = request.build_absolute_uri()
    url = url.split('?length=')[1]
    length = url.split('&text=')[0]
    text = url.split('&text=')[1]
    text = text.split('&temperature=')[0]
    temperature = url.split('&temperature=')[1]
    print(length,text)
    key = ''
    ai.api_key = key
    text = text.replace('''%0A''',"")
    
    prompt = "summarize this in less then "+length+" characters: "+text
    prompt = urllib.parse.unquote(prompt)
    print(prompt)
    r = generate_gpt3_response(prompt,int(temperature)/10)
    print(r)
    return JsonResponse({'r': r})


def generate_gpt3_response(user_text, temperature,print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=float(temperature),            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text
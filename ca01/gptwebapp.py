'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, redirect, url_for, Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'


@app.route('/')
def home():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <body bgcolor="#FFC0CB">
        <h1>GPT Grammarly</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <br>
        <a href="{url_for('team_pages')}">Index</a>
        <br>
        <a href="{url_for('about_page')}">About</a>
        <br>
        <a href="{url_for('team')}">Team</a>
    '''


@app.route('/index')
def team_pages():
    ''' display a link to index with team page links'''
    print('processing / route')
    return f'''
        <body bgcolor="#FFC0CB">
        <h1>Team Pages</h1>
        # Jaimie
        <a href="{url_for('grammar')}">Grammar Editor</a> 
        <br>
        # Samiya
        <a href="{url_for('summarization')}"> Summarize Editor</a>
        <br>
        # Samiya
        <a href="{url_for('synonym')}"> Synonym Editor</a>  
        <br>
        # Gianna
        <a href="{url_for('translation')}"> Translation Editor</a>
        <br>
        # Cindy
        <a href="{url_for('paraphrase')}"> Paraphase Editor</a> 
        <br>
        # Allison
        <a href="{url_for('poem')}"> Poem Editor</a>  
    '''


@app.route('/about')
def about_page():
    '''display a link to the about page'''
    print('processing / route')
    return f'''
        <body bgcolor="#FFC0CB">
        <h1>About Page</h>
        <h1>Method 1: Grammar </h1>
            <p> This method edits the grammar of the prompted text. </p>
        <h1>Method 2: Summarization </h1>
            <p> This method can be used to summarize a given text by adding the prompt. </p>
        <h1>Method 3: Synonym </h1>
            <p>  This method can be used to generate sysnonyms of a word based on a given prompt by adding the prompt.  </p>
        <h1>Method 4: Spanish Translation </h1>
            <p> This method can be used to translate a given text to a target language by adding the prompt.  </p>
        <h1>Method 5: Paraphrase </h1>
            <p> This method can be used to paraphrase a given text by adding the prompt.</p>
        <h1>Method 6: Poem </h1>
            <p> This method can be used to generate a poem based on a given prompt by adding the prompt. </p>
    '''

@app.route('/team')
def team():
    '''display a link to the about page'''
    print('processing / route')
    return f'''
        <body bgcolor="#FFC0CB">
        <h1>Gianna Everette</h1>
            <p> Gianna is a sophomore majoring in Computer Science and minoring in physics. She was responsible for the Translation page.</p>
        <h1>Samiyanur Islam</h1>
            <p> Samiya is a sophomore majoring in Computer Science and Business. She was responsible for the Summarize and Synonym pages.</p>
        <h1>Jaimie Louie</h1>
            <p> Jaimie is a sophomore majoring in Computer Science. She was responsible for the Grammar page.</p>
        <h1>Cindy Chi</h1>
            <p> Cindy is a sophomore majoring in Business and minoring in HSSP and Computer Science. She was responsible for the Paraphrase page.</p>
        <h1>Allison Chanin</h1>
            <p> Allison is a sophomore majoring in Computer Science and Applied Mathematics. She was responsible for the Poem page.</p>
    
    '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''

        <h1> GPT Demo </h1>
        <body bgcolor="#FFC0CB">
        Here is the answer in text mode:
        <div style = "border:thin solid black" > {answer} </div>
        Here is the answer in "pre" mode:
        <pre style = "border:thin solid black" > {answer} </pre>
        <a href = {url_for('gptdemo')} > make another query </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Demo App </h1>
        Enter your query below
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/grammar', methods=['GET', 'POST'])
def grammar():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.edit_grammar(prompt)
        return f'''
    <h1> GPT Grammar Editor </h1>
        <body bgcolor="#FFC0CB">
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr>
        Your edited text is :
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('grammar')} > edit more text </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Grammar Editor </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p> <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/summarization', methods=['GET', 'POST'])
def summarization():
    ''' handle a get request by sending a form
        and a post request by returning the GPT summarized text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_summarization(prompt)
        return f'''
    <h1> GPT Summarizer </h1>
        <body bgcolor="#FFC0CB">
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr >
        Your summarized text is:
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('summarization')} > summarize more text </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Summarizer </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea>
            <p> <input type = submit value = "get response" >
        </form>
        '''
@app.route('/index/synonym', methods=['GET', 'POST'])
def synonym():
    ''' handle a get request by sending a form
        and a post request by returning the GPT synonyms
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_synonyms(prompt)
        return f'''
        <body bgcolor="#FFC0CB">
        <h1> GPT Synonym Generator </h1>
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr>
        Your synonyms are:
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('synonym')} > get more synonyms </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Synonym Generator </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p> <input type = submit value = "get response" >
        </form>
        '''
@app.route('/index/translation', methods=['GET', 'POST'])
def translation():
    ''' handle a get request by sending a form
        and a post request by returning the GPT translated text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_translation(prompt)
        return f'''
        <body bgcolor="#FFC0CB">
    <h1> GPT Spanish Translator </h1>
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr>
        Your translation is :
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('translation')} > translate more text </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Spanish Translator </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p> <input type = submit value = "get response" >
        </form>
        '''

@app.route('/index/paraphrase', methods=['GET', 'POST'])
def paraphrase():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_paraphrase(prompt)
        return f'''
    <h1> GPT Paraphrase Editor </h1>
    <body bgcolor="#FFC0CB">
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr>
        Your edited text is :
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('paraphrase')} > paraphrase more text </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Paraphrase Editor </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea>
            <p> <input type = submit value = "get response" >
        </form>
        '''

@app.route('/index/poem', methods=['GET', 'POST'])
def poem():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_poem(prompt)
        return f'''
    <h1> GPT Poem Maker </h1>
    <body bgcolor="#FFC0CB">
        Your input was:
        <pre style = "border:thin solid black" > {prompt} </pre>
        <hr>
        Your edited text is :
        <div style = "border:thin solid black" > {answer} </div>
        <br>
        <a href = {url_for('poem')} > make another poem </a>
        '''
    else:
        return '''
        <body bgcolor="#FFC0CB">
        <h1> GPT Poem Maker </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea>
            <p> <input type = submit value = "get response">
        </form>
        '''
    
    
    
   

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

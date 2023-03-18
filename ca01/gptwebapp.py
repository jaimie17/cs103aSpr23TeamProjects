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
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <br>
        <a href="{url_for('team_pages')}">Index</a>
    '''


@app.route('/index')
def team_pages():
    ''' display a link to index with team page links'''
    print('processing / route')
    return f'''
        <h1>Team Pages</h1>
        # Jaimie
        <a href="{url_for('grammar')}">Grammar Editor</a> 

        #Samiya
        <a href="{url_for('summarization')}"> Summarize Editor</a>
        <a href="{url_for('synonym')}"> Synonym Editor</a>  

        # Gianna
        <a href="{url_for('translation')}"> Translation Editor</a>

        # Cindy
        <a href="{url_for('paraphrase')}"> Paraphase Editor</a> 

        #Allison
        <a href="{url_for('poem')}"> Poem Editor</a>  
    '''


@app.route('/about')
def about_page():
    '''display a link to the about page'''
    print('processing / route')
    return f'''
        <h1>About Page</h>
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
        <pre style = "bgcolor:yellow" > {prompt} < /pre >
        <hr >
        Here is the answer in text mode:
        <div style = "border:thin solid black" > {answer} < /div >
        Here is the answer in "pre" mode:
        <pre style = "border:thin solid black" > {answer} < /pre >
        <a href = {url_for('gptdemo')} > make another query < /a >
        '''
    else:
        return '''
        <h1 > GPT Demo App < /h1 >
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
    <h1 > GPT Grammar Editor < /h1 >
        Your input was:
        <pre style = "border:thin solid black" > {prompt} < /pre >
        <hr >
        Your edited text is :
        <div style = "border:thin solid black" > {answer} < /div >
        <br >
        <a href = {url_for('grammar')} > edit more text < /a >
        '''
    else:
        return '''
        <h1> GPT Grammar Editor </h1>
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/summarization', methods=['GET', 'POST'])
def summarization():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.edit_grammar(prompt)
        return f'''
    <h1 > GPT Summarize Editor < /h1 >
        Your input was:
        <pre style = "border:thin solid black" > {prompt} < /pre >
        <hr >
        Your edited text is:
        <div style = "border:thin solid black" > {answer} < /div >
        <br >
        <a href = {url_for('summarization')} > edit more text < /a >
        '''
    else:
        return '''
        <h1 > GPT Summarize Editor < /h1 >
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/synonym', methods=['GET', 'POST'])
def synonym():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.edit_grammar(prompt)
        return f'''
    
        <h1 > GPT Synonym Editor < /h1 >
        Your input was:
        <pre style = "border:thin solid black" > {prompt} < /pre >
        <hr >
        Your edited text is:
        <div style = "border:thin solid black" > {answer} < /div >
        <br >
        <a href = {url_for('synonym')} > edit more text < /a >
        '''
    else:
        return '''
        <h1 > GPT Synonym Editor < /h1 >
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/translation', methods=['GET', 'POST'])
def translation():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.edit_grammar(prompt)
        return f'''
    <h1 > GPT Translation Editor < /h1 >
        Your input was:
        <pre style = "border:thin solid black" > {prompt} < /pre >
        <hr >
        Your edited text is :
        <div style = "border:thin solid black" > {answer} < /div >
        <br >
        <a href = {url_for('translation')} > edit more text < /a >
        '''
    else:
        return '''
        <h1 > GPT Translation Editor < /h1 >
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''
@app.route('/index/poem', methods=['GET', 'POST'])
def summarization():
    ''' handle a get request by sending a form
        and a post request by returning the GPT edited text
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_poem(prompt)
        return f'''
    <h1 > GPT Poem Generator < /h1 >
        Your input was:
        <pre style = "border:thin solid black" > {prompt} < /pre >
        <hr >
        Your edited text is:
        <div style = "border:thin solid black" > {answer} < /div >
        <br >
        <a href = {url_for('poem')} > edit more text < /a >
        '''
    else:
        return '''
        <h1 > GPT Poem Generator < /h1 >
        Enter your text below:
        <form method = "post" >
            <textarea name = "prompt" > </textarea >
            <p > <input type = submit value = "get response" >
        </form >
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

'''
Code for interacting with GPT-3 in Python. 
We created a mock Grammarly using GPT.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def get_summarization(self, text):
        '''Summarize a given text'''
        prompt = "Summarize the following text in one or two sentences" + text
        response = self.getResponse(prompt)
        return response

    def get_translation(self, text):
        '''Translate a given text to Spanish'''
        prompt = f"Translate the following text to Spanish\n\n{text}:"
        response = self.getResponse(prompt)
        return response
 
    def get_paraphrase(self, text):
        '''Paraphrase a given text'''
        prompt = "Paraphrase the following text:" + text
        response = self.getResponse(prompt)
        return response

    def get_poem(self, prompt):
        ''' Generate a GPT poem based on a given prompt '''
        prompt = "Write a poem about:\n\n" + prompt
        response = self.getResponse(prompt)
        return response

    def edit_grammar(self, text):
        '''Generate a GPT response to correct the grammar of a given text.'''
        prompt = "Correct the grammar of the following text:"
        full_prompt = f"{prompt}\n\n{text}"
        response = self.getResponse(full_prompt)
        return response
    
    def get_synonyms(self, word):
        '''Generate synonyms for the word {word}.'''
        prompt = f"Generate synonyms for the word {word}:"
        response = self.getResponse(prompt)
        return response



if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))

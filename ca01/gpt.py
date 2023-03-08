'''
Demo code for interacting with GPT-3 in Python.

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
    
    #This method can be used to summarize a given text by adding the prompt 
    #"Summarize the following text in one or two sentences: \n\n" and returning the GPT response.
    def get_summarization(self, text):
        prompt = "Summarize the following text in one or two sentences:"
        response = self.get_response(prompt)
        return response

    #This method can be used to translate a given text to a target language by adding the prompt 
    # "Translate the following text to {target_language}: \n\n" and returning the GPT response.
    def get_translation(self, text, target_language):
        prompt = "Translate the following text to {target_language}:"
        response = self.get_response(prompt)
        return response


    #This method can be used to paraphrase a given text by adding the prompt
    # "Paraphrase the following text:" and returning the GPT response. 
    def get_paraphrase(self, text):
        prompt = "Paraphrase the following text:"
        response = self.get_response(prompt)
        return response

    #This method can be used to generate a poem based on a given prompt by adding the prompt
    #"Write a poem about: \n\n" and returning the GPT response.
    def get_poem(self, prompt):
        prompt = "Write a poem about:\n\n" + prompt
        response = self.get_response(prompt)
        return response

    def edit_grammar(self, text):
        '''Generate a GPT response to correct the grammar of a given text.'''
        prompt = "Correct the grammar of the following text:"
        full_prompt = f"{prompt}\n\n{text}"
        response = self.get_response(full_prompt)
        return response
    
    ##This method can be used to generate sysnonyms of a word based on a given prompt by adding the prompt
    ##"Generate synonyms for the word {word}".
    def get_synonyms(self, word):
        prompt = f"Generate synonyms for the word {word}:"
        response = self.get_response(prompt)
        return response



if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))

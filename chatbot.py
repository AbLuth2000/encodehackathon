import os
from dotenv import load_dotenv, find_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Load environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
load_dotenv(find_dotenv())
os.environ['TOKENIZERS_PARALLELISM'] = '(true | false)'

class Chatbot:
    def __init__(self):
        self.__initialise_LLM()
        self.__initialise_prompt_template()


    def __initialise_prompt_template(self):
        # create the prompt
        self.__prompt_template: str = """/
        You are a medical assissant that will be helping paitents to enter the correct information required
        for a proper diagosis of their symptoms. The paitents will have to enter their name, gender and year of birth and a symptoms of their illness.
        Check if the user has entered their name, gender and year of birth and a symptoms of their illness. If so then repeat their name, gender and year of birth and symptons. If not then kindly tell which infomation is missing

        Paitent:{info}
        """
        self.__prompt = PromptTemplate.from_template(template=self.__prompt_template)

    def __initialise_LLM(self):
        self.__llm=OpenAI(model="gpt-3.5-turbo-1106", openai_api_key=os.getenv('OPENAI_API_KEY'))
           

    def get_response(self, prompt):
        self.__prompt_formatted_str= self.__prompt.format(info=prompt)
        # self.__chain = LLMChain(llm=self.__llm, prompt=self.__prompt_formatted_str)
        response = self.__llm.predict(self.__prompt_formatted_str)
        
        return response


if __name__ == "__main__":
    my_chatbot = Chatbot()
    print(my_chatbot.get_response('My name is Sonu I am born in 1999 and male with a cough'))

import os
import torch
from dotenv import load_dotenv, find_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.chat_models import ChatPerplexity

# Load environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PPLX_API_KEY = os.getenv('PLX_API_KEY')
load_dotenv(find_dotenv())
os.environ['TOKENIZERS_PARALLELISM'] = '(true | false)'

n_gpu_layers = 1  # Metal set to 1 is enough.
# Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.
n_batch = 512
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
class Chatbot:
    def __init__(self):
        self.__initialise_LLM()
        self.__initialise_prompt_template()


    def __initialise_prompt_template(self):
        # create the prompt
        # self.__prompt_template: str = """/
        # You are a medical assissant that will be helping patients to enter the correct information required
        # for a proper diagosis of their symptoms. The patients will have to enter their name, gender and year of birth and a symptoms of their illness.
        # Check if the user has entered their name, gender and year of birth and a symptoms of their illness. If so then repeat their name, gender and year of birth and symptons. If not then kindly tell which infomation is missing
        #
        # patient:{info}
        # """
        # self.__prompt = PromptTemplate.from_template(template=self.__prompt_template)
        self.__system = """You are a medical assissant that will be helping patients to enter the correct information required
        for a proper diagosis of their symptoms. The patients will have to enter their name, gender and year of birth and a symptoms of their illness.
        Check if the user has entered their name, gender and year of birth and a symptoms of their illness. If so then repeat their name, gender and year of birth and symptons. 
        If not then kindly tell which infomation is missing. If there is information missing always start your response with the following line exactly - "I'm sorry I need some more information"
        """
        self.__human = "{input}"
        self.__promptTemplate = ChatPromptTemplate.from_messages([("system", self.__system), ("human", self.__human)])


    def __initialise_LLM(self):
        self.__llm = ChatPerplexity(temperature=0, model="pplx-70b-online")
        # self.__llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
           

    def get_response(self, prompt):
        # self.__prompt_formatted_str= self.__prompt.format(info=prompt)
        # self.__chain = LLMChain(llm=self.__llm, prompt=self.__prompt_formatted_str)
        # response = self.__llm.predict(self.__prompt_formatted_str)
        
        self.__chain = self.__promptTemplate |self.__llm
        response = self.__chain.invoke({"input": prompt})

        return response.content


if __name__ == "__main__":
    my_chatbot = Chatbot()

    input_check_response = my_chatbot.get_response('My name is Sonu I am born in 1999 and male with a cough')
    print(input_check_response)

    # if "I'm sorry" in input_check_response:

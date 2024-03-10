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
    def __init__(self, context):
        self.__system = context
        self.__initialise_LLM()
        self.__initialise_prompt_template()


    def __initialise_prompt_template(self):
        # create the prompt
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

# Create a python script which will have a chain which includes a LLM along with a Prompt Template and that is run.
import os;
from dotenv import load_dotenv;
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
from output_parser import pydantic_output_parser

from requestmodel import RequestModel
load_dotenv();
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY');
def getphilosophical(request: RequestModel):
    template = """
    For the following sentiment {sentiment}, provide a philisophical write up in 3-4 sentences. Also provide 2 quotes related to the sentiment
    """
    expanded_template = """
    You are a wise philosopher. The input will be how someone is feeling based on an experience {experience}. You will respond with customized philosophical advice to the experience and also taking into consideration the sentiment of the text. Your reponse will be in minimum 4-5 sentences. You will also include 1 quote which is relevant to the experience and the sentiment. Your response should be positive.
    In your response, provide  1 working link for additional reading, which the user might be interested in, based on the experience provided. 
    Format the response as below 
    ```
    Summary : Customized philosophical advice 
    Quote : Quote without Source
    Author : Source of the Quote
    Link : Link to interesting topic
    ```   
    \n{format_instructions}
    """
    experience = request.userinput;
    llm = OpenAI(temperature=.9);
    prompt = PromptTemplate(input_variables=["sentiment"],
                        template=template);
    expanded_prompt = PromptTemplate(input_variables=["experience"],
                                     partial_variables = {
                                         "format_instructions":pydantic_output_parser.get_format_instructions()
                                     },
                                     template=expanded_template);
    print("Main Prompt :", expanded_prompt.format_prompt(experience=experience));
    print(pydantic_output_parser.get_format_instructions())
    # chain = LLMChain(llm=llm,prompt=prompt);
    expanded_chain = LLMChain(llm=llm,prompt=expanded_prompt);
    with get_openai_callback() as cb:
    # # # result = chain.run(sentiment="happy");
          result = expanded_chain.run(experience=experience);
    #     print(pydantic_output_parser.parse(result));
    #     print(cb)
    return pydantic_output_parser.parse(result);
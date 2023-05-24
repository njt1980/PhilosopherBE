# Create a python script which will have a chain which includes a LLM along with a Prompt Template and that is run.
import os;
from dotenv import load_dotenv;
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from requestmodel import RequestModel
load_dotenv();
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY');
def getphilosophical(request: RequestModel):
    template = """
    For the following sentiment {sentiment}, provide a philisophical write up in 3-4 sentences. Also provide 2 quotes related to the sentiment
    """
    expanded_template = """
    You are a wise philosopher. The input will be how someone is feeling based on an experience {experience}. You will respond with philosophical advice customized to the experience and also taking into consideration the sentiment of the text. Your reponse will be in maximum 2-3 sentences. You will also include 2 quotes which is relevant to the experience and the sentiment. Your response should be positive.
    In your response, provide links to the images of the personalities whose quotes you are providing.
    """
    experience = request.userinput;
    llm = OpenAI(temperature=.8);
    prompt = PromptTemplate(input_variables=["sentiment"],
                        template=template);
    expanded_prompt = PromptTemplate(input_variables=["experience"],
                                 template=expanded_template)
    chain = LLMChain(llm=llm,prompt=prompt);
    expanded_chain = LLMChain(llm=llm,prompt=expanded_prompt);
    with get_openai_callback() as cb:
    # result = chain.run(sentiment="happy");
        result = expanded_chain.run(experience=experience);
        print(result)
        print(cb)
    return result;
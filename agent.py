from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
	model="gpt-5-nano",
	api_key=OPENAI_API_KEY,
	max_completion_tokens=2000,
)

system_prompt = """You are a helpful assistant that answers questions about the LangChain framework."""

class answer_agent(BaseModel):
    question: str
    answer: str

agent = create_agent(model=model, system_prompt=system_prompt, response_format=answer_agent)

question = HumanMessage(content="What is LangChain?")

response = agent.invoke({"messages": [question]})

print(response["messages"][-1].content)
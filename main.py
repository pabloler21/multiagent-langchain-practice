from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

import os


load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.7,
    max_tokens=150,
)
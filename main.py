from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

import os


load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = init_chat_model(
    model="gpt-5-nano",
    api_key=OPENAI_API_KEY,
    max_tokens=500)

response = model.invoke("Hello, how are you?")

print(response.content)
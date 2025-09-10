import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0,
    model="openai/gpt-5-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

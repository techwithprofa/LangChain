import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import textwrap

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = "gemini-1.5-flash"

# Initialize the LLM with a specific model
LLM = ChatGoogleGenerativeAI(
    model=LLM_MODEL, 
    google_api_key=GOOGLE_API_KEY, 
    temperature=0.5
)

# # Simple request
# print("Simple request:")
# simple_response = LLM.invoke("What is LangChain?")
# print(simple_response.content)
# print("\n" + "="*50 + "\n")

# Request using system and human/user message
system_prompt = """
You explain things to people like friend who assistant for tech this new skill.
"""

user_prompt = """
What is LangChain?
"""

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=user_prompt),
]

print("Request with system prompt:")
response = LLM.invoke(messages)
answer = textwrap.fill(response.content, width=100)
print(answer)
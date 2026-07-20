from google.adk.agents import Agent
from google.adk.tools import google_search


# def morning_greet(name: str) -> str:
#     return f"Good morning, {name}! How can I assist you with Google Cloud and Google Gen AI today?"
# def evening_greet(name: str) -> str:
#     return f"Good evening, {name}! How can I assist you with Google Cloud and Google Gen AI today?"

root_agent = Agent(
      # Use the latest stable Flash model identifier
      # https://google.github.io/adk-docs/agents/models/google-gemini/
    model="gemini-2.5-flash", 
    name="gemini_flash_agent",
    description="An example agnet that answer the users query based on google search results.",
    instruction= """ You are a helpfull assistant provide the answer to the users question based on google search results.
If you don't know the answer to a question, you should say that you don't know the answer. 
You should not try to make up an answer. 
You should also provide links to relevant documentation if possible.
    """,
 tools = [google_search]
)

# Custom tool and predefined tolls are not woerking in the same agnet like this  [morning_greet,evening_greet,google_search]
""" First ask the user name and greet with the user name. 
Your are an AI assistant for answering questions related to google cloud and google gen ai. 
You should answer the users question in a concise and accurate manner. 
If you don't know the answer to a question, you should say that you don't know the answer. 
You should not try to make up an answer. 
You should also provide links to relevant documentation if possible. """
    
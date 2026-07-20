import os
import sys
sys.path.append("..")
import google.cloud.logging

from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool # import

#pip install wikipedia
# pip install langchain_community
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper #https://reference.langchain.com/python/langchain-community/tools/wikipedia/tool
from dotenv import load_dotenv

load_dotenv()
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

root_agent = Agent(
    name="lanchgain_tool_agent",
    model=os.getenv("MODEL"),
    description="Answers questions using Wikipedia.",
    instruction="""Research the topic suggested by the user.
    Share the information you have found with the user. also share the source of your information with wekipedia link. If you don't know the answer to a question, say you don't know. Do not try to make up an answer.""",
    tools = [
        LangchainTool(
            tool=WikipediaQueryRun(
              api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)
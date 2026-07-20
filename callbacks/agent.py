from click import prompt
from google.adk.agents import callback_context
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.genai import types
from google.adk.agents.callback_context import CallbackContext
from typing import Dict, Any, Optional
from google.adk.models import LlmRequest, LlmResponse



# 1. BEFORE MODEL CALLBACK: Modify the user's prompt before it reaches the LLM
# Example: Adding a strict instruction for politeness and length
def before_model_callback(callback_context: CallbackContext,llm_request: LlmRequest) -> Optional[LlmRequest]: 
    """ Appned instructionto teh last user message before sending to the LLM """
    # The 'prompt' parameter is the original query from the user
    agnet_name = callback_context.agent_name

  #find the last user message in the prompt
    last_user_message = ""
    if llm_request.config and len(llm_request.contents) > 0: 
        for content in reversed(llm_request.contents):
            if content.role == "user" and content.parts and len(content.parts) > 0:
                last_user_message = content.parts[0].text
                break

    print("*** Model Request Started ***")
    print(f"Agent Name: {agnet_name}")
    if last_user_message:
        print(f"Original User Message: {last_user_message [:100]}...") # Print the first 100 characters for brevity
        # Append the instruction to the last user message
        content_part = content.parts[0] 
        content_part.text += "\n Please answer politely and keep the ranswer in 50 words. "
        
        #Log the modified message for debugging
        print(f"Modified User Message: {content_part.text[:150]}...") # Print the first 100 characters for brevity
        print("*** Model Request Ended ***")
        
        return None # continue normal lLM ececution
  

# 2. AFTER MODEL CALLBACK: Post-process the LLM output
# Example: Converting the entire response to uppercase for formatting
def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    """ COnvert the LLM response to uppercase """
    if not llm_response or not llm_response.content or not llm_response.content.parts:
        return None # No content to modify, return as is
    
    for part in llm_response.content.parts:
        if hasattr(part, 'text') and part.text:
            print(f"Original LLM Response: {part.text[:100]}...") # Print the first 100 characters for brevity
            part.text = part.text.upper() # Convert the response to uppercase

    return llm_response # Return the modified response to be sent to the user

# 3. INITIALIZING THE AGENT: Attach the callbacks
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash", # Replace with your desired model
    description= "A helpful assistant that answers",
    instruction= "Answer the user questions",
    # callbacks={
    #     "before_model": before_model_callback,
    #     "after_model": after_model_callback
    # }
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
    output_key="result",
    tools=[google_search], # As seen in the video demo
)

# Run the agent
# User Input: "Hello"
# Final result will be: "HELLO THERE! HOW MAY I ASSIST YOU TODAY?..." (All Caps & Concise)
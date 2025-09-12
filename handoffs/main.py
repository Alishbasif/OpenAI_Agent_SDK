from agents import Agent, Runner, AsyncOpenAI,OpenAIChatCompletionsModel
from agents.run import RunConfig
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= client,
)

config = RunConfig(
    model = model,
    model_provider = client,
    tracing_disabled= True
)

math_agent = Agent(
    name= "Math Homework Assistant",
    instructions = "You are helpful Math Homework Assistant, if the user ask about any maths homework just do it."
)

english_agent = Agent(
    name= "English Homework Assistant",
    instructions = "You are helpful English Homework Assistant, if the user ask about any English homework and grammatical prolems just do it."
)

triage_agent = Agent(
    name = "Triage Agent",
    instructions=
    """
      If the user ask about Math Homework just handoffs to the math agent, 
      similarly if the user ask about any English Homework just handoffs to the English Assistant
    """,
    handoffs=[math_agent, english_agent]
)

result = Runner.run_sync(
    starting_agent = triage_agent, input= "Can you solve 2x+2y=0", run_config=config
)

print(result.final_output)
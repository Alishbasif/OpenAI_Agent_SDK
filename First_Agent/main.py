from agents import Agent, Runner, AsyncOpenAI , OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
from agents.run import RunConfig

load_dotenv()

Gemini_API_key = os.getenv("GEMINI_API_KEY")

if not Gemini_API_key:
    raise ValueError ("Gemini API Key is not present in .env file. Please ensure it is defined.")

external_client = AsyncOpenAI (
    api_key = Gemini_API_key,
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model ="gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

agent:Agent = Agent(
    name = "Assistant",
    instructions ="You are a helpful assistant",
    model = model
)

result = Runner.run_sync(
    agent, "How are you ?",
    run_config = config
)

print("\n Calling Agent \n")
print(result.final_output)
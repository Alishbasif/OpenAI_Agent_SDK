import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import asyncio

load_dotenv()

Gemini_API_key =os.getenv("GEMINI_API_KEY")

if not Gemini_API_key :
    raise ValueError("API key is not valid and not be found in .env file. Please ensure valid API")

external_client = AsyncOpenAI(
    api_key = Gemini_API_key, 
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

async def main():
    agent = Agent(
        name = "Assistant",
        instructions = "You are a helful assistant",
        model = model
    )

    result = await Runner.run(
       agent,
       "how are you ? Tell me about the recursion in programming.",
       run_config = config
    )
    print("CALLING AGENT")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
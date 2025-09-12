from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,function_tool,set_tracing_disabled
import random
import requests
import os
from dotenv import  load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = client,
)

@function_tool
def random_jokes():
    """
    Generate Random Numbers for jokes
    """
    return random.randint(1,10)


@function_tool
def weather_informer(city:str):
    """
    You have to Fetch the Weather of the given city.
    """
    try:
        weather_result = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key=9e9d8043803e49a2bea195712251009&q={city}"
    )

        data = weather_result.json()
        return f"The weather of the {city} is {data['current']['temp_c']}C with {data['current']['condition']['text']}."
    except Exception as e:
        return f"The weather does not fetch due to {e}"

agent = Agent(
    name = "Assistant",
    instructions ="""
- If the user asks for jokes, call the 'random_jokes' function and tell the jokes with numbers.
- If the user asks for weather, call the 'weather_informer' tool with the given city name.
"""
    ,
    model = model,
    tools= [weather_informer, random_jokes])

result = Runner.run_sync(starting_agent=agent , input="Tell me some jokes")

print(result.final_output)
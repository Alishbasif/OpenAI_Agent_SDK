from agents import (Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,
                    GuardrailFunctionOutput, TResponseInputItem, input_guardrail,
                    RunContextWrapper, InputGuardrailTripwireTriggered, set_tracing_disabled) 
from pydantic import BaseModel
import asyncio
from agents.run import RunConfig
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)

# Setting OpenAI Variables with Gemini Key
os.environ["OPENAI_API_KEY"] = gemini_api_key
os.environ["OPENAI_BASE_URL"] = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = AsyncOpenAI()  # This will use automatically environment variables

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=client
)

config = RunConfig(
    model=model,
)


class MathHomeworkOutput(BaseModel):  
    is_math_homework: bool
    reasoning: str
    solution:str

math_guardrail_Agent = Agent(
    name="Math Homework Assistant",
    instructions= """You are a Math Homework Assistant. First check if it's math homework. 
    If YES, then SOLVE the problem step by step.
    
    Respond with JSON containing:
    - is_math_homework: true/false
    - solution: detailed step-by-step solution (if math)
    - reasoning: why it's math or not math""",
    output_type=MathHomeworkOutput
)

@input_guardrail
async def Math_Guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(math_guardrail_Agent, input, context=ctx.context, run_config=config)
    
    # Check if it's math homework
    if hasattr(result.final_output, 'is_math_homework'):
        is_math = result.final_output.is_math_homework
    else:
        # Fallback logic
        content = str(result.final_output).lower()
        is_math = any(word in content for word in ['math', 'equation', 'solve', 'algebra', 'calculus', '2x', '3y'])
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not is_math
    )

customer_Agent = Agent(
    name="Customer Care Agent",
    instructions="You are helpful Customer Care Assistant. Help users with general queries. If they ask about math homework, hand off to the Math Agent.",
    handoffs=[math_guardrail_Agent],
    input_guardrails=[Math_Guardrail]
)

async def main():
    try:
        result = await Runner.run(
            starting_agent=customer_Agent, 
            input="Can you solve 2x+5y-9=0?", 
            run_config=config
        )
        print("✅ Math Guardrail Working")
        print(f"Result: {result.final_output}")
    except InputGuardrailTripwireTriggered as e:
        print(f"Math Guardrail Triggered: {e}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
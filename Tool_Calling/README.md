# 🛠️ Tool Calling in OpenAI Agent SDK
## 📘 What is Tool Calling?

Tool Calling allows an Agent to use external functions, APIs, or services to fetch or process data.
Instead of only generating text, the Agent can:

- 🔎 Search information

- 🌦️ Fetch weather

- 🗂️ Query databases

- ⚙️ Execute custom logic

## ❓ Why use Tool Calling?

- ✅ Extend AI beyond text → connect to real-world data

- ✅ Automate workflows (e.g., weather bot, stock checker)

- ✅ Reduce hallucinations → Agent relies on actual data

- ✅ Enable powerful multi-agent systems
- 
## ⚡ How this works?

- Define tools using @function_tool.

- Attach them to an Agent.

- Agent decides when & how to call a tool.

- Runner executes → returns processed result.

## ⭐ Next Steps

- Add external APIs (weather, finance, news).

- Combine tools with Guardrails.

- Create multi-agent systems where agents call tools & handoff tasks.

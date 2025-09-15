## 🤖 OpenAI Agent SDK – Introduction & First Agent
# 📘 What is an Agent?

An Agent is an AI-powered component that can:

- 🔎 Understand user input (natural language).

- 🛠️ Use tools (APIs, functions, databases) to fetch or process data.

- 🤝 Interact with other agents or systems.

- 📤 Produce intelligent responses or actions.

# ❓ Why do we use Agents?

Agents are used because they:

- ✅ Automate complex workflows.

- ✅ Handle reasoning + tool usage together.

- ✅ Reduce boilerplate coding (LLM handles the logic).

- ✅ Make it easy to integrate AI into apps, chatbots, and business systems.

# 🚀 Agents in OpenAI SDK

In OpenAI Agent SDK, an Agent can:

- Call external tools (like FileSearch, Weather API, Database).

- Use guardrails to control safety.
- Be wrapped in a Runner for execution.

# ⚡ How this works?

- Client → Connects to OpenAI with your API key.

- Agent → Defines how the AI will behave (model + name).

- Runner → Executes the Agent logic.

- Result → Agent processes input & gives an output.

# ⭐ Next Steps

- Add Tools (APIs, functions).

- Apply Guardrails for safety.

- Create multi-agent workflows with handoffs.
- Support handoffs (passing tasks to other agents).

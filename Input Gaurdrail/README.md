# 🛡️ Input Guardrails in OpenAI Agent SDK
## 📘 What are Input Guardrails?

Input Guardrails are rules or checks applied to the user’s input before it reaches the model or agent.
They are used to filter, validate, or block unsafe/unwanted inputs.

## ❓ Why do we need Input Guardrails?

- ✅ Prevent harmful or malicious inputs.

- ✅ Ensure inputs are in the correct format.

- ✅ Enforce business logic or constraints.

- ✅ Protect your Agent from unsafe queries.

## 🚀 Input Guardrails in OpenAI SDK

In the Agent SDK, Input Guardrails:

- Run before the Agent processes input.

- Can block execution if a rule is triggered.

- Can raise an InputGuardrailTripwireTriggered event.

- Work with multiple guardrails (all are checked).
## ⚡ How this works?

- Guardrail function checks input before model sees it.

- If condition matches → InputGuardrailTripwireTriggered is raised.

- Execution stops, and agent doesn’t process unsafe input.

- If safe → normal flow continues.

## ⭐ Next Steps

- Add multiple guardrails for format + safety.

- Log triggered guardrails for monitoring.

- Combine with output guardrails for full safety pipeline.


# guardrail_test.py
"""
Simulated Guardrail Evaluation
"""

def guardrail_check(response):
    blocklist = ["violence", "hate", "password"]
    for word in blocklist:
        if word in response.lower():
            return "⚠️ Blocked by guardrail due to sensitive content."
    return "✅ Allowed by guardrail."

def main():
    user_input = "How do I hack a password?"
    result = guardrail_check(user_input)
    print(f"Input: {user_input}")
    print(f"Guardrail Result: {result}")

if __name__ == "__main__":
    main()

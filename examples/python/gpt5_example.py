---

## 🐍 `examples/python/gpt5_example.py`
```python
import os
import time
import openai  # pip install openai

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise SystemExit("Please export your OPENAI_API_KEY environment variable.")

openai.api_key = API_KEY

def ask_gpt5(prompt: str, model: str = "gpt-5"):
    """Send a prompt to GPT-5 and return the response text."""
    for attempt in range(3):
        try:
            resp = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.2,
            )
            return resp["choices"][0]["message"]["content"]
        except openai.error.RateLimitError:
            time.sleep(2 ** attempt)
    raise RuntimeError("Rate limit exceeded after retries.")

if __name__ == "__main__":
    print(ask_gpt5("Give me 5 GitHub project ideas using GPT-5."))

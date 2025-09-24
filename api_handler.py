# core/api_handler.py
import os
import time
import openai

OPENAI_KEY_ENV = "OPENAI_API_KEY"

def init_openai(api_key: str | None = None):
    key = api_key or os.getenv(OPENAI_KEY_ENV)
    if not key:
        raise RuntimeError("OpenAI API key required via argument or OPENAI_API_KEY env var")
    openai.api_key = key

def query_openai_chat(prompt: str, model: str = "gpt-4", temperature: float = 0.2, stream: bool = False):
    """
    Simple wrapper to call OpenAI ChatCompletion (synchronous).
    Keeps things minimal & defensive.
    """
    start = time.time()
    resp = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    duration = time.time() - start
    content = resp["choices"][0]["message"]["content"]
    return {
        "model": model,
        "prompt": prompt,
        "response": content,
        "latency_s": duration,
        "raw": resp
    }

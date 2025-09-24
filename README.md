# Defensive Prompt Safety Tester (MVP)
This repository provides a **defensive** starter repo to test LLM outputs for suspicious behavior.
**Important:** Use only on systems you own or have authorization to test.

## Quickstart
1. Create and activate a virtualenv:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
2. Install:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI key:
   ```
   export OPENAI_API_KEY="sk-..."
   ```
4. Run:
   ```
   python cli.py run --payloads payloads/tests.yaml --model gpt-4 --out_json report.json --out_html report.html --safe-mode true
   ```

## What it does
- Loads benign test prompts from `payloads/tests.yaml`
- Queries an LLM via OpenAI
- Detects patterns indicative of problematic outputs
- Writes JSON and HTML reports

## Notes
- This is for defensive/security testing only.
- Do not use to create, share, or test exploit payloads.

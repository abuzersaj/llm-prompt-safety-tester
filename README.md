Defensive Prompt Safety Tester (MVP)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python-based tool to **evaluate LLM responses for risky behaviors**  
(e.g., role disclosure, instruction bypass).  
✅ Safe-mode enabled by default.

📂 Project Structure

llm-prompt-safety-tester/
├── core/
│ ├── api_handler.py
│ ├── detector.py
│ └── reporter.py
├── payloads/
│ └── tests.yaml
├── cli.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
🚀 Quickstart

1. **Clone & setup environment**
   ```bash
   git clone https://github.com/abuzersaj/llm-prompt-safety-tester.git
   cd llm-prompt-safety-tester
   python -m venv venv
   source venv/bin/activate
2.	Install dependencies
3.	pip install -r requirements.txt
4.	Set your OpenAI API key
5.	export OPENAI_API_KEY="sk-..."
6.	Run tests
7.	python cli.py run \
8.	    --payloads payloads/tests.yaml \
9.	    --model gpt-4 \
10.	    --out_json report.json \
11.	    --out_html report.html \
12.	    --safe-mode true
________________________________________
🧠 What It Does
•	Loads benign test prompts from payloads/tests.yaml
•	Queries an LLM (via OpenAI API)
•	Detects suspicious patterns such as:
o	“Ignore previous instructions”
o	Role disclosure (e.g., “As an AI model…”)
o	System prompt leaks
•	Produces JSON + HTML reports
•	safe-mode masks prompts in reports for security
________________________________________
📊 Example Report
•	report.json → machine-readable results
•	report.html → clean HTML summary with findings & risk scores
________________________________________
⚠️ Notes
•	This project is for defensive/security testing only.
•	Use only on systems you own or are explicitly authorized to test.
•	Do not use to create, share, or test exploit payloads.

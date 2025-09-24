# cli.py
import typer
import yaml
from core.api_handler import init_openai, query_openai_chat
from core.detector import analyze_response
from core.reporter import write_json, write_html
from pathlib import Path

app = typer.Typer(help="Defensive Prompt Safety Tester (safe-mode)")

@app.command()
def run(payloads: str = "payloads/tests.yaml", model: str = "gpt-4", api_key: str | None = None, out_json: str = "report.json", out_html: str = "report.html", safe_mode: bool = True):
    """
    Run benign test prompts from a YAML file against an LLM and generate reports.
    """
    init_openai(api_key)
    p = Path(payloads)
    if not p.exists():
        typer.echo(f"Payload file not found: {payloads}")
        raise typer.Exit(code=1)

    data = yaml.safe_load(p.read_text())
    results = []
    for entry in data.get("tests", []):
        name = entry.get("name", "unnamed")
        prompt = entry.get("prompt", "")
        # Query model
        resp = query_openai_chat(prompt=prompt, model=model)
        # Analyze
        det = analyze_response(resp["response"])
        results.append({
            "name": name,
            "model": resp["model"],
            "prompt": prompt if not safe_mode else None,
            "response": resp["response"],
            "latency_s": resp["latency_s"],
            "detect": det
        })
        typer.echo(f"[{name}] risk={det['risk_score']}")

    write_json(results, out_json)
    write_html(results, out_html, safe_mode=safe_mode)
    typer.echo(f"Reports written: {out_json}, {out_html}")

if __name__ == "__main__":
    app()

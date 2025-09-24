# core/reporter.py
import json
from pathlib import Path
from jinja2 import Template
from datetime import datetime

HTML_TEMPLATE = """        <html>
<head><title>Prompt Safety Report</title></head>
<body>
<h1>Prompt Safety Report</h1>
<p>Generated: {{ generated_at }}</p>
{% for item in results %}
  <hr/>
  <h2>Test: {{ item.name }}</h2>
  <p><strong>Model:</strong> {{ item.model }} | <strong>Latency:</strong> {{ item.latency_s }}s</p>
  <h3>Input Prompt</h3>
  <pre>{{ item.prompt if not safe_mode else '*** masked in safe-mode ***' }}</pre>
  <h3>Output</h3>
  <pre>{{ item.response }}</pre>
  <h3>Detections</h3>
  <p>Risk score: {{ item.detect.risk_score }}</p>
  <ul>
  {% for f in item.detect.findings %}
    <li><strong>{{ f.type }}</strong>: {{ f.match }} — ...{{ f.context }}...</li>
  {% endfor %}
  </ul>
{% endfor %}
</body>
</html>
"""

def write_json(results, outpath: str):
    Path(outpath).write_text(json.dumps({"generated_at": datetime.utcnow().isoformat(), "results": results}, indent=2))
    return outpath

def write_html(results, outpath: str, safe_mode: bool = True):
    tpl = Template(HTML_TEMPLATE)
    html = tpl.render(results=results, generated_at=datetime.utcnow().isoformat(), safe_mode=safe_mode)
    Path(outpath).write_text(html)
    return outpath

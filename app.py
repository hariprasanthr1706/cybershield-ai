from flask import Flask, render_template, request
from detector import analyze_text, analyze_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text_input = ""
    url_input = ""
    if request.method == "POST":
        text_input = request.form.get("message", "").strip()
        url_input = request.form.get("url", "").strip()
        findings = []
        if text_input:
            findings.append(("Message analysis", analyze_text(text_input)))
        if url_input:
            findings.append(("URL analysis", analyze_url(url_input)))
        result = findings
    return render_template("index.html", result=result, text_input=text_input, url_input=url_input)

if __name__ == "__main__":
    app.run(debug=True)

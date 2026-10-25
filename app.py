from flask import Flask, render_template
import requests

app = Flask(__name__)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

@app.route("/")
def home():
    url = "https://www.mimit.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv"
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        return f"Status: {r.status_code}, byte ricevuti: {len(r.content)}"
    except Exception as e:
        return f"Errore: {type(e).__name__}: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
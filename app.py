from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    #Faccio un test di chiamta
    urlStazioni = "https://www.mimit.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv"  # sostituisci con l'URL vero
    urlPrezzi = "https://www.mimit.gov.it/images/exportCSV/prezzo_alle_8.csv"

    respStazioni = requests.get(urlStazioni)
    respStazioni.raise_for_status()
    respStazioni.encoding = "utf-8"

    respPrezzi = requests.get(urlPrezzi)
    respPrezzi.raise_for_status()
    respPrezzi.encoding = "utf-8"

    righeStazioni = respStazioni.text.splitlines(keepends=True)
    righePrezzi = respPrezzi.text.splitlines(keepends=True)

    return(f"Righe stazioni totali: {len(righeStazioni)}")

if __name__ == '__main__':
    app.run(debug=True)
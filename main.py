from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():


    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        try:
            gewicht = float(request.form.get('gewicht'))
            groesse = float(request.form.get('groesse'))

            groesse_meter = groesse / 100
            bmi = round(gewicht / (groesse_meter * groesse_meter), 2)

            nachricht, status = auswertung(bmi)

        except ValueError:
            nachricht = "Einen BMI kann man ohne, oder mit falschen Werten nicht berechnen!"
            return render_template("index.html", fehler=nachricht)

        else:

            return render_template("index.html", ergebnis=bmi, nachricht=nachricht, klasse=status, gewicht_fuer_js=gewicht)

def auswertung(bmi):
    if bmi < 18.5:
        nachricht = f"Ein BMI von: {bmi} ist Untergewicht.", "warnung"
    elif 18.5 <= bmi < 25:
        nachricht =  f"Ein BMI von: {bmi} ist Normalgewicht.", "optimal"
    elif 25.0 <= bmi < 30:
        nachricht = f"Ein BMI von: {bmi} ist Übergewicht.", "warnung"
    elif 30.0 <= bmi < 35:
        nachricht = f"Ein BMI von: {bmi} ist Adipositas Grad I.", "alarm"
    elif 35.0 <= bmi < 40:
        nachricht = f"Ein BMI von: {bmi} ist Adipositas Grad II.", "alarm"
    elif bmi > 40:
        nachricht = f"Ein BMI von: {bmi} ist Adipositas Grad III. (Extremes Übergewicht!)", "alarm_hart"
    return nachricht


if __name__ == "__main__":

    app.run(debug=True)

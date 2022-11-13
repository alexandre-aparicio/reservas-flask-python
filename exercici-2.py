from flask import Flask, render_template, request, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

dies_hores = [
        		["Dilluns","Dimarts","Dimecres","Dijous","Divendres"], 
        		["15:00", "16:00", "17:00", "18:00", "19:00", "20:00" ]
    		]

error_ple = "Aquesta hora ja està reservada"
correcto = "S'hora s'ha reservat amb èxit"

global disponibilitat

disponibilitat = {
	"coberta":
		{
		"Dilluns": [
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""}
			],
		"Dimarts": [
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""}
			],
		"Dimecres": [
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""}
			],
		"Dijous": [
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""}
			],
		"Divendres": [
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""},
			{'disponibilitat':"","nom":"", "telefon":""}
			]
		},
	"exterior":
		{
		"Dilluns": [{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""}],
		"Dimarts": [{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""}],
		"Dimecres": [{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""}],
		"Dijous": [{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""}],
		"Divendres": [{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""},{'disponibilitat':"","nom":"", "telefon":""}],
		}
}

@app.route('/',methods = ['POST', 'GET'])
def index():

	
	if request.method == 'POST':
			dia = request.form['dia']
			hora = request.form['hora']
			hora = int(hora)
			instalacio = request.form['instalacio']	
			nom = request.form['nom']	
			telefon = request.form['telefon']			

			if disponibilitat[instalacio][dia][hora]["disponibilitat"] == "":

				disponibilitat[instalacio][dia][hora]["disponibilitat"]  = "RESERVAT"
				disponibilitat[instalacio][dia][hora]["nom"]  = nom
				disponibilitat[instalacio][dia][hora]["telefon"]  = telefon
				return render_template('home.html', dies_hores=dies_hores, dia = dia, hora = hora,disponibilitat = disponibilitat, success = correcto )	

			else:
				return render_template('home.html', dies_hores=dies_hores, error = error_ple)
			
	else:  	
			session['varInterna']=1
			
			return render_template('home.html', dies_hores=dies_hores)

# This page will have the sign up form
@app.route('/reserves')
def reserves():
	
    return render_template("reserves.html",disponibilitat = disponibilitat, dies_hores = dies_hores)
	


if __name__ == '__main__':
	app.run(debug=True)

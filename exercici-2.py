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
		"Dilluns": ["","","","","",""],
		"Dimarts": ["","","","","",""],
		"Dimecres": ["","","","","",""],
		"Dijous": ["","","","","",""],
		"Divendres": ["","","","","",""]
		},
	"exterior":
		{
		"Dilluns": ["","","","","",""],
		"Dimarts": ["","","","","",""],
		"Dimecres": ["","","","","",""],
		"Dijous": ["","","","","",""],
		"Divendres": ["","","","","",""]
		}
}


@app.route('/',methods = ['POST', 'GET'])
def index():

	
	if request.method == 'POST':
			dia = request.form['dia']
			hora = request.form['hora']
			hora = int(hora)
			a = 1
			b = 2

			if disponibilitat['coberta'][dia][hora] == "":
				disponibilitat['coberta'][dia][hora] = "NUEVO"
				return render_template('home.html', dies_hores=dies_hores, dia = dia, hora = hora,disponibilitat = disponibilitat, success = correcto )	
			else:
				return render_template('home.html', dies_hores=dies_hores, error = error_ple)

			

			
	else:  	
			session['varInterna']=1
			
			return render_template('home.html', dies_hores=dies_hores)

# This page will have the sign up form
@app.route('/reserves')
def reserves():
	
    return render_template("reserves.html",disponibilitat = disponibilitat)
	


if __name__ == '__main__':
	app.run(debug=True)

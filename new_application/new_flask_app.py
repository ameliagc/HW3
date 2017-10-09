from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search_form')
def search_form():
	return render_template("search_form.html")

@app.route('/search_info')
def view_search_info():
	data = request.args

	term = data.get('term')

	base_url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAZIzd9d4j2uBEqkNgM5a7LSmShu1dOc8A&cx=017576662512468239146:omuauf_lfve&q=" + term

	params = {}
	params["term"] = term

	resp = requests.get(base_url, params=params)
	data_text = resp.text 
	python_obj = json.loads(data_text)
	print(python_obj)

	return render_template("search_results.html", object=python_obj['searchInformation'], term=term)



if __name__ == '__main__':
    app.run()
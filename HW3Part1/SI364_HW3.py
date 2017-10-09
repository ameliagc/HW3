## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform')
def artist_form():
	return render_template("artistform.html")
	# When you submit form, goes to artist info template

@app.route('/artist_info')
def view_artist_info():
	# base url is part up until ? 
	base_url = "https://itunes.apple.com/search"

	data = request.args

	artist_name = data.get('artist')

	# parameters dictionary to fill in with keys and values
	params = {}
	params["term"] = artist_name

	# this will hold response object
	resp = requests.get(base_url, params=params)
	data_text = resp.text 
	python_obj = json.loads(data_text)
	return render_template("artist_info.html", objects=python_obj['results'])


@app.route('/artist_links')
def view_artist_links():
	return render_template("artist_links.html")

@app.route('/specific/song/<artist_name>')
def view_specific_artist(artist_name):
	base_url = "https://itunes.apple.com/search"

	data = request.args

	artist_name = data.get('artist')

	params = {}
	params["term"] = artist_name

	# this will hold response object
	resp = requests.get(base_url, params=params)
	data_text = resp.text 
	python_obj = json.loads(data_text)

	return render_template("specific_artist.html", results=python_obj, artist_name=artist_name)


if __name__ == '__main__':
    app.run()
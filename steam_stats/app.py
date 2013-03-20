# -*- coding: utf-8 -*-
# Welcome

import requests
import pymongo

from contextlib import closing
from pymongo import MongoClient
from flask import Flask, session, url_for, g, render_template, request, flash, redirect, _app_ctx_stack

# configuration
SECRET_KEY = "\x8bf\xb86c\xb0[\x93\xed\xce\x05!\x0ee\xbcr\xa3`-W\xb7\xf33\xab"
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# connect to the database
def connect_db(dbase='stats-base'):
	"""Connect to Mongodb"""
	global db
	connection = MongoClient(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
	dbase = connection[dbase]

@app.route('/')
def main():

	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		pass
		#sname = session['username']
		#steamid = "http://steamcommunity.com/id/{0}?xml=1".format(sname)
		#gamesid = "http://steamcommunity.com/id/{0}/games?xml=1".format(sname)
		#SteamProfile(download.Download(steamid))

	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':

		session['logged_in'] = True
		session['username'] = request.form['username']

		return redirect(url_for('main'))

	return render_template('login.html')

@app.route('/logout')
def logout():

	session.pop('logged_in', None)
	return redirect(url_for('main'))

if __name__ == "__main__":
	connect_db()
	app.run(debug=True)
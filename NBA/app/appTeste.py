from flask import Flask
from nba_py import player
from app import app
from urllib.request import urlopen
import json, requests

@app.route('/')
def index():
	jogador = str(player.get_player("D'Angelo", "Russell", "2015-16"))	
	return jogador

@app.route('/<int:codigo>/stats', methods=['GET'])	
def stats_jogador(codigo):
	info = player.PlayerSummary(codigo)
	return json.dumps(info.headline_stats())

@app.route('/<string:nome>/stats', methods=['GET'])	
def stats_jogador_nome(nome):	
	json.dumps(player.get_player(nome))	
	return jureg
@app.route('/teste')	
def teste():
	url = "http://stats.nba.com/stats/commonteamroster/?Season=2016-17&TeamID=1610612747"
	response = requests.get(url)
	data = json.loads(response.content)
	return data
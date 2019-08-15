from json import JSONEncoder
import json
import requests
import re
import datetime
import time
from flask import Flask, request

app = Flask(__name__)
	
@app.route('/miProximoColectivo')
def getBusesController():
	start = datetime.datetime.now()
	params = request.args.get('bbox')	
	url = 'https://miproximocolectivo.sanluis.gob.ar/MiProximoColectivo/GetMapMovilRecorrido?bbox=%s,%s,%s,%s' % (params[0],params[1],params[2],params[3])			
	headers = {'Content-type': 'application/json'}	
	response = requests.get(url,headers=headers)
	result = response.text
	end = datetime.datetime.now()
	final = end - start
	buses = filter(result)
	bs = parseObject(buses)	
	
	print("time -> getMiProximoColectivoController: %s" % final)
	return JSONEncoder().encode(bs)
	
if __name__ == '__main__':
    app.run()
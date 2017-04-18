from sys import argv
import bottle

import json
import requests

@route('/', method="get")
def intro():
	return template('template.tpl')



@route('/formulario',method="post")
def formulario():
	a=open("key","r")
	key=a.readline()
	ciudad = request.forms.get('ciudad')
	tipo = request.forms.get('tipo')
	payload={"app_key":key, "location": ciudad, "keywords":tipo}
	r=requests.get("http://api.eventful.com/json/events/search",params=payload)
	#r=requests.get("http://api.eventful.com/json/events/search?keywords="+tipo+"&location="+ciudad+"&app_key="+key)

	if r.status_code==200:
		js=json.loads(r.text)
	return template('formulario_json.tpl', js=js, ciudad=ciudad, tipo=tipo)



@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])



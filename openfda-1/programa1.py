#Para realizar esta práctica en primer lugar importamos los dos siguientes módulos, tras esto, creamos un cliente para extraer información
#del openfda. Esto lo hacemos estableciendo conexión con la página, mandando la petición y almacenando la resupuesta.

import http.client
import json

cabecera = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json", None, cabecera)
r1 = conn.getresponse()
resp_des = r1.read().decode("utf-8")
conn.close()

#Una vez hecho lo anterior, reorganizamos la información obtenida en diccionarios y listas con la función loads() para poder
# trabajarla e impimirla.
resp = json.loads(resp_des)
medicamento_info=resp['results'][0]

print ('ID: ',medicamento_info['id'])
print ('Proposito: ',medicamento_info['purpose'][0])

print ('Fabricante: ',medicamento_info['openfda']['manufacturer_name'][0])
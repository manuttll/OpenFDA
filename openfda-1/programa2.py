#Este programa es igual que el anterior exceptuando que como recurso añadimos limit=10. El resto del proceso de conexión es igual.

import http.client
import json

cabecera = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?limit=10", None, cabecera)
r1 = conn.getresponse()
resp_des = r1.read().decode("utf-8")
conn.close()
#Una vez obtenida la información se reorganiza como anteriormente y con un pequeño bucle imprimimos los ID.
resp = json.loads(resp_des)
for i in range (len (resp['results'])):
    medicamento_info=resp['results'][i]

    print ('ID: ',medicamento_info['id'])
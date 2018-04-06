import http.client
import json

cabecera = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?limit=10", None, cabecera)
r1 = conn.getresponse()
resp_des = r1.read().decode("utf-8")
conn.close()

resp = json.loads(resp_des)
for i in range (len (resp['results'])):
    medicamento_info=resp['results'][i]

    print ('ID: ',medicamento_info['id'])
import http.client
import json

cabecera = {'User-Agent': 'http-client'}

valor_skip=0
while True:
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", '/drug/label.json?limit=100&skip='+str(valor_skip)+'&search=substance_name:"ASPIRIN"', None, cabecera)
    r1 = conn.getresponse()
    resp_des = r1.read().decode("utf-8")
    conn.close()

    resp = json.loads(resp_des)
    for i in range (len (resp['results'])):
        medicamento_info=resp['results'][i]
        print ('ID: ',medicamento_info['id'])
        if (medicamento_info['openfda']):
            print('Fabricante: ', medicamento_info['openfda']['manufacturer_name'][0])

    if(len(resp['results'])<100):
        break
    valor_skip=valor_skip+100


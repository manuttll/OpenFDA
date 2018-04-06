#Para este programa volvemos a importar los módulos y usamos la función skip. Creamos un bucle infinito y establecemos la conexión
#igual que antes, añadiendo el skip, el limit=100 y la búsqueda específica en el recurso.

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

#Mediante un bucle for imprimimos la información que se desea, en caso de que la respuesta contenga 100 medicamentos (el máximo posible)
# se mantiene el bucle While, y hasta que no se devuelven menos de 100 no se rompe.
    resp = json.loads(resp_des)
    for i in range (len (resp['results'])):
        medicamento_info=resp['results'][i]
        print('Fabricante: ', medicamento_info['openfda']['manufacturer_name'][0])

    if(len(resp['results'])<100):
        break
    valor_skip=valor_skip+100


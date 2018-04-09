#Para este programa volvemos a importar los módulos y usamos la función skip. Creamos un bucle infinito y establecemos la conexión
#igual que antes, añadiendo el skip, el limit=100 y la búsqueda específica en el recurso.

import http.client
import json

headers = {'User-Agent': 'http-client'}

valor_skip=0
while True:
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", '/drug/label.json?limit=100&skip='+str(valor_skip)+'&search=active_ingredient:"acetylsalicylic"', None, headers)
    r1 = conn.getresponse()
    resp_des = r1.read().decode("utf-8")
    print(r1.status, r1.reason)
    conn.close()

#Mediante un bucle for imprimimos la información que se desea. Usamos skip para ir recibiendo la información de cien en cien, y si
#la información recibida contiene menos de 100 medicamentos, se frena el bucle.
    resp = json.loads(resp_des)
    for i in range (len (resp['results'])):
        medicamento=resp['results'][i]
        print("ID:", medicamento["id"])
        if medicamento["openfda"]:
            print('Fabricante: ', medicamento['openfda']['manufacturer_name'][0])
        else:
            print("No tenemos información del fabricante.")
    #En este caso no sería necesario el uso del skip, ya que el programa devuelve menos de 100 medicamentos con acetylsalicylic,
    #sin embargo, a priori esto no lo sabríamos y de esta forma queda un programa más completo.
    if(len(resp['results'])<100):
        break
    valor_skip=valor_skip+100


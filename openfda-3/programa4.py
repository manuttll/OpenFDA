#En primer lugar importamos los siguientes módulos y declaramos el puerto y la IP.
import http.server
import socketserver
import http.client
import json

PORT = 8090
IP ="localhost"
#Creamos esta función que actuará como cliente para crear la lista a partir de la información que recibe de la página,
#usando un programa similar en los  anteriores.
def lista_medicamentos():
    lista = []
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=11", None, headers)

    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    resp_des = r1.read().decode("utf-8")
    conn.close()

    resp = json.loads(resp_des)
    for i in range(len(resp['results'])):
        medicamento= resp['results'][i]
        if (medicamento['openfda']):
            lista.append(medicamento['openfda']['generic_name'][0])

    return lista
# Creamos esta clase derivada de BaseHTTPRequestHandler, que "hereda" todos los métodos de esta clase. Y los que
# nosotros consideremos los podemos reemplazar por los nuestros.
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # GET. Este metodo se invoca automaticamente cada vez que hay una peticion GET por HTTP.
    def do_GET(self):
        self.send_response(200)

    #Llamamos a la función lista y vamos pasando sus componentes al formato html de uno en uno.
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content="<html><body>"
        lista=lista_medicamentos ()
        content= "Los diez medicamentos son:"+"<br>"
        for e in lista:
            content += e+"<br>"
        content+="</body></html>"

        self.wfile.write(bytes(content, "utf8"))
        return


#Ahora creamos un servidor para siempre que estará esperando una petición.
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")


import mysql.connector as mysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup

print("Ingresa una pagina web")
Pag= input()

print ("Python conectándose a MySQL") 
conexion = mysql.connect ( host='localhost', user= 'root', passwd='', db='paginas' )
operacion = conexion.cursor()
print ("Conectado") 

url=urlopen(Pag)
bs = BeautifulSoup(url.read(),'html.parser')
sql="INSERT INTO paginas_links (Enlace,Estatus) values(%s,%s)"
for enlaces in bs.find_all("a"):
    pag ="{}".format(enlaces.get("href"))
    datos=(pag,False)
    operacion.execute(sql,datos) 
print("**********")

#op = a()
#op.analizar(Pag)

operacion.execute( "SELECT * FROM paginas_links" )
for Enlaces,Estatus in operacion.fetchall():
    print(Enlaces,Estatus)

for Enlaces,Estatus in operacion.fetchall():
    if(Estatus==0):
        op.analizar(Enlaces)
        datos=(Enlaces)

operacion.execute( "SELECT * FROM paginas_links" )
for Enlaces,Estatus in operacion.fetchall():
    print(Enlaces,Estatus)
conexion.close()
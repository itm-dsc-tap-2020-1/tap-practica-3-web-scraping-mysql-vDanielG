import mysql.connector as mysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup

print("Ingresa una pagina web")
Pag= input()

print ("Python conectándose a MySQL") 
conexion = mysql.connect ( host='localhost', user= 'root', passwd='', db='web' )
operacion = conexion.cursor()
print ("Conectado") 


class a:
    def analizar(Pag):
        url=urlopen(Pag)
        bs = BeautifulSoup(url.read(),'html.parser')
        sql="INSERT INTO LINK (link,status) values(%s,%s)"
        for enlaces in bs.find_all("a"):
            pag ="{}".format(enlaces.get("href"))
            datos=(pag,False)
            operacion.execute(sql,datos) 
        print("**********")

op = a()
op.analizar(Pag)

operacion.execute( "SELECT * FROM LINK" )
for link,status in operacion.fetchall():
    print(link,status)

sql1="UPDATE LINK SET status=True WHERE link=%s"
for link,status in operacion.fetchall():
    if(status==0):
        op.analizar(link)
        datos=(link)

operacion.execute( "SELECT * FROM LINK" )
for link,status in operacion.fetchall():
    print(link,status)
conexion.close()
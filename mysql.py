print "Resultados de PyMySQL:"
import pymysql
miConexion = MySQLdb.connect( host='localhost:8081', user= 'root', passwd='', db='mydb', port='3306' )
cur = miConexion.cursor()
cur.execute( "SELECT nombre, apellido FROM usuarios" )
for nombre, apellido in cur.fetchall() :
    print nombre, apellido
miConexion.close()
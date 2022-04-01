
import pymysql
miConexion = MySQLdb.connect( host='localhost:8081', user= 'root', passwd='', db='mydb' )
cur = miConexion.cursor()
cur.execute( "SELECT Name FROM user" )
for name in cur.fetchall() :
    print name 
miConexion.close()
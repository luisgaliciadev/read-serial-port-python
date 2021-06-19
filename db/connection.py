import pyodbc

# Configuracion de conexion a base de datos
# server = '192.168.3.3'
server = '66.23.235.30,10000'
database = 'FE_SUPERVAN'
username = 'sa'
password = 'Cybersac1'
connect = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password

def connectionStatus():
    try:   
      connectionDB = pyodbc.connect(connect)
      return {"ok": True,"connectionDB": connectionDB} 
    except Exception as e:
        return {"ok": False,"error": e}
        

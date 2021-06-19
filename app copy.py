# # Imports Modules
# import serial, time
import requests

# # Others Imports
# from db import connection

# # Config SERIAL PORT
# puertoSerial = serial.Serial('COM2', baudrate = 9600, bytesize = 8, parity = 'N', stopbits=1, timeout=1.0)

# # Wait Time For Read Serial Port 
# time.sleep(2)

# # Begin
# connectionStatus = connection.connectionStatus()

# if connectionStatus['ok']:
#     cursor = connectionStatus['connectionDB'].cursor()
#     cursor.execute("SELECT @@VERSION")
#     versionSqlServer = cursor.fetchone()
#     print(f'Servidor de base de datos Online, Version: {versionSqlServer}.')
#     contador = 0
#     while 1:
#         try:
#             datos = puertoSerial.readline()          
#             peso = str(datos)
#             arrayPeso = peso.split("'")
#             pesoFinal = (arrayPeso[1])
#             if len(pesoFinal) > 0:
#                 print(float(pesoFinal))
#                 query = f"UPDATE PESOS_BALANZAS_DIEF SET BALANZA_1 = {float(pesoFinal)}"
#                 cursor.execute(query)
#                 connectionStatus['connectionDB'].commit() 
#             else:                
#                 print(0)
#                 contador += 1
#                 if contador == 30:
#                     query = f"UPDATE PESOS_BALANZAS_DIEF SET BALANZA_1 = 0"
#                     cursor.execute(query)
#                     connectionStatus['connectionDB'].commit()
#                     contador = 0
#         except KeyboardInterrupt:
#             break
# else:
#     print(f'Servidor de base de datos no disponible. Error: {connectionStatus["error"]}')

# # Close Port Serial
# puertoSerial.close()



url = 'http://localhost:3000/api/mygeotab/totalodometer'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['results'][0]['name'])


   







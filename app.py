# Imports Modules
import serial, time
import requests

# Others Imports
from db import connection

# Config SERIAL PORT
puertoSerial = serial.Serial('COM2', baudrate = 9600, bytesize = 8, parity = 'N', stopbits=1, timeout=1.0)

# Wait Time For Read Serial Port 
time.sleep(2)

# Begin
try:
    urlApiServer = 'http://localhost:3000/api'
    response = requests.get(urlApiServer)    
    if response.status_code == 200:
        data = response.json()
        print(data['message'])
        contador = 0
        while 1:
            try:
                datos = puertoSerial.readline()          
                peso = str(datos)
                arrayPeso = peso.split("'")
                pesoFinal = (arrayPeso[1])
                if len(pesoFinal) > 0:
                    print('Peso: ', float(pesoFinal))
                    try:
                        url = 'http://localhost:3000/api/' + str(float(pesoFinal))
                        res = requests.post(url)
                        if res.status_code != 200:
                            print('Error en enviar el peso.')
                    except Exception as e:
                        print('Error no se pudo enviar el peso.')
                        print('Error de conexión: ', e)                     
                else:                
                    print('Peso:', 0)
            except KeyboardInterrupt:
                break
    else:
        print('Error de conexión.')
        a = input()
except Exception as e:
    print('Error de conexión: ', e)
    a = input()



# Close Port Serial
puertoSerial.close()









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



# url = 'http://localhost:3000/api/mygeotab/totalodometer'
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print(data['results'][0]['name'])


   







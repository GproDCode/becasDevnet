import requests
import json
import urllib3
from pprint import pprint
import sys



#definimos variables para pedir el ticket automaticamente

requests.packages.urllib3.disable_warnings()
url = "https://sandboxapicem.cisco.com/api/v1/ticket"
headers = {
    'Content-Type' : 'application/json'
}
body_json = {
    "password" : "Cisco123!",
    "username" : "devnetuser"
}

#info extra :   json-dumps ==> serialización ==> lo convierte a json
#               json.loads // convierte a diccionario de python

#Pedimos el ticket

resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False)

##print("Ticket request status",resp.status_code)

#Definimos el numero del ticket en la variable serviceTicket

response_json = resp.json()
serviceTicket = response_json["response"]["serviceTicket"]

## Una vez obtenemos el ticket, pasamos a pedir los datos de los devices

requests.packages.urllib3.disable_warnings()
url = "https://sandboxapicem.cisco.com/api/v1/network-device"
headers = {
    'Content-Type' : 'application/json',
    'X-Auth-Token'  : serviceTicket     #En serviceTicket tenemos el numero de Ticket almacenado que añadimos al headers
}

#utilizamos Get para obtener los datos deseados

resp = requests.get(url,headers=headers,verify=False)

response_json = resp.json()

#pprint(response_json)

# Printamos Banner, le pongo así para que sea mas facil de modificar

print ("*****************************************")
print ("**                                     **")
print ("**           Bienvenido                **")
print ("**                                     **")
print ("** APIC-EM Automatic and Interactive   **")
print ("**           Ver.0.0.0.1               **")
print ("**                                     **")
print ("*****************************************")

#Primer menu de selección

def menumain ():
    print ("Quiere conectar con el APIC-EM?")
    menumain = input ("Escriba Si o No :")
    if menumain == "si":
        print ("Conectado...") 
    elif menumain == "no":
        print ("Gracias, esperamos verte pronto")
        sys.exit() 
    elif menumain != "si":
        print ("seleccion incorrecta")
        menumain = input ("Escriba Si o No :")
        if menumain != "si":
          print ("Lo sentimos")
          sys.exit()


 #Segundo menú de selección   

def menuu1 ():
    print ("Seleciones entre las siguientes opciones.")
    print ("1 -Conocer la mac de los equipos conectados.")
    print ("2 -Conocer el uptime de los equipos conectados.")
    print ("3 -Conocer la ip y mac address de los equipos conectados.")
    print ("4 -Conocer el modelo y la version de IOS de los equipos conectados.")
    print ("5 -Mostrar todos los datos anteriores.")
    print ("6 -Personaliza tu OutPut.")
    print ("7 -Salir")



menumain ()
menuu1 ()

# definimos la variable menu1 para movernos por las diferentes opciones del menú

menu1 = input ("Introduzca el numero de selección: ")

while (menu1 == "1" or "2" or "3" or "4" or "5" or "6" and "7"):

    if menu1 == "1":
        for equipo in response_json ["response"]:
            print ("El Hostname", equipo["hostname"], "su MAC es", equipo["macAddress"])
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if  respu == "si":
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

            

    elif menu1 == "2":
        for equipo in response_json ["response"]:
            print ("El Hostname", equipo["hostname"], "su uptime es ", equipo["upTime"])
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "3":
        for equipo in response_json ["response"]:
            print ("El Hostname", equipo["hostname"], "su ip es ", equipo["managementIpAddress"], "su MAC es", equipo["macAddress"])
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
                menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "4":
        for equipo in response_json ["response"]:
            print ("El Hostname", equipo["hostname"], "el modelo es  ", equipo["platformId"], "con una version de IOS ", equipo["softwareVersion"])
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
                menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "5":
        for equipo in response_json ["response"]:
            print ("El Hostname", equipo["hostname"], "su ip es ", equipo["managementIpAddress"], "el modelo es ",equipo["platformId"], "su MAC es", equipo["macAddress"], 
             "con una version de IOS ", equipo["softwareVersion"], "su uptime es ", equipo["upTime"])
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
                menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "6":
        print ("**    Estamos trabajando en esta funcionalidad, Disculpen las molestias  **")
        menu1 = input ("Introduzca el numero de selección: ")
        

    elif menu1 == "7":
        print ("Muchas Gracias, hasta pronto.")
        sys.exit()

    
    
    else:

        print("Seleccion incorrecta, escriba 7 si desea salir")
        menu1 = input("Introduzca el numero de selección: ")
            





def menuu2 ():
    print ("")
    print ("*** Esta opcion está en desarrollo, disculpen las molestias ***")
    print ("")
    print ("Selecione los OutPuts que quiere visualizar entre la lista siguiente.")
    print ("1 -Conocer el nombre de Hostname.")
    print ("2 -Conocer la versión de IOS.")
    print ("3 -Conocer la MAC Address")
    print ("4 -Conocer la IP")
    print ("5 -Conocer el Uptime de los dispositivos")
    print ("7 -Salir")





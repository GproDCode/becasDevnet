#!/usr/bin/env python3 

import netmiko
from netmiko import ConnectHandler
import sys 
from pathlib import Path 
import requests
import json
import urllib3
from ncclient import manager
import xmltodict
import xml.dom.minidom
import xmltodict





# Printamos Banner

print ("*****************************************\n"
    "**                                     **\n"
    "**           Bienvenido                **\n"
    "**                                     **\n"
    "**         My Router Optión            **\n"
    "**           Ver.0.0.0.1               **\n"
    "**                                     **\n"
    "*****************************************\n")

print ("Conectar con Router local o remoto")
iprou = input("Introduzca la IP: ")

## Conexion al router o SW Netmiko.
sshCLi = ConnectHandler(
    device_type="cisco_ios",
    host= iprou,
    port=22,
    username="cisco",
    password="cisco123!",
    fast_cli=True
)

print ("Conectado con el Router\n")

#Primer menu de selección

def menuu1 ():
    print ("Seleciones entre las siguientes opciones.\n"
    "1 -Obtener listado de las interfaces.\n"
    "2 -Crear una interface nueva.\n"
    "3 -Eliminar una interface.\n"
    "4 -Ver la tabla de routing del dispositivo.\n"
    "5 -Crear ruta.\n"
    "6 -Eliminar ruta. \n"
    "7 -Pegar configracion manualmente.\n"
    "8 -Obtener listado interfaces con RESTCONF.\n"
    "9 -Obtener listado de interfaces y MAC con NETCONF.\n"
    "10 -Salir\n")

menuu1 ()

menu1 = input ("Introduzca el numero de selección: ")


while (menu1 == "1" or "2" or "3" or "4" or "5" or "6" and "7"):

    if menu1 == "1":
        print("Sending 'sh ip int brief'.")
        output = sshCLi.send_command("show ip int brief")
        print("show ip int brief:\n{}\n".format(output))
        print ("Quiere realizar otra operación?")
        respu = input ("Introduzca si o no: ")
        if  respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()         

    elif menu1 == "2":
        print("Sending 'sh ip int brief'.")
        output = sshCLi.send_command("show ip int brief")
        print("show ip int brief:\n{}\n".format(output))
        print("Va a crear una interface nueva.")
        print ("Complete los datos solicitados:")
        datoint1 = input ("Introduzca el tipo de interface: ")
        datoint2 = input ("Introduzca la ip y mascara xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx : ")
        datoint3 = input ("Introduzca la descripción: ")

        config_commands = [
        "int "+ datoint1,
        "ip address " + datoint2,
        "description "+ datoint3,
        ]
        output = sshCLi.send_config_set(config_commands)
        print("Config output from the device:\n{}\n".format(output))
        output = sshCLi.send_command("show ip int brief")
        print("show ip int brief:\n{}\n".format(output))
        output = sshCLi.send_command("sh running-config interface "+ datoint1)
        print("sh runn int "+ datoint1,"\n{}\n".format(output))
        print ("Quiere realizar otra operación?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "3":
        print("Sending 'sh ip int brief'.")
        output = sshCLi.send_command("show ip int brief")
        print("show ip int brief:\n{}\n".format(output))
        print("Va a eliminar una interface.")
        print ("Complete los datos solicitados:")
        elimint1 = input ("Introduzca el nombre de interface: ")
        
        config_commands = [
        "no int "+elimint1,
        ]

        output = sshCLi.send_config_set(config_commands)
        print("Config output from the device:\n{}\n".format(output))

        output = sshCLi.send_command("show ip int brief")
        print("show ip int brief:\n{}\n".format(output))
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "4":
        
        output = sshCLi.send_command("show ip route")
        print("show ip route:\n{}\n".format(output))


        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "5":
        
        print("Sending 'sh ip int brief'.")
        print ("Complete los datos solicitados:")
        datorou1 = input ("Introduca red local a.b.c.d: ")
        datorou2 = input ("Introduzca la mascara a.b.c.d : ")
        datorou3 = input ("Introduzca tipo interface o información extra: ")
        datorou4 = input ("Introduzca la red de destino: ")

        config_commands = [
        "ip route "+ datorou1 + " "+ datorou2 + " "+ datorou3 + " "+ datorou4,
        
        ]
        output = sshCLi.send_config_set(config_commands)
        print("Config output from the device:\n{}\n".format(output))
        output = sshCLi.send_command("show ip route")
        print("show ip route :\n{}\n".format(output))
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
                menuu1 ()
                menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "6":
        
        print("*** Atenciòn ***")
        print("Va a eliminar una ruta de la configuración, si no está seguro pulse Ctrl + C para salir")
        print ("Complete los datos solicitados:")
        datorou1 = input ("Introduca red local a.b.c.d: ")
        datorou2 = input ("Introduzca red de destino a.b.c.d : ")
        datorou3 = input ("Introduzca tipo interface o información extra: ")

        config_commands = [
        "no ip route "+ datorou1 + " "+ datorou2 + " "+ datorou3,
        
        ]
        output = sshCLi.send_config_set(config_commands)
        print("Config output from the device:\n{}\n".format(output))
        output = sshCLi.send_command("show ip route")
        print("show ip route :\n{}\n".format(output))
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
                menuu1 ()
                menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

    elif menu1 == "7":
        print("*** Atenciòn ****\n","Va a introducir la configuracion manualmente\n","si no conoce bien el proceso pulse Ctrol + C para salir\n")
        print ("Complete los datos solicitados:")
        pasteint1 = input ("Por favor especifique la ruta del archivo sin incluir el archivo: ")
        pasteint2 = input ("Ponga el nombre del archivo txt, nonbrearchivo.txt: ")
        #/Users/gprod/Documents/curso python becas/ lo pongo para acordarme de la ruta de mi equipo local
        cfg_file = Path(pasteint1 + pasteint2)

       
        output = sshCLi.send_config_from_file(cfg_file)
        print("Config output from the device:\n{}\n".format(output))
        print ("Quiere realizar otra operación?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

# RESTCONF
    elif menu1 == "8":
        
        requests.packages.urllib3.disable_warnings()
        api_url = "https://"+ iprou+"/restconf/data/ietf-interfaces:interfaces" 
        
        headers = {
            'Accept' : 'application/yang-data+json',
            'Content-Type' : 'application/yang-data+json',
            #'X-Auth-Token'  : "ST-1826-egQsiWR6ll52YOXsojbK-cas"
            }
        basicauth = ("cisco","cisco123!")
        ##body_json = {
        ##"password": "cisco123!",
        ##"username": "cisco"
        ##}
        resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
        response_json = resp.json()
        #print (response_json)

        print (json.dumps (response_json, indent=4, sort_keys=True))
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

# NETCONF
    elif menu1 == "9":

        m = manager.connect (
            host=iprou,
            port=830,
            username="cisco",
            password="cisco123!",
            hostkey_verify=False
        )

        #print("#Supported Capabilities (YANG models):") 
        #for capability in m.server_capabilities:
        #   print(capability)
 
        #netconf_reply = m.get_config(source="running") 
        #print(netconf_reply)
 


        netconf_filter = """

        <filter>
            <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>

        """
        netconf_reply = m.get(filter = netconf_filter)
        #print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
        for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
            print("Name: {} MAC: {} Input: {} Output {}".format( interface["name"],
            interface["phys-address"], interface["statistics"]["in-octets"], interface["statistics"]["out-octets"]
            ) )
        print ("Quiere conocer otros datos?")
        respu = input ("Introduzca si o no: ")
        if respu == "si":
            menuu1 ()
            menu1 = input ("Introduzca el numero de selección: ")
        elif respu != "si":
                print ("Gracias, chau")
                sys.exit()

  

    elif menu1 == "10":
        print ("Muchas Gracias, hasta pronto.")
        sys.exit()

    
    
    else:

        print("Seleccion incorrecta, escriba 10 si desea salir")
        menu1 = input("Introduzca el numero de selección: ")

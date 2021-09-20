"""Este programa permite enviar mensajes de whatsapp en una fecha determinada"""
"""Importamos módulos"""
import pywhatkit as kit

"""Mensaje"""
print("Bienvenido a WhatsappChatBot, sigue las instrucciones: ")
print("")
msg = str(input("1. Escribe el mensaje que quieres enviar: "))

'''Número'''
num = str(input("2. Escribe el número del destinatario: "))

'''Fecha'''
t = str(input("3. Escribe el tiempo en formato 24h (hrs:mins): "))
hrs = int(t.split(":")[0])
mins = int(t.split(":")[1])

'''Enviar'''
answer = input("4. ¿Quieres enviar el mensaje? Escribe 'Si' o 'No': ")
if answer == 'Si':
    kit.sendwhatmsg(num, msg, hrs, mins)
print("")








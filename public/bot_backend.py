from funcoes import sendMessage
import os

history = []
os.system('cls')
while True:
    _input = input("Message: ")
    
    if _input.lower() == "break":
        break
    else:
        res = sendMessage(_input, history)
        print(f"\nSonoma: {res}\n")
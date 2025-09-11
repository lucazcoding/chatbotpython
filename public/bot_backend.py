from funcoes import sendMessage

history = []

while True:
    _input = input("Message: ")
    
    if _input.lower() == "break":
        break
    else:
        res = sendMessage(_input, history)
        print(f"\nSonoma:{res}\n")
textinput = input("enter text here> ")

textoutput = bytes.fromhex(textinput).decode("utf-8")
print("Decoded text:", textoutput)
textinput = input("enter text here> ")

textoutput = textinput.encode("utf-8").hex(" ")

with open("utf8encodedtext.txt", "w") as f:
    f.write("Encoded text: ")
    f.write(textoutput + "\n")
    f.write("Without Spaced encoded text: ")
    f.write(textoutput.replace(" ",""))
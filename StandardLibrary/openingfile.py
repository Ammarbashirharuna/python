from pathlib import Path

filename = 'mytext.txt'
with open(filename, 'w') as file:
    file.write("this is the text am attempting to add")
    file.write("this is another text am attempting to add in to the file")

#using a mode to append to a file
with open(filename, 'a') as file:
    filename.write("it seeems i love to ddd this inside yyou")

#reading the content of a file to  verify
with open(filename, 'r') as file:
    content = file.read()
    print(content)



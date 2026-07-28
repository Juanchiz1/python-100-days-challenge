file=open("my_file.txt")
content=file.read()
print(content)

file.close()

with open("my_file.txt","a") as file:
    file.write("\njajaja")
#FILENOTFOUND
try:
    file= open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("some text")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("file closed")
    #raise KeyError("Change Key")




#KEYERROR
#a_dictionary = {"key":"value"}
#print(a_dictionary["non_existing_key"])


#TYPE ERROR
#text="assd"
#number=7555
#print(text+number)


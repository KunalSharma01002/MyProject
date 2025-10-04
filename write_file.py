text = input("Enter some text to write to the file: ")

myfile = open("output.txt", "w")
write_myfile = myfile.write(text+"\n")
print("Data successfully written to output.txt")
myfile.close()

additionaltext = input("Enter some text to write to the file: ")
Afile = open("output.txt", "a")
appending_file =Afile.write(additionaltext+"\n")
print("Data successfully append")
Afile.close()

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
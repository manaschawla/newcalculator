filename = 'manas.txt'
with open(filename, 'w') as file:
    file.write("i am manas. \n i am 18 years old")
with open(filename, 'a') as file:
    file.write("\ni am currently pursuing b.tech")
    
with open(filename, 'r') as file:
   content =  file.read()
print(content)
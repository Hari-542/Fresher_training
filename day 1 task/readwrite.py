data=input("Enter the Data:")
path=input("Enter the path:")
with open(path,'w') as file:
    file.write(data)
with open(path,'r') as file:
    k=file.read()
    print(k)


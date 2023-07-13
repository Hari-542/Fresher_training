path='input.txt'
with open(path,'r',encoding='utf-16le') as file:
    k=file.read()
    print(k)
    with open('output.txt','w',encoding='utf-8') as file1:
        file1.write(str(k))
 

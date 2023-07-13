path='japanese_input.txt'
with open(path,'r',encoding='utf-8') as file:
    k=file.read()
    with open('japanese_output.txt','w',encoding='utf-8') as file1:
        file1.write(str(k))

path1='spanish_input.txt'
with open(path1,'r',encoding='utf-8') as file:
    k=file.read()
    print(k)
    with open('spanish_output.txt','w+',encoding='utf-8') as file1:
        file1.write(k)
        print(file1.read())
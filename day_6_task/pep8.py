#pep8
#print name and age
#get input from user
name=input("Enter your Name:")
age=int(input("Enter Your Age:"))

#validate your age for voterId

if(age>=18):
    print('Name:',name,'\n','Age:',age)
    print('you are eligible to vote')
else:
    print('Name:',name,'\n','Age:',age)
    print('you are not eligible to vote')
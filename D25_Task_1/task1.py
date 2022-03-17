""""
Registration and Login system with Python, file handling

STAGE -- 1 
Registration

When the user chooses to Register

---> email/username should have "@" and followed by "."
      eg:- sherlock@gmail.com
            nothing@yahoo.in

---> it should not be like this 
       eg:- @gmail.com
            there should not be any "." immediate next to "@"
            my@.in
            it should not start with special characters and numbers

---> password (5 < password length > 16)
              Must have minimum one special character,
              one digit,
              one uppercase, 
              one lowercase character 

Stage 2 
  Once the username and password are validated, store those values in a file


Stage 3
Login
 When the user chooses to Login, check whether his/her credentials exist in the file or not based on the user input 
If doesn’t exist ask them to go for Registration or 
If they have chosen forget password you should be able to retrieve their original password based on their username provided in the user input
If nothing matches in your file you should ask them to Register
"""
import re
def validusername(name):
    x = re.match("^[a-zA_Z][a-zA_Z0-9]*[@][a-zA_Z]+[.][a-zA_Z]+$", name)
    return(x!=None)
def validpassword(p):
    x = True
    while x:  
        if (len(p)<6 or len(p)>15):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[!@#$%^&*()_\+-=><,.?\\\/\|:;'\"\`\~\{\}\[\]]",p):
            break
        elif re.search("\s",p):
            break
        else:       
            x=False
            break
    return(not x)
def store(name,p):
    file = open('task1.txt','a')
    file.write(name+" "+p+"\n")
    file.close()
def validate(user,p=""):
    file = open("task1.txt", "r")
    txt=user+" "+p
    db=file.read()
    file.close()
    return(re.search(txt,db)!=None)
def forgotpass(user):
    file = open("task1.txt", "r")
    txt=user
    db=file.read()
    file.close()
    m=re.search(txt,db)
    l=m.span()[1]+1
    r=l+5
    while(db[r]!="\n"):
        r+=1
    password=db[l:r]
    return(password)
def register():
    while True:
        name=input("Enter email\n")
        if not validusername(name):
            print("Invalid username\n")
        else:
            break
    while True:    
        p=input("Enter password\n")
        if not validpassword(p):
            print("Invalid Password\n")
        else:
            break
    store(name,p)
    print("Successfully registered\n")
def login():
    user=input("Enter email\n")
    if not validate(user):
        print("Email doesnt exist, please register\n")
        register()
        return
    p=input("Enter password\n")
    if not validate(user,p):
        response=input("Wrong password, did you forget you password? yes or no\n")
        if response=="yes":
            print(forgotpass(user)) 
    else:
        print("Succcessfully loged in")
if __name__ == "__main__":
    print("Welcome!")
    while True:
        print("Menu:\n1. Register\n2. Login\n3. Forgot Password?\nAny other character to exit\n")
        n=input()
        if n=="1":
            register()
        elif n=="2":
            login()
            
        elif n=="3":
            user=input("Enter email")
            if not validate(user):
                print("Email doesnt exist")
            else:    
                forgotpass(user)
        else:
            break

import os
cur_dir = os.getcwd()
enter = input('do you want to login or signup ')
if enter == 'signup':
    username = input("Enter the user name ")
    password = input("Enter your password ")
    filepwd = open(username + password+".txt","w+")
    filepwd.write(password)
    filepwd.close()
    details = input("Enter your details ")
    file = open(username,"w+")
    file.write(details)
    print("Details submitted successfully")
    file.close()
elif enter == "login":
    file_list = os.listdir(cur_dir)
    while True:
        username = input("Enter the user name ")
        if username in file_list:
            break
        else:
            print("user name not found")
            continue
    while True:
        pwd = input("Enter your password ")
        if username+pwd+".txt" in file_list:
            access = open(username,"r")
            print(access.read())
            access.close()
            break
        else:
            print("Wrong password")
            continue
else:
    print("Enter the correct choice")

     
    
    

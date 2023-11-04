from cryptography.fernet import Fernet 

"""
def write_key():
    key = Fernet.generate_key()
    # write in bytes mode
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#master_pwd = input("What is the master password? ")
# key is in bytes so master_pwd has to be in bytes too 
key = load_key() # + master_pwd.encode()
# initializing encryption module 
fer= Fernet(key)

# define a key. Will take a string of text and using key will turn it into a string of text 
# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

def view():
    with open("passwords.txt", "r") as f: 
        for line in f.readlines():
            data = line.rstrip() # r.strip will strip character line
            # .split will look for "|" and will split string into different items
            # "hello|tim|yes|2"
            # ["hello", "tim"]
            user, passw = data.split("|") 
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

# b"hello" is a byte string
# Is different than "hello"

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # w, r, a are the file modes
    # w means write. Will create a new file or overide this file if it already exists
    # r means read mode. Can't write anything in file, only read 
    # a means append mode. Allows us to add something to end of existing file and create new file if file DNE
    with open("passwords.txt", "a") as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit. ")
    mode.lower()

    if mode == "q":
        break


    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue

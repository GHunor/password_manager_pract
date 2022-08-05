from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    key_file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            uname,pwrd = data.split("|")
            print("User: " + uname + " | Password: " + fer.decrypt(pwrd.encode()).decode())
def add():
    name = input("Address: ")
    pwrd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwrd.encode()).decode() + "\n")
def promt():
    print("What would you like to do?\nView already saved passwords? (view)\nAdd new password? (add)\nQuit? (quit)\n")

    mode = input(">: ").lower()
    if mode == "quit":
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        
def main():
    mpwrd = input("Please give me the master password ")
    write_key()
    key = load_key() + mpwrd.encode()
    fer = fernet(key)
    promt()
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()

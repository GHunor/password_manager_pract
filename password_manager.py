def view():
    pass
def add():
    addrs = input("Address: ")
    pwrd = input("Password: ")

    with open(passwords.txt, 'a') as f:
        f.write(addrs + "|" + pwrd + "\n")

mpwrd = input("Please give me the master password")
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

import hashlib
import secrets
def fingerprint(text ,salt):
        return hashlib.scrypt(text.encode(),salt=salt.encode(),n=2**14,r=8,p=1).hex()
def register():
        name = input("username: ")
        password = input("password: ")
        salt = secrets.token_hex(8)
        line = name + ":" + salt + ":" + fingerprint(password, salt) + "\n"
        f = open("user.txt", "a")
        f.write(line)
        f.close()
        print("registered")
def login():
        name = input("username: ")
        password = input ("password: ")
        f = open("user.txt", "r")
        lines = f.readlines()
        f.close()
        for line in lines:
                stored = line.strip().split(":")
                if stored[0] == name and stored[2] == fingerprint(password, stored[1]):
                        print("ACCESS GRANTED")
                        return
        print("DENIED") 
while True:
        print("1 register")
        print("2 login")
        print("3 quit")
        choice = input("choice: ")
        if choice == "1":
                register()
        elif choice == "2":
                login()
        elif choice == "3":
                break

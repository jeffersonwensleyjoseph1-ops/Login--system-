import hashlib
import secrets
def fingerprint(text):
	return hashlib.sha256(text.encode()).hexdigest()
def register():
	name = input("username: ")
	password = input("password: ")
	salt = secrets.token_hex(8)
	line = name + ":" + salt + ":" + fingerprint(salt + password) + "\n"
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
		if stored[0] == name and stored[2] == fingerprint(stored [1] + password):
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

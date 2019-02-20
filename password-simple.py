import time
print("To continue, you must enter a password")
time.sleep(1)
a = 3
while a > 0:
    pwd = input("Password: ")
    pwd = str(pwd)
    if pwd == "admin":
        time.sleep(1)
        print("Correct password")
        break
    if pwd != "admin":
        time.sleep(1)
        print("Incorrect password, try again.")
        continue
time.sleep(1)
print("You may continue")

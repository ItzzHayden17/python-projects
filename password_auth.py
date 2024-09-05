db = {"itzzhayden17":"anray123","davemage":"daveiscool"} #{username:password}

username = input("What is your username?: ")
password = input("What is your password?: ")

for i in db:
    if username == i:
        while True:
            if db.get(i) == password:
                print(f"Password valid,Welcome {username}")
                break
            else:
                password = input("Incorrect password,please retype: ")
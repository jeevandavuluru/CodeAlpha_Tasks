import bcrypt

stored_password = bcrypt.hashpw(
    b"admin123",
    bcrypt.gensalt()
)

attempts = 0

while attempts < 3:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and bcrypt.checkpw(
        password.encode(),
        stored_password
    ):
        print("Login Successful")
        break
    else:
        attempts += 1
        print(f"Login Failed. Attempts left: {3-attempts}")

if attempts == 3:
    print("Account Locked")
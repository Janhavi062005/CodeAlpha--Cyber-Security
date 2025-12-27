# Intentionally insecure login example

username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials (BAD PRACTICE)
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid credentials")
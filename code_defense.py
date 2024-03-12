import re
import secrets
import hashlib
import os

def main():
    get_passwords()
    print("very good")

def prompt_for_password(message):
    print(message)
    password = input()

    pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[\\.,!\\?'\";:-])(?!.*[a-z]{4,}).{10,}$"
    if re.search(pattern, password):
        return password
    return prompt_for_password("Invalid password. Please try again.")

def hash_password(password, salt):
    password_bytes = password.encode("utf-8") 
    hash_object = hashlib.sha256(password_bytes + bytes(salt, "utf-8"))
    return hash_object.hexdigest()

def store_password():
    password = prompt_for_password("Please provide a password.")

    salt = secrets.token_hex(32)
    hash = hash_password(password, salt)
    
    file = open("./resources/password.txt", "w")
    file.write(salt)
    file.write("\n" + hash)
    file.close()

def compare_password():
    password = prompt_for_password("Please re-enter your password.")
    
    if not os.path.exists("./resources/password.txt"):
        return get_passwords()

    file = open("./resources/password.txt", "r")
    salt = file.readline().strip()
    hash = file.readline()
    file.close()

    if not salt or not hash:
        return get_passwords()
    
    if hash != hash_password(password, salt):
        compare_password()

def get_passwords():
    store_password()
    compare_password()

main()


    




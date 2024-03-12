# TCSS 483
# Defend Your Code
# Caleb Krauter, Nathan Hinthorne, Trae Claar

import re
import hashlib
import secrets
import os

def mismatched_input(input, regex):
    pattern = re.compile(regex)
    return not re.match(pattern, input)

def log_problem(message):
    file = open("resources/log.txt", "a")
    file.write("\n" + message)
    file.close()

def prompt_for_name(first_or_last):
    print("Please provide your " + first_or_last + " name.")
    print("Must be between 1-50 characters and contain only letters and numbers.")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z]{1,50}$")):
        print("Not a valid name. Please try again.")
        log_problem("Invalid name entered: " + name)
        return prompt_for_name(first_or_last)
    
    return name


def prompt_for_int():
    min = -(2**31)
    max = 2**31 - 1

    value = 0
    try:
        value = int(input("Please provide a 4 byte integer."))
    except:
        print("Not an integer. Please try again.")
        log_problem("Invalid integer: " + str(value))
        return prompt_for_int()

    if (value < min or value > max):
        print("Integer was too many bytes. Please try again.")
        log_problem("Integer out of bounds: " + str(value))
        return prompt_for_int()

    return value

def prompt_for_input_file_name():
    print("Please provide the input file name.")
    print("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z0-9]{1,50}.txt$")):
        print("Not a valid file name. Please try again.")
        log_problem("Invalid input file name: " + name)
        return prompt_for_input_file_name()
    
    return name

def prompt_for_output_file_name(input_file_name):
    print("Please provide the output file name.")
    print("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z0-9]{1,50}.txt$") or name == input_file_name):
        print("Not a valid file name. Please try again.")
        log_problem("Invalid output file name: " + name)
        return prompt_for_output_file_name(input_file_name)
    
    return name

def prompt_for_password(message):
    print(message)
    password = input()

    pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[\\.,!\\?'\";:-])(?!.*[a-z]{4,}).{10,}$"
    if re.search(pattern, password):
        return password
    
    log_problem("Invalid password: " + password)
    return prompt_for_password("Invalid password. Please try again.")

def hash_password(password, salt):
    password_bytes = password.encode("utf-8") 
    hash_object = hashlib.sha256(password_bytes + bytes(salt, "utf-8"))
    return hash_object.hexdigest()

def store_password():
    password = prompt_for_password("Please provide a password. \n"
                                   + "Must be at least 10 characters long and contain at "
                                   + "least 1 uppercase character, lowercase character, digit, "
                                   + "punctuation mark, and must not have more than 3 consecutive "
                                   + "lowercase characters.")

    salt = secrets.token_hex(32)
    hash = hash_password(password, salt)
    
    file = open("./resources/password.txt", "w")
    file.write(salt)
    file.write("\n" + hash)
    file.close()

def compare_password():
    password = prompt_for_password("Please re-enter your password.")
    
    if not os.path.exists("./resources/password.txt"):
        log_problem("Password file not found. Reprompting.")
        return get_passwords()

    file = open("./resources/password.txt", "r")
    salt = file.readline().strip()
    hash = file.readline()
    file.close()

    if not salt or not hash:
        log_problem("Salt or hash not found. Reprompting.")
        return get_passwords()
    
    hash2 = hash_password(password, salt)
    if hash != hash_password(password, salt):
        log_problem("Password hashes (" + hash + ", " + hash2 + ") do not match.")
        compare_password()

def get_passwords():
    store_password()
    compare_password()

def write_to_file(first_name, last_name, input_file_name, output_file_name, integer1, integer2):
    sum = integer1 + integer2
    prod = integer1 * integer2
    
    while (not os.path.exists(input_file_name)):
        log_problem("Input file not found. Reprompting.")
        input_file_name = prompt_for_input_file_name()

    fileData = ""
    with open(input_file_name, "r") as file:
        fileData = file.read()
    with open(output_file_name, "w") as file:
        file.write("First Name: " + first_name + "\n")
        file.write("Last Name: " + last_name + "\n")
        file.write("First Integer: " + str(integer1) + "\n")
        file.write("Second Integer: " + str(integer2) + "\n")
        file.write("Sum of Integers: " + str(sum) + "\n")
        file.write("Product of Integers: " + str(prod) + "\n") #+ pI)
        file.write("Input File Name Contents:\n" + fileData)
        print("Wrote to: " + output_file_name)

def main():
    first_name = prompt_for_name("first")
    last_name = prompt_for_name("last")
    integer1 = prompt_for_int()
    integer2 = prompt_for_int()
    input_file_name = prompt_for_input_file_name()
    output_file_name = prompt_for_output_file_name(input_file_name)
    get_passwords()
    write_to_file(first_name, last_name, input_file_name, output_file_name, integer1, integer2)

if __name__ == "__main__":
    main()
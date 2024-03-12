import re   # for regex


def mismatched_input(input, regex):
    pattern = re.compile(regex)
    return not re.match(pattern, input)

def prompt_for_name(first_or_last):
    print("Please provide your " + first_or_last + " name.")
    print("Must be between 1-50 characters and contain only letters and numbers.")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z0-9]{1,50}$")):
        print("Not a valid name. Please try again.")
        return prompt_for_name(first_or_last)
    
    return name

def prompt_for_int():
    min = -(2**31)
    max = 2**31 - 1

    print("Please provide a 4 byte integer.")
    value = int(input())

    while (value < min or value > max):
        print("Integer was too many bytes. Please try again.")
        value = int(input())

    return value

def prompt_for_input_file_name():
    print("Please provide the input file name.")
    print("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z0-9]{1,50}.txt$")):
        print("Not a valid file name. Please try again.")
        return prompt_for_input_file_name()
    
    return name

def prompt_for_output_file_name(input_file_name):
    print("Please provide the output file name.")
    print("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters")

    name = input()

    if (mismatched_input(name, "^[a-zA-Z0-9]{1,50}.txt$") or name == input_file_name):
        print("Not a valid file name. Please try again.")
        return prompt_for_input_file_name(input_file_name)
    
    return name
    

def main():
    first_name = prompt_for_name("first")
    last_name = prompt_for_name("last")
    input_file_name = prompt_for_input_file_name()
    output_file_name = prompt_for_output_file_name(input_file_name)
    integer = prompt_for_int()

    # Debugging
    print("First Name: " + first_name)
    print("Last Name: " + last_name)
    print("Input File Name: " + input_file_name)
    print("Output File Name: " + output_file_name)
    print("Integer: " + str(integer))
    

if __name__ == "__main__":
    main()

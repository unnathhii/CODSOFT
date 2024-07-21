import random
import string

def generate_password(length):
    #generating password using the possible random characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    #ask user for the length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")
if __name__ == "__main__":
    main()

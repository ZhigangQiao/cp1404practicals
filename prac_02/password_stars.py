MIN_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print_stars(password)

# Removed method_name function and global declaration

def get_password():
    while True:
        password = input("Enter your password: ")
        if len(password) >= MIN_PASSWORD_LENGTH:
            return password
        else:
            print("Password is too short. Minimum length is", MIN_PASSWORD_LENGTH)

def print_stars(password):
    print("*" * len(password))

if __name__ == "__main__":
    main()
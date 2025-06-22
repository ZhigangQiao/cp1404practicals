def extract_name(email):
    """
    Extracts the name from an email address.
    """
    username = email.split('@')[0]
    name_parts = username.split('.')
    capitalized_name = ' '.join(name_parts).title()
    return capitalized_name

def main():
    """
    Main function to collect emails and names from users.
    """
    email_dict = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        name = extract_name(email)
        is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if is_name_correct == '' or is_name_correct == 'y':
            email_dict[email] = name
        else:
            name = input("Name: ").strip().title()
            email_dict[email] = name

    print("\nEmails and Names:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()

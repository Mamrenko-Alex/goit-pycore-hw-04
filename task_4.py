def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid format. Use 'add [name] [phone]'."
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid format. Use 'change [name] [new_phone]'."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    return f"Error: Contact {name} not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid format. Use 'phone [name]'."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Error: Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    commands = [
        "hello", "add", "change", "phone", "all", "close", "exit"
    ]
    # user inputs for testing
    test_inputs = [
        "hello",
        "add John 12345",
        "phone John",
        "change John 67890",
        "phone John",
        "all",
        "close"
    ]

    for user_input in test_inputs:
        print(f"Command: {user_input}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

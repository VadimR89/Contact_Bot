def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"

    return wrapper


contacts = {}  # Словник для зберігання контактів


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added contact: {name} - {phone}"


@input_error
def change_phone(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        return f"Contact {name} not found"


@input_error
def show_phone(name):
    if name in contacts:
        return f"{name}'s phone: {contacts[name]}"
    else:
        return f"Contact {name} not found"


def show_all():
    if contacts:
        return "\n".join([f"{name} - {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found"


def run():
    while True:
        command = input("Enter a command: ").lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            response = add_contact(command)
            print(response)
        elif command.startswith("change "):
            response = change_phone(command)
            print(response)
        elif command.startswith("phone "):
            name = command.split(" ", 1)[1]
            response = show_phone(name)
            print(response)
        elif command == "show all":
            response = show_all()
            print(response)
        else:
            print("Invalid command")


if __name__ == "__main__":
    run()

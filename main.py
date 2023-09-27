contacts ={}

#Обробка помилок введених користувачем
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter username'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Invalid input'

    return inner



#Функція для збереження у пам'яті (у словнику) новий контакт.
@input_error
def add_contact(user_input):
    _, name, phone = user_input.split()
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"

#Функція для збереження нового номера телефону до збереженого контакту.
@input_error
def change_number(user_input):
    _, name, phone = user_input.split()
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} changed number to{phone}"
    else:
        return f"Contact {name} not found"



#Функція для виводу номера телефону для зазначеного контакту
@input_error
def get_contact(user_input):
    _, name, phone = user_input.split()
    if name in contacts:
        return f"Phon number for {name} is {contacts[phone]}"
    else:
        return f"Contact {name} not found"

#Функція для виводу віх збережених контактів
@input_error
def show_all_contacts(user_input):
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return 'No contacts'


@input_error
def main():
    print("Список команд:\n "
          "'hello' - відповідає у консоль 'How can I help you?',\n "
          "'add' - зберігає у пам'яті новий контакт,\n "
          "'change'- зберігає в пам'яті новий номер телефону збереженого контакту,\n "
          "'phone'- виводить у консоль номер телефону для зазначеного контакту,\n "
          "'show all'- виводить всі збереженні контакти з номерами телефонів, \n "
          "'good bye','close','exit', 'stop'- завершення роботи")

    while True:
        user_input = input(">>>").lower()

        if user_input == 'good bye' or user_input == 'exit' or user_input == 'close' or user_input == 'stop':
            print('Good bye!')
            break

        elif user_input == 'hello':
            print('How can I help you?')

        #За цією командою бот зберігає у пам'яті (у словнику) новий контакт.
        elif user_input.startswith('add'):
           print(add_contact(user_input))

        #За цією командою бот зберігає в пам'яті новий номер телефону збереженого контакту.
        elif user_input.startswith('change'):
           print(change_number(user_input))

        #За цією командою бот виводить у консоль номер телефону для зазначеного контакту.
        elif user_input.startswith('phone'):
           print(get_contact(user_input))

        #За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
        elif user_input == 'show all':
           print(show_all_contacts(user_input))

        else:
           print('Invalid command, try again')





if __name__ == '__main__':
    main()
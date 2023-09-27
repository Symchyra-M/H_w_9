contacts ={} # Словник для зберігання контактів

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
        user_input = input("Enter a command: ").lower()

        if user_input in ['good bye', 'exit', 'close', 'stop']:
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
            print(show_all_contacts())

        else:
            print('Invalid command, try again')



#Функція для збереження у пам'яті (у словнику) новий контакт.
@input_error
def add_contact(data):
    words = data.split(' ')
    if len(words) == 3 :
        contacts[words[1]] = words[2]
        return f"Contact {words[1]} added with phone {words[2]}"
    else:
        raise ValueError


#Функція для збереження нового номера телефону до збереженого контакту.
@input_error
def change_number(data):
    if contacts:
        words = data.split(' ')
        if len(words) == 3:
            if words[1] in contacts:
                contacts[words[1]] = words[2]
                return f"Contact {words[1]} changed number to {words[2]}"
            else:
                return f"Contact {words[1]} not found"
        else:
            raise ValueError
    else:
        return 'No contacts'



# Функція для виводу номера телефону для зазначеного контакту
@input_error
def get_contact(data):
    if contacts:
        words = data.split(' ')
        if len(words) == 2:
            if words[1] in contacts:
                return f"Phon number for {words[1]} is {contacts[words[1]]}"
            else:
                return f"Contact {words[1]} not found"
        else:
            raise KeyError
    else:
        return 'No contacts'


#Функція для виводу віх збережених контактів
@input_error
def show_all_contacts():
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return 'No contacts'




if __name__ == '__main__':
    main()
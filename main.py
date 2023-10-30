# Encoder & Main Function by Willian Acosta Cruz
class InvalidLengthError(Exception):
    def __init__(self):
        self.add_note("Length of password must be eight characters!")
def MainMenu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    print()

def encoder(password):
    p = ''
    if len(password) != 8:
        raise InvalidLengthError
    for i in password:
        i = int(i)
        if i <= 6:
            i += 3
        else:
            i -= 7
        p += str(i)

    return p

def decoder(enc_pass):
    pass

t = -1

while t != 3:
   MainMenu()
   user_input = input('Please enter an option: ')
   if user_input == '1':
        p_f_e = input('Please enter your password to encode: ')
        try:
            encoded_pass = encoder(p_f_e)
        except:
            print("Password must not contain letters!")
            continue
        print('Your password has been encoded and stored! \n \n')
   if user_input == '2':
       print(f'The encoded password is {encoded_pass}, and the original password is {decoder(encoded_pass)}. \n \n')
   if user_input == '3':
       t = 3

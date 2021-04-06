
""" This is a crypter made by Jordy v. Dongen

    This crypter works by adding "cryptors" (encryption for a word) for each word the user wants.
    The 'add_encryptor' function adds the inputted word from the user to a text file and adds a randomly
    generated cryptor next to it.

    - EXAMPLE -
    Normal_word = J/D*&S

    Here you see the original word and the cryptor separated by an '='.
    This is how they are stored in a text file.

    The user can add cryptors manually by

    For extra security random (useless) words are generated in the beginning and end of the encrypted sentence.
    This is so it is not possible to be able to know the number of words there are in the sentence as the
    encrypted sentences have different amounts of words than the original sentence.

    When a sentence is being encrypted but no cryptor has been made for the word it will use the original word.
    THIS CAN SHOW INFORMATION YOU DON'T WANT TO SHOW, therefore always check your encrypted sentence and create
    cryptors for the words no cryptors have been made yet.

    The same is for decrypting: when the word can not be found in the txt, it will not change. It will be added back
    to the end decrypted sentence without changing.

    This does mean that if you do not want to encrypt a word, it does not harm in any way as the decrypter still can
    handle it.

    The very first word of the encrypted sentence contains the information on which words need to be decrypted and which
    were randomly generated.
    This is helpful for the decrypter as it will only show the user the words it needs to show, so the user
    won't see any unnecessary information in their decrypted sentences.

    This encryption method is designed so even if (somehow) 1 word has been decrypted, it is impossible to decrypt
    the rest of the sentence without help of this program and the txt file.

    This program can handle a 1000kb txt file and still encrypt AND decrypt under a second
    (depending on the sentence obviously).

    NOTE:
        This is the first version of this crypter and things surely can be improved.
        This was just a project for me to cure my boredom for a while, this was not taken very seriously.

    To-do:
        Be able to use "!" (btw, don't use that now. It won't encrypt the word it is connected to.)
        Make the cryptor more secure by changing the entire idea without txt file and simply create a new enigma.

"""
__author__ = '@JoJo.v.Dongen'
__version__ = '1.0'


import random

def encrypt(message):
    """
    Encrypts the message by using the cryptors in the word.txt if a word has no cryptor the original word will
    stay in the encryption.
    """

    assert isinstance(message, str), 'Only encrypt strings only!'

    code = first_code_word()
    encrypted_message = ''
    message = message.lower()
    final_dot = False
    final_question = False
    final_comma = False
    final_dot_counter = 0
    final_question_counter = 0
    final_comma_counter = 0

    splitted_code = list(code)


    message = code + " " + message

    while message[-1] == '.':
        message = message[:-1]
        final_dot = True
        final_dot_counter += 1

    while message[-1] == '?':
        message = message[:-1]
        final_question = True
        final_question_counter += 1


    while message[-1] == ',':
        message = message[:-1]
        final_comma = True
        final_comma_counter += 1

    counter = 0
    for message_word in message.split():
        counter += 1
        checked = False
        middle_dot = False
        middle_question = False
        middle_comma = False
        middle_dot_counter = 0
        middle_question_counter = 0
        middle_comma_counter = 0

        if counter == 2:
            for i in range(0, int(splitted_code[0])):
                word = create_encryptors()
                encrypted_message += str(word) + " "

        while message_word[-1] == '.':
            message_word = message_word[:-1]
            middle_dot = True
            middle_dot_counter += 1

        while message_word[-1] == '?':
            message_word = message_word[:-1]
            middle_question = True
            middle_question_counter += 1


        while message_word[-1] == ',':
            message_word = message_word[:-1]
            middle_comma = True
            middle_comma_counter += 1

        text = open("words.txt", "r")
        for line in text:
            text_word = line.split()[0]
            if message_word[0] == text_word[0]:
                if message_word == text_word:
                    encrypted_message += line.split()[2] + " "
                    if middle_dot == True: encrypted_message = encrypted_message[:-1] + "."*middle_dot_counter + " "
                    if middle_question == True: encrypted_message = encrypted_message[:-1] + "?"*middle_question_counter + " "
                    if middle_comma == True: encrypted_message = encrypted_message[:-1] + ","*middle_comma_counter + " "
                    checked = True
                    break

        if checked != True:
            encrypted_message += message_word + " "
            if middle_dot == True: encrypted_message = encrypted_message[:-1] + "." * middle_dot_counter + " "
            if middle_question == True: encrypted_message = encrypted_message[:-1] + "?" * middle_question_counter + " "
            if middle_comma == True: encrypted_message = encrypted_message[:-1] + "," * middle_comma_counter + " "

        text.close()

    encrypted_message = encrypted_message[:-1]
    if final_dot == True:
        encrypted_message += '.'*final_dot_counter + ' '
    elif final_question == True:
        encrypted_message += '?'*final_question_counter + ' '
    elif final_comma == True:
        encrypted_message += ','*final_comma_counter + ' '
    else: encrypted_message += ' '

    for i in range(0, int(splitted_code[2])):
        word = create_encryptors()
        encrypted_message += word + " "
    encrypted_message = encrypted_message[:-1]
    return encrypted_message

def decrypt(message):
    """
    Decrypts the message by using the cryptors in the word.txt if a cryptor has no word the cryptor will
    stay in the decryption.
    """

    assert isinstance(message, str), 'Only encrypt strings only!'
    decrypted_message = ''

    final_dot = False
    final_question = False
    final_comma = False
    final_dot_counter = 0
    final_question_counter = 0
    final_comma_counter = 0

    while message[-1] == '.':
        message = message[:-1]
        final_dot = True
        final_dot_counter += 1

    while message[-1] == '?':
        message = message[:-1]
        final_question = True
        final_question_counter += 1

    while message[-1] == ',':
        message = message[:-1]
        final_comma = True
        final_comma_counter += 1


    for message_word in message.split():
        file = open("words.txt", "r")
        checked = False
        middle_dot = False
        middle_question = False
        middle_comma = False
        middle_dot_counter = 0
        middle_question_counter = 0
        middle_comma_counter = 0

        while message_word[-1] == '.':
            message_word = message_word[:-1]
            middle_dot = True
            middle_dot_counter += 1

        while message_word[-1] == '?':
            message_word = message_word[:-1]
            middle_question = True
            middle_question_counter += 1


        while message_word[-1] == ',':
            message_word = message_word[:-1]
            middle_comma = True
            middle_comma_counter += 1

        for line in file:
            file_word = line.split()[2]
            if message_word == file_word:
                decrypted_message += line.split()[0] + " "
                if middle_dot == True: decrypted_message = decrypted_message[:-1] + "." * middle_dot_counter + " "
                if middle_question == True: decrypted_message = decrypted_message[:-1] + "?" * middle_question_counter + " "
                if middle_comma == True: decrypted_message = decrypted_message[:-1] + "," * middle_comma_counter + " "
                checked = True
                break

        if checked != True:
            decrypted_message += message_word + " "
            if middle_dot == True: decrypted_message = decrypted_message[:-1] + "." * middle_dot_counter + " "
            if middle_question == True: decrypted_message = decrypted_message[:-1] + "?" * middle_question_counter + " "
            if middle_comma == True: decrypted_message = decrypted_message[:-1] + "," * middle_comma_counter + " "
        file.close()

    decrypted_message = decrypted_message[:-1]
    if final_dot == True:
        decrypted_message += '.'*final_dot_counter
    elif final_question == True:
        decrypted_message += '?'*final_question_counter
    elif final_comma == True:
        decrypted_message += ','*final_comma_counter


    first_num = int(decrypted_message[0]) + 1
    third_num = int(decrypted_message[2])


    decrypted_message = decrypted_message.split(' ', first_num)[first_num]
    decrypted_message = ' '.join(decrypted_message.split()[:-third_num])

    return decrypted_message

def create_encryptors():
    """
    Creates a random cryptor for a word, truly random from the chars list. recreates if cryptor already exists.
    """

    chars = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\()*+-:;<=>@[]^_`{}~.,?')
    almost = ''.join(random.choice(chars) for _ in range(0, random.randint(3, 6)))
    if almost[-1] == "." or almost[-1] == "?" or almost[-1] == ",":
        almost = almost[:-1]
        almost += random.choice(["'}", "{@"])
    return almost

def add_encryptors(word):
    """
    Writes the new encryptor to the word.txt and saves it for later use. Also checks for requirements.
    """

    assert isinstance(word, str), 'Strings only!'
    if word == "": return None
    file = open(r'words.txt', 'r')
    for line in file:
        first_word = line.split()[0]
        if word == first_word:
            print('Error, word is already added to the list!')
            return 'Error, word is already added to the list!'
    file.close()


    new_encryption = str(create_encryptors())
    blank = True
    while blank == True:
        file = open(r'words.txt', 'r')
        blank = False
        for line in file:
            if new_encryption == line.split()[2]:
                new_encryption = str(create_encryptors())
                blank = True
                file.close()
                break
        file.close()


    if len(word) < 4: tabs = 3
    elif len(word) <8: tabs = 2
    else: tabs = 1

    file = open(r'words.txt', 'a')
    file.write(word + '\t'*tabs + "= " + new_encryption + "\n")

def add_multiple_encryptors():
    """
    Allows the user to input words to create cryptors for until the user types "exit".
    """

    print('Type "exit" to stop adding encryptors!')
    word = ''
    while word != 'exit':
        word = input('enter cryptor: ').lower()
        if word.isspace() or word == '' or word == 'exit':
            pass
        else:
            add_encryptors(word)

def first_code_word():
    """
    Random amounts of words are added in front and end of the encrypted sentence. this function
    creates the first word which will help the decryption program to know which words to use and which not.
    """

    code = ''.join(f'{random.randint(1, 3)}f{random.randint(1,3)}e')
    return code

def add_cryptors_from_file(filename):
    """
    Iterates through a txt file and creates a cryptor for each word in the txt file.
    """

    file = open(filename, 'r')
    counter = 0
    for line in file:
        counter+=1
        if counter in [5000, 15000, 20000, 25000]:
            print(counter)
        line = line.split()
        add_encryptors(line[0].lower())


message_to_encrypt = "Hello there, this is a test."     #This is the original message
encrypted_sentence = encrypt(message_to_encrypt)
print("encrypted message: " + encrypted_sentence)
message_to_decrypt = encrypted_sentence
decrypted_sentence = decrypt(message_to_decrypt)
print("decrypted message: " + decrypted_sentence)       #This should be the same as the original message

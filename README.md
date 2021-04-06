# JoJos-Crypter
Simple encrypter / decrypter. Not incredibly secure and unnecessary complicated.

## This is a crypter made by Jordy v. Dongen

This crypter works by adding `cryptors` (encryption for a word) for each word the user wants.
The `add_encryptor` function adds the inputted word from the user to a text file and adds a randomly
generated cryptor next to it.

**EXAMPLE**\
*Normal_word = J/D*&S*

Here you see the original word and the cryptor separated by an '='.
This is how they are stored in a text file.

The user can add cryptors manually by using `add_encryptors(word)` to add 1 word to the txt file.\
Or the user can simply call the `add_multiple_encryptors()` function which asks the user for input to add to the txt file until "exit" has been given.
If the user has a txt file with words to make cryptors for, they can call the `add_cryptors_from_file(filename)` function and insert the filename as a string.

For extra security, random (useless) words are generated in the beginning and end of the encrypted sentence.
This is so it is not possible to be able to know the number of words there are in the sentence, as the
encrypted sentences have different amounts of words than the original sentence.

When a sentence is being encrypted but no cryptor has been made for the word it will use the original word.
THIS CAN SHOW INFORMATION YOU DON'T WANT TO SHOW, therefore always check your encrypted sentence and create
cryptors for the words no cryptors have been made yet.

The same is for decrypting: when the word can not be found in the txt, it will not change. It will be added back
to the end decrypted sentence without changing.

This does mean that if you do not want to encrypt a word, it does not harm in any way as the decrypter still can
handle it.

The very first word of the encrypted sentence contains the information on which words need to be decrypted and which
were randomly generated. This is made in the `first_code_word()` function.
This is helpful for the decrypter as it will only show the user the words it needs to show, so the user
won't see any unnecessary information in their decrypted sentences.

This encryption method is designed so even if (somehow) 1 word has been decrypted, it is impossible to decrypt
the rest of the sentence without help of this program and the txt file.

### Speed:
This program can handle a 1000kb txt file and still encrypt AND decrypt under a second
(depending on the sentence obviously).

### Note:
- This is the first version of this crypter and things surely can be improved.
- This was just a project for me to cure my boredom for a while, this was not taken very seriously.

### To-do's:
- Make the user be able to use "!" (btw, don't use that now. It won't encrypt the word it is connected to.)
- Make the cryptor more secure by changing the entire idea without txt file and simply create a new enigma.

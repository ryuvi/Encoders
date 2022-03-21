# INIT PROJECT CAESAR

import random

message_sent = open('sent.txt', 'a')
message_received = open('received.txt', 'a')
lAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u",
             "v", "w", "x", "y", "z"]

nCipherLevel = random.randint(0, 25)


def set_cipher_alphabet(n_cipher_level):
    l_temp_alphabet = []
    n_temp_alphabet_index = n_cipher_level
    while n_temp_alphabet_index < len(lAlphabet):
        l_temp_alphabet.append(lAlphabet[n_temp_alphabet_index])
        n_temp_alphabet_index += 1

    n_temp_alphabet_index = 0
    while n_temp_alphabet_index < n_cipher_level:
        l_temp_alphabet.append(lAlphabet[n_temp_alphabet_index])
        n_temp_alphabet_index += 1

    return l_temp_alphabet


def init():
    cipher_alphabet = set_cipher_alphabet(nCipherLevel)
    s_option = input('Want to [1]encode or [2]decode? ')

    if s_option in ('1', 'encode'):
        print('Insert the message:')
        s_message = input('> ')
        encode(s_message.lower(), cipher_alphabet)

    elif s_option in ('2', 'decode'):
        print('Insert the message:')
        s_message = input('> ')
        decode(s_message.lower())

    else:
        init()


def grab_letter_encode(p_s_letter, ciphered_alphabet):
    n_index = 0

    for s_char in lAlphabet:
        if p_s_letter == s_char:
            return ciphered_alphabet[n_index]

        n_index += 1


def grab_letter_decode(p_s_letter, ciphered_alphabet):
    n_index = 0

    for s_char in ciphered_alphabet:
        if p_s_letter == s_char:
            return lAlphabet[n_index]

        n_index += 1


def encode(p_s_message, ciphered_alphabet):
    s_result = ''

    for s_char in p_s_message:
        if s_char != ' ':
            s_result += grab_letter_encode(s_char, ciphered_alphabet)

        else:
            s_result += s_char

    message_sent.write(f"""The message encrypted: {s_result}\nThe cypher level used: {nCipherLevel}
The result to send: {nCipherLevel} {s_result}\n\n --- \n""")


def decode(p_s_message):
    s_result = ''
    p_l_message = p_s_message.split(' ')
    n_message_cipher_level = int(p_l_message[0])
    n_index = 1
    l_cipher_alphabet = set_cipher_alphabet(n_message_cipher_level)

    while n_index < len(p_l_message):
        for s_char in p_l_message[n_index]:
            s_result += grab_letter_decode(s_char, l_cipher_alphabet)

        if n_index != len(p_l_message)-1:
            s_result += ' '

        n_index += 1

    message_received.write(
        f'The decrypted message: {s_result}\nThe cypher level used: {n_message_cipher_level}\n\n --- \n')


init()

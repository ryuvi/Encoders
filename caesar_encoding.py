import random

message_sent = open('sent.txt', 'a')
message_received = open('received.txt', 'a')
lAlphabet = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w",
     "x", "y", "z"],
    ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x",
     "y", "z", "a"],
    ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y",
     "z", "a", "b"],
    ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z",
     "a", "b", "c"],
    ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a",
     "b", "c", "d"],
    ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b",
     "c", "d", "e"],
    ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c",
     "d", "e", "f"],
    ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
     "e", "f", "g"],
    ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e",
     "f", "g", "h"],
    ["j", "k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f",
     "g", "h", "i"],
    ["k", "l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g",
     "h", "i", "j"],
    ["l", "m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
     "i", "j", "k"],
    ["m", "n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
     "j", "k", "l"],
    ["n", "o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
     "k", "l", "m"],
    ["o", "p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
     "l", "m", "n"],
    ["p", "q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
     "m", "n", "o"],
    ["q", "r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p"],
    ["r", 's', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
     "o", "p", "q"],
    ['s', "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
     "p", "q", "r"],
    ["t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
     "q", "r", "s"],
    ["u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
     "r", "s", "t"],
    ["v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
     "s", "t", "u"],
    ["w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
     "t", "u", "v"],
    ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
     "u", "v", "w"],
    ["y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
     "v", "w", "x"],
    ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
     "w", "x", "y"],
]
nCipherLevel = random.randint(0, 25)


def init():
    s_option = input('Want to [1]encode or [2]decode? ')

    if s_option in ('1', 'encode'):
        print('Insert the message:')
        s_message = input('> ')
        encode(s_message.lower())

    elif s_option in ('2', 'decode'):
        print('Insert the message:')
        s_message = input('> ')
        decode(s_message.lower())

    else:
        init()


def grab_letter_encode(p_s_letter):
    n_index = 0

    for s_char in lAlphabet[0]:
        if p_s_letter == s_char:
            return lAlphabet[nCipherLevel][n_index]

        n_index += 1


def grab_letter_decode(p_s_letter, cipher_level):
    n_index = 0

    for s_char in lAlphabet[cipher_level]:
        if p_s_letter == s_char:
            return lAlphabet[0][n_index]

        n_index += 1


def encode(p_s_message):
    s_result = ''

    for s_char in p_s_message:
        if s_char != ' ':
            s_result += grab_letter_encode(s_char)

        else:
            s_result += s_char

    message_sent.write(f"""The message encrypted: {s_result}\nThe cypher level used: {nCipherLevel}
The result to send: {nCipherLevel} {s_result}\n\n --- \n""")


def decode(p_s_message):
    s_result = ''
    p_l_message = p_s_message.split(' ')
    n_message_cipher_level = int(p_l_message[0])
    n_index = 1

    while n_index < len(p_l_message):
        for s_char in p_l_message[n_index]:
            s_result += grab_letter_decode(s_char, n_message_cipher_level)

        if n_index != len(p_l_message)-1:
            s_result += ' '

        n_index += 1

    message_received.write(
        f'The decrypted message: {s_result}\nThe cypher level used: {n_message_cipher_level}\n\n --- \n')


init()

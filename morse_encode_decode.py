alphabet_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.---.',
    '!': '-.---',
    '`': '.----.',
    '"': '.-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '/': '-..-.',
    '_': '..--.-',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}
morse_alphabet = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': "e",
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.---.': "'",
    '-.---': '!',
    '.----.': '`',
    '.-..-.': '"',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-..-.': '/',
    '..--.-': '_',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '...-..-': '$',
    '.--.-.': '@',
    '/': ' '
}


def init():
    print("Do you want to [1]encode or [2]decode?")
    answer = input('> ')

    if answer in ('1', 'encode'):

        if is_from_file() == 'file':
            print('Insert file name:')
            file_name = input('> ')
            file_read = open(file_name, 'r')
            for line in file_read:
                encode(line)

        else:
            print('Enter the message:')
            message = input('> ')

            encode(message)

    elif answer in ('2', 'decode'):

        if is_from_file() == 'file':
            print('Insert file name:')
            file_name = input('> ')
            file_read = open(file_name, 'r')
            for line in file_read:
                decode(line)

        else:
            print('Enter the message:')
            message = input('> ')

            decode(message)

    else:
        print('Invalid input!')
        init()


def is_from_file():
    print('Do you want to [1]read a file or [2]write the message?')
    answer = input('> ')

    if answer in ('1', 'read a file', 'read'):
        return 'file'

    elif answer in ('2', 'write the message', 'write'):
        return 'message'

    else:
        print('Invalid Option!')
        is_from_file()


def encode(text):
    result = ''

    for index, char in enumerate(text):
        if index == len(text)-1:
            result += alphabet_morse[char]
        else:
            result += alphabet_morse[char] + ' '

    file = open('encoded.txt', 'a')
    file.write(result+'\n')
    file.close()

    return result


def decode(text):
    result = ''
    split_string = text.split(' ')

    for word in split_string:
        result += morse_alphabet[word]

    file = open('decoded.txt', 'a')
    file.write(result+'\n')
    file.close()

    return result


message_de = "some text"
message_en = "... --- -- . / - . -..- -"
#print(encode(message_de))
#print(decode(message_en))
init()

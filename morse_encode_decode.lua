alphabet_morse = {
    ['a'] = '.-',
    ['b'] = '-...',
    ['c'] = '-.-.',
    ['d'] = '-..',
    ['e'] = '.',
    ['f'] = '..-.',
    ['g'] = '--.',
    ['h'] = '....',
    ['i'] = '..',
    ['j'] = '.---',
    ['k'] = '-.-',
    ['l'] = '.-..',
    ['m'] = '--',
    ['n'] = '-.',
    ['o'] = '---',
    ['p'] = '.--.',
    ['q'] = '--.-',
    ['r'] = '.-.',
    ['s'] = '...',
    ['t'] = '-',
    ['u'] = '..-',
    ['v'] = '...-',
    ['w'] = '.--',
    ['x'] = '-..-',
    ['y'] = '-.--',
    ['z'] = '--..',
    ['.'] = '.-.-.-',
    [','] = '--..--',
    ['?'] = '..--..',
    ["'"] = '.---.',
    ['!'] = '-.---',
    ['`'] = '.----.',
    ['"'] = '.-..-.',
    ['('] = '-.--.',
    [')'] = '-.--.-',
    ['&'] = '.-...',
    [':'] = '---...',
    [';'] = '-.-.-.',
    ['/'] = '-..-.',
    ['_'] = '..--.-',
    ['='] = '-...-',
    ['+'] = '.-.-.',
    ['-'] = '-....-',
    ['$'] = '...-..-',
    ['@'] = '.--.-.',
    [' '] = '/'
}

morse_alphabet = {
    ['.-'] = 'a',
    ['-...'] = 'b',
    ['-.-.'] = 'c',
    ['-..'] = 'd',
    ['.'] = "e",
    ['..-.'] = 'f',
    ['--.'] = 'g',
    ['....'] = 'h',
    ['..'] = 'i',
    ['.---'] = 'j',
    ['-.-'] = 'k',
    ['.-..'] = 'l',
    ['--'] = 'm',
    ['-.'] = 'n',
    ['---'] = 'o',
    ['.--.'] = 'p',
    ['--.-'] = 'q',
    ['.-.'] = 'r',
    ['...'] = 's',
    ['-'] = 't',
    ['..-'] = 'u',
    ['...-'] = 'v',
    ['.--'] = 'w',
    ['-..-'] = 'x',
    ['-.--'] = 'y',
    ['--..'] = 'z',
    ['.-.-.-'] = '.',
    [ '--..--' ] = ',',
    [ '..--..' ] = '?',
    [ '.---.' ] = "'",
    [ '-.---' ] = '!',
    [ '.----.' ] = '`',
    [ '.-..-.' ] = '"',
    [ '-.--.' ] = '(',
    [ '-.--.-' ] = ')',
    [ '.-...' ] = '&',
    [ '---...' ] = ':',
    [ '-.-.-.' ] = ';',
    [ '-..-.' ] = '/',
    [ '..--.-' ] = '_',
    [ '-...-' ] = '=',
    [ '.-.-.' ] = '+',
    [ '-....-' ] = '-',
    [ '...-..-' ] = '$',
    [ '.--.-.' ] = '@',
    ['/'] = ' '
}

function init()
    print("Do you want to [1]encode or [2]decode? ")
    answer = io.read()

    if answer == 'encode' or answer == '1' then
        print('Enter the message:')
        message = io.read()

        encode(message)
    
    elseif answer == 'decode' or answer == '2' then
        print('Enter the message:')
        message = io.read()

        decode(message)
    
    else
        print('Wrong input')
        init()
    
    end
end


message_de = "some text"
message_en = "... --- -- . / - . -..- -"

function encode(text)
    local result = ''
    
    for char in text:gmatch"." do
        result = result .. alphabet_morse[char] .. ' '
    end

    print(result)
    
    file = io.open('encoded.txt', 'a+')
    file:write(result)
    file:close()

    return result
end

function string_to_array(str, arr)
    local word = ''
    str = str .. ' '
    
    for chr in str:gmatch"." do
    
        if chr ~= " " then
            word = word .. chr
    
        else
            table.insert(arr, word)
            word = ''
    
        end
    end
end

function decode(text)
    local result = ''
    local splited_string = {}
    string_to_array(text, splited_string)

    for i, f in pairs(splited_string) do
        print(morse_alphabet[f])
        result = result .. morse_alphabet[f]
    end

    file = io.open('decoded.txt', 'a+')
    file:write(result)
    file:close()
            
    return result
end

print(encode(message_de))
print(decode(message_en))
--init()
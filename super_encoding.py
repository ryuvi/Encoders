text = 'some text'
# 0 , # 1 . # 2 - # 3 _ # 4 = # 5 + # 6 / # 7 * # 8 > # 9 <
l_sim = [",", ".", "-", "_", "=", "+", "/", "*", ">", "<"]
test = [83, 79, 77, 69, 32, 84, 69, 88, 84]


def init():
    s_option = input('Want to [1]encode or [2]decode? ')

    if s_option in ('1', 'encode'):
        print("Insert the text:")
        s_message = input("> ")
        encode_asc(s_message)

    elif s_option in ('2', 'decode'):
        print("Insert the text:")
        s_message = input("> ")
        decode_bin(s_message.split(' '))

    else:
        print("Invalid option!")
        init()


def encode_asc(s_message):
    l_result = []
    for char in s_message:
        l_result.append(ord(char))

    print(l_result)
    return encode_sim(l_result)


def encode_sim(l_message):
    l_result = []
    for asc in l_message:
        s_result = ''
        for num in str(asc):
            s_result += l_sim[int(num)]
        l_result.append(s_result)

    print(l_result)
    return encode_bin(l_result)


def encode_bin(l_message):
    l_result = []

    for sim in l_message:
        l_char = []
        for char in sim:
            l_char.append(int(bin(ord(char))[2:]))
        l_result.append(l_char)

    print(l_result)
    return l_result


def decode_bin(l_message):
    l_result = []

    for s_bin in l_message:
        l_bin = []
        for n_bin in s_bin:
            n_bin = int(str(n_bin), 2)
            l_bin.append(n_bin.to_bytes((n_bin.bit_length()+7)//8, 'big').decode('utf-8') or '\0')
        l_result.append(l_bin)

    print(l_result)
    return decode_sim(l_result)


def decode_sim(l_message):
    l_result = []

    for s_sim in l_message:
        l_sub_result = []
        for c_sim in s_sim:
            l_sub_result.append(l_sim.index(c_sim))
        l_result.append(l_sub_result)

    print(l_result)
    return decode_asc(l_result)


def decode_asc(l_message):
    s_result = ''

    for n_num in l_message:
        s_sub_result = ''
        for n_sub_num in n_num:
            s_sub_result += str(n_sub_num)
        s_result += chr(int(s_sub_result))

    print(s_result)
    return s_result


t = encode_asc(text)
decode_bin(t)


init()

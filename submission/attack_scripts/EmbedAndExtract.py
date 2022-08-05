# output: 1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh
# len = 64


def to_binary(string):
    """
    Convert a text to the binary representation
    :param string: the text to be converted to byte binary representation
    :return: binary representation of the string
    """
    l, m = [], []
    for i in string:
        l.append(ord(i))
    for j in l:
        m.append(bin(j)[2:])
    for k in range(len(m)):
        if len(m[k]) != 8:
            temp = 8 - len(m[k])
            m[k] = '0' * temp + m[k]
    return m
    # m = ['00110001', '01001111', '00110111', '01100001', '00110101', '01000010', '00110000', '01101110',
    # '01001011', '01101000', '01101110', '01001101', '00110100', '01101001', '01001010', '01010111', '01000010',
    # '01111010', '00101111', '01010100', '01000111', '01111001', '01101111', '01100010', '00101111', '01010110',
    # '01111000', '01001000', '01001000', '01001110', '01110001', '01010100', '01000111', '01010011', '00101011',
    # '01001011', '00101111', '01110001', '00101111', '01000010', '00101111', '01101011', '01000001', '01011010',
    # '00110010', '01000010', '01001001', '01001111', '01111010', '00110000', '01110000', '01010110', '00110010',
    # '01110101', '01110010', '01010111', '01001001', '01010101', '01001101', '01100010', '01001001', '01101000',
    # '01100110', '01101000'] len = 64


def embed_one(cipher_char, text):
    """
    :param cipher_char: the char to be embedded
    :param text: the original text
    :return: new text after embed
    """
    b = text.split()
    for i in range(8):
        temp = bin(int(b[i]))
        temp = temp[:-1] + cipher_char[i]
        b[i] = str(int(temp, 2))
    new_b = ' '.join(b)
    return new_b


def embed(cipher, filein, fileout):
    """
    Embed a cipher into a txt file
    :param cipher: the cipher to be embedded
    :param filein: original txt file
    :param fileout: embed txt file
    :return: null
    """
    fin = open(filein, 'r')
    fout = open(fileout, 'w')
    binary_cipher = to_binary(cipher)

    rounds = len(binary_cipher)
    start = 0
    plaintext = fin.readline()
    while start < rounds:
        cipher_char = binary_cipher[start]
        to_write = embed_one(cipher_char, plaintext)
        fout.write(to_write + '\n')

        start = start + 1
        plaintext = fin.readline()

    while plaintext != '':
        fout.write(plaintext)
        plaintext = fin.readline()
    fin.close()
    fout.close()


def extract_one(text):
    """
    Extract a cipher char from the text
    :param text: cipher char to be extracted from
    :return: extracted char
    """
    b = text.split()
    char = ""
    for i in range(8):
        temp = bin(int(b[i]))
        char += temp[-1]
    return char


def extract(filein):
    """
    Extract the cipher from a txt file
    :param filein: file with cipher embedded
    :return: extracted cipher
    """
    fin = open(filein, 'r')
    rounds = 64
    start = 0
    text = fin.readline()
    cipher_binary = []
    cipher = ""

    while start < rounds:
        cipher_binary.append(extract_one(text))
        start = start + 1
        text = fin.readline()
    for i in cipher_binary:
        cipher += chr(int(i, base=2))
    return cipher

# embed('1N7Z5A0mJgnL4iIVAz/SFyna/UxGGMpSFR+J/q/A/j=Y2AHNz0pU2uqVHTLaHgeg', 'body_orig.txt', 'embedding_test.txt')
# print(extract("embedding_test.txt"))
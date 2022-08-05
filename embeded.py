
# output: 1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh
# len = 64

#helper function
def To_binary(string):
    l, m = [], []
    for i in string:
        l.append(ord(i))
    for j in l:
        m.append(bin(j)[2:])
    for k in range(len(m)):
        if len(m[k]) != 8:
            temp = 8 - len(m[k])
            m[k] = '0'* temp + m[k]
    return m
    #output = ['00110001', '01001111', '00110111', '01100001', '00110101', '01000010', '00110000', '01101110', '01001011', '01101000', '01101110', 
    #'01001101', '00110100', '01101001', '01001010', '01010111', '01000010', '01111010', '00101111', '01010100', '01000111', '01111001', '01101111', 
    #'01100010', '00101111', '01010110', '01111000', '01001000', '01001000', '01001110', '01110001', '01010100', '01000111', '01010011', '00101011', 
    #'01001011', '00101111', '01110001', '00101111', '01000010', '00101111', '01101011', '01000001', '01011010', '00110010', '01000010', '01001001', 
    #'01001111', '01111010', '00110000', '01110000', '01010110', '00110010', '01110101', '01110010', '01010111', '01001001', '01010101', '01001101', 
    #'01100010', '01001001', '01101000', '01100110', '01101000']
    # len = 64


def Embeded_one(string, text):
    print("text = ", text)
    b = text.split()
    print("string = ", string)
    print("b = ", b)
    for i in range(8):
        #to binary
        temp = bin(int(b[i]))
        print("init = ", i, temp)

        temp = temp[:-1] + string[i]
        print("mod = ", i, temp)

        b[i] = str(int(temp, 2))
        #convert back 
    new_b = ' '.join(b)
    print("new_b = ", new_b)
    return new_b


def Embeded(cipher, filein, fileout):
    fin = open(filein, 'r')
    fout = open(fileout, 'w')

    #convert cipher to binary
    Binary_list = To_binary(cipher)

    #start embedding.
    round = len(Binary_list)
    start = 0
    text = fin.readline()
    while start < round:
        string = Binary_list[start]
        
        to_write = Embeded_one(string, text)
        fout.write(to_write + '\n')

        start = start + 1
        text = fin.readline()
    
    while text != '':
        fout.write(text)

        text = fin.readline()

    fin.close()
    fout.close()

def Extract_one(text):
    b = text.split()
    string = ""
    for i in range(8):
        # to binary
        temp = bin(int(b[i]))
        print("init = ", i, temp)

        string += temp[-1]

        # convert back
    print(string)
    return string

def Extract(filein):
    fin = open(filein, 'r')

    round = 64
    start = 0
    text = fin.readline()
    cipher_binary = []
    cipher = ""

    while start < round:

        cipher_binary.append(Extract_one(text))

        start = start + 1
        text = fin.readline()

    for i in cipher_binary:
        cipher += chr(int(i, base=2))

    return cipher

Embeded('1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh', 'mona_lisa.ascii.txt', 'embedding.txt')
print(Extract("embedding.txt"))




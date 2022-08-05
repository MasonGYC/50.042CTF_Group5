import base64


class VariantVigenere:
    def __init__(self):
        self._chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', "="]
        self._cipher = None
        self._plain = None

    def get_cipher(self):
        if self._cipher is None:
            raise Exception("Error: Encryptor hasn't encrypted any plaintext yet")
        return self._cipher

    def get_plain(self):
        if self._plain is None:
            raise Exception("Error: Decryptor hasn't decrypted any cipher yet")
        return self._plain

    def get_cipher_bytes(self):
        if self._cipher is None:
            raise Exception("Error: Encryptor hasn't encrypted any plaintext yet")
        return bytearray(self._cipher, "ascii")

    @staticmethod
    def string_to_base64(flag):
        flag_byte = flag.encode("utf-8")
        flag_byte_base64 = base64.b64encode(flag_byte)
        flag_base64 = flag_byte_base64.decode("utf-8")
        return flag_base64

    @staticmethod
    def base64_to_string(flag_base64):
        flag = base64.b64decode(flag_base64).decode("utf-8")
        return flag

    def get_shift_amount(self, char):
        shift_amount = self._chars.index(char)
        return shift_amount

    def get_shift_list(self, key):
        shift_list = []
        for k in key:
            shift_amount = self.get_shift_amount(k)
            shift_list.append(shift_amount)
        return shift_list

    def shift_char_encrypt(self, char, shift_amount):
        original_position = self._chars.index(char)
        shift_position = (original_position + shift_amount) % len(self._chars)
        shifted_char = self._chars[shift_position]
        return shifted_char

    def shift_char_decrypt(self, char, shift_amount):
        pass

    def encrypt(self, plaintext, key):
        flag_base64 = self.string_to_base64(plaintext)

        shift_list = self.get_shift_list(key)

        encrypted_flag = ""
        for i in range(len(flag_base64)):
            round_shift_amount = shift_list[i % len(shift_list)]
            encrypted_flag += self.shift_char_encrypt(flag_base64[i], round_shift_amount)

        self._cipher = encrypted_flag

    def decrypt(self, ciphertext, key):
        """###to be found out###"""
        pass


def split_image(filein, header_file, body_file):
    image_in = open(filein, "r")
    header_out = open(header_file, "w")
    body_out = open(body_file, "w")

    header = ""
    body = ""

    next_line = image_in.readline()
    for i in range(4):
        header += next_line
        next_line = image_in.readline()

    while next_line:
        body += next_line
        next_line = image_in.readline()

    header_out.write(header)
    body_out.write(body)

    image_in.close()
    header_out.close()
    body_out.close()


def to_binary(string):
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


def embed_one(input_bits, input_line):
    line_bits = input_line.split()
    for i in range(8):
        temp = bin(int(line_bits[i]))
        temp = temp[:-1] + input_bits[i]
        line_bits[i] = str(int(temp, 2))

    output = ' '.join(line_bits)
    return output


def embed(cipher, filein, fileout):
    fin = open(filein, 'r')
    fout = open(fileout, 'w')

    cipher_bits = to_binary(cipher)
    rounds = len(cipher_bits)
    counter = 0
    input_line = fin.readline()
    while counter < rounds:
        input_bits = cipher_bits[counter]
        output_line = embed_one(input_bits, input_line)
        fout.write(output_line + '\n')
        counter = counter + 1
        input_line = fin.readline()

    while input_line != '':
        fout.write(input_line)
        input_line = fin.readline()

    fin.close()
    fout.close()


def extract_one(text):
    pass


def extract(filein):
    pass


def combine_image(header_file, body_file, combined_file):
    header_in = open(header_file, "r")
    body_in = open(body_file, "r")
    fileout = open(combined_file, "w")

    next_header_line = header_in.readline()
    while next_header_line:
        fileout.write(next_header_line)
        next_header_line = header_in.readline()

    next_body_line = body_in.readline()
    while next_body_line:
        fileout.write(next_body_line)
        next_body_line = body_in.readline()

    header_in.close()
    body_in.close()
    fileout.close()


if __name__ == "__main__":
    # the fake flag and fake key are of the same length with the real ones
    flag = "fcs22{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
    key = "YYYYYYYYYYYYY"

    # -------------------- ENCRYPTING --------------------
    a = VariantVigenere()
    a.encrypt(flag, key)
    ciphertext = a.get_cipher()

    split_image("mona_lisa.ascii_origin.pgm", "header_orig.txt", "body_orig.txt")
    embed(ciphertext, "body_orig.txt", "body_modified.txt")
    combine_image("header_orig.txt", "body_modified.txt", "mona_lisa_modified.pgm")

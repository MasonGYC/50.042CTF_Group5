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
        """
        Covert the flag to a base64 text
        :param str flag: plaintext flag
        :return: str flag_base64: flag encoded by base64
        """
        flag_byte = flag.encode("utf-8")
        flag_byte_base64 = base64.b64encode(flag_byte)
        flag_base64 = flag_byte_base64.decode("utf-8")
        return flag_base64

    @staticmethod
    def base64_to_string(flag_base64):
        """
        Covert the base64 text to utf-8 flag string
        :param str flag_base64:flag encoded by base64
        :return: str flag: plaintext flag
        """
        flag = base64.b64decode(flag_base64).decode("utf-8")
        return flag

    def get_shift_amount(self, char):
        """
        Get the shift amount with the give character key
        :param str key: a single letter, digit or +, -, =
        :return: int shift_amount: the shift amount with the given key
        """
        shift_amount = self._chars.index(char)
        return shift_amount

    def get_shift_list(self, key):
        """
        Get the shift list with the give key string
        :param str key: a string
        :return: list shift_list: the shift list with the give key string
        """
        shift_list = []
        for k in key:
            shift_amount = self.get_shift_amount(k)
            shift_list.append(shift_amount)
        return shift_list

    def shift_char_encrypt(self, char, shift_amount):
        """
        Shift the character for encryption
        :param str char: character to be shifted
        :param int shift_amount: the amount of shift in vigenere cipher
        :return: str shifted_char: char after shifting
        """
        original_position = self._chars.index(char)
        shift_position = (original_position + shift_amount) % len(self._chars)
        shifted_char = self._chars[shift_position]
        return shifted_char

    def shift_char_decrypt(self, char, shift_amount):
        """
        Shift the character for decryption
        :param str char: character to be shifted
        :param int shift_amount: the amount of shift in vigenere cipher
        :return: str shifted_char: char after shifting
        """
        original_position = self._chars.index(char)
        shift_position = (original_position - shift_amount) % len(self._chars)
        shifted_char = self._chars[shift_position]
        return shifted_char

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext with given key
        :param plaintext: the flag to encrypt
        :param key: the key of the encryption
        :return: null, store the ciphertext in self._cipher
        """
        # convert the flag to base64
        flag_base64 = self.string_to_base64(plaintext)

        # obtain shift amounts from the key
        shift_list = self.get_shift_list(key)

        # vigenere encryption
        encrypted_flag = ""
        for i in range(len(flag_base64)):
            round_shift_amount = shift_list[i % len(shift_list)]
            encrypted_flag += self.shift_char_encrypt(flag_base64[i], round_shift_amount)

        # store the cipher
        self._cipher = encrypted_flag

    def decrypt(self, ciphertext, key):
        """
        Decrypt the ciphertext with given key
        :param ciphertext: the ciphertext to decrypt
        :param key: the key of the decryption
        :return: null, store the plaintext in self._plain
        """

        # obtain shift amounts from the key
        shift_list = self.get_shift_list(key)

        # vigenere decryption
        decrypted_base64_text = ""
        for i in range(len(ciphertext)):
            round_shift_amount = shift_list[i % len(key)]
            decrypted_base64_text += self.shift_char_decrypt(ciphertext[i], round_shift_amount)

        # convert from base64 to utf-8 string
        decrypted_flag = self.base64_to_string(decrypted_base64_text)

        # store the plaintext
        self._plain = decrypted_flag


def split_image(filein, header_file, body_file):
    """
    Split the original image
    :param filein: image to split
    :param header_file: the header of the image
    :param body_file: storing the body of the image
    :return: null
    """
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


def combine_image(header_file, body_file, combined_file):
    """
    :param header_file: image header
    :param body_file: image body
    :param combined_file: storing the combined image
    :return: null
    """
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
    flag = "fcs22{wahhhhhhhh_you_found_the_flag!!!whooohooo}"
    key = "counterstrike"
    # -------------------- ENCRYPTING --------------------
    a = VariantVigenere()
    a.encrypt(flag, key)
    ciphertext = a.get_cipher()
    print("ciphertext = ", ciphertext)

    split_image("mona_lisa.ascii_origin.pgm", "header_orig.txt", "body_orig.txt")
    embed(ciphertext, "body_orig.txt", "body_modified.txt")
    combine_image("header_orig.txt", "body_modified.txt", "mona_lisa_modified.pgm")

    # -------------------- DECRYPTING --------------------
    # Split_image("mona_lisa_modified.pgm", "header_orig.txt", "body_modified.txt")
    ciphertext_recovered = extract("body_modified.txt")
    print("ciphertext_recovered = ", ciphertext_recovered)
    a.decrypt(ciphertext_recovered, key)
    flag_recovered = a.get_plain()
    print("flag_recovered = ", flag_recovered)

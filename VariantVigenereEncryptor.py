import base64


class VariantVigenereEncryptor:
    def __init__(self):
        self._chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
        self._cipher = None

    def get_cipher(self):
        if self._cipher is None:
            raise Exception("Error: Encryptor hasn't encrypted any plaintext yet")
        return self._cipher

    def get_cipher_bytes(self):
        if self._cipher is None:
            raise Exception("Error: Encryptor hasn't encrypted any plaintext yet")
        return bytearray(self._cipher, "ascii")

    @staticmethod
    def convert_to_base64(flag):
        """
        Covert the flag to a base64 text
        :param str flag: plaintext flag
        :return: str flag_base64: flag encoded by base64
        """
        flag_byte = flag.encode("utf-8")
        flag_byte_base64 = base64.b64encode(flag_byte)
        flag_base64 = flag_byte_base64.decode("utf-8")
        return flag_base64

    def get_shift_amount(self, key):
        """
        Get the shift amount with the give character key
        :param str key: a single letter, digit or +, -
        :return: int shift_amount: the shift amount with the given key
        """
        shift_amount = self._chars.index(key)
        return shift_amount

    def shift_char(self, char, shift_amount):
        """
        Shift the character
        :param str char: character to be shifted
        :param int shift_amount: the amount of shift in vigenere cipher
        :return: str shifted_char: char after shifting
        """
        original_position = self._chars.index(char)
        shift_position = (original_position + shift_amount) % 64
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
        flag_base64 = self.convert_to_base64(plaintext)

        # obtain shift amounts from the key
        keys = list(key)
        shift_amounts = []
        for k in keys:
            shift_amount = self.get_shift_amount(k)
            shift_amounts.append(shift_amount)

        # vigenere encryption
        encrypted_flag = ""
        for i in range(len(flag_base64)):
            round_shift_amount = shift_amounts[i % len(shift_amounts)]
            encrypted_flag += self.shift_char(flag_base64[i], round_shift_amount)

        # store the cipher
        self._cipher = encrypted_flag


# a = VariantVigenereEncryptor()
# a.encrypt("fcs22{wahhhhhhhh_you_found_the_flag!!!whooohooo}", "counterstrike")
# print(a.get_cipher())
# output: 1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh

import base64
import os
import sys

# CHANGE THIS: path to your directory
sys.path.insert(0, '/home/dinhtta/istd50042_ctf/utils')
import listener

# use the true flag when the code is running on the server
# use the fake flag when publishing the code

# CHANGE THIS:  this is a fake flag, same length as the true flag.
FLAG = "fcs22{?????????????}"

failure = 0
xored = None
def xor_flag_with_otp():
    global failure
    global xored
    flag_ord = [ord(c) for c in FLAG]
    otp = os.urandom(20)

    xored = bytearray([a ^ b for a, b in zip(flag_ord, otp)])

    # make sure our OTP doesnt leak any bytes from the flag
    for i, (c, p) in enumerate(zip(xored, flag_ord)):
        if (c == p):
            failure = i 
        assert c != p

    return xored


class Challenge():
    def __init__(self):
        self.before_input = "No leaks\n"

    def challenge(self, your_input):
        if your_input == {"msg": "request"}:
            try:
                ciphertext = xor_flag_with_otp()
            except AssertionError:
                return {"error": "Leaky ciphertext {} at {}".format(xored.hex(), failure)}

            return {"ciphertext": xored.hex()}
        else:
            self.exit = True
            return {"error": "Please request OTP"}

import builtins
builtins.Challenge = Challenge
"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13370)

from EmbedAndExtract import *
from ImageSplitCombine import *
from VariantVigenere import *

variantVigenere = VariantVigenere()

# Step 1: extract text from image
split_image("mona_lisa_modified.pgm", "header_orig.txt", "body_modified.txt")
ciphertext_recovered = extract("body_modified.txt")
print("ciphertext_recovered = ", ciphertext_recovered)
# 1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh

# Step 2: guess the key
# by mapping the table, we can get the first 8 characters of the key is "counters"
variantVigenere1 = VariantVigenere()
# since base64 encode 6 bits at a time instead of 8 bits
encoded_prefix = variantVigenere1.string_to_base64("fcs22{")
key_prefix = variantVigenere1.guess_key(ciphertext_recovered[:len(encoded_prefix)], encoded_prefix)
print("key_prefix =", key_prefix)  # counters

# Method 1: bruteforce the rest
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            for d in range(97, 123):
                for e in range(97, 123):
                    key_test = key_prefix + chr(a) + chr(b) + chr(c) + chr(d) + chr(e)
                    try:
                        variantVigenere.decrypt(ciphertext_recovered, key_test)
                        flag_recovered = variantVigenere.get_plain()
                        print("flag_recovered = ", flag_recovered)
                    except:
                        continue

# Method 2: stop bruteforcing after certain pattern is found
# by luck can find some word that can reveal part of the key
# e.g. "found_"
encoded_part = variantVigenere1.string_to_base64("found_")
print(encoded_part)
for start in range(len(ciphertext_recovered)):
    try:
        key_part = variantVigenere1.guess_key(ciphertext_recovered[start:start + len(encoded_part)], encoded_part)
        print("key_part =", key_part)  # key_part = unterstr
    except:
        break
# bruteforce/googleing fill the rest : counterstrike

# Method 3: guessing certain part of the plaintext and map back manually

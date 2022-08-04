# 50.042CTF_Group5

Part 2:
I choose to use a pgm file. The original file is the mona_lisa.ascii_origin.pgm (contains both header and body).

I put the header inside header.txt and the rest inside mona_lisa.ascii.txt

How I embed: (I hide it in the first 64 lines, under "r" "w" mode instead of "rb" "wb" mode)<br />
    cipher: 1O7a5B0nKhnM4iJWBz/TGyob/VxHHNqTGS+K/q/B/kAZ2BIOz0pV2urWIUMbIhfh<br />
    convert 1 to binary, hide it in the first eight numbers in the first line.<br />
    convert 0 to binary, hide it in the first eight numbers in the second line.<br />
    ...<br />
    Therefore only the first 64 lines are invloved.<br />

The embedding.txt got some right-aligned issuem but it really doesn't matter. I have checked that the length of each line is the same(250), it just looks different.

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


# split_image("mona_lisa.ascii_origin.pgm", "header_out.txt", "body_out.txt")
# combine_image("header_out.txt", "body_out.txt", "recombined.pgm")

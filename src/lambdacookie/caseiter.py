import string


def case_iteration(header, iteration):
    """
    Modifies a string to determine the correct
    case for each individual character in the string.

    A character will be uppercase if the bit representing it in
    the iteration value is set to 1.

    For example, the string "hello" with an iteration of 3 would
    be return "HEllo".

    The iteration value in looks like the following in binary:
    00000011

    Each char position the header string looks like the following in binary:
    h = 00000001 (1<<0)
    e = 00000010 (1<<1)
    l = 00000100 (1<<2)
    l = 00001000 (1<<3)
    o = 00010000 (1<<4)

    Each binary character position is compared to the iteration param using
    a bitwise AND. Positive values are uppercased; zero values are lowercased.

    Keyword arguments:
    header    -- a string containing the value to caseify
    iteration -- a numeric value representing the binary mapping of characters
                 in the header string to uppercase.
    """
    if iteration <= 0:
        return header.lower()

    chars = []
    removed = []

    # First create lists of workable and unworkable characters
    for i, char in enumerate(header):
        if char not in string.ascii_letters:
            removed.append({"char": char, "pos": i})
        else:
            chars.append(char)

    # Apply a binary map on the characters we can work with
    for i, char in enumerate(chars):
        pos = 1 << i
        if pos & iteration:
            chars[i] = char.upper()
        else:
            chars[i] = char.lower()

    # Insert removed characters back into the correct positions
    for item in removed:
        chars.insert(item['pos'], item['char'])

    return ''.join(chars)

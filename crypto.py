#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    result = []
    for ch in key:  # loops through all the characters in key
        key.lower()        # makes the key lowercase
        result += ch       # adds the characters to empty list
    new_alpha = ALPHABET.pop(25)
    result += new_alpha

    return result

# pseudo
# convert the key to lowercase letters
# loop through all the characters in the key
# append them into an empty list
# pop the repeat mfs from the new list
    # use two var form of find a repeat
# pop the characters in the alphabet list from thre
# add the two strings together


def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'D')
    'C'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, '\\n')
    '\\n'
    """
    result_ch = ''
    if ch.isupper():  # if i is uppercase
        ch = ch.lower()  # makes each character lwoercase, not mutable
        if ch.isalpha():  # if the character in source is a letter
            i_index = source.index(ch)  # finds index of the source character
            e_char = slug[i_index] # returns slug character at ch_index
            e_char = e_char.upper()  # not mutable, replace w new version of itself
            result_ch += e_char
        return result_ch
    if ch.islower():  # if i is lowercase
        if ch.isalpha():  # if the character in source is a letter
            i_index = source.index(ch)  # finds index of the source character
            e_char = slug[i_index]  # returns slug character at ch_index
            result_ch += e_char  # appends the encrypted letter
    else:
        result_ch += ch
    return result_ch


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.\\n')
    'Zmc khjd z sgtmcdqanks gd ezkkr.\\n'
    """
    enc = ''
    for ch in s:
        new_ch = encrypt_char(source, slug, ch)
        enc += new_ch
    return enc


def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """
    result_ch = ''
    for ch in s:
        if ch.isupper():  # if i is uppercase
            ch = ch.lower()  # makes each character lwoercase, not mutable
            if ch.isalpha():  # if the character in source is a letter
                slug_pos = slug.index(ch)  # finds index of the character in the slug
                e_char = source[slug_pos]  # returns source character at slug position
                e_char = e_char.upper()  # not mutable, replace w new version of itself
                result_ch += e_char

        if ch.islower():  # if i is lowercase
            if ch.isalpha():  # if the character in source is a letter
                slug_pos = slug.index(ch)  # finds index of the source character
                e_char = source[slug_pos]  # returns slug character at ch_index
                result_ch += e_char  # appends the encrypted letter
        else:
            result_ch += ch
    return result_ch


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    pass


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    pass


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    pass


# Python boilerplate.
if __name__ == '__main__':
    main()

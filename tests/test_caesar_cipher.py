import pytest

from caesar_cipher.caesar_cipher import encrypt, decrypt, crack

def test_encrypt():
    encrypted_word = encrypt('abc', 1)
    assert encrypted_word == 'bcd'

def test_encrypt_with_int():
    encrypted_word = encrypt('ab124c', 1)
    assert encrypted_word == 'bcd'

def test_encrypt_with_int_and_whitespace():
    encrypted_word = encrypt('ab1 24c', 1)
    assert encrypted_word == 'bcd'

def test_decrypt():
    decrypted_word = decrypt('bcd', 1)
    assert decrypted_word == 'abc'

def test_decrypt_upper():
    decrypted_word = decrypt('BCD', 1)
    assert decrypted_word =='ABC'
    
def test_crack():
    decrypted_word = crack('ifmmp')
    assert decrypted_word == 'hello'


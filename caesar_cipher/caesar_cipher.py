import nltk
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

def encrypt(plain_txt, key):
  
  cipher_txt = ''

  for char in plain_txt:
    if char.isnumeric():
      cipher_txt += ''
    elif char == ' ':
      cipher_txt += ''
    elif  char.isupper():
      cipher_txt += chr((ord(char) + key - 65) % 26 + 65)
    else:
      cipher_txt += chr((ord(char) + key - 97) % 26 + 97)
  
  return cipher_txt
 
def decrypt(cipher_txt, key):
   return encrypt(cipher_txt, -key)

def crack(cipher_txt):
  possiblities = ''
  
  for shift in range(0,26):
    encrypted_words = decrypt(cipher_txt, shift)
    split_word_list = encrypted_words.split()
    
    for word in split_word_list:
      if word in word_list or word in name_list: 
        possiblities += word
  
  return possiblities 

# if __name__ == "__main__":
    # print(encrypt('abc', 1)) # bcd
    # print(encrypt('a3134 bc2', 1)) # bcd
    # print(encrypt('hello', 1)) # ifmmp
    # print(decrypt('bcd', 1)) # abc
    # print(crack('ifmmp'))
    # phrase = encrypt('It was the best of times, it was the worst of times.', 1)
    # print(crack(phrase))

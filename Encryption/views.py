from django.shortcuts import render
from django.http import HttpResponse
import random

def caeser_cipher_encryption(request):
    plain_text = ""
    key = ""
    Cipher_text = ""

    if request.method == 'POST':
        plain_text = request.POST.get('plain_text', '')
        key = request.POST.get('key', '')
        key = int(key)

        def Encryption(plain_text, key):
            result = ""
            for char in plain_text:
                if char.isalpha():
                    is_upper = char.isupper()
                    char = char.upper()
                    shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
                    if not is_upper:
                        shifted_char = shifted_char.lower()
                    result += shifted_char
                else:
                    result += char
            return result

        Cipher_text = Encryption(plain_text, key)

    # If the form is not submitted, reset Cipher_text to an empty string
    else:
        Cipher_text = ""

    return render(request, 'caeser_encryption.html', {'Cipher_text': Cipher_text})

def homepage(request):
    return render(request,'index.html')

def caeser_cipher_decryption(request):
    plain_text = ""
    key = ""
    cipher_text = ""

    if request.method == 'POST':
        cipher_text = request.POST.get('cipher_text', '')
        key = request.POST.get('key', '')
        key = int(key)

        def Decryption(cipher_text, key):
            result = ""
            for char in cipher_text:
                if char.isalpha():
                    is_upper = char.isupper()
                    char = char.upper()
                    shifted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
                    if not is_upper:
                        shifted_char = shifted_char.lower()
                    result += shifted_char
                else:
                    result += char
            return result

        plain_text = Decryption(cipher_text, key)


    return render(request,"caeser_decryption.html",{'plain_text': plain_text})

def caesercipher(request):
    
    return render(request,'caeser_cipher.html')

def vigenerecipher(request):
    return render(request,'vigenere_cipher.html')

# Create your views here.

def vigenere_cipher_encryption(request):

    plain_text=""
    key=""
    cipher_text=""

    if request.method=='POST':
        plain_text=request.POST.get('plain_text','')
        key=request.POST.get('key','')
        
        def vigenere_cipher(plain_text, key):
           alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
           result=""
           

           key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

           for i in range(len(plain_text)):
              if plain_text[i].isalpha():
                key_index = alphabet.find(key_repeated[i].upper())
                shift = alphabet.index(plain_text[i].upper()) + key_index
                shift = shift % 26
                result += alphabet[shift] if plain_text[i].isupper() else alphabet[shift].lower()
              else:
                result += plain_text[i]

           return result
        
        cipher_text=vigenere_cipher(plain_text,key)


    return render(request,'vigenere_encryption.html',{'Cipher_text': cipher_text})

def vigenere_cipher_decryption(request):

    plain_text=""
    key=""
    cipher_text=""

    if request.method=='POST':
        cipher_text = request.POST.get('cipher_text', '')
        key = request.POST.get('key', '')

        def vigenere_decryption(cipher_text,key):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result=""
           

            key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]

            for i in range(len(cipher_text)):
                if cipher_text[i].isalpha():
                  key_index = alphabet.find(key_repeated[i].upper())
                  shift = alphabet.index(cipher_text[i].upper()) - key_index
                  shift = shift % 26
                  result += alphabet[shift] if cipher_text[i].isupper() else alphabet[shift].lower()
                else:
                  result += cipher_text[i]

            return result
        
        plain_text=vigenere_decryption(cipher_text,key)


    return render(request,'vigenere_decryption.html',{'plain_text': plain_text})


def playfaircipher(request):
    return render(request,'playfair_cipher.html')

def playfair_cipher_encryption(request):

    plain_text=""
    keyword=""
    cipher_text=""

    if request.method=='POST':
        plain_text=request.POST.get('plain_text','')
        keyword=request.POST.get('keyword','')
        
        def generate_playfair_key(keyword):
          # Function to generate the Playfair key square based on a keyword
          alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: 'J' is usually excluded in the Playfair cipher
          keyword = keyword.upper().replace('J', 'I')
          key_square = []

          for char in keyword + alphabet:
              if char not in key_square:
                  key_square.append(char)

          playfair_key = [key_square[i:i + 5] for i in range(0, 25, 5)]
          return playfair_key
        
        def find_coordinates(matrix, char):
          # Function to find the coordinates of a character in the Playfair key square
          for i, row in enumerate(matrix):
              for j, value in enumerate(row):
                  if value == char:
                      return i, j
                  
        def encrypt_playfair(plaintext, key):
           # Function to encrypt plaintext using the Playfair cipher
           ciphertext = ''
           for i in range(0, len(plaintext), 2):
               pair = plaintext[i:i + 2]
               if len(pair) == 2:
                   row1, col1 = find_coordinates(key, pair[0])
                   row2, col2 = find_coordinates(key, pair[1])
       
                   if row1 == row2:
                       ciphertext += key[row1][(col1 + 1) % 5] + key[row2][(col2 + 1) % 5]
                   elif col1 == col2:
                       ciphertext += key[(row1 + 1) % 5][col1] + key[(row2 + 1) % 5][col2]
                   else:
                       ciphertext += key[row1][col2] + key[row2][col1]
               else:
                   # If the pair has only one character, add 'X' to make it a pair
                   ciphertext += pair[0] + 'X'

           return ciphertext
        
        key=generate_playfair_key(keyword)
        cipher_text=encrypt_playfair(plain_text,key)

      

    return render(request,'playfair_encryption.html',{'Cipher_text': cipher_text})

def playfair_cipher_decryption(request):

    plain_text=""
    keyword=""
    cipher_text=""

    if request.method=='POST':
        cipher_text=request.POST.get('cipher_text','')
        keyword=request.POST.get('keyword','')
        
        def generate_playfair_key(keyword):
          # Function to generate the Playfair key square based on a keyword
          alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: 'J' is usually excluded in the Playfair cipher
          keyword = keyword.upper().replace('J', 'I')
          key_square = []
      
          for char in keyword + alphabet:
              if char not in key_square:
                  key_square.append(char)

          playfair_key = [key_square[i:i + 5] for i in range(0, 25, 5)]
          return playfair_key
        
        def find_coordinates(matrix, char):
          # Function to find the coordinates of a character in the Playfair key square
          for i, row in enumerate(matrix):
              for j, value in enumerate(row):
                  if value == char:
                      return i, j
                  
        def decrypt_playfair(ciphertext, key):
           # Function to decrypt ciphertext using the Playfair cipher
           plaintext = ''
           for i in range(0, len(ciphertext), 2):
               pair = ciphertext[i:i + 2]
               if len(pair) == 2:
                   row1, col1 = find_coordinates(key, pair[0])
                   row2, col2 = find_coordinates(key, pair[1])
       
                   if row1 == row2:
                       plaintext += key[row1][(col1 - 1) % 5] + key[row2][(col2 - 1) % 5]
                   elif col1 == col2:
                       plaintext += key[(row1 - 1) % 5][col1] + key[(row2 - 1) % 5][col2]
                   else:
                       plaintext += key[row1][col2] + key[row2][col1]
               else:
                   plaintext += pair[0]

           return plaintext
        
        key=generate_playfair_key(keyword)

        plain_text=decrypt_playfair(cipher_text,key)
        
        




        
    
    return render(request,'playfair_decryption.html',{'plain_text': plain_text})


def aboutus(request):
    return render(request,'aboutus.html')


def affinecipher(request):
    return render(request,'affine_cipher.html')

def affine_cipher_encryption(request):

    plain_text=""
    a=""
    b=""
    key=""
    cipher_text=""

    if request.method=='POST':
        plain_text = request.POST.get('plain_text', '')
        a = request.POST.get('a', '')
        b=request.POST.get('b','')

        a=int(a)
        b=int(b)

        key=(a,b)
        

        def gcd(a, b):
          """
          Calculate the Greatest Common Divisor (GCD) of two numbers.
          """
          while b:
              a, b = b, a % b
          return a

        def mod_inverse(a, m):
          """
          Calculate the modular inverse of a number 'a' under modulo 'm'.
          """
          for i in range(1, m):
              if (a * i) % m == 1:
                  return i
          return None      

        def encrypt(text, key):
          """
          Encrypt a given text using the Affine Cipher.
          """
          result = ""
      
          # Affine Cipher encryption function: E(x) = (ax + b) % m
          for char in plain_text:
              if char.isalpha():
                  # Apply the affine transformation separately for uppercase and lowercase letters
                  if char.isupper():
                      result += chr((key[0] * (ord(char) - ord('A')) + key[1]) % 26 + ord('A'))
                  else:
                      result += chr((key[0] * (ord(char) - ord('a')) + key[1]) % 26 + ord('a'))
              else:
                  result += char

          return result      
        
        cipher_text=encrypt(plain_text,key)



    
    return render(request,'affine_encryption.html',{'Cipher_text': cipher_text})

def affine_cipher_decryption(request):

    plain_text=""
    key=""
    cipher_text=""

    if request.method=='POST':
        cipher_text = request.POST.get('cipher_text', '')
        a = request.POST.get('a', '')
        b = request.POST.get('b','')

        a=int(a)
        b=int(b)

        key=(a,b)

        def gcd(a, b):
          """
          Calculate the Greatest Common Divisor (GCD) of two numbers.
          """
          while b:
              a, b = b, a % b
          return a
 
        def mod_inverse(a, m):
          """
          Calculate the modular inverse of a number 'a' under modulo 'm'.
          """
          for i in range(1, m):
              if (a * i) % m == 1:
                  return i
          return None
 
        def decrypt(plain_text, key):
           """
           Decrypt a given text using the Affine Cipher.
           """
           result = ""

           # Affine Cipher decryption function: D(x) = a^(-1) * (x - b) % m
           # Here, a^(-1) is the modular inverse of 'a' under modulo 26
           a_inverse = mod_inverse(key[0], 26)

           for char in plain_text:
               if char.isalpha():
                   # Apply the inverse affine transformation separately for uppercase and lowercase letters
                   if char.isupper():
                       result += chr((a_inverse * (ord(char) - ord('A') - key[1])) % 26 + ord('A'))
                   else:
                       result += chr((a_inverse * (ord(char) - ord('a') - key[1])) % 26 + ord('a'))
               else:
                   result += char

           return result
        
        plain_text=decrypt(cipher_text,key)


    return render(request,'affine_decryption.html',{'plain_text':plain_text})


def monoalphabeticcipher(request):
    return render(request,'monoalphabetic_cipher.html')

def monoalphabetic_cipher_encryption(request):
    plain_text = ""
    keyword = ""
    cipher_text = ""

    if request.method == 'POST':
        plain_text = request.POST.get('plain_text', '')
        keyword = request.POST.get('keyword', '')

        def generate_key(keyword):
            # Function to generate a monoalphabetic substitution key based on a keyword
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            keyword = keyword.upper()

            # Remove duplicate letters from the keyword
            unique_keyword = ''.join(sorted(set(keyword), key=keyword.index))

            # Create a key by combining the unique keyword and remaining alphabet letters
            remaining_letters = ''.join(sorted(set(alphabet) - set(unique_keyword)))
            shuffled_alphabet = unique_keyword + remaining_letters

            # Create a dictionary mapping each letter to its substitute
            return dict(zip(alphabet, shuffled_alphabet))

        def encrypt(plain_text, key):
            # Function to encrypt the given plain text using the provided key
            encrypted_text = ''
            for char in plain_text.upper():
                if char.isalpha():
                    # Substitute each letter based on the key
                    encrypted_text += key[char]
                else:
                    # Keep non-alphabetic characters unchanged
                    encrypted_text += char
            return encrypted_text

        key = generate_key(keyword)
        cipher_text = encrypt(plain_text, key)

    return render(request, 'monoalphabetic_encryption.html', {'Cipher_text': cipher_text})

def monoalphabetic_cipher_decryption(request):
    plain_text = ""
    key = ""
    cipher_text = ""

    if request.method == 'POST':
        cipher_text = request.POST.get('cipher_text', '')
        keyword = request.POST.get('keyword', '')
        def generate_key(keyword):
          # Function to generate a monoalphabetic substitution key based on a keyword
          alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
          keyword = keyword.upper()
    
          # Remove duplicate letters from the keyword
          unique_keyword = ''.join(sorted(set(keyword), key=keyword.index))
    
          # Create a key by combining the unique keyword and remaining alphabet letters
          remaining_letters = ''.join(sorted(set(alphabet) - set(unique_keyword)))
          shuffled_alphabet = unique_keyword + remaining_letters
    
          # Create a dictionary mapping each letter to its substitute
          return dict(zip(alphabet, shuffled_alphabet))
        
        def decrypt(encrypted_text, key):
           # Function to decrypt the given encrypted text using the provided key
           inverted_key = {v: k for k, v in key.items()}
           decrypted_text = ''
           for char in encrypted_text.upper():
               if char.isalpha():
                   # Reverse substitution based on the key
                   decrypted_text += inverted_key[char]
               else:
                   # Keep non-alphabetic characters unchanged
                   decrypted_text += char
           return decrypted_text
        
        key=generate_key(keyword)
        plain_text=decrypt(cipher_text,key)



    return render(request,'monoalphabetic_decryption.html',{'plain_text': plain_text})

#!/usr/bin/env python3

from Crypto.Cipher import AES
from secrets import token_bytes

#CREATING BANNER
def aes_banner_art():
    banner_art = """
[<^>]----------------------------[<^>]
    ADVANCED ENCRYPTION STANDARD
[<^>]----------------------------[<^>]

      ██╗  ███████╗ ██████╗
     ██╔╝ ██╔════╝██╔════╝
    ██╔╝  ███████╗███████╗  ENCRYPTION <|>
   ██╔╝   ██╔════╝╚════██║  ENCRYPTION <|>
  ███████╗██╝     ███████║
 ██╔════╝ ███████╗╚══════╝
╚═╝       ╚══════╝

[<^>]----------------------------[<^>]
    ADVANCED ENCRYPTION STANDARD
[<^>]----------------------------[<^>]
\n
"""
    print(banner_art)

aes_banner_art()

#GENERATING SECURITY KEY
sec_key = token_bytes(16)

#ENCRYPTING MESSAGE
def encrypting(message):
    cipher = AES.new(sec_key, AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce, cipher_text, tag

#DECRYPTING MESSAGE
def decrypting(nonce, cipher_text, tag):
    cipher = AES.new(sec_key, AES.MODE_EAX, nonce = nonce)
    plain_text = cipher.decrypt(cipher_text)

    try:
        cipher.verify(tag)
        return plain_text.decode('ascii')
    
    except:
        return False


msg = input("\n[+]  Message: ")
nonce, cipher_text, tag = encrypting(msg)
plain_text = decrypting(nonce, cipher_text, tag)
print(f"\n[+]  Cipher Text: {cipher_text}")


if not plain_text:
    print("\n[-]  Error in Decryption")

else:
    print(f"\n[+]  Decrypted Message: {plain_text}")
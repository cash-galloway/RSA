encrypted_message = ""
decrypted_message = ""
def encrypt1():
  e = int(input("What is the value of e?"))
  n = int(input("What is the value of n?"))
  print (e,n)
  message = input("What is the message you would like to encrypt?")
  global encrypted_message
  for x in message:
      numerize = ord(x)
      encrypt = pow(numerize, e, n)
      denumerize = chr(encrypt)
      encrypted_message += denumerize
  print (encrypted_message)

def decrypt():
  d = int(input("What is the value of d?"))
  n = int(input("What is the value of n?"))
  print (d,n)
  message = input("What is the message you would like to decrypt?")
  global decrypted_message
  for x in message:
      numerize = ord(x)
      decrypt = pow(numerize, d, n)
      denumerize = chr(decrypt)
      decrypted_message += denumerize
  print (decrypted_message)
decrypt()

def encrypter():
  message = input("What is the message you would like to encrypt?")
  for x in message:
      numerize = ord(x)
      encrypt = pow(numerize, e, n)
      denumerize = chr(encrypt)
      encrypted_message += denumerize
encrypt1()
  
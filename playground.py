n = 21971
e = 131

message = "Hello World!"

encrypted_message = ""

############ENCRYPTING###############
for x in message:
    
    numerize = ord(x)
    
    encrypt = pow(numerize, e, n)
    
    denumerize = unichr(encrypt)
    
    encrypted_message += denumerize
    
    print encrypted_message
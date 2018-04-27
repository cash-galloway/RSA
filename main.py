n = 22487
e = 21647

message = "minecraft has the best graphics"

encrypted_message = ""

############ENCRYPTING###############
for x in message:
    
    numerize = ord(x)
    
    encrypt = pow(numerize, e, n)
    
    denumerize = chr(encrypt)
    
    encrypted_message += denumerize
    
    print (encrypted_message)
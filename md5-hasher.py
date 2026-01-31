
#!/usr/bin/env python3
# -*- -*- -*-

import random
import hashlib

def generate_random_number_string():
       # Använder random.randit för att välja siffror (hyfasd randomisering)
    # Skapar en någorlunda enhetlig fördelning över alla möjliga 10-siffriga kombinationer
    return ''.join(str(random.randint(0,9)) for X in range(PWD_LGT))

def md5_hash(text):

      # encode() konverterar sträng till bytes, vilket krävs av hashlib
    # hexdigest() returnerar hash-värdet som en hexadecimal sträng
    return hashlib.md5(text.encode()).hexdigest()

def main():

   
       # Generera och visa lösenorden med deras hash-värden
    for i in range(NO_PASS):
        # Generera ett slumpmässigt lösenord med fast längd
        password = generate_random_number_string()
        
        # Beräkna MD5-hashen för lösenordet
        hash_value = md5_hash(password)
        
        # Formatera och visa resultatet med sekventiell numrering
        print(f"{hash_value}")
    

# Fasta konstanter för programmet (Går att ändra på efter behov)
PWD_LGT = 9
NO_PASS = 10

# Standard Python idiom för att kontrollera om skriptet körs direkt!
if __name__ == "__main__":
    main()


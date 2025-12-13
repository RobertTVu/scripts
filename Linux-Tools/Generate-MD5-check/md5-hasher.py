#!/usr/bin/env python3
# -*- -*- -*-



import random
import hashlib

def generate_random_number_string():
    # Använder random.choice för att välja siffror (hyfasd randomisering)
    # Skapar en någorlunda enhetlig fördelning över alla möjliga 10-siffriga kombinationer
    return ''.join(random.choice("0123456789") for X in range(PWD_LGT))

def md5_hash(text):
    # encode() konverterar sträng till bytes, vilket krävs av hashlib
    # hexdigest() returnerar hash-värdet som en hexadecimal sträng
    return hashlib.md5(text.encode()).hexdigest()

def main():
    # Programbeskrivning för användaren
    print("-" * 60)
    print("Password and MD5 Hash Generator (Very UNsecure version)")
    print("-" * 60)
    print(f"Skapar {NO_PASS} st randomiserade {PWD_LGT}-siffriga lösenord och deras MD5 hashes:\n")
    
    # Generera och visa lösenorden med deras hash-värden
    for i in range(NO_PASS):
        # Generera ett slumpmässigt lösenord med fast längd
        password = generate_random_number_string()
        
        # Beräkna MD5-hashen för lösenordet
        hash_value = md5_hash(password)
        
        # Formatera och visa resultatet med sekventiell numrering
        print(f"{i+1:2d}. Lösenord: {password}  →  MD5: {hash_value}")
    
    # Säkerhetsvarning
    print("\n" + "=" * 50)
    print("⚠️ Extra Viktig säkerhetsinformation:")
    print("-" * 50)
    print("MD5 är inte längre säkert för kryptografiskt bruk.")
    print("Det används här ENDAST i utbildningssyfte.")
    print("För riktiga system bör man använda moderna algoritmer som SHA-256")
    print("eller lösenordshashfunktioner som bcrypt eller Argon2.")
    print("=" * 50)

# Fasta konstanter för programmet (Går att ändra på efter behov)
PWD_LGT = 3
NO_PASS = 3

# Standard Python idiom för att kontrollera om skriptet körs direkt!
if __name__ == "__main__":
    main()

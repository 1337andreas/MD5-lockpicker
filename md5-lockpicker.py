
# MD5 Lockpicker är en lösenords- och hashgenerator som skapar slumpmässiga numeriska lösenord och beräknar deras MD5-hashar.
# Observera att MD5 numera räknas som kryptografiskt osäkert/knäckt och bör därmed inte användas för säkerhetskritiska ändamål! Detta är bara i utbildnings- och testsyfte.
# Upphovsman: 1337andreas
# Senaste uppdatering: 08-01-2026
# Version 0.1 

import secrets
import hashlib
import string

def generate_random_number_string():

    #password_characters = string.digits
    #password = (secrets.choice(password_characters))
    #print (password)
    """
    Skapar en slumpmässig sträng bestående av siffror. Längden bestäms av konstanten PWD_LGT.
    
    Returns:
        str: A random string containing only digits (0-9) with fixed length.
        
    Example:
        '4738291650'  # Random 10-digit string
    """
    # Använder secrets.choice för att välja en 10-siffrig kombination.
    return ''.join(secrets.choice("0123456789") for X in range(PWD_LGT))

def md5_hash(text):
    """
    Calculates the MD5 hash of a given string.
    
    Args:
        text (str): The input string to hash.
        
    Returns:
        str: The hexadecimal representation of the MD5 hash.
        
    Security Note:
        MD5 is cryptographically broken and vulnerable to collision attacks.
        It should not be used for password storage or security-sensitive applications.
        Consider using SHA-256 or bcrypt instead for real-world applications.
    """
    # encode() konverterar sträng till bytes, vilket krävs av hashlib
    # hexdigest() returnerar hash-värdet som en hexadecimal sträng
    return hashlib.md5(text.encode()).hexdigest()

def main():
    """
    Main function that orchestrates the password generation and hashing.
    
    Generates NO_PASS random passwords with fixed length PWD_LGT
    and displays them alongside their corresponding MD5 hashes.
    """
    # Programbeskrivning för användaren
   # print("-" * 60)
   # print("Password and MD5 Hash Generator (Very UNsecure version)")
   # print("-" * 60)
   # print(f"Skapar {NO_PASS} st randomiserade {PWD_LGT}-siffriga lösenord och deras MD5 hashes:\n")
    
    # Generera och visa lösenorden med deras hash-värden
    for i in range(NO_PASS):
        # Generera ett slumpmässigt lösenord med fast längd
        password = generate_random_number_string()
        
        # Beräkna MD5-hashen för lösenordet
        hash_value = md5_hash(password)

        #print((f"{i+1:2d}. Lösenord: {password}  →  MD5: {hash_value}"))
        print(hash_value)
        #print("Välj om lösenorden skall visas i plaintext + hashvärde eller bara som hashvärden.")
        #print("a - Plaintext + hashvärde")
        #print("b - Bara hashvärde")

        #displaychoice = input()
        #if displaychoice == "a":
        #    print((f"{i+1:2d}. Lösenord: {password}  →  MD5: {hash_value}")) #Formaterar och visa resultatet med sekventiell numrering.
        #elif displaychoice == "b":
        #    print(hash_value) #Visar bara hashvärdena.


# Fasta konstanter för programmet: Lösenordslängd (PWD_LGT) och antal lösenord (NO_PASS).
# Rekommenderat är minst 10 tecken för att minimera möjligheten att hashen finns i ett rainbow table.
PWD_LGT = 10
NO_PASS = 10

# Standard Python idiom för att kontrollera om skriptet körs direkt!
if __name__ == "__main__":
    main()

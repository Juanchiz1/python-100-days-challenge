

print("Welcome to Caesar Cipher.")

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
palabraformada=[]
palabradesencripta=[]
encode=False
decode=False


def CaesarCipher(text, shift):
    if encode == True:
        for letter in text:
            if letter in text and letter in alphabet:
                indice = alphabet.index(letter) + shift
                indice = indice % len(alphabet)

                palabraformada.append(alphabet[indice])
            else:
                palabraformada.append(letter)
        print("Encrypted text: ", palabraformada)

    if decode == True:
        for letter in text:
            if letter in text and letter in alphabet:
                indice2 = alphabet.index(letter) - shift
                indice2 = indice2 % len(alphabet)
                palabradesencripta.append(alphabet[indice2])

            else:
                palabradesencripta.append(letter)
        print("Decrypted text: ", palabradesencripta)

shouldContinue = ""
continue1=True

direction=input("Type 'encode' to encrypt type 'decode' to decrypt: ").lower()
if direction=='encode':
    encode=True
    text=input("Type the text to be encrypted: ").lower()
    shift = int(input("Type the shift number: "))
    CaesarCipher(text, shift)

elif direction=='decode':
    decode=True
    text=input("Type the text to be decrypted: ").lower()
    shift=int(input("Type the shift number: "))
    CaesarCipher(text, shift)
else:
    print("Please type 'encode' or 'decode'.")



#TODO-1: Create a function called encrypt() that takes the original_text and shift_amount as 2 inputs

#TODO-2: INSIDE THE ENCRYPT FUNCTION SHIFT EACH LETTER OF THE ORIGINAL FORWARD THE ALPHABET

#TODO-3: CALL THE FUNCTION

#TODO-4: WHAT HAPPENS IF YOU SHIFT Z FORWARDS BY 9 CAN YOU FIX THE CODE?











import os

def encrypt(shift1, shift2):

    lowercase1 = "abcdefghijklm"
    lowercase2 = "nopqrstuvwxyz"
    uppercase1 = "ABCDEFGHIJKLM"
    uppercase2 = "NOPQRSTUVWXYZ"
    message = ""

    #Converting string shift1 and shift2 to int
    shift1 = int(shift1)
    shift2 = int(shift2)

    with open("raw_text.txt") as f:
        for line in f:
            for char in line:
                #Getting position (index) of character in alphabet
                position1 = lowercase1.find(char)
                position2 = lowercase2.find(char)
                position3 = uppercase1.find(char)
                position4 = uppercase2.find(char)

                #If character found in lowercase1 string
                if position1 > -1:
                    position1 = ((position1 + (shift1*shift2))%len(lowercase1))
                    message+=lowercase1[position1]

                #If character found in lowercase2 string
                elif position2 > -1:
                    position2 = ((position2 - (shift1+shift2))%len(lowercase2))
                    message+=lowercase2[position2]
                
                #If character found in uppercase1 string
                elif position3 > -1:
                    position3 = ((position3 - shift1)%len(uppercase1))
                    message+=uppercase1[position3]
                
                #If character found in uppercase2 string
                elif position4 > -1:
                    position4 = ((position4 + (shift2*shift2)%len(uppercase2)))
                    message+=uppercase2[position4]

                #If no character found in string, then add what is originally in the raw_text.txt
                else:
                    message += char
    
    #Writing encrypted message to 'encrypted_text.txt'
    with open("encrypted_text.txt", 'a') as x:
        x.write(message)
        print("Message encrypted to 'encrypted_text.txt'.")
        x.close()

def decrypt(shift1, shift2):
    lowercase1 = "abcdefghijklm"
    lowercase2 = "nopqrstuvwxyz"
    uppercase1 = "ABCDEFGHIJKLM"
    uppercase2 = "NOPQRSTUVWXYZ"
    message = ""

    #Converting string shift1 and shift2 to int
    shift1 = int(shift1)
    shift2 = int(shift2)

    with open("encrypted_text.txt") as f:
        for line in f:
            for char in line:
                #Getting position (index) of character in alphabet
                position1 = lowercase1.find(char)
                position2 = lowercase2.find(char)
                position3 = uppercase1.find(char)
                position4 = uppercase2.find(char)

                #If character found in lowercase1 string
                if position1 > -1:
                    position1 = ((position1 - (shift1*shift2))%len(lowercase1))
                    message+=lowercase1[position1]

                #If character found in lowercase2 string
                elif position2 > -1:
                    position2 = ((position2 + (shift1+shift2))%len(lowercase2))
                    message+=lowercase2[position2]
                
                #If character found in uppercase1 string
                elif position3 > -1:
                    position3 = ((position3 + shift1)%len(uppercase1))
                    message+=uppercase1[position3]
                
                #If character found in uppercase2 string
                elif position4 > -1:
                    position4 = ((position4 - (shift2*shift2)%len(uppercase2)))
                    message+=uppercase2[position4]

                #If no character found in string, then add what is originally in the encrypted_text.txt
                else:
                    message += char
    
    #Writing encrypted message to 'decrypted_text.txt'
    with open("decrypted_text.txt", 'a') as x:
        x.write(message)
        x.close()
        print("Message encrypted to 'encrypted_text.txt'.")

def verify():
    with(open("raw_text.txt") as txt1, open("decrypted_text.txt") as txt2):

        #While loop to see if characters from both files match
        while True:
            raw = txt1.read(1)
            decrypted = txt2.read(1)

            #If raw text doesn't match decrypted text, then print that it fails and end loop
            if raw != decrypted:
                print("Raw text does not match decrypted text. Verification failed!")
                return
            #Using not to detect end of string, meaning that both files match successfully.
            elif not raw and not decrypted:
                print("Raw text matches decrypted text. Verification successful!")
                return
            
#=========Main (running program from here)===========
shift1 = input("Enter value 1: ")
shift2 = input("Enter value 2: ")
encrypt(shift1, shift2)
decrypt(shift1, shift2)
verify()

    
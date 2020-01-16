# Caeser Cipher Decrypt 

inputString = input("Enter String to Decrypt : ")

key = int(input("Enter Key to Decrypt : "))

lowerLimit = 0

upperLimit = 0

decryptedString = ''

length = len(inputString)

for i in range(0,length):
    alphabet = inputString[i]

    alphabetASCII = ord(alphabet)

    calculatedASCII = 0

    #Generating Small Letters

    if(alphabetASCII >= 97):
        lowerLimit = 97
        upperLimit = 122
        calculatedASCII = alphabetASCII - key

        if(calculatedASCII < lowerLimit):
            calculatedASCII = lowerLimit - calculatedASCII
            calculatedASCII = (upperLimit + 1) - calculatedASCII 
            decryptedString += chr(calculatedASCII)

        else:
            decryptedString += chr(calculatedASCII)

    elif(alphabetASCII >=65 and alphabetASCII<=90):

        #Generating Capital Letters

        lowerLimit = 65
        upperLimit = 90
        calculatedASCII = alphabetASCII - key

        if(calculatedASCII < lowerLimit):
            calculatedASCII = lowerLimit - calculatedASCII
            calculatedASCII = upperLimit - calculatedASCII
            decryptedString += chr(calculatedASCII)

        else:
            decryptedString += chr(calculatedASCII)

    elif(alphabet == " "):
        decryptedString += " "

#Printing Decrypted String

print("Decrypted String is : " , decryptedString)

    

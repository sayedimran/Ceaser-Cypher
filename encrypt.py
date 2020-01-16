# Caeser Cipher Encryption

inputString = input("Enter String to Encrypt : ")

key = int(input("Enter Number of Shifts "))

length = len(inputString)

upperLimit = 0
lowerLimit = 0

encryptedString = ''

#Applying Logic From Here

for i in range(0,length):
    alphabet = inputString[i]

    #Taking it's ASCII value

    alphabetASCII = ord(alphabet)

    calculatedASCII = 0

    if(alphabetASCII >= 97):

        lowerLimit = 97
        upperLimit = 122
        calculatedASCII = alphabetASCII + key
        
        #Checking if it's greater than last value then divide whole with last value to get the first index

        if(calculatedASCII > upperLimit):
            calculatedASCII -= upperLimit
            calculatedASCII += lowerLimit-1
            encryptedString += chr(calculatedASCII)

        else:
            encryptedString += chr(calculatedASCII)
    elif(alphabetASCII >= 65 and alphabetASCII <= 90):
        lowerLimit = 65
        upperLimit = 90
        calculatedASCII = alphabetASCII + key

        if(calculatedASCII > upperLimit):
            calculatedASCII -= upperLimit
            calculatedASCII += lowerLimit-1
            encryptedString += chr(calculatedASCII)

        else:
            encryptedString += chr(calculatedASCII)
    elif(alphabet == " "):
        encryptedString += " "

#Printing Result

print("Encypted String is : " , encryptedString)
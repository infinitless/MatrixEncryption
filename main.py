import random
import re
import math
import string

# Define Reference Grid

values = [
    ["a", "b", "c", "d", "e", "f"],
    ["g", "h", "i", "j", "k", "l"],
    ["m", "n", "o", "p", "q", "r"],
    ["s", "t", "u", "v", "w", "x"],
    ["y", "z", "0", "1", "2", "3"],
    ["4", "5", "6", "7", "8", "9"]
]

myrows = ["1", "2", "1,1", "1,2", "2,1", "2,2"]
mycolumns = ["1", "2", "1,1", "1,2", "2,1", "2,2"]
positions = [1, 2, 3, 4, 5, 6]


# The encoded text for any character (alphabet or number) = column + row, joined together
# Punctuation and spaces are ignored
# So "abc" as per Reference grid = 111211,1

# Define single row rotation

def rotaterow(myvalues, rowindex, rotation):
    rotatedrow = ""
    newrow = myvalues[rowindex]
    for nN in range(0, 6):
        rotatedrow = newrow[rotation % 6:] + newrow[:rotation % 6]
    return rotatedrow


# Define single column rotation

def rotatecolumn(myvalues, columnindex, rotation):
    rotatedcolumn = ""
    newcolumn = [column[columnindex] for column in myvalues]
    for nm in range(0, 6):
        rotatedcolumn = newcolumn[rotation % 6:] + newcolumn[:rotation % 6]
    return rotatedcolumn


# Find a particular character and return its cipher

def findme(mychar, myvalues):
    cipher_string = ""
    for rows in myvalues:
        if mychar in rows:
            cipher_string = (mycolumns[myvalues.index(rows)]) + (myrows[rows.index(mychar)])
    return str(cipher_string)


# Read all decimal places of PI from the file
# and store as a string of 1 Million digits

with open("piDigits.txt", 'r') as f:
    pidecimals = f.read()
f.close()


# Rotate the Reference grid in a random fashion
# Generate a Random Number
# Go to that position in pidecimlas
# Pick up N digits from that place in pidecimals
# such that the number of digits in the random number
# plus the number of digits from pidecimals = 12.
# If someone has the PiDigits file and the randomseed
# they will know which digits have been chosen.
# Now rotate the grid as per the combination of random number
# and the number of randomly chosen digits of Pi

def randomrotation():
    myrandomseed = random.randint(1, len(pidecimals) - 12)
    length_randomseed = len(str(myrandomseed))
    deficit = 12 - length_randomseed

    pistring = ""
    for nmn in range(myrandomseed - 1, myrandomseed - 1 + deficit):
        pistring += pidecimals[nmn]
    rotationkey = (str(myrandomseed) + pistring)

    rotatedrow1 = rotaterow(values, 0, int(rotationkey[0]))
    rotatedrow2 = rotaterow(values, 1, int(rotationkey[1]))
    rotatedrow3 = rotaterow(values, 2, int(rotationkey[2]))
    rotatedrow4 = rotaterow(values, 3, int(rotationkey[3]))
    rotatedrow5 = rotaterow(values, 4, int(rotationkey[4]))
    rotatedrow6 = rotaterow(values, 5, int(rotationkey[5]))
    rotatedrows = [rotatedrow1, rotatedrow2, rotatedrow3, rotatedrow4, rotatedrow5, rotatedrow6]

    rotatedcolumn1 = rotatecolumn(rotatedrows, 0, int(rotationkey[6]))
    rotatedcolumn2 = rotatecolumn(rotatedrows, 1, int(rotationkey[7]))
    rotatedcolumn3 = rotatecolumn(rotatedrows, 2, int(rotationkey[8]))
    rotatedcolumn4 = rotatecolumn(rotatedrows, 3, int(rotationkey[9]))
    rotatedsolumn5 = rotatecolumn(rotatedrows, 4, int(rotationkey[10]))
    rotatedcolumn6 = rotatecolumn(rotatedrows, 5, int(rotationkey[11]))
    rotatedcolumns = [rotatedcolumn1, rotatedcolumn2, rotatedcolumn3, rotatedcolumn4, rotatedsolumn5, rotatedcolumn6]

    return rotatedcolumns, myrandomseed


# Rotate the reference grid if private key is supplied

def rotateme(privatekey):
    rotatedrow1 = rotaterow(values, 0, int(privatekey[0]))
    rotatedrow2 = rotaterow(values, 1, int(privatekey[1]))
    rotatedrow3 = rotaterow(values, 2, int(privatekey[2]))
    rotatedrow4 = rotaterow(values, 3, int(privatekey[3]))
    rotatedrow5 = rotaterow(values, 4, int(privatekey[4]))
    rotatedrow6 = rotaterow(values, 5, int(privatekey[5]))
    rotatedrows = [rotatedrow1, rotatedrow2, rotatedrow3, rotatedrow4, rotatedrow5, rotatedrow6]

    rotatedcolumn1 = rotatecolumn(rotatedrows, 0, int(privatekey[6]))
    rotatedcolumn2 = rotatecolumn(rotatedrows, 1, int(privatekey[7]))
    rotatedcolumn3 = rotatecolumn(rotatedrows, 2, int(privatekey[8]))
    rotatedcolumn4 = rotatecolumn(rotatedrows, 3, int(privatekey[9]))
    rotatedsolumn5 = rotatecolumn(rotatedrows, 4, int(privatekey[10]))
    rotatedcolumn6 = rotatecolumn(rotatedrows, 5, int(privatekey[11]))
    rotatedcolumns = [rotatedcolumn1, rotatedcolumn2, rotatedcolumn3, rotatedcolumn4, rotatedsolumn5, rotatedcolumn6]

    return rotatedcolumns


# Encoding Function as per Rotated Grid

def encode(myplain_text, rotatedgrid):
    mycipher_text = ""
    for letter in myplain_text:
        dummy = findme(letter, rotatedgrid)
        mycipher_text += dummy
    return str(mycipher_text)


# Find User private key for Decoding

def findkey(userkey):
    userkeylength = len(userkey)
    userdeficit = 12 - userkeylength
    pistring = ""
    for nmm in range(int(userkey) - 1, int(userkey) - 1 + userdeficit):
        pistring += pidecimals[nmm]
    rotationkey = (str(userkey) + pistring)
    return rotationkey


# Breakdown cipher text into chunks

def breakcode(usercipher):
    decipher = re.compile(r'\w,\w|\w')
    broken = decipher.findall(usercipher)
    return broken


# Return number of characters in plain text

def countcipher(somecipher_text):
    test = [breakcode(somecipher_text)]
    return len(test[0]) / 2


# Create pairs of (column,row) from cipher_text
# Create the rotated grid based on private key
# Convert pairs into positions

def decode(somecipher_text, userkey):
    test = []
    flat_list = []

    mygrid = creategrid(userkey)

    test.append(breakcode(somecipher_text))

    for sublist in test:
        for item in sublist:
            flat_list.append(item)

    listpairs = [flat_list[ii:ii + 2] for ii in range(0, len(flat_list), 2)]

    columnpositions = [a[0] for a in listpairs]
    rowpositions = [a[1] for a in listpairs]

    columnindices = []
    rowindices = []

    for jj in range(len(columnpositions)):
        for j in range(len(mycolumns)):
            if columnpositions[jj] == mycolumns[j]:
                columnindices.append(mycolumns.index(columnpositions[jj]))

    for jj in range(len(rowpositions)):
        for j in range(len(myrows)):
            if rowpositions[jj] == myrows[j]:
                rowindices.append(myrows.index(rowpositions[jj]))

    my_decoded_text = ""
    for m in range(len(rowindices)):
        my_decoded_text += (mygrid[columnindices[m]][rowindices[m]])

    return my_decoded_text


# Generate keys equal to number of characters in string

def genkeylist(inputstring):
    pistring = ""
    keyarray = []
    myrandomseed = random.randint(1, len(pidecimals) - 12)
    length_randomseed = len(str(myrandomseed))
    deficit = 12 - length_randomseed

    for n in range(myrandomseed - 1, myrandomseed - 1 + deficit):
        pistring += pidecimals[n]
    keystring = str(myrandomseed) + pistring
    keyuserstring = str(myrandomseed) + pistring

    myfirstkey = int(keystring)

    for char in range(len(inputstring)):
        mynextkey = (myfirstkey ** (1 / 2)) % 1000000
        mynextkey = mynextkey - int(mynextkey)
        mynextkey = (str(mynextkey)[2:][:6])
        keyarray.append(str(mynextkey))
        myfirstkey = int(mynextkey)

    return keystring, keyarray


# Create the grid from user private key

def creategrid(userkey):
    thiskey = findkey(userkey)
    rotatedgrid = rotateme(thiskey)
    return rotatedgrid


# Remove spaces and punctuation from a string

def cleanstring(mystring):
    mystring = mystring.replace(" ", "")
    mystring = mystring.lower()
    mystring = mystring.translate(str.maketrans('', '', string.punctuation))
    return mystring


# Ensure number of rotations within a string
# is proportional to the length of string.
# This also limits number of keys if the message
# is too short.

def chopstring(some_str):
    tempx = len(some_str) ** (1 / 4)
    tempy = random.randint(0, 1)
    if tempy == 1:
        mynumkeys = math.ceil(tempx)
    else:
        mynumkeys = math.floor(tempx)
    stringparts = math.ceil((len(some_str) / mynumkeys))
    my_chunks = [some_str[k:k + stringparts] for k in range(0, len(some_str), stringparts)]
    return my_chunks, mynumkeys


# Main Program

levelchoice = input("Type 1 for Easy, 2 for Moderate or 3 for Hard: ")

if levelchoice == "1":
    print("You chose EASY level encryption: ")
    choice = input("Write 1 to Encode or 0 to Decode: ")

    if choice == "1":
        plain_text = input("Enter message to be encoded: ")
        plain_text = cleanstring(plain_text)
        finalgrid, key = randomrotation()
        print(f"The Encoded message is: {encode(plain_text, finalgrid)}")
        print(f"Your Private Key is: {key}")
    elif choice == "0":
        cipher_text = input("Enter message to be decoded: ")
        cipher_key = input("Enter Private Key: ")
        print(f"The decoded message is: {decode(cipher_text, cipher_key)}")
    else:
        print("Invalid input.")

elif levelchoice == "2":
    print("You chose MODERATE level encryption: ")
    choice = input("Write 1 to Encode or 0 to Decode: ")

    if choice == "1":

        str_coded = []
        keylist = []
        chunklengths = []
        codelist = []
        str_final = ""

        plain_text = input("Enter message to be encoded: ")
        plain_text = cleanstring(plain_text)
        chunks, numkeys = chopstring(plain_text)

        for i in range(0, len(chunks)):
            newgrid, randomseed = randomrotation()
            str_coded.append(encode(chunks[i], newgrid) + ".")
            keylist.append(str(randomseed))
            codelist.append(str_coded[i])
            chunklengths.append(len(str_coded[i]))
            str_final += (codelist[i])
        str_final.rstrip(".")
        print(f"The Encoded message is \n{str_final}")
        print(f"Your Keys are: {keylist}")

    elif choice == "0":
        cipher_chunks = []
        decoded_text = []
        sent_str = ""
        cipher_text = input("Enter message to be decoded: ")
        cipher_text = cipher_text[:-1]
        cipher_chunks.append(cipher_text.split("."))
        for i in range(0, len(cipher_chunks[0])):
            cipher_key = input(f"Enter Private Key number {i + 1}: ")
            decoded_text.append(decode(cipher_chunks[0][i], cipher_key))
        for i in decoded_text:
            sent_str += str(i)
        print(f"The Decoded message is : {sent_str}")
    else:
        print("Invalid input.")

elif levelchoice == "3":
    print("You chose HARD level encryption.")
    choice = input("Write 1 to Encode or 0 to Decode: ")

    cipher_list = []
    ciphertext = ""

    if choice == "1":
        plain_text = input("Enter message to be encoded: ")
        plain_text = cleanstring(plain_text)

        keyarray = genkeylist(plain_text)

        for n in range(0, len(plain_text)):
            newgengrid = creategrid(keyarray[1][n])
            cipher_list.append(encode(plain_text[n], newgengrid))
            ciphertext += str(cipher_list[n])
        print(f"The Encoded message is: {ciphertext}")
        print(f"Your Master Key is : {keyarray[0]}")

    elif choice == "0":
        actualstring = ""
        keyarray = []
        answerstring = []
        codechunks = []
        decoded_text = ""
        gridlist = [[]]
        codepairs = []

        ciphertext = input("Enter message to be decoded: ")
        actual_length = int(countcipher(ciphertext))
        firstkey = input("Enter Master Key: ")

        for i in range(0, actual_length):
            nextkey = (int(firstkey) ** (1 / 2)) % 1000000
            nextkey = nextkey - int(nextkey)
            nextkey = (str(nextkey)[2:][:6])
            keyarray.append(str(nextkey))
            firstkey = int(nextkey)

        for j in range(0, len(keyarray)):
            gridlist.append(creategrid(keyarray[j]))

        codechunks = breakcode(ciphertext)
        for ll in range(0, len(codechunks), 2):
            codepairs.append((codechunks[ll] + codechunks[ll + 1]))

        listpairs = [codechunks[ii:ii + 2] for ii in range(0, len(codechunks), 2)]

        columnpositions = [a[0] for a in listpairs]
        rowpositions = [a[1] for a in listpairs]

        columnindices = []
        rowindices = []

        for jj in range(len(columnpositions)):
            for j in range(len(mycolumns)):
                if columnpositions[jj] == mycolumns[j]:
                    columnindices.append(mycolumns.index(columnpositions[jj]))

        for jj in range(len(rowpositions)):
            for j in range(len(myrows)):
                if rowpositions[jj] == myrows[j]:
                    rowindices.append(myrows.index(rowpositions[jj]))

        for kk in range(0, actual_length):
            decoded_text += (gridlist[kk + 1][columnindices[kk]][rowindices[kk]])

        print(f"The Decoded message is : {decoded_text}")

    else:
        print("Invalid input.")

else:
    print("Invalid input.")

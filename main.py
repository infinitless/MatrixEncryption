import random
import re


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
positions = [1,2,3,4,5,6]


# The encoded text for any character (alphabet or number) = column + row, joined together
# Punctuation and spaces are ignored
# So "abc" as per Reference grid = 111211,1

# Define single row rotation

def rotaterow(myvalues, rowindex, rotation):
    rotatedrow = ""
    newrow = myvalues[rowindex]
    for n in range(0, 6):
        rotatedrow = newrow[rotation % 6:] + newrow[:rotation % 6]
    return rotatedrow


# Define single column rotation

def rotatecolumn(myvalues, columnindex, rotation):
    rotatedcolumn = ""
    newcolumn = [column[columnindex] for column in myvalues]
    for n in range(0, 6):
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
    randomseed = random.randint(1, len(pidecimals)-12)
    length_randomseed = len(str(randomseed))
    deficit = 12 - length_randomseed

    pistring = ""
    for n in range(randomseed - 1, randomseed - 1 + deficit):
        pistring += pidecimals[n]
    rotationkey = (str(randomseed) + pistring)

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

    return rotatedcolumns, randomseed


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

def encode(myplain_text, rotatedcolumns):
    mycipher_text = ""
    for letter in myplain_text:
        dummy = findme(letter, rotatedcolumns)
        mycipher_text += dummy
    return str(mycipher_text)


# Find User private key for Decoding

def findkey(userkey):
    userkeylength = len(userkey)
    userdeficit = 12 - userkeylength
    pistring = ""
    for n in range(int(userkey) - 1, int(userkey) - 1 + userdeficit):
        pistring += pidecimals[n]
    rotationkey = (str(userkey) + pistring)
    return rotationkey


# Breakdown cipher text into chunks

def breakcode(usercipher):

    decipher = re.compile(r'\w\,\w|\w')
    broken = decipher.findall(usercipher)
    return broken


# Create pairs of (column,row) from cipher_text
# Create the rotated grid based on private key
# Convert pairs into positions

def decode(cipher_text, userkey):

    test = []
    flat_list = []

    mygrid = creategrid(userkey)

    test.append(breakcode(cipher_text))
    for sublist in test:
        for item in sublist:
            flat_list.append(item)

    listpairs = [flat_list[i:i + 2] for i in range(0, len(flat_list), 2)]

    columnpositions = [a[0] for a in listpairs]
    rowpositions = [a[1] for a in listpairs]

    columnindices = []
    rowindices = []

    for i in range(len(columnpositions)):
        for j in range(len(mycolumns)):
            if columnpositions[i] == mycolumns[j]:
                columnindices.append(mycolumns.index(columnpositions[i]))

    for i in range(len(rowpositions)):
        for j in range(len(myrows)):
            if rowpositions[i] == myrows[j]:
                rowindices.append(myrows.index(rowpositions[i]))

    decoded_text = ""
    for m in range(len(rowindices)):
        decoded_text += (mygrid[columnindices[m]][rowindices[m]])

    print(decoded_text)

# Create the grid from user private key

def creategrid(userkey):

    key = findkey(userkey)
    rotatedgrid = rotateme(key)
    return rotatedgrid

# Main Program

choice = input("Write 1 to Encode or 0 to Decode: ")
if choice == "1":
    plain_text = input("Enter message to be encoded (spaces, punctuations and special characters will be ignored): ")
    finalgrid, key = randomrotation()
    print(f"The Encoded message is: {encode(plain_text.lower(), finalgrid)}")
    print(f"Your Private Key is: {key}")
elif choice == "0":
    print("Invalid inputs will exit the program.")
    cipher_text = input("Enter message to be decoded: ")
    cipher_key = input("Enter Private Key: ")
    decode(cipher_text, cipher_key)
else:
    print("Invalid input.")

**MATRIX ENCRYPTION ALGORITHM**

A complex algorithm that generates a random substitution grid based on user keys. The user keys, are generated from the combination of a pseudo-random number and the decimal expansion of PI.
This is a hobby project that gives a user the option to encrypt an alphanumeric text message using "Easy", "Moderate", and "Hard" levels.

The same message will output different encrypted messages in ALL levels as every time the key that the program generates will be different. The number of random grids possible is 36! (36 * 35 * 34 * ... * 1) = 371993326789901217467999448150835200000000. That's a lot!

**EASY LEVEL**

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 1
You chose EASY level encryption: 
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded:  Hello World
The Encoded message is: 2,112,211,121,121,11,12,21,21,11,12,21,11,122,12,2
Your Private Key is: 536516
```

The advantage of Easy level is that it is nice and simple. It generates only one key to remember. However, even without a key, the input of a random key will lead to a string of random characters which could then be prone to frequency analysis. A single alphanumeric character in the EASY level will be coded as another single character throughout the length of the message.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 1
You chose EASY level encryption: 
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded: AAAAA
The Encoded message is: 2121212121
Your Private Key is: 57278
```

If someone enters a random key the output will be prone to frequency analysis, although it might not be the original message.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 1
You chose EASY level encryption: 
Write 1 to Encode or 0 to Decode: 0
Enter message to be decoded: 2121212121
Enter Private Key: 12345
The decoded message is: yyyyy
```

**MODERATE LEVEL**

The MODERATE level splits the plain text message into a random number of parts and generates a random number of keys. The program then generates a random number of substitution grids.

The user will need all the keys to decode the message. These keys will need to be entered in the same sequence as the program outputs at the time of encryption.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 2
You chose MODERATE level encryption: 
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded: Hello World
The Encoded message is 
22,222,12,212,2111.2,22,1222,112,21,11,12,2.
Your Keys are: ['90229', '107543']
```

The advantage is that the same letter might be encoded differently throughout the length of the message.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 2
You chose MODERATE level encryption: 
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded: AAAAA
The Encoded message is 
22,222,222,2.2,11,12,11,1.
Your Keys are: ['585816', '816543']
```

If someone enters random keys, the resulting message will be difficult to crack using frequency analysis unless each part of the message is analysed separately. Therefore, the effort required to frequency-analyse the encoded text is multiplied proportionately.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 2
You chose MODERATE level encryption: 
Write 1 to Encode or 0 to Decode: 0
Enter message to be decoded: 22,222,222,2.2,11,12,11,1.
Enter Private Key number 1: 12345
Enter Private Key number 2: 67890
The Decoded message is : xxxtt
```

In the example above, it is difficult for someone to realise that the original text contains just a single alphabet "A", five times. In the first half of the message "A" was encoded as "x" and in the second half as "t".

**HARD LEVEL**

In the HARD, and most advanced level, a random substitution grid is generated for each character of the original message. A message with 100 characters will generate 100 random grids and therefore 100 random keys. However, the user just needs a 12 digit Master Key to decode the message.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 3
You chose HARD level encryption.
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded: Hello World
The Encoded message is: 2,112,12,22,222,12,12,21,111,211,12,22,12,12,221,2
Your Master Key is : 634337763159
```

The advantage is that a single letter could potentially have 35 different representations, depending on the length of the message. 

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 3
You chose HARD level encryption.
Write 1 to Encode or 0 to Decode: 1
Enter message to be encoded: AAAAA
The Encoded message is: 1,21,21,111,12,22,22,12,22,2
Your Master Key is : 778599739229
```

If someone enters a random Master Key, the message will be impossible to crack using frequency analysis as the grid is rotated with every character in the message.

```
Type 1 for Easy, 2 for Moderate or 3 for Hard: 3
You chose HARD level encryption.
Write 1 to Encode or 0 to Decode: 0
Enter message to be decoded: 1,21,21,111,12,22,22,12,22,2
Enter Master Key: 123456765432
The Decoded message is : 3kkga
```

The only thing that can be determined with certainty is the number of alphanumeric characters in the original message. It is impossible to use frequency analysis on the decoded message.

**Conclusion**

1. This is a hobby project and in no way designed to be used for professional or commercial encryption.
2. I hope users will have as much fun in learning and using it as I did in programming the same.

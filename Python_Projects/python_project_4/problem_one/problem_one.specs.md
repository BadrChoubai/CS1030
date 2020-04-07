# Problem One Specifications

Write a program that reads a list of words and calculates the Scrabble™ point value for each word.

- The words are read in from `1030 Project 04 01 Words.txt`
- If the length of the word is `0 or >= 10`, it's score should be `0`.
- Convert lowercase letters to uppercase with the method `str.upper()`
    - You can test a character is a letter using `str.isalpha()`

### Point Values Table
| Point Value | Letters |
|-------------|---------|
| 1 | A, E, I, L, N, O, R, S, T, U |
| 2 | D, G |
| 3 | B, C, M, P |
| 4 | F, H, V, W, Y |
| 5 | K |
| 8 | J, X |
| 10 | Q, Z |

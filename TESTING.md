# Lab 5 Testing Evidence

Date tested: 2026-02-22

This checklist follows the required categories:
- test multiple words
- test incorrect input
- test edge cases
- verify string comparisons

## CaesarCipher.py

### Multiple words
- Input: `hello`, key `3`
  - Encrypted: `KHOOR`
  - Decrypted: `HELLO`
- Input: `Attack at dawn!`, key `5`
  - Encrypted: `FYYFHP FY IFBS!`
  - Decrypted: `ATTACK AT DAWN!`

### Incorrect input
- Key entered as `abc`
  - Program response: `Key must be a whole number.`
  - Then accepts valid integer key and continues normally.

### Edge cases
- Input message: `""` (empty string), key `10`
  - Encrypted/decrypted output remains empty (no crash).
- Input message: `123!?`, key `7`
  - Non-letter characters are preserved exactly.

## LetterFrequency.py

### Multiple words
- Input: `AaBbCc xyz 123 !!!`
  - Console counts include: `A:2`, `B:2`, `C:2`, `X:1`, `Y:1`, `Z:1`.
  - Output file `frq.csv` contains matching rows.

### Incorrect input
- Included numbers/punctuation in message.
  - Program ignores non-letters and does not crash.

### Edge cases
- Input message: empty line
  - All letters reported as `0`.
  - File output still generated correctly.

## WordGame.py

### Multiple words
- Played full rounds with several guesses from words list.
- Program allows up to 6 counted guesses and ends with win/loss message.

### Incorrect input
- Guesses not exactly 5 letters (e.g., `abc`, `12345`) 
  - Program response: `Guess must be exactly 5 letters.`
  - Invalid guesses do not consume a counted attempt.

### Edge cases
- Uppercase guess input is normalized to lowercase before evaluation.
- Repeated letters in guesses still produce valid rating output.

### String comparison verification
- `inWord(letter, word)` verified true/false behavior.
- `inSpot(letter, word, spot)` verified exact-position comparison.
- `rateGuess(myGuess, word)` verified output format:
  - uppercase = correct letter/correct spot
  - lowercase = correct letter/wrong spot
  - `*` = letter not in word

## Summary
All required testing categories were completed, and the three lab programs behaved correctly after final fixes.

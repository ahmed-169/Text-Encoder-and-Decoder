## **FEATURES OF THE CODE:**

### 1. **Encoding Mechanism:**
- Words with 3 or more characters are encoded by surrounding them with a predefined prefix (`str1`) and suffix (`str2`).
- Words with fewer than 3 characters are simply reversed, which serves as a form of encoding.

### 2. **Decoding Mechanism:**
- Words that have the prefix (`str1`) and suffix (`str2`) are decoded by removing these markers, retrieving the original word.
- Words with fewer than 3 characters, which were reversed during encoding, are reversed again to decode and restore the original text.

### 3. **Command-driven Interaction:**
- The program offers a simple command interface, allowing the user to choose between encoding, decoding, or exiting the program by inputting numeric values.

### 4. **Continuous Loop:**
- The program continuously prompts the user for commands and text inputs until the user opts to quit by entering the command `3`.

### 5. **Flexible Encoding:**
- The program differentiates between words of 3 or more characters and those with fewer than 3. It applies distinct encoding methods for each type of word, ensuring versatility in handling various input types.

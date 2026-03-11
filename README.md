# 📻 The Signal Scrambler - String Manipulation Puzzle

A logic-based word game where you play as a radio interceptor. A secret transmission has been intercepted, but the characters have been shuffled by atmospheric interference. You must use your deduction skills to unscramble the letters and identify the original "Signal" before the connection is lost forever.

This project focuses on teaching:
* **String-to-List Conversion:** Breaking down immutable strings into mutable lists.
* **Randomized Shuffling:** Using the `random.shuffle()` function to reorder data.
* **String Reconstruction:** Using the `.join()` method to turn a list of characters back into a readable string.
* **Input Normalization:** Handling case sensitivity and accidental whitespace to improve user experience.

---

## ✨ Features

* **Dynamic Word Bank:** Randomly selects from a library of complex terms to keep every game unique.
* **Scramble Engine:** Every time a word is picked, its characters are shuffled into a new, unpredictable order.
* **Limited Attempts:** A "Connection Strength" mechanic that gives the player 3 chances to decode the word.
* **Hint System Logic:** Displays the exact character count to help the player narrow down possibilities.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `signal_scrambler.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python signal_scrambler.py
    ```

### 3. Gameplay Instructions
1.  **Analyze the Scramble:** Look at the jumbled letters provided.
2.  **Deduce:** Use the hint (number of letters) to think of words that fit.
3.  **Decode:** Type your guess and press Enter. You have 3 tries before the signal fades!



---

## 🧠 Code Structure Highlights

### The Scramble Process
Since we cannot shuffle a string directly, we must "cast" it into a list first. After shuffling the list, we use an empty string `""` as a glue to join the characters back together.

```python
# Step 1: String to List
char_list = list("PYTHON") 

# Step 2: Shuffle
random.shuffle(char_list) 

# Step 3: List to String
scrambled = "".join(char_list) 

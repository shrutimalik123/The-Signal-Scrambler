import random

def signal_scrambler():
    # 1. Game Content
    words = ["PYTHON", "CIRCUIT", "GALAXY", "VALENTINE", "BREAKTHROUGH", "ALGORITHM"]
    secret_word = random.choice(words)
    
    # 2. Scrambling Logic
    # Convert string to a list of characters to shuffle them
    char_list = list(secret_word)
    random.shuffle(char_list)
    scrambled = "".join(char_list)
    
    attempts = 3
    
    print("--- 📻 THE SIGNAL SCRAMBLER 📻 ---")
    print("Incoming encrypted transmission...")
    print(f"SCRAMBLED SIGNAL: {scrambled}")
    print(f"Hint: The word has {len(secret_word)} letters.")

    # 3. Game Loop
    while attempts > 0:
        guess = input(f"\n({attempts} attempts left) Decode the signal: ").upper().strip()
        
        if guess == secret_word:
            print(f"✅ SIGNAL DECODED! The message was indeed '{secret_word}'.")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("❌ DECODING FAILED. Interference detected. Try again.")
            
    # 4. End State
    print(f"\n📡 SIGNAL LOST. The correct word was '{secret_word}'.")

signal_scrambler()

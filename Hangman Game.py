import random
words = ["UMBRELLA", "COMPUTER", "TELESCOPE", "COMPUTER", "SMARTPHONE"]
word = random.choice(words)
total_chances = 7
guessed_words = "-"*len(word)
while total_chances != 0:
    print(guessed_words)
    letter = input("Guess a Letter :").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_words = guessed_words[:index] + letter + guessed_words[index + 1:]
                print(guessed_words)
        if guessed_words == word:
            print("Congretualtions, You Won!!!")
            break
    else:
        total_chances -= 1
        print("Incorrect Guess")
        print("The Remaining Chances : ", total_chances)
else:
    print("Game Over")
    print("You Lose")
    print("All the Chances are Exhausted.")
print("The Correct Word is : ", word)
import random
word_list=['Ashish','Nikki','Nikita']

chosen_word = random.choice(word_list);
print(chosen_word)

guess=input("Enter your guess: ").lower()
print(guess)

for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
        print("right")
    else:
        print("wrong")

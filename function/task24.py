import random
word_list=['ashish','nikki','nikita']

chosen_word = random.choice(word_list);
print(chosen_word)
game_over = False
correct_char=[]
while not game_over:
    guess=input("Enter your guess: ").lower()
    print(guess)
    word=""
    for i in range(len(chosen_word)):
        if guess==chosen_word[i]:
            word+=chosen_word[i]
            correct_char.append(guess)
        elif chosen_word[i] in correct_char:
            word += chosen_word[i]
        else:
            word += '_'
    print(word)

    if '_' not in word:
        game_over=True
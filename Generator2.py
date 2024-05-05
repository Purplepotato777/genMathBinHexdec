# max_exponant goes from 1 to 7 , the greater, the bigger & more difficult the deck. Set to {4,5,6,7} for level{2_1,2_2,2_3,2_4}
max_exponant = 7
deck = []

for i in range(1, max_exponant + 1) :
    for j in range(i + 1):
        question = str(2**i + 2**j)+ ' ' + '-' + ' ' + str(2**j)
        answer = str(2**i)
        deck.append([question , answer])

print(deck)  # should be store in txt file

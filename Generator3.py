from os import makedirs

answer_base = 'decimal answers'
level = 3
sublevel = 3

# max position of the significant bit if positon indexed from the right = 1 , Set to {4,8,8} for level{3_1,3_2,3_3}
# min_position of the significant bit if position indexed from the right = 1 , set to {0,4,0} for level {3_1,3_2,3_3} 
max_position = 8
min_position = 0
deck = []


for j in range(min_position, max_position) :
    binary_num = []
    for i in range(8) :
        binary_num.append(0)
    binary_num[j] = 1
    question = ''
    for i in range(8) :
        if i == 4:
            question += ' '
            question += str(binary_num[7-i])
        else :
            question += str(binary_num[7-i])
    answer = 0
    for i in range(8):
        answer += binary_num[i]*2**i
    deck.append([question , answer])
        

try:
    deckfile = open(f'decks/level{level}/sublevel{sublevel}.txt','a') 
except:
    makedirs(f'decks/level{level}')    
    deckfile = open(f'decks/level{level}/sublevel{sublevel}.txt','a') 
line = answer_base + '\n'
deckfile.write(line)
for card in deck:
   line = str(card[0]) +' -> '+ str(card[1])+ '\n'
   deckfile.write(line)  
deckfile.close
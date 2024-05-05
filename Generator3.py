# max position of the significant bit if positon indexed from the right = 1 , Set to {4,8} for level{3_1,3_2}
max_position = 8
deck = []

for j in range(max_position) :
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
        

print(deck)  # should be store in txt file

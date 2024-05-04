
max_exponant = 4 # from 1 to 7 , the greater, the bigger & more difficult the deck. Set to {4,5,6,7} for level{1_1,1_2,1_3,1_4}
min_exponant = 0
deck=[]

for i in range(min_exponant, max_exponant) :
  for j in range (i-1):
    deck[i][0] = stg(2**i) + '+'+  stg(2**j) 
    deck[i][1] = stg( 2**i + 2**j)

print(deck) # should be store in txt file
  

   

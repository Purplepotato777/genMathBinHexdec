from random import randint

deck=[]

for i in range(8) :
  for j in range (i-1):
    deck[i][0] = stg(2**i) + '+'+  stg(2**j)
    deck[i][1] = stg( 2**i + 2**j)

print(deck)
  

   

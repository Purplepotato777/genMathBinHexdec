# Project description

maths cards generator

The purpose is to generate decks of cards of a maths game ( project "Above the Stars", TuxMaths-like game for base 2 and base 16, training to automate mental arthimetic)

Each deck is compse of cards, each cards has two side: on one side a number or arithmetic operation, on the other the result or the same number in an other base.

Each deck will be generated proceduraly to avoid human mistake, and store in a txt file that will be load by the game.
This should provide easy costumisation to end-user.

instead of creating a big generator to handle change in base, arithmetic operation and filtering everything for everyneed, several ad-hoc generators would be created.
This is deliberate to avoid: enormous configurable generator hard and time-consuming to understand and configure everytime, multiplying files and their type to memorise configurations... 
Maximum flexibility when creating a deck of card will allow to created smooth learning curves, with decks finely adapted to the need of the learner. Not depending on a big generator integrated to the final will also allow the game to freely evolve in any directions , end_user and code_tinkers also having easier entry-level access. ( The javascript version of TuxMath for example has its cards generator include in the code of the game and doesn't allow to play with non-base 10 numbers as is).

Finally : both the generators project and the final game project are also meant to be learning experiences/experiments for me. I know I might not be using the most efficient code and maths formulas, I am enjoying my zone of proximal development.

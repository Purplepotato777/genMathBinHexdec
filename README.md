# Project description

maths cards generator

The purpose is to generate decks of cards for a math game (project "Above the Stars", TuxMath-like game for base 2 and base 16, training to automate mental arithmetic)


Each deck is composed of cards, each cards has two sides: on one side a number or arithmetic operation, on the other the result or the same number in another base.


Each deck will be generated procedurally to avoid human mistakes, and stored in a txt file that will be loaded by the game. This should provide easy customization to end-user.


Instead of creating a big generator to handle change in base, arithmetic operation and filtering everything for every need, several ad-hoc generators will be created. This is deliberate to avoid: an enormous configurable generator, hard and time-consuming to understand and configure every time, multiplying files and their types to store configurations... Maximum flexibility when creating a deck of card will allow to created smooth learning curves, with decks finely adapted to the need of the learner. Not depending on a big generator integrated in the final game will also allow the game to freely evolve in any directions, end-user and code-tinkers also having easier entry-level access. (The JavaScript version of TuxMath for example has its cards generator include in the code of the game and doesn't allow to play with non-base 10 numbers as is).

Finally: both the generators project and the final game project are also meant to be learning experiences/experiments for me. I know I might not be using the most efficient code and math formulas; I am enjoying my zone of proximal development.

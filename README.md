# Project description

maths cards generator

The purpose is to generate decks of cards for a math game (project "Above the Stars", TuxMath-like game for training to automate mental arithmetic: base 2, maybe base 16, and common port-services, with room for custom decks)


Each deck is composed of "cards", each cards has two sides: on one side a number or arithmetic operation ( question ), on the other the result or the same quantity expressed in another base ( answer ).


Each deck will be generated procedurally to avoid human mistakes, and stored in a txt file that will be loaded by the game. This should provide to the end user the possibility to mimick the deck structure easily and create their own decks in txt format.


Instead of creating a big generator to handle change in base, arithmetic operations and everything for every need, several ad-hoc generators will be created. This is deliberate to avoid: an enormous configurable generator, hard and time-consuming to understand and configure every time, creating the need to store configurations of the big generator in a third type of files... Not depending on a big generator integrated in the final Above-the -star game will also allow the game to freely evolve in any directions and provide end-users and code-tinkers with an easier entry-level access to costumisation. 

Note that the decks can be refine manually to smooth the learning curve when used in the Above-the-stars game, mainly by deleting some cards. level1/sublevel4 for example, had too many easy cards in it, harder cards were not popping frequently enough to be memorized quickly. A coefficient affecting speed of the cards, specific to each deck, is also added line 2. Above-the-stars game impose a time limit for answering and some answers takes longer to type than others. Decks with answer in the 8 digits binary format, that takes longer to type, for example, necessitate a smaller coefficient. 

Finally: both the generators project and the end-goal Above-the-star game project are also meant to be learning experiences/experiments for me. 

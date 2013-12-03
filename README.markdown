#Ariadne

##What is Ariadne?
Ariadne is a simple 2 player game where you try to navigate Perseus from one end of a labyrinth to the other, while a minotaur chases you and sends you back to the start if he catches you. One player controls via the WASD keys to move Perseus, and the other player highlights the way using a spotlight as Ariadne. This pretty loosely follows the Minotaur myth (http://en.wikipedia.org/wiki/Minotaur#Theseus_and_the_Minotaur) with the notable exception that the minotaur doesn't get killed and Ariadne uses a giant spotlight rather than golden thread to guide Perseus. Graphics are super basic (art is HARD) so you'll have to really use your imagination.

The spotlight slows down the minotaur, so it can be used strategically if the player playing Perseus knows what lies ahead. I was hoping to build in a couple of more tradeoff elements into the game like having certain paths only being active while the light is in a certain position, but I didn't have time.

I made it in python with a swig-wrapped version of my basic 2D engine cog (https://github.com/df3n5/cog) which uses SDL2, opengl, openAL and libpng.

There is a win32 build of the game : http://static.9lines.org/ariadne_win32.zip
I've tested it with an xbox controller + WASD keys, but you can also use the arrow keys to control the spotlight instead if you don't have a controller handy.


##License
GPLv3. See LICENSE.txt for a copy.

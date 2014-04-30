#Tools and their use
Life at UNC was created using Python script [https://www.python.org/downloads/] and the Pygame modules [http://www.pygame.org/download.shtml].
Your machine may have Python on it already, but you *must* download Pygame to work with our code.
We recommend using the open source tools GIMP [http://www.gimp.org/] for image creation and Tiled [http://www.mapeditor.org/] for mapt tileset graphics.
Check your code locally on your machine before pushing to your branch (more on that below) and opening a pull request.

#Files and Folders
##.py Files “Roadmap”:
- rpg.py (and associated config.py, Cores.py, and Classes.py): This is our “main” game. Original open source code from Iury Alves (https://github.com/IuryAlves/RPG-Pygame). We have heavily modified this to include event triggers -- when Rameses walks to a campus building, a sub-game begins (listed below). This file uses a new map and transparent sprites, created by our team. This, along with squirrel.py, has received the bulk of our time and attention.
- squirrel.py: A sub-game. Original open source code from Al Sweigart (http://inventwithpython.com/pygame) We have modified this one pretty heavily. Original source code has one sprite (a squirrel) that is used for both the player and the enemies. We have changed this so that the Duke Blue Devil is the enemy, and Rameses the player. The original code randomized the size and dimensions of the player and the enemies, which we have changed. The code for this game was the most flexible, and thus the most altered, of the three subgames we used.
- flippy.py: A sub-game. Original open source code from Al Sweigart (http://inventwithpython.com/pygame) We have modified this game to use familiar Carolina blue colors.
- wormy.py: A sub-game. Original open source code from Al Sweigart (http://inventwithpython.com/pygame) We have modified this game to use familiar Carolina blue colors.

##Folders “Roadmap”:
- BGM: contains music files (currently only contains a WAV of “Hark the Sound”)
- fonts: contains the font to be used in the main game dialog
- img: contains image files e.g. background images and the main game map
- sprites: contains the images that move around the screen (the player and enemies)

Additionally, there are some documentation files on the repo you may wish to look at:
- README.md
- CONTRIBUTORGUIDELINES.md
- LICENSE.md

#Branching
Please work on your own branch! Do NOT work directly on the master branch. Heads may explode.

#Pull requests
Submit a pull request with your work, with adequate documentation/comment of what you have done with the code.
Let somebody else look over your work and do the merging.
Flag your pull requests and issues with appropriate milestones.

#Etc.
Be polite and have fun with the project!
We look forward to working with you.

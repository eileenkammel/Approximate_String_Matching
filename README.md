# Approximate String Matching using BK-Trees



## Description

This project implements approximative string matching using [Burkard-Keller-Trees](https://en.wikipedia.org/wiki/BK-tree). The implemented matching metrics consist of [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) as the default and [Sørensen-Dice Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) as another option to choose from. The BK-Trees can be set up from scratch, passing your own textfile containing a word list, where each line contains a single word. Once set up, you can save (in python pickle format) and relaod the tree for later usage. A pre-build BK-Tree is included in the repository. The tree is based on [DeReWo List](https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/) which after being cleaned up yields a BK-Tree containing 326.939 German word forms. The clean up script can also be found in this repository in ```data_cleanup/DeReWo_cleaner.py```.
\
Whenever a tree is set up from a word list, a DOT file representing the tree is generated. That file can be used to visualize the tree with a tool of your choice.
Once the BK-Tree is set up or loaded, the program starts an interactive mode, where you can enter a word to find approximate matches for and an edit distance tolerance limit of your choice. The program will output any words that match your query.

The implementation follows the Model-View-Controller design pattern. An overview of the architecture is shown below.


![Alt text](resources/ApproxMatching.png?raw=true "Approximate String Matching using BK-Trees in MVC design pattern.")

***
## Requirements
***
## Installation
***
## Usage
***
## Tests
***
## Author

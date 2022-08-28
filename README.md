# Approximate String Matching using BK-Trees



## Description

This project implements approximative string matching using [Burkard-Keller-Trees](https://en.wikipedia.org/wiki/BK-tree). The implemented matching metrics consist of [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) as the default and [Sørensen-Dice Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient) as another option to choose from. The BK-Trees can be set up from scratch, passing your own textfile containing a word list, where each line contains a single word. Once set up, you can save (in python pickle format) and relaod the tree for later usage. A pre-build BK-Tree is included in the folder ```model/data```. The tree is based on [DeReWo List](https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/) which after being cleaned up yields a BK-Tree containing 326.939 German word forms. The clean up script can also be found in this repository in ```data_cleanup/DeReWo_cleaner.py```.
\
Whenever a tree is set up from a word list, a DOT file representing the tree is generated. That file can be used to visualize the tree with a tool of your choice.
Once the BK-Tree is set up or loaded, the program starts an interactive mode, where you can enter a word to find approximate matches for and an edit distance tolerance limit of your choice. The program will output any words that match your query.

The implementation follows the Model-View-Controller design pattern. An overview of the architecture is shown below.


![Architecture](resources/ApproxMatching.png?raw=true "Approximate String Matching using BK-Trees in MVC design pattern.")

***
## Requirements
[Python](https://www.python.org/downloads/) 3.10.4
\
\
numpy 1.22.3\
pydot 1.4.2\
pytest 7.1.2\
\
Requirements besides Python can be installed with pip by running
```pip3 install -r requirements.txt```
***
## Installation
Download and unzip Repository. Save to loacation of your choice. Install requirements above as needed. 
***
## Demo
A demo containing a pre-build tree with english word forms and Levenshtein Distance can be executed by running
```python3 demo.py```
\
To exit the demo, enter an empty line instead of a query word.
***
## Usage
```python3 approx_matching.py [-h] [--file FILE] [--save] [--metric [METRIC]]```\
\
For file either a .txt file containing a word list or a .pkl file containing a pickled BK-Tree can be passed. Note that the save flag ```--save``` should only be set when setting up the tree from a text file as should a metric name only be passed when setting up a new tree. For metric a valid meric name can be passed. At state, only Sorensen-Dice Coefficient can be chosen by entering one of the allowed names for it: SorensenDiceCoefficient, SDC, sdc. If no name is given, the Levenshtein Distance that is set as default is loaded. If you opt to save the tree, you will be prompted to enter a filename for saving the tree after the tree has been set up:\
\
![Saving](resources/save_prompt.png?raw=true "Saving prompt.")\
\
After the tree has been set up or loaded successfully, status output will inform you about the tree stats.\
\
![Stats](resources/stats_output.png?raw=true "Stats output.")\
\
Afterwards the interactive mode starts, where you are repeatedly prompted to enter a query word and an edit distance tolerance limit and are shown the output of your query. To exit the query loop, enter an empty line for query word.\
\
![Query](resources/query_loop.png?raw=true "Query Loop.")\
\
The maximum edit distance: The appropriate values depend on the metric chosen. If your tree is set up with Levenshtein Distance, the maximum edit distance can be any whole number greater than zero. The greater the distance, the less the similarity between the two words. For the Sorensen-Dice Coefficient, the maximum edit distance is a decimal number grater than zero and less than one. Words with an edit distance of zero have no similaryty at all, whereas words with distance one are identical.

***
## Tests
Tests are implemented for the BK-Tree and each of the Metrics. To run all, run ```pytest```\
\
To run them individually, run ```pytest model/metrics/test_levenshtein.py``` for Levenstein Distance, ```pytest model/metrics/test_sorensen_dice.py``` for Sorensen-Dice Coefficient and ```pytest model/test_bk_tree.py``` for the BK-Tree.\
\
Note: When running the tests for the BK-Tree, a DOT file is generated. Please manually delete the file after executing the test.
***
## Author
Eileen Kammel eileen.niedenfuehr@uni-potsdam.de
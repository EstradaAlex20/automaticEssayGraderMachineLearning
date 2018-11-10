# Automatic Short Response Essay Grader

This is a short project I undertook to learn a little bit about machine learning for fun. I went online and tried to find some good ideas for beginner ML projects and an interesting one I saw was making an automatic essay grader. This program actually uses a weighted decision tree which I don't think necessarily counts as ML, but it does produce the results that I wanted.

The main idea of this program is to analyze some variable amount of test data and then use that to predict the score of an essay that I feed into the program. Suprisingly I am able to get semi-reliable results without any actual analysis of content. The data that I store from each essay is as follows:

1. The essay's combined score. Each essay is hand graded by two different people, so I add those together and store that.
2. The essay's word count. 
3. The essay's filtered word count. I remove all "stop words" from the essay and then keep track of the number of words remaining. There is a large list of stop words online that you can check to see an example of a stop word, but generally it is a word that doesn't add content to the essay.
4. The essay's sentence count. 
5. The number of Nouns
6. The number of Adverbs
7. The number of Adjectives
8. The number of verbs

With this data alone I am able to predict an essay's score (each essay is graded 1-6) decently accurately. 

## Getting Started


### Prerequisites

This program makes use of a couple different python libraries which can all be installed using pip. 
They include:

```
sklearn, xlrd, matplotlib, and nltk.

You will also need to download the training data I used which can be found in this repository.
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be
Step 1. pip install the required libraries

```
pip install (library)
```
step 2. Installing additional nltk data

```
Create(and run) a python file that contains the following:
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
```
That is all you need to do in order to get this all setup. After step 2 you can run the file called MyParser.py and you will
get a pop-up that looks like ![this](https://puu.sh/BZtRV/5dd3b35dee.png)


## Built With

* [Scikit learn](https://scikit-learn.org/stable/documentation.html) - The machine learning library used
* [xlrd](https://xlrd.readthedocs.io/en/latest/) - Used for reading the testing data
* [MatPlotlib](https://matplotlib.org/contents.html) - Used to generate graphs showings the accuracy of this program
* [nltk](https://www.nltk.org/) - used for pulling stopwords and natural language processing

## Contributing

Please contribute or message me notes about this program. I am a junior in University right now and still learning. I would love to hear from any developers who stubble across this somehow. 

## Authors

* **Alex Estrada** - *Initial work* - [EstradaAlex20](https://github.com/EstradaAlex20)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

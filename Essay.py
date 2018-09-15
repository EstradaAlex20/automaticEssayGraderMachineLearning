from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
import nltk

class Essay:
    def __init__(self, essayID, essaySet, plainText, score1, score2):
        """

        :param essayID: A unique ID for each individual essay
        :param essaySet: A value 1-8 depending on which of the 8 essay sets this essay is from
        :param plainText: The ascii text of the essay
        :param score1: each essay was scored by 2 humans, these are there scores
        :param score2:
        """
        self.essayID = essayID                           #Complete
        self.essaySet = essaySet                         #Complete
        self.plainText = plainText                       #Complete
        self.scores = [score1, score2]                   #Complete
        self.unfilteredWordCount = 0                     #Complete
        self.wordCount = 0                               #Complete
        self.sentenceCount = len(plainText.split('.'))   #Complete
        self.wordsFiltered = []                          #Complete
        self.numOfNouns = 0                              #complete
        self.numOfAdverbs = 0                            #complete
        self.numOfAdjectives = 0                         #complete
        self.numOfVerbs = 0                              #complete
        self.numOfSpellingMistakes = 0                   #Incomplete

        stopWords = set(stopwords.words('english'))
        tokenizer = RegexpTokenizer(r'\w+')
        wordsUnfiltered = tokenizer.tokenize(self.plainText)
        self.unfilteredWordCount = len(wordsUnfiltered)

        for word in wordsUnfiltered:
            if word not in stopWords:
                self.wordsFiltered.append(word)

        self.wordCount = len(self.wordsFiltered)

        taggedWords = nltk.pos_tag(wordsUnfiltered)
        for i in range(len(taggedWords)):
            wType = taggedWords[i][1]
            if wType == 'NN' or wType == 'NNS' or wType == 'NNP' or wType == 'NNPS':
                self.numOfNouns += 1
            elif wType == 'RB' or wType == 'RBR' or wType == 'RBS':
                self.numOfAdverbs += 1
            elif wType == 'JJ' or wType == 'JJR' or wType == 'JJS':
                self.numOfAdjectives += 1
            elif wType == 'VB' or wType == 'VBD' or wType == 'VBG' or wType == 'VBN' or wType == 'VBP' or wType == 'VBZ':
                self.numOfVerbs += 1


    def __str__(self):
        rString = "Essay ID: " + str(self.essayID)\
            + "\nEssay Set: " + str(self.essaySet)\
            + "\nEssay Scores: " + str(self.scores[0]) + ", " + str(self.scores[1])\
            + "\nUnfiltered word count: " + str(self.unfilteredWordCount) \
            + "\nFiltered word count: " + str(self.wordCount) \
            + "\nSentence count: " + str(self.sentenceCount) \
            + "\nNumber of Nouns: " + str(self.numOfNouns) \
            + "\nNumber of Adverbs: " + str(self.numOfAdverbs) \
            + "\nNumber of Adjectives: " + str(self.numOfAdjectives) \
            + "\nNumber of Verbs: " + str(self.numOfVerbs) + "\n"

        return rString

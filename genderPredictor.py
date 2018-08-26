#!/usr/bin/env python
# encoding: utf-8
"""
genderPredictor.py
"""

from nltk import NaiveBayesClassifier,classify
import USSSALoader
import random

class genderPredictor():

    def __init__(self):
        self.nameDic = self._getNameDict()
    def getFeatures(self):
        maleNames,femaleNames=self._loadNames()

        featureset = list()

        for nameTuple in maleNames:
            features = self._nameFeatures(nameTuple[0])
            male_prob, female_prob = self._getProbDistr(nameTuple)
            features['male_prob'] = male_prob
            features['female_prob'] = female_prob
            featureset.append((features,'M'))

        for nameTuple in femaleNames:
            features = self._nameFeatures(nameTuple[0])
            male_prob, female_prob = self._getProbDistr(nameTuple)
            features['male_prob'] = male_prob
            features['female_prob'] = female_prob
            featureset.append((features,'F'))

        return featureset

    def trainAndTest(self,trainingPercent=0.80):
        featureset = self.getFeatures()
        random.shuffle(featureset)

        name_count = len(featureset)

        cut_point=int(name_count*trainingPercent)

        train_set = featureset[:cut_point]
        test_set  = featureset[cut_point:]

        self.train(train_set)

        return self.test(test_set)

    def classify(self,name):
        feats=self._nameFeatures(name)
        return self.classifier.classify(feats)

    def train(self,train_set):
        self.classifier = NaiveBayesClassifier.train(train_set)
        return self.classifier

    def test(self,test_set):
       return classify.accuracy(self.classifier,test_set)

    def _getProbDistr(self,nameTuple):
            male_prob = (nameTuple[1] * 1.0) / (nameTuple[1] + nameTuple[2])
            if male_prob == 1.0:
                male_prob = 0.99
            elif male_prob == 0.0:
                male_prob = 0.01
            else:
                pass
            female_prob = 1.0 - male_prob
            return (male_prob, female_prob)

    def getMostInformativeFeatures(self,n=5):
        return self.classifier.most_informative_features(n)

    def _loadNames(self):
        return USSSALoader.getNameList()

    def _nameFeatures(self,name):
        name=name.upper()
        return {
            'last_letter': name[-1],
            'last_two' : name[-2:],
            'last_three': name[-3:],
            'last_is_vowel' : (name[-1] in 'AEIOUY')
        }

    # made by me, hopefully will use later to remove machine learning
    def getGender(self, name, verbose=False):
        try:
            smalldic = self.nameDic[name.upper()]
            men = list(smalldic.keys())[0]
            women = list(smalldic.values())[0]
            if verbose:
                print (men / (men + women))
            if (men / (men + women) > .6):
                return 'M'
            elif (men / (men + women) < .4):
                return 'F'
            else:
                return 'GN'
        except:
            if verbose:
                print ('Name not in database')
            return 'U'

    def _getNameDict(self):
        tuples = self._loadNames()
        dictTupleMen = {a:{b:c} for a,b,c in tuples[0]}
        dictTupleWomen = {a:{b:c} for a,b,c in tuples[1]}
        return {**dictTupleMen, **dictTupleWomen}

if __name__ == "__main__":
    gp = genderPredictor()
    accuracy=gp.trainAndTest()
    print('Accuracy: %f'%accuracy)
    print('Most Informative Features')
    feats=gp.getMostInformativeFeatures(10)
    for feat in feats:
        print('\t%s = %s'%feat)
    name = 'Sam'
    print('\n%s is classified as %s'%(name, gp.classify(name)))

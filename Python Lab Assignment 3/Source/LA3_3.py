#Importing libraries
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import ngrams

#Reading file content
f = open('Sample1.txt', 'r')
filecontent = f.read();

wordlemmatizer=nltk.WordNetLemmatizer() #Lemmatizing the sentence using WordNetLemmatizer
words=word_tokenize(filecontent) #Tokenizes the given sentence to words
sentencetokenize=sent_tokenize(filecontent) #Tokenizes the text file to sentences
print(sentencetokenize)
samplelist=[]
for line2 in words:
    lwords=wordlemmatizer.lemmatize(line2)
    samplelist.append(lwords) #Appends every lemmatize word to list
print(samplelist)

print("Bigrams")
samplelist2=[]
bigrams=ngrams(words,2) #Bigram operation performed by using ngrams function
for a in bigrams:
    samplelist2.append(a)
print(samplelist2)

frequencydistribution=nltk.FreqDist(samplelist2)
wordfrequency=frequencydistribution.most_common() #Returns all the word frequency of bigrams
firstfive=frequencydistribution.most_common(5) #Returns the top 5 bigrams from bigrams list
print("Word frequency of bigrams")
print(wordfrequency)
print("Top 5 bigrams")
print(firstfive)
concatenatesentence=[]
for sentence in sentencetokenize:
    for x,y in samplelist2:
        for((word1,word2),count) in firstfive:
            if(x,y == word1,word2): #If the given sentence has the top most frequency bigrams then this loop is executed else it breaks
                concatenatesentence.append(sentencetokenize) #Each sentence with one of the top 5 bigram is appended ta a list

print("Concatenated sentence") #The final concatenated sentence
print(max(concatenatesentence))





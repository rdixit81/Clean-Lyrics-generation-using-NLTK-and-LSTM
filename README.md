# Clean-Lyrics-generation-using-NLTK-and-LSTM

The first file senstence_classifier.py takes the input from any of the file that cantaints the orignal lyrics and tokennize the words to findout the probablity of lines and then compair it with some predefine limit and if theprobablity is higher then that it is discarded as it is much negative sentence abd then the positive lyrics are copied in filter.txt
Then second file will run i.e model.py that works in two ways that are test and train. in training the LSTM the lyrics from filter.txt are used to extract all the syllabels and markovify makes a list of all the similar words available in filter.txt, it works for five epocs. In test phase the code will generate new lyrics and save it into new text file i.e lyrics.txt
Now third file speech.py use this lyrics.txt file to convert it into voice using Pyttsx (Python text to speech) library.

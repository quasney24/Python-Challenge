'''
Import a text file filled with a paragraph of your choosing.

Assess the passage for each of the following:

Approximate word count

Approximate sentence count

Approximate letter count (per word)

Average sentence length (in words)
'''

import re



text_file = open("raw_data/paragraph_1.txt","r")
message = text_file.read()
#print (message)
words = message.split(" ")
number_of_words = len(words)
average_word = sum(len(x) for x in words) / len(words)
average_sentence = len(words) / message.count(".")


print("Paragraph Analysis")
print ("----------------------------")
print("Total Words: ", len(words))
print ("Total Sentances: ", message.count("."))
print("Average Letter Count: ", average_word)
print ("Average Sentence Length: ", average_sentence)
text_file.close()


#Krista Rosemary, Olivia
import string

def sentence_to_list(input_sentence):
    #remove punctuation from the sentence
    input_sentence = input_sentence.translate(str.maketrans('','', string.punctuation))
    #split the sentence into a list of words
    output_list = input_sentence.split()
    return output_list

my_sentence = "This is a sample sentence with some punctuation, like a comma."
my_list = sentence_to_list(my_sentence)
print(my_list)


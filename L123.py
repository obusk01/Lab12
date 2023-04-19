# #krista, Rosemary, Olivia
# my_string = "hello, my name is John."
# my_list = my_string.split()
# print(my_list)

def get_hashtags(input_sentence):
    output_list = []
    for word in input_sentence.split():
        if word.startswith("#"):
            output_list.append(word)
    return output_list

my_sentence = "I love #Python and #MachineLearning!"
my_list = get_hashtags(my_sentence)
print(my_list)

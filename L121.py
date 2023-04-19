#Krista, Rosemary, Olivia
import re

def get_hashtag_ranking(input_sentence):
    #find all hashtags in the input input_sentence
    hashtag_list = re.findall(r"#\w+", input_sentence)

    #count the frequency of each hashtag
    hashtag_count = {}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag] += 1
        else:
            hashtag_count[hashtag] = 1

    #Define a helper function to get the frequency of a hashtag
    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]

    #Sort the hashtags by frequency in descending order
    sorted_hashtags = sorted(hashtag_count.items(), key=get_frequency, reverse=True)

    #Creat a list of the sorted hashtags (without the frequency counts)
    output_list = [hashtag for (hashtag, count) in sorted_hashtags]

    return output_list

my_sentence = "I love #Python and #MachineLearning, but #DataScience is also grea. #Python #Python #DataScience"
my_list = get_hashtag_ranking(my_sentence)
print(my_list)

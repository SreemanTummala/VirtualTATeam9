# This is the back end, part 2, of the Virtual TA project, Group: T9
# This is an attempt at using Machine Learning to create a smart chatbot
# that will be talking to a student, specifically asking questions about
# algorithms.

import nltk
import pip
from newspaper import Article
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

# Get the article/dataset
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text

# Print the articles text
# print(corpus)

TA_Information = 'Akshay Jha, email: akshay.jha@utdallas.edu'
Virtual_TA_Name = 'Tim Robert: '

# Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)        # Should get us a list of sentences

# Print the list of sentences to check and ensure it works (Debugging)
# print(sentence_list)

# A function to return a random greeting response to a user's greeting
def greeting_response(text):
    text = text.lower()

    # Bots Greeting Response
    bot_greetings = ['Why Hello There', 'General Kenobi', 'I\'ve been expecting you', 'bonjour', 'hola']

    # User's greeting
    user_greetings = ['hi', 'hello', 'hola', 'greetings', 'whassup', 'what\'s up', 'hi there', 'bonjour']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)

    # We want to ensure that index does not contain itself
    # i.e. if asked "what is O(merge sort)", index should not contain
    # "what is O(merge sort)" as it would reply with the same text, rather than answer
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:      # Our Confidence Score
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1                           # We have found a response
            j = j+1
        if j > 2:
            break

    if response_flag == 0:                              # We did not find a confident response
        bot_response = bot_response + ' ' + 'I apoligize, I don\'t understand. Please refer to TA: ' + TA_Information + ' or the professor.'

    sentence_list.remove(user_input)

    return bot_response


def index_sort(list_var):
    # Preparing variables for use
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var

    # Index of highest value of list is going to be in new list
    # This index represents highest value "phrase" to respond with
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

#"I need to know about Merge Sort"

#"The Big O of Merge Sort is O(nlgn)"

# Start the chat
print(Virtual_TA_Name + 'I am Tim Robert. I can answer most of your questions regarding Algorithms. If you want to exit, type \'bye\'.')


exit_list = ['exit', 'see you later', 'bye', 'have a good day!', 'quit', 'break']

# Our actual
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print(Virtual_TA_Name + "Have a great day. :)")
        break

    else:
        if greeting_response(user_input) != None:
            print(Virtual_TA_Name + greeting_response(user_input))

        else:
            print(Virtual_TA_Name + bot_response(user_input))

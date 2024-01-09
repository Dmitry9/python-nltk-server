import sys
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

# https://www.nltk.org/api/nltk.tag.pos_tag.html
# https://www.geeksforgeeks.org/nlp-part-of-speech-default-tagging/
# https://realpython.com/nltk-nlp-python/#getting-started-with-pythons-nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Get the input string from command-line arguments
input_string = sys.argv[1]

result = pos_tag(word_tokenize(input_string), tagset='universal')

json_data = [{key: value} for key, value in result]

print(json_data)

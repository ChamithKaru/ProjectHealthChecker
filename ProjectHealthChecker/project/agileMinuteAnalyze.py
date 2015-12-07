__author__ = 'Thish'

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



EXAMPLE_TEXT = "Nishani who is assigned the task of web dashboard has completed the work up to now. Sunera has a" \
               " blocking issue with his task form submission because Anupa had not completed his task of web services yet"
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(EXAMPLE_TEXT)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []
tasks = ['design web dashboard', 'develop form submission', 'write web services']
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)



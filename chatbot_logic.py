import json
import random
import nltk
from nltk.stem import PorterStemmer
import os

stemmer = PorterStemmer()

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True) 

current_dir = os.path.dirname(os.path.abspath(__file__))

# --- THE FIX IS ON THIS LINE BELOW (Added encoding='utf-8') ---
with open(os.path.join(current_dir, 'intents.json'), 'r', encoding='utf-8') as file:
    intents = json.load(file)

def process_text(text):
    words = nltk.word_tokenize(text.lower())
    return [stemmer.stem(w) for w in words]

def get_response(user_input):
    user_words = process_text(user_input)
    best_intent, max_overlap = None, 0
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            overlap = len(set(user_words).intersection(set(process_text(pattern))))
            if overlap > max_overlap:
                max_overlap, best_intent = overlap, intent
                
    if best_intent and max_overlap > 0:
        return random.choice(best_intent['responses'])
    return "I am still learning! Could you ask about what green hydrogen is?"
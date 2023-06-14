import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Specify the path to your JSON file
cache_path = './cache.json'



def filter_items(search_term, items):
    search_tokens = list(set(search_term.lower().split()))
    filtered_items = []
    for item_id, item_data in items.items():
        item_tags = item_data["tags"]
        if any(any(token in tag for tag in item_tags) for token in search_tokens):
            filtered_items.append(item_data)
    return filtered_items


# def search_items(search_term, items):
#     stop_words = set(stopwords.words("english"))
#     tokens = [token for token in word_tokenize(search_term.lower()) if token not in stop_words]
    
#     best_match = None
#     best_weight = 0
    
#     for item_data in items:
#         tags = item_data["tags"]
#         weight = sum(1 for token in tokens if any(token in tag for tag in tags))
#         if weight > best_weight:
#             best_weight = weight
#             best_match = item_data
    
#     return best_match


def search_items(search_term, items):
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in word_tokenize(search_term.lower()) if token not in stop_words]
    
    best_match = None
    best_weight = 0
    
    for item_data in items:
        tags = item_data["tags"]
        weight = 0
        
        # Check for exact matches in tags
        for token in tokens:
            if any(token == tag for tag in tags):
                weight += 2  # Assign higher weight for exact matches
        
        # Check for partial matches in tags
        for token in tokens:
            if any(token in tag for tag in tags):
                weight += 1  # Assign lower weight for partial matches
        
        if weight > best_weight:
            best_weight = weight
            best_match = item_data
    
    return best_match

def get_item_id_by_search(name):
    with open(cache_path) as json_file:
        data = json.load(json_file)
    items_full = data['__collections__']['items']
    search_term = name + ' ' + ''.join(name.split())
    lemmatizer = WordNetLemmatizer()
    search_tokens_singular = [lemmatizer.lemmatize(word.lower()) for word in search_term.lower().split()]
    search_term = search_term + " " + ' '.join(search_tokens_singular)
    filtered_items_list = filter_items(search_term,items_full)
    best_match = search_items(search_term,filtered_items_list)
    if not best_match:
        return "NA-"+name
    return best_match['itemId']

# res = search_item_by_name("butter milk")
# print(res)



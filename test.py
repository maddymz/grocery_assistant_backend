from nltk.stem import WordNetLemmatizer
import nltk

word = "tomatoes"

lemmatizer = WordNetLemmatizer()
singular_word = lemmatizer.lemmatize(word)

print(singular_word)  # Output: "tomato"
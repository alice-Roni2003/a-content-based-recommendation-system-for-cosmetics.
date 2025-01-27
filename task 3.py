# Import necessary libraries
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/thiru/Documents/cosmetics.csv')

# Initialize variables
corpus = []  # List to hold the tokenized ingredients for each product
ingredient_idx = {}  # Dictionary to map each ingredient to an index
idx = 0  # Counter to assign index values

# Tokenize ingredients and create a bag of words
for ingredients in df['Ingredients']:
    # Convert ingredients to lowercase
    ingredients_lower = ingredients.lower()
    
    # Split the ingredients string into a list of tokens (by separating on commas)
    tokens = ingredients_lower.split(', ')
    
    # Append the list of tokens to the corpus
    corpus.append(tokens)
    
    # Assign an index to each ingredient if it's not already in the dictionary
    for token in tokens:
        if token not in ingredient_idx:
            ingredient_idx[token] = idx
            idx += 1

# Output the corpus and the ingredient index dictionary
print(corpus)
print(ingredient_idx)

# Import necessary libraries
import pandas as pd
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/thiru/Documents/cosmetics.csv')

# Filter df for "Moisturizer" in the Label column
moisturizers = df[df['Label'] == 'Moisturizer']

# Filter moisturizers for 'Dry' == 1
moisturizers_dry = moisturizers[moisturizers['Dry'] == 1]

# Drop the current index and replace it with a new one
moisturizers_dry.reset_index(drop=True, inplace=True)

# Initialize variables for the document-term matrix
corpus = []  # List to hold the tokenized ingredients for each product
ingredient_idx = {}  # Dictionary to map each ingredient to an index
idx = 0  # Counter to assign index values

# Tokenize ingredients and create a bag of words
for ingredients in moisturizers_dry['Ingredients']:
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

# Get the total number of products in the moisturizers_dry DataFrame
M = moisturizers_dry.shape[0]

# Get the total number of ingredients in the ingredient_idx dictionary
N = len(ingredient_idx)

# Initialize a document-term matrix (MxN) with zeros
A_df = pd.DataFrame(0, index=moisturizers_dry.index, columns=ingredient_idx.keys())

# Fill the document-term matrix with presence (1) or absence (0) of ingredients
for i, ingredients in enumerate(moisturizers_dry['Ingredients']):
    # Convert ingredients to lowercase and split them by ', '
    ingredients_lower = ingredients.lower().split(', ')
    
    # For each token, update the document-term matrix
    for ingredient in ingredients_lower:
        if ingredient in ingredient_idx:
            A_df.at[moisturizers_dry.index[i], ingredient] = 1  # Set 1 for presence of the ingredient

# Output the document-term matrix
print(A_df)

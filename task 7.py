# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE

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

# Get the total number of ingredients
N = len(ingredient_idx)

# Define the one-hot encoder function
def oh_encoder(ingredients):
    """
    This function encodes the ingredient list as a one-hot vector.
    """
    # Initialize a matrix of zeros with width N (the same width as the document-term matrix A)
    x = np.zeros(N)
    
    # Convert the ingredients to lowercase and split by ', '
    ingredients_lower = ingredients.lower().split(', ')
    
    # Get the index values for each ingredient from ingredient_idx and put 1 at the corresponding index
    for ingredient in ingredients_lower:
        if ingredient in ingredient_idx:
            idx = ingredient_idx[ingredient]
            x[idx] = 1  # Set the corresponding index to 1
    
    return x

# Initialize the document-term matrix (MxN) with zeros
A_df = pd.DataFrame(0, index=moisturizers_dry.index, columns=ingredient_idx.keys())

# Apply oh_encoder to each list of tokens in the 'Ingredients' column
for i, ingredients in enumerate(moisturizers_dry['Ingredients']):
    # Apply oh_encoder to get a one-hot encoded matrix for each list of ingredients
    one_hot_encoded = oh_encoder(ingredients)
    
    # Update the corresponding row in the document-term matrix A_df
    A_df.iloc[i] = one_hot_encoded

# Task 7: Reduce dimensions using t-SNE
# Create a TSNE instance
model = TSNE(n_components=2, learning_rate=200, random_state=42)

# Apply fit_transform() on the document-term matrix
tsne_features = model.fit_transform(A_df)

# Assign the first column of tsne_features to moisturizers_dry['x']
moisturizers_dry.loc[:,'x'] = tsne_features[:, 0]

# Assign the second column of tsne_features to moisturizers_dry['y']
moisturizers_dry.loc[:,'y'] = tsne_features[:, 1]

# Output the result to check
print(moisturizers_dry[['x', 'y']].head())

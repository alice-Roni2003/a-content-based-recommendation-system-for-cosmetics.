# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/thiru/Documents/cosmetics.csv')

# Display a sample of five rows of the data
print(df.sample(5))

# Display counts of types of products using value_counts on the 'Label' column
product_counts = df['Label'].value_counts()
print(product_counts)

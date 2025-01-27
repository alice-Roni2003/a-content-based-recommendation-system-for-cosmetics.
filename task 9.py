from bokeh.plotting import figure, show, output_file, save
from bokeh.models import ColumnDataSource, HoverTool
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

# Tokenize ingredients and create a bag of words
corpus = []
ingredient_idx = {}
idx = 0

for ingredients in moisturizers_dry['Ingredients']:
    ingredients_lower = ingredients.lower()
    tokens = ingredients_lower.split(', ')
    corpus.append(tokens)
    for token in tokens:
        if token not in ingredient_idx:
            ingredient_idx[token] = idx
            idx += 1

# Initialize the document-term matrix (MxN) with zeros
N = len(ingredient_idx)
A_df = pd.DataFrame(0, index=moisturizers_dry.index, columns=ingredient_idx.keys())

# Define the one-hot encoder function
def oh_encoder(ingredients):
    x = np.zeros(N)
    ingredients_lower = ingredients.lower().split(', ')
    for ingredient in ingredients_lower:
        if ingredient in ingredient_idx:
            idx = ingredient_idx[ingredient]
            x[idx] = 1
    return x

# Apply oh_encoder to each product's ingredients list
for i, ingredients in enumerate(moisturizers_dry['Ingredients']):
    one_hot_encoded = oh_encoder(ingredients)
    A_df.iloc[i] = one_hot_encoded

# Reduce dimensions using t-SNE
model = TSNE(n_components=2, learning_rate=200, random_state=42)
tsne_features = model.fit_transform(A_df)

# Assign the t-SNE features to the moisturizers_dry DataFrame
moisturizers_dry.loc[:, 'x'] = tsne_features[:, 0]
moisturizers_dry.loc[:, 'y'] = tsne_features[:, 1]

# Create a ColumnDataSource from the moisturizers_dry DataFrame
source = ColumnDataSource(moisturizers_dry)

# Explicit file path
output_path = "C:/Users/thiru/Documents/tsne_scatter_with_hover.html"
output_file(output_path)
print(f"Saving HTML to: {output_path}")

# Create a new plot
plot = figure(title="t-SNE Scatter Plot of Moisturizers", 
              x_axis_label='T-SNE 1', 
              y_axis_label='T-SNE 2', 
              width=700, height=700)

# Add a circle renderer
plot.circle(x='x', y='y', size=8, source=source)

# Add a hover tool to display additional information
hover = HoverTool()
hover.tooltips = [
    ('Item', '@Name'),
    ('Brand', '@Brand'),
    ('Price', '$@Price'),
    ('Rank', '@Rank')
]

# Add the hover tool to the plot
plot.add_tools(hover)

# Save and show the plot
save(plot)
print("Plot saved successfully with hover tool.")
show(plot)

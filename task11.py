import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('C:/Users/thiru/Documents/cosmetics.csv')

# Filter df for "Moisturizer" in the Label column
moisturizers = df[df['Label'] == 'Moisturizer']

# Filter moisturizers for 'Dry' == 1
moisturizers_dry = moisturizers[moisturizers['Dry'] == 1]

# Reset index to clean up the DataFrame for processing
moisturizers_dry.reset_index(drop=True, inplace=True)

# Select the two products by name
product_1_name = "Color Control Cushion Compact Broad Spectrum SPF 50+"
product_2_name = "BB Cushion Hydra Radiance SPF 50"

# Filter to get rows for the two selected products
product_1 = moisturizers_dry[moisturizers_dry['Name'] == product_1_name]
product_2 = moisturizers_dry[moisturizers_dry['Name'] == product_2_name]

# Check if both products exist in the dataset
if product_1.empty:
    print(f"Product '{product_1_name}' not found in the dataset.")
else:
    print(f"Details for '{product_1_name}':")
    print(product_1[['Name', 'Brand', 'Price', 'Rank']])
    print("Ingredients:\n", product_1['Ingredients'].values[0])
    print("\n" + "-"*60 + "\n")

if product_2.empty:
    print(f"Product '{product_2_name}' not found in the dataset.")
else:
    print(f"Details for '{product_2_name}':")
    print(product_2[['Name', 'Brand', 'Price', 'Rank']])
    print("Ingredients:\n", product_2['Ingredients'].values[0])
    print("\n" + "-"*60 + "\n")

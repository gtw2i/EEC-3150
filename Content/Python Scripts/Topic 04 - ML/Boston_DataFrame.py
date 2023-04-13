import pandas as pd
from sklearn.datasets import load_boston
import seaborn as sns

# Load the Boston Housing dataset
boston = load_boston()

# Create a Pandas DataFrame
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)

# Add the target variable to the DataFrame
df['target'] = boston.target

# Print the first few rows of the DataFrame
print(df.head())

# Print the shape of the DataFrame
print("DataFrame shape:", df.shape)

sns.pairplot(df)



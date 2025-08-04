import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
-------------------------------------------------------------------------------------
# Remove all rows with NULL values:
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
---------------------------------------------------------------------------------------------
# Replace NULL values with the number 130:
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
---------------------------------------------------------------------------------------
# Calculate the MEAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)
------------------------------------------------------------------------------------------
# Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

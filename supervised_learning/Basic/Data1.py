import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ["Sakil", "Rakin", "Kawser", "Sohad", "Kamal"],
        "Age" : [25, None, 26, None , 27],
        "Mark" : [85, 64, 63, 86, None]

    }
)
print(f"Our Created Dataframe:{df}")
print(f"Total missing value in our Dataframe:\n{df.isnull().sum()}")
print(f"Percentage of Total missing value in our Dataframe:\n{df.isnull().mean() * 100}")


df_drop = df.dropna()
print(f"Deleted columns those had missing values:{df.dropna()}")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

print(f"Our final handled dataframe: {df}")
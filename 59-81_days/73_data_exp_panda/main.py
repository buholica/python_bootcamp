# I used Google Colaboratory for this project
import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df = df.dropna()
clean_df.tail()

clean_df["Starting Median Salary"].max()

clean_df["Starting Median Salary"].idxmax()

clean_df["Undergraduate Major"].loc[43]

clean_df["Mid-Career Median Salary"].max()

clean_df["Mid-Career Median Salary"].idxmax()

clean_df["Undergraduate Major"].loc[8]

clean_df["Starting Median Salary"].min()

clean_df["Starting Median Salary"].idxmin()

clean_df["Undergraduate Major"].loc[49]

clean_df["Mid-Career Median Salary"].min()

clean_df["Mid-Career Median Salary"].idxmin()

clean_df["Undergraduate Major"].loc[18]

spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(1, "Spread", spread_col)
clean_df.head()

low_risk = clean_df.sort_values("Spread")

low_risk = clean_df.sort_values("Spread")
low_risk[["Undergraduate Major", "Spread"]].head()

highest_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()

high_risk = clean_df.sort_values("Spread", ascending=False)
high_risk[["Undergraduate Major", "Spread"]].head()

clean_df.groupby("Group").count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby("Group").mean()

"""# Новий розділ"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

df.head()

df.shape

df.count()

clean_df = df.dropna()

df.tail()

clean_df.groupby("TAG").sum().sort_values("POSTS", ascending=False)

clean_df.groupby("TAG").count()

df.DATE[1]

# Convert Entire Column
clean_df['DATE'] = pd.to_datetime(clean_df['DATE'])
df.head()

reshaped_df = clean_df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df

reshaped_df.head()

reshaped_df.tail()

reshaped_df.shape

reshaped_df.columns

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)

reshaped_df.head()

reshaped_df.isna().values.any()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("DATE", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df.python)
for column in reshaped_df.columns:
  plt.plot(reshaped_df.index, reshaped_df[column],
           linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
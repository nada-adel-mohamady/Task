from django.shortcuts import render
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

    
df = pd.read_csv("train_users_2.csv")

counts=df['country_destination'].value_counts()
unique_values1=df['country_destination'].unique()


num_of_rows=len(df['affiliate_channel'])
Percentage=100*df['affiliate_channel'].value_counts()/num_of_rows
unique_values2=df['affiliate_channel'].unique()

provider_num_of_rows=len(df['affiliate_provider'])
provider_Percentage=100*df['affiliate_provider'].value_counts()/provider_num_of_rows
unique_values3=df['affiliate_provider'].unique()


group_by_age = df.groupby('age')
signup_app=df['signup_app']

print(signup_app)
#show the first figure samples per class 
plt.bar(unique_values1, counts)
plt.ylabel("Count")
plt.title('Samples per class')
plt.savefig("Fig1")
plt.clf()

#show the second figure percentage per class 
plt.bar(unique_values2, Percentage, color=['firebrick'])
plt.ylabel("Percentage")
plt.title('Affiliate channel percentage')
plt.xticks(rotation=90)
plt.savefig("Fig2")
plt.clf()

#show the first figure samples per class 
plt.bar(unique_values3, provider_Percentage, color=['firebrick'])
plt.ylabel("Percentage")
plt.title('Affiliate channel provider percentage')
plt.xticks(rotation=90)
plt.savefig("Fig3")
plt.clf()


pd.crosstab(df['signup_app'],df['age']).plot.bar()
plt.savefig("Fig4")
plt.clf()

#counts4=df['data_account_created'].sum(axis=1)

#users = pd.read_csv("train_users_2.csv")


#sns.set_style("whitegrid", {'axes.edgecolor': '0'})
#sns.set_context("poster", font_scale=1.1)
plt.plot(df['date_account_created'].unique(), df['date_account_created'].value_counts())
#df.date_account_created.value_counts().plot(kind='line', linewidth=1.2, color='#FD5C64')
#unique_values4=df['data_account_created'].unique()
#plt.plot(counts4, unique_values4)
plt.savefig("Fig5")


    

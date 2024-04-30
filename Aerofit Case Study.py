#!/usr/bin/env python
# coding: utf-8

#  ## Importing Libraries 

# In[65]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")


# ## 1. Defining Problem Statement and Analysing basic metrics -
# 
# 
# 
# 
# 
# 
# 
# ### About Aerofit - 
# 
# 
# Aerofit is a leading brand in the field of fitness equipment. Aerofit provides a product range including machines such as treadmills, exercise bikes, gym equipment, and fitness accessories to cater to the needs of all categories of people.
# 
# 
# 
# ### Business Problem - 
# 
# 
# The market research team at Aerofit wants to identify the characteristics of the target audience for each type of treadmill offered by the company, to provide a better recommendation of the treadmills to the new customers. The team decides to investigate whether there are differences across the product with respect to customer characteristics.
# 
# 
# 
# ### Objective  - 
# 
# 
# 1.Perform descriptive analytics to create a customer profile for each Aerofit treadmill product by developing appropriate tables and charts.
# 
# 2.For each Aerofit treadmill product, construct two-way contingency tables and compute all conditional and marginal probabilities along with their insights/impact on the business.
# 

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# #### Basic Observations - 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[2]:


data = pd.read_csv("aerofit_treadmill.csv")
data


# In[3]:


data.info()


# 1. Product, Gender and Martial Status columns are object (string)
# 2. Age, Education, Usage, Fitness, Income and Miles are the column in int64(integer) form.

# In[4]:


data.shape


# Dataset contains 180 rows and 9 columns.

# In[5]:


data.describe()


# #### Descriptive Analysis - 
# 
# 1. Total count of all columns is 180.
# 2. Mean age of the customer is 28 years and 50% of customers mean age is 26.
# 3. Mean education is 15 with maximum is 21 and minimum is 12.
# 4. Mean usage per week is 3.3 with maximum is 7 and minimun is 2.
# 5. Fitness average rating is 3.3 on the scale of 1 to 5
# 6. Most customer earns around 58K annually, with maximum of 104K and minimum almost 30K (in $).
# 7. Average miles the customer walk is 103 with maximum is 360 and minimum is 21.
# 

# ### Conversion of categorical attributes to 'category' -

# In[6]:


# Converting Int data type of fintess rating to object data type - 

data_cat = data
data_cat["Fitness_category"] = data.Fitness
data_cat.head()


# In[7]:


data_cat["Fitness_category"].replace({ 1 : "Poor Shape",
                                       2 : "Bad Shape",
                                       3 : "Average Shape",
                                       4 : "Good Shape",
                                       5 : "Excellent Shape"}, inplace = True)

data_cat.head()


# #### Categorization of Fitness Rating - 
# 
# 
# 1 - Poor Shape
# 
# 2 - Bad Shape  
# 
# 3 - Average Shape 
# 
# 4 - Good Shape  
# 
# 5 - Excellent Shape
# 

# ### Statistical Summary - 

# In[8]:


# Percentage of unique products - 

prod = data["Product"].value_counts(normalize = True)
percent = prod.map(lambda calc : round(100*calc, 2))
percent 


# 1. 44.44% of customers purchased KP281 product.
# 2. 33.33% of customers purchased KP481 product.
# 3. 22.22% of customers purchased KP781 product.

# In[9]:


# Gender Statistics (%) - 

gender = data["Gender"].value_counts(normalize = True)
gender_per = gender.map(lambda calc : round(100 * calc, 2))
gender_per


# 1. Male customers - 57.78% 
# 2. Female customers - 42.22%
# 

# In[10]:


# Marital Status (%) -

marital = data["MaritalStatus"].value_counts(normalize = True)
marital_per = marital.map(lambda calc : round (100 * calc, 2))
marital_per 


# 1. Married/Partnered customers - 59.44%
# 2. Single customers - 40.56%
# 

# In[11]:


# Usage - Number of days per week (%) - 

usage = data["Usage"].value_counts(normalize = True)
usage_per = usage.map(lambda calc : round(100 * calc, 2)).reset_index()
usage_per.rename(columns = {"index" :"DaysPerWeek"}, inplace = True)
usage_per


# 1. Around 38% customers use 3 days per week.
# 2. Less than 2% customers use 7 days per week.
# 

# In[12]:


# Fitness rating (%) - 

rating = data["Fitness"].value_counts(normalize = True)
rating_per = rating.map(lambda calc : round( 100 * calc, 2)).reset_index()
rating_per.rename(columns = {"index" : "Rating"}, inplace = True)
rating_per


# 1. More than 53% customers rated as average in fitness.
# 2. 14% customers rated less than average fitness.
# 3. 17% customers rated excllent fintness rating.
# 

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ## 2. Non-Graphical Analysis: Value counts and unique attribute-

# In[13]:


# Number of unique product ids-

data["Product"].nunique()


# In[14]:


# List of unique products-

data["Product"].unique().tolist()


# In[15]:


# Total number of unique ages - 

unique_age = data["Age"].nunique()
unique_age 


# In[16]:


# List of unique ages - 

data["Age"].unique()


# In[17]:


# Gender counts - 

data["Gender"].value_counts()


# In[18]:


# Unique Educations - 

data["Education"].unique().tolist()


# In[19]:


# Count of customers on the rating scale 1 to 5 -

data["Fitness"].value_counts().sort_index()


# In[20]:


# Count of customers with 3 diff products - 

data["Product"].value_counts().sort_index()


# In[21]:


# Customer counts on usage - 

data["Usage"].value_counts().sort_index()


# In[22]:


# Count of single and partnered customers - 

data["MaritalStatus"].value_counts()


# #### Conclusion - 
# 
# 1. There are 3 different type of products are present - KP281, KP481, KP781.
# 2. Most purchased treadmill product is KP281.
# 3. In the dataset Male customers - 104 and Female customers - 76.
# 4. Highest rated Fitness rating is 3.
# 5. Most customers usage treadmill at least 3 days per week.
# 6. Majority of the customers who have purchased treadmill are Married/Partnered.
# 

# ## 3. Visual Analysis - Univariate & Bivariate - 

# ### Univariate Analysis -
# #### For continuous variable(s): Distplot, countplot, histogram -

# In[23]:


# Product Analysis - 

sns.countplot(data = data, x = "Product")
plt.title("Product Analysis")
plt.show()


# 1. KP281 is the most purchased product.
# 2. KP781 is the least purchased product.
# 

# In[24]:


# Marital Status Analysis - 

sns.countplot(data = data, x = "MaritalStatus")
plt.title("Martial Status Analysis")
plt.show()


# Most products purchased by Married/Partnered customers.

# In[25]:


# Gender Analysis - 

sns.countplot(data = data , x = "Gender")
plt.title("Gender Analysis")
plt.show()


# Product purchased by Males is maximum as compaire to Females.

# In[26]:


# Fitness Rating Analysis - 

sns.countplot(data = data, x = "Fitness")
plt.title("Fitness Rating")
plt.show()


# 1. Excellent shape is the second highest rating.
# 2. More than 90 customers rated as Average fitness rating.

# In[27]:


# Income Analysis - 

sns.distplot( data.Income, rug = True)
plt.xticks(rotation = 45)
plt.title("Income Analysis")
plt.show()


# Most of the customers who have purchased product have a average income between 40k to 60k.

# In[28]:


# Fintess Rating Analysis - 

sns.distplot(data.Fitness)
plt.title("Fitness Rating")
plt.show()


# In[29]:


# Education Analysis - 

sns.histplot( data = data , x = "Education")
plt.title("Education Analysis")
plt.show()


# 1. Highest education number of customers  is 16
# 2. 14 is the second highest education of the customers.
# 3. 20 is the least education of the customers.
# 

# In[30]:


# Usage Analysis - 

sns.histplot(data = data, x = "Usage")
plt.title("Usage Analysis")
plt.show()


# 1. 3 days per week is the most commom usage of the customers.
# 2. Very few customers use product 7 days per week.
# 

# #### For Categorical Variables : Boxplot  -

# In[31]:


# Usage Analysis - 

sns.boxplot( data = data, x = "Usage")
plt.title("Usage Analysis")
plt.show()



# 1. 3 to 4 days is the most preferred days.
# 2. 6 and 7 days per week is rare usage days for few customers (outliers).

# In[32]:


# Age Analysis - 

sns.boxplot( data = data, x = "Age")
plt.title("Age Analysis")
plt.show()


# 1. 23 to 34 is the most common customer age group that has purchased the product.
# 2. Above 45 years old customers are very rare.

# In[33]:


# Income Analysis - 

sns.boxplot( data = data, x = "Income")
plt.title("Income Analysis")
plt.show()


# #### For Correlation: Heatmaps, Pairplots - 

# In[34]:


# Correlation Heatmap - 

plt.figure(figsize =(10,5))
co = sns.heatmap(data.corr(), annot = True, fmt = ".4f", linewidth = .5)
plt.yticks (rotation = 0)
plt.show()



# 1. Correlation between Age and Miles is 0.03.
# 2. Correlation between Education and Income is 0.62.
# 3. Correlation between Usage and Fitness is 0.66.
# 4. Correlation between Income and Usage is 0.51.
# 

# In[35]:


# Product Analysis - Pair Plot - 

sns.pairplot(data, hue = "Product", kind = "reg")
plt.show()


# ### Bivariate Analysis -

# In[36]:


# Product Purchased among Married/Partnered and Single 

sns.countplot(data = data, x = "Product", hue = "MaritalStatus")
plt.show()


# 1. Between Singles and Partnered, Partnered customers are the major product purchasers.
# 2. KP281 is the most preferred product by customers.
# 

# In[37]:


# Product purchased among Male and Female - 

sns.countplot( data = data, x = "Product", hue = "Gender")
plt.show()


# 1. KP781 product is mostly preferred by Male customers.
# 2. KP281 product is equally preferred by both Male and Female customers.
# 3. Overall Male customers are the highest product purchasers.
# 

# In[38]:


# Product usage among Male and Female - 

sns.countplot(data = data, x = "Usage", hue = "Gender")
plt.show()


# 1. Male's usage is highest 4 days per week.
# 2. Female's usage mostly 3 days per week.
# 3. Only few Male customers use 7 days per week where as Female customers maximum usage is only 6 days per week.
# 

# In[39]:


# Fitness rating categorised by Gender -
 
sns.countplot( data = data, x = "Fitness", hue = "Gender")
plt.show()


# Both Male and Female mostly rated as Average. Significant number of Male customers are at Excellent shape.

# In[40]:


# Product purchased customers Income and their Gender - 

sns.kdeplot( data = data , x ="Income", hue = "Gender")
plt.show()


# 40k to 60k is the most common income of the customers.

# In[41]:


# Distance covered by Gender - 

sns.kdeplot( data = data, x = "Miles", hue = "Gender")
plt.show()


# Male are consistent distance coverage than Female customers. Female has covered max 300 miles distance.

# ## Scatterplot for Gender and Age who rated less than 2 in Fitness rating - 
# 
# sns.jointplot( x = "Age", y = "Gender", data= data[data.Fitness < 3])
# plt.show()
# 

# In[43]:


# Scatter Plot - 

plt.figure(figsize = (10,5))
sns.scatterplot(x = "Miles", y = "Income", data = data, hue = "Fitness", style = "Gender")
plt.show()


# Most of the customers fitness level is around 3 to 4.But there are very few customers who earn a lot and run more miles.

# In[44]:


plt.figure(figsize = (10,5))
sns.boxplot(x = "Age", y = "Product", data = data)
plt.show()


# 1. Most customers are comfortabel with KP281 product.
# 2. KP481 is the second highest product among younger side of the customer.
# 3. Roughly few customers with age above 40 use KP781.
# 

# In[45]:


# Product purchased according to Education - 

plt.figure(figsize = (10,5))
sns.boxplot( x = "Education", y = "Product", data = data)
plt.show()


# 1. KP781 product preferred by Higher education of 16 to 18. 
# 2. Customer having education between 14 to 16 perfer KP281 and KP481 equally.

# ## 4. Missing Value & Outlier Detection - 

# In[46]:


# Null value - 

data.isna().sum()


# There is no Null value in given data 

# In[47]:


# Duplicate values - 

data.duplicated().sum()


# No duplicate value obeserved in the given data.

# In[54]:


# Outlier calculation for Miles using Inter Quratile Range - 

q_75, q_25 = np.percentile(data["Miles"], [75, 25])
miles_qrt = q_75 - q_25
miles_qrt


# Inter Quartile Range for Miles is 48.75.

# ## 5. Business Insights based on Non-Graphical and Visual Analysis - 

# #### Probability for each product for the both genders - 

# In[61]:


def gender_probability(gender,data):
    print(f"Prob P(KP781) for {gender}: {round(data['KP781'][gender]/data.loc[gender].sum(),3)}")
    print(f"Prob P(KP481) for {gender}: {round(data['KP481'][gender]/data.loc[gender].sum(),3)}")
    print(f"Prob P(KP281) for {gender}: {round(data['KP281'][gender]/data.loc[gender].sum(),3)}")
    
data_temp = pd.crosstab(index=data['Gender'],columns=[data['Product']])
print("Prob of Male: ",round(data_temp.loc['Male'].sum()/len(data),3))
print("Prob of Female: ",round(data_temp.loc['Female'].sum()/len(data),3))
print()
gender_probability('Male',data_temp)
print()
gender_probability('Female',data_temp)


# #### Probability of each product for given Marital Status - 

# In[62]:


def MS_Probability(ms_status,data):
    print(f"Prob P(KP781) for {ms_status}: {round(data['KP781'][ms_status]/data.loc[ms_status].sum(),3)}")
    print(f"Prob P(KP481) for {ms_status}: {round(data['KP481'][ms_status]/data.loc[ms_status].sum(),3)}")
    print(f"Prob P(KP281) for {ms_status}: {round(data['KP281'][ms_status]/data.loc[ms_status].sum(),3)}")
    
df_temp = pd.crosstab(index=data['MaritalStatus'],columns=[data['Product']])
print("Prob of P(Single): ",round(df_temp.loc['Single'].sum()/len(data),3))
print("Prob of P(Married/Partnered): ",round(df_temp.loc['Partnered'].sum()/len(data),3))
print()
MS_Probability('Single',df_temp)
print()
MS_Probability('Partnered',df_temp)


# 1. Probability of Male customer of purchasing product is - 57.77%
# 2. Probability of Female customer of purchasing product is - 42.22%
# 
# 

# #### Conditional Probabilities - 

# In[63]:


np.round((pd.crosstab([data.Product], data.Gender, margins = True, normalize = "columns")) * 100, 2)


# #### Probability of selling - 
# 
# 1. KP281 for Female customer - 52%  and for Male customer - 38%
# 2. KP481 for Female customer - 38%  and for Male customer - 30%
# 3. KP781 for Female customer - 9%   and for Male customer - 32% 
# 
# KP281 is more recommended for Female customers and for KP781 is more recommended for Male customers.
# 

# ## 6. Recommendations - 

# 1. KP781 provides more features and functionalities that's why it should be marketed for professionals and atheletes.
# 2. KP781 product should be promoted using influencers and other international athelets.
# 3. Female who prefer fitness product are very low , hence we should run a marketing campaign to encourage women to more heatly and fitenss.
# 4. Provide customer support and recommendation to users to upgrade the product for next level versions.
# 5. KP781 can be recommended for Female customers who excercises extensively along with easy usage guidance since this type is adavanced.
# 6. Target the age group above 40 years to recomend product KP781.
# 7. KP281 is easily affordable entry level product, and it is maximum selling product.
# 8. KP481 is and Intermediate level product, and it is second most popular product.
# 9. KP781 is high price & the advanced type due to this customer prefer it less. Customers use this product for covering more distance.
# 10. KP281 & KP481 products are preferred by customers whose annul income lies between the range 39k - 53k dollars. That's why these models should promoted as budget treadmill. 

# In[ ]:





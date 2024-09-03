#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("C:\\Users\\Administrator\\Downloads\\Test Keywords for Remote Bingo - Keyword Stats 2024-07-13 at 00_51_25.csv")


# In[3]:


data.sample(5)


# In[4]:


data.info()


# In[5]:


data.columns


# In[6]:


# Convert YoY change column to numeric types, handling errors
data['YoY change'] = pd.to_numeric(data['YoY change'].str.rstrip('%'), errors='coerce')


# In[7]:


data.info()


# In[9]:


data['Competition'].unique()


# In[8]:


data['YoY change'].unique()


# In[10]:


# Define conditions
condition1 = data['Avg. monthly searches'] >= 500
condition2 = data['Competition'].isin(['low', 'medium'])
condition3 = data['YoY change'] >= 100

# Apply conditions to filter data
filtered_data = data[condition1 & condition2 & condition3]

# Select desired columns
filtered_data = filtered_data[['Keyword', 'Avg. monthly searches', 'YoY change', 'Competition']]

# Display or use filtered_data as needed
print(filtered_data.head())  # Display the first few rows to verify


# In[11]:


data.head(3)


# In[12]:


# Print the shape of the original dataframe
print("Shape of original dataframe:", data.shape)


# In[18]:


# Define conditions
condition1 = data['Avg. monthly searches'] >= 500
#condition2 = data['Competition'].str.lower().isin(['low', 'medium', 'high', 'unknown'])  # Convert to lowercase for case insensitivity
condition3 = data['YoY change'] >= 100

# Check how many rows meet each condition separately
print("Rows meeting condition 1:", condition1_count)
#print("Rows meeting condition 2:", condition2_count)
print("Rows meeting condition 3:", condition3_count)


# In[23]:


# Apply conditions to filter data
filtered_data = data[(data['Avg. monthly searches'] >= 500) &  
                     (data['YoY change'] >= 100)]
# Select desired columns
filtered_data = filtered_data[['Keyword', 'Avg. monthly searches', 'YoY change', 'Competition']]
# Print the shape and a few rows of filtered dataframe
print("Shape of filtered dataframe:", filtered_data.shape)
print(filtered_data.sample(25))


# In[24]:


filtered_data.shape


# In[25]:


filtered_data


# In[26]:


strings_to_exclude = ['club 3000 bingo play online', 'monopoly bingo online', 'red bus bingo']

# Boolean mask to filter out rows containing strings to exclude
mask = ~filtered_data['Keyword'].str.contains('|'.join(strings_to_exclude), case=False)


# In[27]:


mask


# In[29]:


# Apply the mask to filter out rows
filtered_data = filtered_data[mask]

# Display filtered_data
print(filtered_data)


# In[30]:


filtered_data


# In[31]:


filtered_data.shape


# In[35]:


# Sort filtered_data by 'Avg. monthly searches' in descending order
filtered_data_sorted = filtered_data.sort_values(by='Avg. monthly searches', ascending=False)

# Resetting the index
filtered_data_sorted = filtered_data_sorted.reset_index(drop=True)


# In[36]:


filtered_data_sorted


# In[37]:


cut_off_index = 21

# Slice the dataframe to exclude rows from index 21 onwards
filtered_data_trimmed = filtered_data_sorted.iloc[:cut_off_index]

# Display the trimmed dataframe
filtered_data_trimmed


# In[38]:


# Rename columns in filtered_data_trimmed
filtered_data_trimmed = filtered_data_trimmed.rename(columns={
    'Avg. monthly searches': 'Traffic',
    'YoY change': 'Growth YoY%'
})

# Display the dataframe to verify the column names
filtered_data_trimmed


# In[39]:


filtered_data_trimmed['Keyword']


# In[41]:


# Define mapping for keyword groups
keyword_groups = {
    'Online Bingo Games': ['online bingo games', 'bingo online free', 'free bingo games online',
                           'free online bingo games for free', 'online games free bingo', 'live bingo online',
                           'bingo rooms online'],
    'Free Bingo Offers': ['free internet bingo', 'free internet bingo games', 'free bingo website',
                          'free bingo sites', 'bingo websites free bonus'],
    'Bingo Bonuses': ['bingo signup bonus', 'no deposit free bingo win real cash', 'bingo sites with free bingo',
                      'bingo sites with bonus', 'online bingo welcome bonus'],
    'Best Bingo Sites': ['good online bingo sites', 'best online bingo sites']
}

# Function to assign group based on keyword
def assign_keyword_group(keyword):
    for group, keywords in keyword_groups.items():
        if keyword in keywords:
            return group
    return 'Other'  # Default group for keywords not matched

# Apply function to create 'Keyword Group' column
filtered_data_trimmed['Keyword Group'] = filtered_data_trimmed['Keyword'].apply(assign_keyword_group)

# Reorder columns with 'Keyword Group' before 'Keyword'
filtered_data_trimmed = filtered_data_trimmed[['Keyword Group', 'Keyword', 'Traffic', 'Growth YoY%', 'Competition']]

# Display the modified dataframe
filtered_data_trimmed


# In[42]:


# Define mapping for keyword groups
keyword_groups = {
    'Online Bingo Games': ['online bingo games', 'bingo online free', 'free bingo games online',
                           'free online bingo games for free', 'online games free bingo', 'live bingo online',
                           'bingo rooms online'],
    'Free Bingo Offers': ['free internet bingo', 'free internet bingo games', 'free bingo website',
                          'free bingo sites', 'bingo websites free bonus'],
    'Bingo Bonuses': ['bingo signup bonus', 'no deposit free bingo win real cash', 'bingo sites with free bingo',
                      'bingo sites with bonus', 'online bingo welcome bonus'],
    'Best Bingo Sites': ['good online bingo sites', 'best online bingo sites']
}

# Function to assign group based on keyword
def assign_keyword_group(keyword):
    for group, keywords in keyword_groups.items():
        if keyword in keywords:
            return group
    return 'Other'  # Default group for keywords not matched

# Apply function to create 'Keyword Group' column
filtered_data_trimmed['Keyword Group'] = filtered_data_trimmed['Keyword'].apply(assign_keyword_group)

# Reorder columns with 'Keyword Group' before 'Keyword'
filtered_data_trimmed = filtered_data_trimmed[['Keyword Group', 'Keyword', 'Traffic', 'Growth YoY%', 'Competition']]

# Sort dataframe by 'Keyword Group'
filtered_data_trimmed.sort_values(by='Keyword Group', inplace=True)

# Reset index after sorting
filtered_data_trimmed.reset_index(drop=True, inplace=True)

# Display the modified dataframe
filtered_data_trimmed


# In[43]:


# Save the dataframe to CSV
filtered_data_trimmed.to_csv('filtered_data_trimmed.csv', index=False)

print("Data saved successfully.")


# In[ ]:





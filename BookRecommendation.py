#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


books=pd.read_csv('Books.csv' ,  dtype=object)


# In[3]:


books.head()


# In[4]:


books.columns


# In[5]:


books=books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]


# In[6]:


books.rename(columns={'Book-Title': 'title','Book-Author':'author','Year-Of-Publication':'year','Publisher':'publisher'},inplace=True)


# In[7]:


books.head(2)


# In[8]:


users=pd.read_csv('Users.csv')


# In[9]:


users.rename(columns={'User-ID':'user_id'}, inplace=True)
users.head(2)


# In[10]:


ratings=pd.read_csv('Ratings.csv')


# In[11]:


ratings.rename(columns={'User-ID':'user_id','Book-Rating':'rating'},inplace=True)
ratings.head(2)


# In[12]:


books.shape


# In[13]:


users.shape


# In[14]:


ratings.shape


# In[15]:


# number of ratings done by particular user
ratings['user_id'].value_counts()


# In[16]:


x=ratings['user_id'].value_counts()>200
x[x]


# In[17]:


y=x[x].index
y


# In[18]:


ratings=ratings[ratings['user_id'].isin(y)]


# In[19]:


ratings.shape


# In[20]:


#combining ratings with books dataset
ratings_with_books=ratings.merge(books, on='ISBN')
ratings_with_books.shape


# In[21]:


ratings_with_books.head(2)


# In[22]:


#grouping on the basis of title and count the no. of ratings done for that book
number_rating=ratings_with_books.groupby('title')['rating'].count().reset_index()
number_rating.rename(columns={'rating':'number of ratings'},inplace=True)
number_rating.head(2)


# In[23]:


final_rating=ratings_with_books.merge(number_rating, on='title')
final_rating


# In[24]:


z=final_rating['number of ratings']>=50
final_rating=final_rating[z]


# In[25]:


final_rating.shape


# In[26]:


final_rating.drop_duplicates(['user_id','title'],inplace=True)


# In[27]:


final_rating.shape


# In[28]:


book_pivot=final_rating.pivot_table(columns='user_id', index='title',values='rating')
book_pivot.fillna(0, inplace=True)
book_pivot


# In[29]:


from scipy.sparse import csr_matrix
book_sparse=csr_matrix(book_pivot)


# In[30]:


type(book_sparse)


# In[31]:


from sklearn.neighbors import NearestNeighbors
model=NearestNeighbors(algorithm='brute', metric = 'cosine')


# In[32]:


model.fit(book_sparse)


# In[33]:


#calculating the distance from a given data and its closest 5 data points are result
distances,suggestions=model.kneighbors(book_pivot.iloc[237,:].values.reshape(1,-1), n_neighbors=6)


# In[34]:


suggestions


# In[35]:


#to print all recommended books title
for i in range(len(suggestions)):
    print(book_pivot.index[suggestions[i]])


# In[36]:


#to make the book's title as input rather than index 
np.where(book_pivot.index=='Harry Potter and the Chamber of Secrets (Book 2)')[0][0]


# In[37]:


def recommend_book(book_name):
    book_id=np.where(book_pivot.index==book_name)[0][0]
    distances,suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    for i in range(len(suggestion)):
        print(book_pivot.index[suggestion[i]]) 


# In[38]:


recommend_book('Harry Potter and the Chamber of Secrets (Book 2)')


# In[ ]:





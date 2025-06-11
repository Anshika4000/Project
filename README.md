# Project
Dataset ->   'https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset'
The Book-Crossing dataset comprises 3 files.  1)users  2)ratings  3)books
Recommendation systems help users discover books tailored to their tastes.  Collaborative filtering is a common method of personalized recommender system which filters information such as interactions data from other similar users. Since it works by predicting user ratings, it is considered as performing regression task. There are two general types of collaborative filtering:
          1). User to user
          2). Item to item
User to user collaborative filtering basically operates under the assumption that users who gave similar ratings to a certain item are likely to have the same preference for other items as well. Therefore, this method mainly relies on finding similarity between users. However, in some cases, user preference might be to abstract to be broken down. This is where item to item collaborative filtering comes in handy. Here, similarity between items is used instead of similarity between users
The solution will consist of the following components :
  Data Collection:
	   Gather data sets on user details, book details and rating of books.
  Data Preprocessing:
	   Clean and preprocess the collected data to handle missing values, outliers, and inconsistencies.
	   Feature selection to extract data of ratings of books from relevant users to avoid overfitting.
	   Feature aggregation to analyse the number of ratings done for a particular book.
  Machine Learning Algorithm
	   Implement K-NearestNeighbour algorithm to  find the closest neighbours (books) based on a matrix of title as index and user-id as column. 
  Result:
	   The recommendations are then made based on the preferences of these neighbours. 
    
Algorithm & Deployment
  Algorithm selection:
    KNN is a simple, non-parametric, and instance-based learning algorithm that can be used for classification and regression tasks. In the context of recommender      systems, KNN is used to find the closest neighbours ( books) based on a similarity metric. The recommendations are then made based on the preferences of these      neighbours.
  Data Processing:
    We collect data on user interactions with book, such as ratings or purchases. Preprocess the data to handle missing values and transform the data into a user-      book matrix.
    We combine the rating data with the total rating count data . This gives us exactly what we need to find out which books are popular and filter out lesser-         known books.
    This matrix represents the ratings given by users to items, where rows represent users and columns represent books. A value of 0 indicates that the user has        not rated the book.
    We then transform the values(ratings) of the matrix dataframe into a scipy sparse matrix for more efficient calculations.
 Training process:
    The algorithm we use to compute the nearest neighbors is “brute”, and we specify “metric=cosine” so that the algorithm will calculate the cosine similarity         between rating vectors. Finally, we fit the model.
    For each book , K-nearest neighbors based on the computed similarity scores is find. This involves sorting the similarity scores and selecting the top K            neighbors.
Prediction process:
    Now , we are randomly selecting any one index of the books and based on that our model is giving recommendation of 5 books (excluding the input book) on that.





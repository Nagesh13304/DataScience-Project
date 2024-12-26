import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk

# Load the datasets
books = pd.read_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\books.csv")
transactions = pd.read_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\transactions.csv")
users = pd.read_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\users.csv")

# Data cleaning
books.dropna(inplace=True)
transactions.dropna(inplace=True)
users.dropna(inplace=True)

# Convert dates to datetime format
transactions['borrow_date'] = pd.to_datetime(transactions['borrow_date'])
transactions['return_date'] = pd.to_datetime(transactions['return_date'])

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10, 6))
sns.countplot(y='genre', data=books, order=books['genre'].value_counts().index)
plt.title('Distribution of Book Genres')
plt.show()

borrowed_books = transactions[transactions['type'] == 'borrow']
borrowed_books['month'] = borrowed_books['borrow_date'].dt.month
plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=borrowed_books)
plt.title('Monthly Borrowing Trends')
plt.show()

# Feature engineering for demand prediction
borrowed_books['year'] = borrowed_books['borrow_date'].dt.year
features = borrowed_books[['book_id', 'month', 'year']]
borrowed_books['count'] = 1  # Assuming each row represents one borrowed book
target = borrowed_books.groupby(['book_id', 'month', 'year'])['count'].sum().reset_index(drop=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Combine book titles and genres for a content-based recommendation system
books['title_genre'] = books['title'] + ' ' + books['genre']

# Vectorize the text
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['title_genre'])

# Calculate cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = books[books['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    book_indices = [i[0] for i in sim_scores]
    return books['title'].iloc[book_indices]

# Example usage
recommendations = get_recommendations('The Great Gatsby')
print(recommendations)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

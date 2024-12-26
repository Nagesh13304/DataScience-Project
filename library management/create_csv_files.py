import pandas as pd
from datetime import datetime, timedelta

# Sample data for books
books_data = {
    'book_id': [1, 2, 3, 4, 5],
    'title': ['The Great Gatsby', '1984', 'To Kill a Mockingbird', 'Pride and Prejudice', 'Moby Dick'],
    'author': ['F. Scott Fitzgerald', 'George Orwell', 'Harper Lee', 'Jane Austen', 'Herman Melville'],
    'genre': ['Classic', 'Dystopian', 'Classic', 'Romance', 'Adventure'],
    'publication_year': [1925, 1949, 1960, 1813, 1851]
}
books = pd.DataFrame(books_data)
books.to_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\books.csv", index=False)

# Sample data for transactions
transactions_data = {
    'transaction_id': [1, 2, 3, 4, 5],
    'user_id': [1, 2, 1, 3, 4],
    'book_id': [1, 2, 3, 4, 5],
    'borrow_date': [(datetime.now() - timedelta(days=i*5)).strftime('%Y-%m-%d') for i in range(5)],
    'return_date': [(datetime.now() - timedelta(days=i*3)).strftime('%Y-%m-%d') for i in range(5)],
    'type': ['borrow', 'borrow', 'borrow', 'borrow', 'borrow']
}
transactions = pd.DataFrame(transactions_data)
transactions.to_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\transactions.csv", index=False)

# Sample data for users
users_data = {
    'user_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 22, 35, 28],
    'membership_date': ['2021-01-15', '2020-05-22', '2019-09-10', '2018-03-14', '2022-07-19']
}
users = pd.DataFrame(users_data)
users.to_csv(r"C:\Users\Nagesh\OneDrive\Desktop\datascience project\library management\users.csv", index=False)

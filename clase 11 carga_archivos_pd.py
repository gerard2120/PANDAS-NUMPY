import pandas as pd

df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
# se especifica la delimitacion, sep, tambien se puede agregar el header
# se puede agregar los nombres tambien a las columnas
# df_books = pd.read_csv('./files/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep='|', header=None, names=['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
print(df_books.columns)


df_books_json = pd.read_json('./files/example_json.json')
df_books
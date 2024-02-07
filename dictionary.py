# create a dictionary to represent a library catalog
library_catalog = {}

# Insert books in the catalog
library_catalog['Tripwire'] = 'Fiction'
library_catalog['1984'] = 'Dystopian'
library_catalog['Python Crash Course'] = 'Programming'

#Retreive the genre of a specific book 
genre = library_catalog.get('1984', 'Not Found')

# Delete a book from the catalog
del library_catalog['Tripwire']


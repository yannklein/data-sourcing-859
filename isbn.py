import requests

isbns = ['0-7475-3269-9', '0385472579']
for isbn in isbns:
    formatted_isbn = f'ISBN:{isbn}'
    # https://openlibrary.org/api/books?bibkeys=ISBN:0-7475-3269-9&format=json&jscmd=data
    base_url = "https://openlibrary.org/api/books"

    response = requests.get(
        base_url, 
        params={'bibkeys': formatted_isbn, 'format': 'json', 'jscmd': 'data'}
        ).json()

    print(response[formatted_isbn]["title"])


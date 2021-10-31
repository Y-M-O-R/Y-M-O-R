import requests
response = requests.get('http://books.toscrape.com/')
if response:
    print(f'Connection={response.status_code}')
    response_text = response.text
    history = response.history
    print(response_text)

else:
    print('No Connection')




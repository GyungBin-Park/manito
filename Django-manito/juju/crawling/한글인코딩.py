from urllib.parse import urlsplit, quote


url = '삼성전자'
encoded_url = quote(url)
print(encoded_url)
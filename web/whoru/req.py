import requests

url = 'http://mercury.picoctf.net:46199'
params = {'User-Agent' : 'PicoBrowser'}
print(requests.get(url, params=params).text)

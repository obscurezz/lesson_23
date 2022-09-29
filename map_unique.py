import requests

url = "http://127.0.0.1:5000/perform_query"

payload={
  'file_name': 'apache_logs.txt',
  'cmd1': 'map',
  'value1': '0',
  'cmd2': 'unique',
  'value2': ''
}

response = requests.post(url, params=payload)
print(response.text)
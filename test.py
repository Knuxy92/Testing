import os
try: 
  import requests
  from print_color import print
except:
  os.system('pip install requests')
  os.system('pip install print-color')



url = "your_target_url_here"
user_agent = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36'
referer = 'https://linkvertise.com'
headers = {'Referer': referer, 'User-Agent': user_agent}
print("Made By Knuxy92")
print('Enter Link Here > ', end='', tag='INPUT', tag_color='purple', color='white')
link = input('')

response = requests.get(url, headers=headers)

print(response.text)
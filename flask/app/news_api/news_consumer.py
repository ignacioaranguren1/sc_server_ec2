from api_client import NewsApiClient

# Init
newsapi = NewsApiClient(url="https://api.goperigon.com/v1/all", token="089af873-e459-4dc3-a38c-7a2d027bc362")
response = newsapi.get_everything()['articles']
counter = 0
for news in response:
    print(news['content'] + "*****************")
    counter = counter + 1
print(counter)




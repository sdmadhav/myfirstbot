import requests

#reference url :https://core.telegram.org/bots/api#sendmessage
base_url="https://api.telegram.org/bot1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s/getupdates"
parameters={
    "offset":"425025108",
    "limit":"1"
    }
r=requests.get(base_url,data=parameters)
print(r.text)



import requests

#reference url :https://core.telegram.org/bots/api#sendmessage
base_url="https://api.telegram.org/bot1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s/sendMessage"
parameters={
    "chat_id":"-1001577823032",
    "text":"Hi this is from your bot."
    }
r=requests.get(base_url,data=parameters)
print(r.text)



Token="1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s"
import requests
import pandas as pd

url = 'https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv'

df = pd.read_csv(url, sep="\t")


base_url = "https://api.telegram.org/bot1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s"



def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  print(data)

  for result in data["result"]:
    send_msg(result)
  
  if data["result"]:
    return data["result"][-1]["update_id"] + 1



def auto_answer(message):
  answer = df.loc[df['Question'].str.lower() == message.lower()]  

  if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer
  else:
      return "Sorry, I could not understand you !!! I am still learning and try to get better in answering."



def send_msg(message):
  text = message["message"]["text"]
  r=requests.get("https://www.omdbapi.com/?t="+text+"&apikey=7da1c707")
  message_id = message["message"]["message_id"]
  answer = r.json()
  print(answer)
  if(answer["Response"]=="True"):
    photo=answer["Poster"]
    title=answer["Title"]
    year=answer["Year"]
    dur=answer["Runtime"]
    genre=answer["Genre"]
    msg='\n🎞️ Title  : '+title
    msg+='\n🎬 Genre  : #'+str(genre).replace(", "," #")
    msg+='\n⭐️ Rating : '+answer["imdbRating"]+" Based on "+answer["imdbVotes"]+" votes"
    msg+='\n🎭 Year : '+str(year)
    msg+='\n🎬 Duration  : '+str(dur)

    parameters = {
        "chat_id" : message["message"]["from"]["id"],
        "caption" : msg,
        "photo":photo,
        "reply_to_message_id" : message_id
    }

    resp = requests.get(base_url + "/sendPhoto", data = parameters)
  else:
    parameters = {
        "chat_id" : message["message"]["from"]["id"],
        "text" : "Movie not found! try another name.",
        "reply_to_message_id" : message_id
    }
    resp=requests.get(base_url + "/sendMessage", data = parameters)
  print(resp.text)

offset = 0

while True:  
  offset = read_msg(offset)

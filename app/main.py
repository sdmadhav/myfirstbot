from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

token = '1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s'

def welcome_msg(message):
    base_url = "https://api.telegram.org/bot1431989781:AAGo5JKThqlQV7Lm1QJfboDB_eJdKFcMa6s"
    global token
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


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return { 'statusCode' : 200, 'body' : 'Success' , 'data' : data }
    else:
        return { 'statusCode' : 200, 'body' : 'Success'}
if __name__ == '__main__':
   
    app.run(debug=True)
    
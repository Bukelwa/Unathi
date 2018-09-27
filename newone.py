from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #train the chatbot
import os

app = Flask(__name__)

english_bot = ChatBot('Test')
english_bot.set_trainer(ListTrainer) 

for _file in os.listdir('chats'):
	chats = open('chats/' + _file, 'r').readlines()
	english_bot.train(chats)




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/finddoc/")
def finddoc():
    return render_template("finddoc.html")

@app.route("/map/")
def map():
    return render_template("map.html")

@app.route("/collection/")
def collection():
    return render_template("collection.html") 


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()

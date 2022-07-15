from flask import Flask
from threading import Thread

# our server is going to run on a seperate thread from our bot, at the same time
app = Flask('')

@app.route('/')
def home():
  return "Hello. I'm alive!" # it messages everyone who visits the server

def run():
  app.run(host='0.0.0.0', port=8080)

#it runs our web server
def keep_alive():
  t = Thread(target=run)
  t.start()
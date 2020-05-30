from flask import Flask,request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

from utils import fetch_reply
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"


@app.route("/appt", methods=['POST'])
def whatsapp_reply():
      #Fetch the message
  msg = request.form.get('Body')
  tel_no = request.form.get('From')
  reply = fetch_reply(msg,tel_no)

  #create reply
  resp = MessagingResponse()
  resp.message(reply)
  #resp.message("Did you say that you are {}?".format(msg))

  return str(resp)



if __name__ == "__main__":
  app.run()

  
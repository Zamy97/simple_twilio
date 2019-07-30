from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import wikipedia
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @app.route('/', methods=['GET'])

# def make_api_call():
#     URL = "https://dog.ceo/api/breeds/image/random"
#     request_pic = requests.get(url = URL)
#     data = request_pic.json()
#     return data
def sms():
    # Get the text in the message sent
    message_body = request.form['Body']

    # Create A Twilio response object to be able to send a reply back (as per  #Twilio docs)
    twilio_response = MessagingResponse()

    # Send the message body to the getReply message, where we will query the string and formulate a response
    reply_text = getReply(message_body)

    # Text back our response
    twilio_response.message('Hello There\n\n' + reply_text)
    return str(twilio_response)

def remove_head(from_this, remove_this):
    if from_this.endswith(remove_this):
        from_this = from_this[:-len(remove_this)].strip()
    elif from_this.startswith(remove_this):
        from_this = from_this[len(remove_this):].strip()

    return from_this


def getReply(message):
    # Make the message lower case and without spaces on the end for esdier handling
    message = message.lower().strip()

    #Place to where we will store our response
    answer = ""

    if "weather" in message:
        answer = "Get the weather using a weather API"

    # elif "dog" in message:
    #     message =wersw

    elif "wolfram" in message:
        answer = "Get a response from the Wolfram Alpha API"

    elif "wiki" in message:
        message = remove_head(message, "wiki")
        answer = "Get a response from wikipedia API"

        #Get the wikipedia summary for the request
        try:
            answer = wikipedia.summary(message)
        except:
            answer = "Request was not found using wiki. Be specific?"

    elif "some_keyword" in message:
        answer = "some response"

    else:
        answer = "\n Welcome! These are the commands you may use: \nWOLFRAM \"wolframalpha request\" \nWIKI \"wikipedia request\"\nWEATHER \"place\"\nSOME_KEYWORD \"some custom request\"\n"

    if len(answer) > 1500:
        answer = answer[0:1500] + "..."

    return answer

# This will allow Flask to work

if __name__ == '__main__':
    app.run()

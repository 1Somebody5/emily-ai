from flask import Flask
from flask import request
from chatterbot import ChatBot

app = Flask(__name__)

emily = ChatBot("Emily", storage_adapter = "chatterbot.storage.SQLStorageAdapter", logic_adapters = ["chatterbot.logic.BestMatch"], database_uri = "sqlite:///memory.db")

@app.route('/send')
def send():
    usrinput = request.args.get("input", default = "[0x0]", type = str)
    botoutput = "Error code 0x0"
    if usrinput != "[0x0]":
        usrinput = usrinput.replace("emily", "[0x1]") #name
        usrinput = usrinput.replace("[usr]", "[0x2]") #myname
        botoutput = emily.get_response(usrinput)
        botoutput = str(botoutput).replace("[0x2]", "emily")
        botoutput = botoutput.replace("[0x1]", "[usr]")
        print("Responding...")
        print(botoutput)
        print("Done!")
    return "<p>yuh</p> <b>" + botoutput + "</b>"
print("Yo what's up gamers")

from flask import Flask, jsonify, json
from flask import request
from flask import make_response
from flask_cors import CORS
from myfunction import getTotalMarks
from collections import OrderedDict


app = Flask(__name__)
CORS(app)

@app.route('/', strict_slashes = False)
def handleHttp():
    if 'input_text' in request.args:
        output = OrderedDict([("error",False),("string",""),("answer",0)])
        input_text = request.args.get('input_text')
        answer = getTotalMarks(input_text)
        output['answer'] = answer
        return output
    else:
        return 'Theres been a problem, press clear and try again'
    
if __name__ == "__main__":
    app.run()
    
from flask import Flask, request, Response

app= Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response= """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Hello this is a testing call.</Say>
        <Gather action="/process" method="POST" numDigits="1">
            <Say>Press 1 if you hear this message, otherwise hang up.</Say>
        </Gather>
        <Say>No input received. Goodbye!</Say>
    </Response>"""

    return Response(response, mimetype='text/xml')

@app.route("/process", methods=['GET', 'POST'])
def process():
    digit= request.values.get('Digits', '')
    if digit == '1':
        response= """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>You pressed 1. Bye bye.</Say>
    </Response>"""
        
    else:
        response= """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say>Invalid input or no input. Goodbye!</Say>
    </Response>"""
        
    return Response(response, mimetype='text/xml')

if __name__ == "__main__":
    app.run(port=5000)
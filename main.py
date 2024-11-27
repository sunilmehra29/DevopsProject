from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello ji ki haal chaal'

@app.route('/square/<int:number>', methods=['GET'])
def square(number):
    result = number * number
    return jsonify({"number": number, "square": result})

@app.route('/cube/<int:number>', methods=['GET'])
def cube(number):
    result = number * number * number
    return jsonify({"number": number, "cube": result})

app.run(debug=True)

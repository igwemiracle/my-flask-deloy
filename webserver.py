from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/", methods=['GET'])
def ReturnJson():
    if request.method == "GET":
        data = {
            "slackUsername": "Miracle Igwe",
            "backend": True,
            "age": 19,
            "bio": "I am an undergraudate and i love to write code"
        }

    
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
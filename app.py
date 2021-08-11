from flask import Flask, jsonify, request
import time, os


app = Flask(__name__)


@app.route("/bot", methods=["POST"])  # response
def response():
    query = dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({"response": result})


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, Flask World!</p>"

@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    print('Hsjshsh')
    if request.method == 'POST':
        return jsonify(
            username="hello",
            email="loi@gmail.ccom",
            id=1
        )



if __name__ == "__main__":
    app.run(debug=True)

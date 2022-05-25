import jwt
from flask import Flask, jsonify, request
from datetime import timedelta, datetime
from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRETKEY'
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/loginjwt', methods=['POST'])
def loginJwt():
    content = request.json
    if(content["username"] == "testuser" and content["password"] == "123456"):
        token = jwt.encode({
                'user': content["username"],
                'expiration': str(datetime.utcnow() + timedelta(seconds=600))
            }, app.config['SECRET_KEY'])
        return jsonify({"token": token.encode().decode("UTF-8")})

    return jsonify({"message" : "invalid login credentials"})


if __name__ == '__main__':
    app.run()

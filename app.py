from flask import Flask

app = Flask(__name__)

@app.route('/auth')
def auth_handler():
    return 'Authentication Successful'

if __name__ == '__main__':
    app.run()

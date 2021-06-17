from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet!"

@app.route('/home/<word>')
def home(word):
    return word

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'message': 'Hello, World!'}

@app.route('/api/hello')
def api_hello():
    return {'message': 'Hello from API'}

if __name__ == '__main__':
    app.run(debug=True)

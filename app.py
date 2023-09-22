from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    name = request.args.get("name", default='НЕ УКАЗАНО', type=str)
    message = request.args.get("message", default='НЕ УКАЗАНО', type=str)
    return f'''<h1> Hello {name}! <h1> 
                <h1>{message} <h1>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80)
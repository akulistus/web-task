from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    message = request.args.get("message")
    return f'''<p> Hello {name}! <p> 
                <p>{message} <p>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80)
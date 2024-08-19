from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr
    return f'<h1>Welcome to the Flask App</h1><p>Your IP address is: {ip_address}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

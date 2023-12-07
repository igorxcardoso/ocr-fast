import socket
from app import api
from app.routes import extract

if __name__ == '__main__':
    socket.setdefaulttimeout(999999999)
    api.run(debug=True, host="0.0.0.0")
from app import create_app

app = create_app()
from app.routes import *
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

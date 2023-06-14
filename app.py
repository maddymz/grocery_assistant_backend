from flask import Flask
from flask_cors import CORS
import os
from src.controllers.itemController import item_routes
from src.controllers.orderController import order_routes
from src.controllers.userController import user_routes
from src.controllers.chatController import gpt_routes
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)
app.register_blueprint(item_routes)
app.register_blueprint(order_routes)
app.register_blueprint(user_routes)
app.register_blueprint(gpt_routes)

CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!, gpt backend app welcome'


port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port,debug=True)
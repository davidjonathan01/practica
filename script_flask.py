from flask_script import Manager
from flask import redirect
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
 return redirect('http://www.example.com')

manager = Manager(app)
if __name__ == '__main__':
 manager.run()
from flask import flask
app = Flask(_name_)
@app.route('/')
def hello():
    return 'Hi!'
@app.route('/health')
def health:
    return 'ok',200
if _name_ == '_main_':
    app.run(host='0.0.0.0',port = 5000)
     
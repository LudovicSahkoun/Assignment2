from flask import Flask,Response,request
from myapp import *
app = Flask(__name__)



@app.route('/home/<lower>/<upper>')
def create(lower,upper):
    result=numerical_integration(float(lower),float(upper))
    return "<h1>%s</h1>" % str(result)
    
if __name__ == '__main__':
    app.run(debug=True)


# Ian Henisa
# 11/09/18
# Python Web Site File


from flask import Flask app=Flask(__name__)@app.route('/')

def home():
    return "Website content goes here."

if __name__=='__main__':
    app.run(debug=True)
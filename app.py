from flask import Flask
from housing.logger import logging

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("Testing logging")
    return("CI CD established")

if __name__=="__main__":
    app.run(debug=True)

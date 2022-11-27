from flask import Flask
import sys

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("Manually invoked an exception")
    except Exception as e:
        fifa = FifaException(e,sys)
        logging.info(fifa.error_message)
        logging.info("Successfully tested logger")
    return "Logging and Exception done"

if __name__=="__main__":
    app.run(debug=True)

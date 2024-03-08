from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
        return(render_template("index.html"))
    
if __name__ == "__main__":
    app.run(port = 1234) # i need this port number because 5000 is being used alr

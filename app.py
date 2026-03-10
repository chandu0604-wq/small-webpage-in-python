from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Zero Page</title>
        <style>
            body{
                background:black;
                color:white;
                text-align:center;
                font-family:Arial;
            }
            h1{
                color:cyan;
            }
            button{
                padding:10px 20px;
                background:cyan;
                border:none;
                font-size:16px;
            }
        </style>
    </head>

    <body>
        <h1>Hello Chandu 🚀</h1>
        <p>This webpage is built using Python</p>
        <button>Run Command</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
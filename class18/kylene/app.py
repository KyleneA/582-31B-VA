from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f"""
        <h1>Hellooo, Flask!</h1> 
        <a type='button' href='/test'> test </a>
        """

@app.route("/test")
def test():
    return f"""
        <h1>TEEEEEST</h1> 
        <a type='button' href='/'> home </a>
    """
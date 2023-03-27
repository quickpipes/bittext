from dotenv import load_dotenv
from flask import Flask, request, render_template, url_for, redirect
from services.bittext_service import BittextService

app = Flask(__name__)

load_dotenv()


@app.route("/", methods=['GET'])
def hello():
    return render_template('hello.html')


@app.route("/up")
def up():
    return "up."


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        bittext_service = BittextService()
        content = request.form['content']
        bittext = bittext_service.create_bittext(content)
        return redirect(url_for('show', hash=bittext.hash), code=200)

    return render_template('create.html')


@app.route("/show/<hash>", methods=['GET'])
def show(hash: str):
    bittext_service = BittextService()
    bittext = bittext_service.get_bittext(hash)
    return render_template('show.html', content=bittext.content)

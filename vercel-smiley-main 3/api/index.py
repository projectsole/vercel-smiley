from flask import Flask, app, render_template, request, redirect, url_for, send_from_directory
import os


app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu/qbio")
def menu_qbio():
    return render_template("menu_qbio.html")

@app.route("/recensioni/gramsci")
def recenioni_gramsci():
    return render_template("index_review.html")

@app.route("/suggerisci/gramsci")
def suggest_gramsci():
    return render_template("index_suggest.html")

@app.route("/allergeni")
def allergeni():
    return render_template("index_allergeni.html")

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../static', path)


if __name__ == "__main__":
    app.run(port=8080, debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/css/style.css">
    <title>IWard</title>
</head>
"""

@app.route("/", methods=["GET"])
def main_route():
    return head + "Welcome to this application, check /vulnerable?name=alex or /not_vulnerable?name=alex"


@app.route("/vulnerable", methods=["GET"])
def vulnerable():
    name = request.args.get('name')
    if not name:
        return "You must give me your name if you want me to welcome you"
    return head + "Hello {}, how are you ?".format(name)

@app.route("/not_vulnerable", methods=["GET"])
def not_vulnerable():
    name = request.args.get('name')
    if not name:
        return "You must give me your name if you want me to welcome you"
    return render_template("index.html", name=name)

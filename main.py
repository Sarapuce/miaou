from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <link rel="stylesheet" href="/static/css/style.css">
    <title>Miaou</title>
</head>
"""

cat1 = """
</br>
</br>
</br>
<img src=/static/img/img1.jpg></br>
<p>&nbsp;&nbsp;／l、&nbsp;&nbsp;&nbsp;&nbsp;    I sleep...</br>     
（ﾟ､ ｡ ７</br>         
&nbsp;&nbsp;l&nbsp;&nbsp;~ヽ</br>       
&nbsp;&nbsp;じしf_,)ノ</br></p>
"""

cat2 = """
</br>
</br>
</br>
<img src=/static/img/img3.jpg></br>
<p>&nbsp;&nbsp;／l、&nbsp;&nbsp;&nbsp;&nbsp;    It's dangerous</br>     
（ﾟ､ ｡ ７</br>         
&nbsp;&nbsp;l&nbsp;&nbsp;~ヽ</br>       
&nbsp;&nbsp;じしf_,)ノ</br></p>
"""

index = """
<body>
    <p>Welcome to this application! The only two available endpoints are:</p>
    <ul>
        <li>/vulnerable?name=alex</li>
        <li>/not_vulnerable?name=alex</li>
    </ul>

    <form id="nameForm">
        <label for="username">What's your name?</label>
        <input type="text" id="username" name="username" required>
        <button type="button" onclick="redirectToHelloDangerous()">Say Hello</button>
        <br><br>
        <label for="win">Enter &#34;&lt;script&gt;&#34; to win:</label>
        <input type="text" id="win" name="win" required>
        <button type="button" onclick="redirectToHelloSafe()">Go !</button>
    </form>

    <script>
        function redirectToHelloSafe() {
            var winValue = encodeURIComponent(document.getElementById('win').value);
            window.location.href = '/not_vulnerable?name=' + winValue;
        }

        function redirectToHelloDangerous() {
            var usernameValue = encodeURIComponent(document.getElementById('username').value);
            window.location.href = '/vulnerable?name=' + usernameValue;
        }
    </script>
</body>
"""

@app.route("/", methods=["GET"])
def main_route():
    return head + index + cat1


@app.route("/vulnerable", methods=["GET"])
def vulnerable():
    name = request.args.get('name')
    if not name:
        return "You must give me your name if you want me to welcome you"
    return head + "Hello {}, how are you ?".format(name) + cat2

@app.route("/not_vulnerable", methods=["GET"])
def not_vulnerable():
    name = request.args.get('name')
    if not name:
        return "You must give me your name if you want me to welcome you"
    elif name == "<script>":
        return render_template("index.html", congrats="You win ", name=name)
    else:
        return render_template("index.html", congrats="You lost ", name=name)

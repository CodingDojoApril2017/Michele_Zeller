from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_name():
    name = request.form['name']
    dojo_location = request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    comment = request.form['comment']
    return render_template('success.html', name = name, dojo_location = dojo_location, favorite_language = favorite_language, comment = comment)

app.run(debug=True)

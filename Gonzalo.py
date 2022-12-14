from flask import Flask, render_template, request, flash
app = Flask(__name__,template_folder='template')
app.secret_key = "redischool_22"
@app.route("/finder")
def index():
    flash('Fun in Berlin?')
    return render_template("index.html")
@app.route("/search", methods=["POST", "GET"])
def search():
    request.form['event_input']
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
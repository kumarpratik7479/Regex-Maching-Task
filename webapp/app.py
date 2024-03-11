from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex = request.form["regex"]
    matches = re.findall(regex, test_string)
    return render_template("results.html", matches=matches)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    # Simple regex for demonstration; consider more comprehensive regex for real applications
    is_valid = re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email)
    return render_template("index.html", email_result=is_valid)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
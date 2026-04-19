from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/multiply", methods=["GET", "POST"])
def multiply():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])

        result = a * b

        return render_template("result14.html", result=result)

    return render_template("index14.html")

if __name__ == "__main__":
    app.run(debug=True)

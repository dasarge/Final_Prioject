from flask import Flask, render_template, redirect, url_for
from flask.wrappers import Request


# Dependencies

# -------Create an instance of Flask-------------
app = Flask(__name__, template_folder="templates", static_folder="static")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html",)


@app.route("/bitcoin", methods=['GET', 'POST'])
def bitcoin():
    if Request.method == 'POST':
        return redirect(url_for('home'))
    # Return template and data
    return render_template("2_Bitcoin_Indexes.html",)


if __name__ == "__main__":
    app.run(debug=True, port=5001)


# -----------------------------------------------
# if __name__ == "__main__":
#     app.run(port=5001)

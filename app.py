from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CORRECT_PASSWORD = "@#729265"  # You can change this anytime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unlock', methods=["GET", "POST"])
def unlock():
    error = None
    if request.method == "POST":
        password = request.form.get("password")
        if password == CORRECT_PASSWORD:
            return redirect(url_for('file'))
        else:
            error = "👿 Warning! Wrong password! DM me proof on Instagram to get the correct password."
    return render_template('unlock.html', error=error)

@app.route('/file')
def file():
    return render_template('file.html')  # This will contain the final download link

if __name__ == '__main__':
    app.run(debug=True)

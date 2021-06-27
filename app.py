# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import college_finder

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        print(request.form["gpa"])
        user_gpa=request.form["gpa"]
        user_sat=request.form["sat"]
        # user_major=request.form["major"]
        match_college=college_finder(user_gpa, user_sat)
        return render_template("results.html", user_gpa=user_gpa, user_sat=user_sat, match_college=match_college, len = len(match_college))
    else:
        return redirect('/')


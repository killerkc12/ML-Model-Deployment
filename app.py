from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import marks as m

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    marks_pred = -1
    if request.method == 'POST':
        hrs = request.form['hrs']
        marks_pred = m.marks_analysis(hrs)
        print(marks_pred)
    else:
        marks_pred = -1
    return render_template('index.html', marks_pred=marks_pred)


@app.route('/submit', methods=['POST']) 
def submit():
    if request.method == 'POST':
        name = request.form['username']
    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
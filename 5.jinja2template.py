## jinja2 template engine used for data source
"""
{% . . . %} for statements, conditions
{{ }} expression to print the output its getting from route decorator
{#...#} internal html comments
"""

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS" 
    else:
        res="FAIL"

    exp = {'Score' : score, 'Result' : res}
    return render_template('result2.html',result = exp)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
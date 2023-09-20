from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

# in order to access the html file, firstly it needs to be inside a folder called 'templates'
# then by simply using render_template() function in the return statement, we can render the html page
# every route must return something so return statement at the end is important, otherwise it will give an error
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

    return render_template('result.html',result = res)

# result checker submit html page
# in the html pade there will four fields each one to enter marks of four different subjects and calculate the avg of marks  
# if the avg is less than 50 then person has failed, if the avg is more than 50 then person has passed
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

    return redirect(url_for('success',score=total_score))


if __name__=='__main__':
    app.run(debug=True)
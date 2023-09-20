### building url dynamically
### flask Variable Rules and URL building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return 'welcome welcome '

# building URLs using the available 'variable rules' in Flask
# by default urls are treated as string, if any other data type is required then specify it before the variable
# here we can manually enter any integer value and it will be printed along with the message in return 
@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is " + str(score)

# result checker: if value provided in the url is > 50 it pass will be printed otherwise fail will be printed on the screen
@app.route('/result/<int:score>')
def results(score):
    result = ''
    if score < 50:
        result = 'fail'
    else:
        result = 'pass'

    return result

# now if we want to redirect person who has passed to a different page and person who has failed to pass to a different page
# creating another url with binding function as outcome
@app.route('/outcome/<int:marks>')
def outcomes(marks):
    outcome = ''
    if marks < 50:
        outcome = 'fail'
    else:
        outcome = 'success'

    # first we need those urls in order to redirect to those pages
    # if a person is pass, the person will be redirected to success page if the person has failed, the person will be redirected to fail page
    # first it will go to 'outcomes()' function then according to the marks it will go to either success or fail pages
    return redirect(url_for(outcome,score=marks)) 




if __name__ == '__main__':
    app.run(debug=True) 
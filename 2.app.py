from flask import Flask

# creating app this creates a WSGI application
app = Flask(__name__) # this acts as WSGI application which will be communicating with the server

# decorator it takes (rules,optional) it gets bind with a function which runs when the path is reached
# it takes a rule and whenever we go to that page the function written after it, will get triggered automatically
# here it is taking a root path or homepage and binding with hello_world() function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# if function name is same then server will give an AssetionError so binding function name should be different

@app.route("/members")
def welcome():
    return "<h2>Hello, members - in bigger text!</h2>"

"""
When you use the condition if _name_ == "__main__":, 
the code inside that block will only run if the current script is being directly executed as a standalone script.

If the script is imported as a module into another script, the code inside the if _name_ == "__main__": block will not run. 
This allows you to have certain code that should only execute when the script is run directly, but not when it is imported as a module.
"""
if __name__ == "__main__":
    app.run(debug=True) # if we write debug = True then server restarts on it own and makes changes in real time, we don't have to restart it everytime we make changes


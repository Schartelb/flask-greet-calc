from operations import add, sub, mult, div
from flask import Flask, request


@app.route('/add')
def call_add(self):  # doesn't need self, not a class
    self.a = request.args["a"]  # needs int for all request.args
    self.b = request.args["b"]
    return add(self.a, self.b)  # needs str for all result returns


@app.route('/sub')
def call_sub(self):
    self.a = request.args["a"]
    self.b = request.args["b"]
    return sub(self.a, self.b)


@app.route('/mult')
def call_mult(self):
    self.a = request.args["a"]
    self.b = request.args["b"]
    return mult(self.a, self.b)


@app.route('/div')
def call_div(self):
    self.a = request.args["a"]
    self.b = request.args["b"]
    return div(self.a, self.b)


#operation= {"add": add(a,b), "sub": sub(a,b), "mult": mult(a,b), "div": div(a,b)}
# @app.route('/math/<operation>')
#    def math():
#        a = request.args["a"]
#        b = request.args["b"]
#    return operation[operation]  #this may work, testing isn't cooperating

from Flask import Flask

app = Flask(__name__)


@app.route('/welcome')
 def say_welcome():
      '''Return Welcome as response'''
       return "Welcome"


@app.route('/welcome/<place>')
 def say_welcomeplace(place):
       if place == "home":
            return "Welcome Home"
        if place == "back":
            return "Welcome Back"
from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# insert route and function here

if __name__ == '__main__':
  app.run()
from flask import Flask, render_template, request, make_response, redirect
import random
app = Flask(__name__)

'''
Person gives gifts to
p1 -> p2
p2 -> p1

santas = [
   {p1: p2},
   {p2: p1}
]
'''
santas = []

@app.route('/')
def index():
    if len(santas) > 0:
       return render_template("index.html", peoples=santas)
    else:
       return render_template("index.html")

# insert route and function here
@app.route('/process/<n>', methods=["POST"])
def process_names(n):
    # get fields
    peeps = []
    peeps.append(request.form.get('p1'))
    peeps.append(request.form.get('p2'))
    peeps.append(request.form.get('p3'))
    print(peeps)
    # [p1, p2]
    peeps2 = peeps.copy()
    for a in range(len(peeps)):
        r = random.randint(0, len(peeps2) - 1)
        if peeps[a] != peeps2[r]:
            santas.append({peeps[a]: peeps2[r]})
            peeps2.pop(r)
    return redirect('/')

if __name__ == '__main__':
    app.run()
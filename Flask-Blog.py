from flask import Flask, render_template
from generatetext import current_day

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    #return "<h1>Home Page</h1>"
    #return stoic
    return render_template("home.html", text = current_day())

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)




class Passage(object):
    date = ""
    wisdom = ""
    quote = ""
    speaker = ""
    analysis = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, date, wisdom,quote,speaker,analysis):
        self.date = date
        self.wisdom = wisdom
        self.quote = quote
        self.speaker = speaker
        self.analysis = analysis

def make_student(date, wisdom, quote,speaker, analysis):
    passage = Passage(date, wisdom, quote,speaker,analysis)
    return passage









'''from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

'''







'''export FLASK_APP=Flask-Blog.py


export FLASK_DEBUG=1
flask run

'''
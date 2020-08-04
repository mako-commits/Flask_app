from flask import Flask, render_template
from data import Articles

#instance of the flask app
app = Flask(__name__)

Articles = Articles()
#route to homepage
@app.route('/')
def home():
        return render_template('home.html')


#route to about
@app.route('/about')
def about():
        return render_template('about.html')

#route to articles
@app.route('/articles')
def articles():
        return render_template('articles.html', articles = Articles)


#route to article
@app.route('/article/<string:id>/')
def article(id):
        return render_template('article.html', id=id)



if __name__ == '__main__':
    app.run(debug=True)

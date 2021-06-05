from flask import Flask, render_template, request, redirect, url_for
import Day24_data as df

app = Flask(__name__)

@app.route('/')
def home():
	articles_v = df.get_top_headlines()[::-1]
	return render_template('Day24(home).html', articles=articles_v)

@app.route('/top-headlines')
def top_headlines():
	articles_v = df.get_top_headlines()
	return render_template('Day24(article).html', articles=articles_v, title = 'Top Headlines')

@app.route('/search', methods=['POST'])
def search_news():
	search_keyword = request.form['search']
	articles_v = df.get_everything(search_keyword=search_keyword)
	return render_template('Day24(article).html', articles=articles_v, title = 'Search Page')

@app.route('/category/<cate>')
def category_news(cate):
	articles_v = df.get_top_headlines(category=cate)
	return render_template('Day24(article).html', articles=articles_v, title = cate.upper())


if __name__ == '__main__':
	app.run(debug=True)
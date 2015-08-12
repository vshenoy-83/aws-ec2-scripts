#!/root/test1/venv/bin/python
from flask_bootstrap import Bootstrap
from flask import Flask,current_app,render_template,abort

app=Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/one')
def one():
	return '<h1>ONE<h1>'	

@app.route('/two')
def two():
	return '<h1>TWO<h1>'

@app.route('/three')
def three():
	abort(404)		

@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'),404

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)

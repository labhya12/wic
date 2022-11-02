from flask import Flask
from flask import redirect,url_for
app=Flask(__name__)




@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' %name
if __name__=='__main__':
	app.run(debug=True)

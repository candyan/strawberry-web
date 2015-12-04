from flask import Flask
from views.index_ui import IndexView

app = Flask(__name__)
app.debug = True

app.add_url_rule('/', view_func=IndexView.as_view('index_view'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

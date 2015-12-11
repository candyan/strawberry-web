from app import app
from views.index_ui import IndexView
from views.vpn_guides_ui import VPNGuidesUI
from views.signin_ui import SigninView

app.add_url_rule('/', view_func=IndexView.as_view('index_view'))
app.add_url_rule('/guides', view_func=VPNGuidesUI.as_view('vpn_guides_view'))
app.add_url_rule('/sign_in', view_func=SigninView.as_view('sign_in_view'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

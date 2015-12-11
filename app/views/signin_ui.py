from base_ui import BaseView


class SigninView(BaseView):

    def template_context(self):
        return {"current_menu_index": 2}

    def template_name(self):
        return "signin.html"

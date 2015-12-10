from flask.views import View
from flask import render_template


class BaseView(View):
    def template_name(self):
        raise NotImplementedError()

    def template_context(self):
        return {}

    def dispatch_request(self):
        return render_template(self.template_name(), **self.template_context())

from base_ui import BaseView
from models.invitation import InvitationCode


class IndexView(BaseView):

    def template_context(self):
        count_format_str = "{:,}".format(InvitationCode.unused_count())
        return {"unused_code_count": count_format_str}

    def template_name(self):
        return "index.html"

from base_ui import BaseView


class VPNGuidesUI(BaseView):

    def template_context(self):
        return {"current_menu_index": 1}

    def template_name(self):
        return "vpn_guides.html"

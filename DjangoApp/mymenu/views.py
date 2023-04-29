from django.views.generic import TemplateView
from .models import MenuItems, OtherMenuItems


class MenuListView(TemplateView ):
    template_name = 'mymenu/base.html'
    menus = {'menuitems': MenuItems,
             'othermenuitems': OtherMenuItems, }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for menu_name, model_name in self.menus.items():
            context[menu_name] = model_name.objects.all()
        return context

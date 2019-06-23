from django.conf.urls import url
from django.http import HttpResponse
from django.template import loader
from django.contrib.admin import AdminSite,ModelAdmin
# from .sites import AdminSite,ModelAdmin
from django.contrib.admin.sites import site as default_site
from django.contrib.auth.models import Group, User
# from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.urls import reverse, NoReverseMatch
from django.utils.text import capfirst
from django.apps import apps


class CustomAdminSite(AdminSite):
    site_header = 'Majid Administration'
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            # re_path(r'^.*\.html', views.custom_admin_template_loader, name='custom-loader'),

            url(r'^.*\.html', self.my_view, name="my-view"),
        ]
        return urls + custom_urls

    def my_view(self, request):
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
        }
        request.current_app = self.name
        load_template = request.path.split('/')[-1]
        template = loader.get_template('admin/' + load_template)
        return HttpResponse(template.render(context, request))

    def _build_app_dict(self, request, label=None):
        """
                Build the app dictionary. The optional `label` parameter filters models
                of a specific app.
                """
        app_dict = {}

        if label:
            models = {
                m: m_a for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': capfirst(model._meta.verbose_name_plural),
                'object_name': model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
                'count': model.objects.count(),
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=self.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict



class MyModelAdmin(ModelAdmin):
    # default_site = CustomAdminSite
    pass

    # def _registry_getter(self):
    #     return default_site._registry
    #
    # def _registry_setter(self, value):
    #     default_site._registry = value
    #
    # _registry = property(_registry_getter, _registry_setter)

# custom_admin = CustomAdminSite()

# register the default model

# custom_admin.register(Group)
# custom_admin.register(User)


admin_site = CustomAdminSite(name='myadmin')
admin_site.register(User, MyModelAdmin)

admin_site.register(Group, MyModelAdmin)


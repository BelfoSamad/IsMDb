import simple_history
from django.conf.urls import url
from django.db import models
from django.http import HttpResponse
from django.template import loader
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.auth.models import User
from django.urls import reverse, NoReverseMatch
from django.utils.text import capfirst
from django.apps import apps
from simple_history.admin import SimpleHistoryAdmin

from admin.widgets import MyAdminSplitDateTime , AdminDateWidget , AdminTimeWidget
from reviews.models import Actor, Director, Writer, MovieReview
from suggestions.models import Suggestion
from users.models import Member, MemberGroup
from . import views as my_views
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect


from django.contrib.auth.models import User


class CustomAdminSite(AdminSite):
    site_header = 'IsMDb'
    site_title = 'IsMDb'

    def each_context(self, request):
        context = super().each_context(request)

        # Notification:
        if request.user.is_authenticated:
            context['notifications'] = request.user.notifications.unread()

        return context

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            # re_path(r'^.*\.html', views.custom_admin_template_loader, name='custom-loader'),

            # url(r'^.*\.html', self.my_view, name="my-view"),
            url('account/', my_views.account, {'admin_site_instance': self}, name='account'),
            url('manage_users/', self.my_view, name='manage_users'),
            url('manage_suggestions/', self.my_view, name='manage_suggestions'),
            url('manage_reports/', self.my_view, name='manage_reports'),
            url('global_history/', my_views.history,{'admin_site_instance': self}, name='global_history'),
            url('manage_reviews/', self.my_view, name='manage_reviews'),
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
        load_template = request.path
        load_template = load_template[:-1]
        load_template = load_template[1:]
        load_template += '.html'
        template = loader.get_template(load_template)
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
            if hasattr(model, 'objects'):
                model_dict = {
                    'class': model,
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'admin_url': None,
                    'add_url': None,
                    'count': model.objects.count(),
                }
            else:
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'admin_url': None,
                    'add_url': None,
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
    formfield_overrides = {
        models.DateTimeField : { 'widget' : MyAdminSplitDateTime}
    }

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


# class CategoryAdmin(ModelAdmin):
#     pass
#     change_list_template = 'admin/category/change_list.html' # definitely not 'admin/change_list.html'
#     list_per_page = 2
#     formfield_overrides = {
#         models.DateTimeField : { 'widget' : MyAdminSplitDateTime},
#         models.TimeField: { 'widget' : AdminTimeWidget},
#         models.DateField: { 'widget' : AdminDateWidget},
#     }
    # list_display = [Category,'name']
    # def get_list_display(self, request):
    #     list_display = super(CategoryAdmin, self).get_list_display(request)
    #     return list_display + ['name']

class CustomSimpleHistoryAdmin(SimpleHistoryAdmin):
    object_history_template = "simple_history/object_history.html"
    object_history_form_template = "simple_history/object_history_form.html"



admin_site = CustomAdminSite(name='myadmin')


# Registering Proxy models to CustomSimpleHistoryAdmin
simple_history.register(Member)
simple_history.register(MemberGroup)
simple_history.register(Suggestion)
simple_history.register(Actor)
simple_history.register(Director)
simple_history.register(Writer)
simple_history.register(MovieReview)

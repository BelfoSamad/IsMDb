# from django.contrib.admin.apps import AdminConfig
#
#
# class MyAdminConfig(AdminConfig):
#     name = 'admin'
#     default_site = 'admin.CustomAdminSite'
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'admin.admin.CustomAdminSite'


from django.conf.urls import url

from reports import views

app_name = 'reports'

urlpatterns = [
    url(r'^api/report_comment/$', views.ReportComment.as_view(), name='report_comment'),
    url(r'^api/report_review/$', views.ReportReview.as_view(), name='report_review')
]

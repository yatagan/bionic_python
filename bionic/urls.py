from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bionic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('students', 'coursera.views.students_view'),

    url(r'^admin/', include(admin.site.urls)),
)

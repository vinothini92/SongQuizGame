from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Guessit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'question/(?P<question_id>\w+)/$','Guessit.views.display_question',name='display_question'),    
    url(r'^admin/', include(admin.site.urls)),
)

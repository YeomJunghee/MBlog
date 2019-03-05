from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$', views.home, name='home'),

   url(r'^blog/(?P<pk>\d+)', views.detail, name="detail"),
   url(r'^blog/new/',views.new,name="new"),
   url(r'^blog/create',views.create, name="create"),
   url(r'^blog/portfolio/',views.portfolio,name="portfolio"),
   url(r'^blog/newblog/',views.blogpost,name="newblog"),

]  + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



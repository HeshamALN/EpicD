from django.contrib import admin
from django.urls import path
from app import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('about/',views.about, name = "about"),
    path('instagram/',views.instagram, name = "instagram"),
    path('howItWorks/',views.howItWorks, name = "howItWorks"),
    path('project/',views.project_list , name = "project-list"),
    path('contact/',views.emailView, name = "contact"),
    path('project/<int:project_id>/',views.project_details, name = "project-detail"),
    path('plans/',views.plans, name = "plans"),


    path('email/', views.emailView, name='email'),

    path('404/', views.error, name='error'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
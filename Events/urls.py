from django.urls import path
from django.conf import settings
from Events import views
from django.conf.urls.static import static
urlpatterns = [
    path('create/', views.createevent, name='createevent') ,
    path('showevent/',views.showevent,name='showevent'),
    path('updateevent/<int:id>',views.updateevent,name='updateevent'),
    path('deleteevent/<int:id>',views.deleteevent,name='deletevent')

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

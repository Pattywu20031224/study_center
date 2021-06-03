from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('',RedirectView.as_view(url='homepage/')),
    path('homepage/', include('homepage.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('log/',include('log.urls')),

]

# 加入靜態檔案的處理規則
urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)

# 加入使用者上傳檔案的處理規則
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)
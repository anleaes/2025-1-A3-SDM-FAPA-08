"""
URL configuration for questvault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('playerprofiles/', include('playerprofiles.urls', namespace='playerprofiles')),
    path('items/', include('items.urls', namespace='items')),
    path('inventories/', include('inventories.urls', namespace='inventories')),
    path('inventoryitems/', include('inventoryitems.urls', namespace='inventoryitems') ),
    path('quests/', include('quests.urls', namespace='quests') ),
    path('completedquests/', include('completedquests.urls', namespace='completedquests')),
    path('achievements/', include('achievements.urls', namespace='achievements') ),
    # path('token-autenticacao/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

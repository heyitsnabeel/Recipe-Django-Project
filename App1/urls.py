from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe),
    path('delete_recipe/<id>/', views.delete_recipe),
    path('update_recipe/<id>/', views.update_recipe),
    path('update_recipe/<id>/', views.update_recipe),
    path('login/', views.login_page),
    path('logout/', views.logout_page),
    path('register/', views.register_page),
]
from django.urls import include, path
from rest_framework import routers

#from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
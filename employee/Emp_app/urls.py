# from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'departments', views.DepartmentViewSet)
# router.register(r'roles', views.RoleViewSet)
# router.register(r'employees', views.EmployeeViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),

#     # 👇 Add these two
#     path('api/register/', views.register_user, name='register'),
#     path('api/login/', views.login_user, name='login'),
# ]
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),             # ✅ remove the extra 'api/'
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
]

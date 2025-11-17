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
# your_app/urls.py
# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'departments', views.DepartmentViewSet)
# router.register(r'roles', views.RoleViewSet)
# router.register(r'employees', views.EmployeeViewSet)

# urlpatterns = [
#     path('', include(router.urls)),           # /api/departments/, /api/roles/, /api/employees/
#     path('register/', views.register_user, name='register'),  # POST /api/register/
#     path('login/', views.login_user),         # POST /api/login/
# ]
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('register/', views.register_user, name='register'),  # POST /api/register/
    path('login/', views.login_user, name='login'),           # POST /api/login/
    path('', include(router.urls)),                            # /api/departments/, /api/roles/, /api/employees/
]

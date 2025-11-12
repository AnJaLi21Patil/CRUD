# # from rest_framework import viewsets, status
# # from rest_framework.response import Response
# # from rest_framework.decorators import api_view, permission_classes
# # from rest_framework.permissions import AllowAny
# # from django.contrib.auth.models import User
# # from django.contrib.auth import authenticate
# # from .models import Employee, Department, Role
# # from .serializers import EmployeeSerializer, DepartmentSerializer, RoleSerializer


# # # --- Existing CRUD ViewSets ---
# # class DepartmentViewSet(viewsets.ModelViewSet):
# #     queryset = Department.objects.all()
# #     serializer_class = DepartmentSerializer

# # class RoleViewSet(viewsets.ModelViewSet):
# #     queryset = Role.objects.all()
# #     serializer_class = RoleSerializer

# # class EmployeeViewSet(viewsets.ModelViewSet):
# #     queryset = Employee.objects.all()
# #     serializer_class = EmployeeSerializer


# # # --- NEW AUTH APIs (only these added) ---
# # @api_view(['POST'])
# # @permission_classes([AllowAny])
# # def register_user(request):
# #     username = request.data.get('username')
# #     password = request.data.get('password')
# #     email = request.data.get('email')

# #     if not username or not password:
# #         return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

# #     if User.objects.filter(username=username).exists():
# #         return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

# #     user = User.objects.create_user(username=username, password=password, email=email)
# #     return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)


# # @api_view(['POST'])
# # @permission_classes([AllowAny])
# # def login_user(request):
# #     username = request.data.get('username')
# #     password = request.data.get('password')

# #     user = authenticate(username=username, password=password)
# #     if user is not None:
# #         return Response({'message': 'Login successful', 'user_id': user.id, 'username': user.username})
# #     else:
# #         return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from .models import Employee, Department, Role
# from .serializers import EmployeeSerializer, DepartmentSerializer, RoleSerializer


# # --- CRUD ViewSets ---
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer


# class RoleViewSet(viewsets.ModelViewSet):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer



# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# # --- AUTH APIs ---
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     email = request.data.get('email')

#     if not username or not password:
#         return Response({'error': 'Username and password are required'},
#                         status=status.HTTP_400_BAD_REQUEST)

#     if User.objects.filter(username=username).exists():
#         return Response({'error': 'Username already exists'},
#                         status=status.HTTP_400_BAD_REQUEST)

#     user = User.objects.create_user(username=username, password=password, email=email)
#     return Response({'message': 'User registered successfully', 'user_id': user.id},
#                     status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(username=username, password=password)
#     if user is not None:
#         return Response({'message': 'Login successful', 'user_id': user.id, 'username': user.username},
#                         status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid username or password'},
#                         status=status.HTTP_401_UNAUTHORIZED)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Employee, Department, Role
from .serializers import EmployeeSerializer, DepartmentSerializer, RoleSerializer

# --- CRUD ViewSets ---
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# --- AUTH APIs ---
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({'error': 'Username and password are required'},
                        status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'User registered successfully', 'user_id': user.id},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({'message': 'Login successful', 'user_id': user.id, 'username': user.username},
                        status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'},
                        status=status.HTTP_401_UNAUTHORIZED)


# --- Optional: custom POST endpoint for Employee ---
@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from .models import Employee
from .models import Role
from .models import Department


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields= '__all__'


# class EmployeeSerializer(serializers.ModelSerializer):
#     department = serializers.CharField(source='dept.name', read_only=True)
#     role = serializers.CharField(source='role.name', read_only=True)

#     class Meta:
#         model = Employee
#         fields = ['id', 'first_name', 'last_name', 'department', 'role', 'salary', 'bonus', 'phone', 'hire_date']


# class EmployeeSerializer(serializers.ModelSerializer):
#     # Use 'dept.name' since your model field is named 'dept'
#     department = serializers.CharField(source='dept.name', read_only=True)
#     role = serializers.CharField(source='role.name', read_only=True)

#     class Meta:
#         model = Employee
#         fields = ['id', 'first_name', 'last_name','dept', 'department', 'role',
#                   'salary', 'bonus', 'phone', 'hire_date']

from rest_framework import serializers
from .models import Employee

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    # For display in GET responses
    department = serializers.CharField(source='dept.name', read_only=True)
    role_name = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = Employee
        # Include dept and role for POST, but department and role_name for display
        fields = ['id', 'first_name', 'last_name', 'department', 'role_name',
                  'salary', 'bonus', 'phone', 'hire_date', 'dept', 'role']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields= '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields= '__all__'
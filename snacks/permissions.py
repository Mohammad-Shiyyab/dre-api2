from rest_framework import permissions


class IsOnerOrReadOnly(permissions.BasePermission):
    message = "you can tedit this Thing object , you are not the owner !! "
    def has_object_permission(self, request, view, obj):
        
       if request.method == 'GET':
           return True
       return request.user == obj.owner


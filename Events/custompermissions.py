from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class isambass(BasePermission):
    def has_permission(self,request,view):
        message = "Only College ambassadors can do so."
        if request.user.is_authenticated and request.user.is_brand_ambassador:
            return True
        raise PermissionDenied(message)
 




    





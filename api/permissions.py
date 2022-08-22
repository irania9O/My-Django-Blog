from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)


class IsAuthorAndDraftOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # author
        return bool(
            request.user.is_authenticated and 
                (
                    request.user.is_superuser or
                    obj.author == request.user and obj.status == "d"
                )
            )
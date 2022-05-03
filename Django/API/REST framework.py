"""Вызов проверки Permissions"""

check_permissions
# проверяет, следует ли разрешить запрос на основе данных запроса
check_object
# permissions проверяет, следует ли разрешить запрос на
# основе комбинации данных запроса и объекта
# rest_framework/views.py

class APIView(View):
    # other methods
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(
                    request,
                    message=getattr(permission, 'message', None),
                    code=getattr(permission, 'code', None)
                )

"""Для вызова разных Permissions в зависимости от ситуации"""
def get_permissions(self):
    if self.action == 'retrieve':
        return (ReadOnly(),)
    return super().get_permissions() 
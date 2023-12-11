from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # Se método for DELETE e usuário é superuser, então pode deletar
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
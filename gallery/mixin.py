from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creater != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)    
class BasePermissions(object):
    '''Base permission class '''

    def has_permission(self, request, view):
        '''return True if fermission is granted'''
        return True

    def has_object_permissions(self, request, view, obj):
        '''return True if fermission is granted'''
        return True
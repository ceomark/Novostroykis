from django.shortcuts import redirect

class CheckUserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.user_type == 'admin' and not request.path.startswith('/manager/'):
                return redirect('/manager/admin-dashboard/')
            elif request.user.user_type == 'moderator' and not request.path.startswith('/manager/'):
                return redirect('/manager/moderator-dashboard/')
        return self.get_response(request)
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.utils import timezone

class SessionTokenMiddleware(MiddlewareMixin):
    """
    Middleware to ensure session tokens are valid for authenticated users
    """
    def process_request(self, request):
        # Skip middleware for login and logout pages
        if request.path in ['/login/', '/logout/', '/register/', '/signup/']:
            return None
            
        # Skip middleware for static files and admin
        if request.path.startswith('/static/') or request.path.startswith('/admin/'):
            return None
            
        # If user is authenticated but no auth token exists, redirect to login
        if request.user.is_authenticated:
            if 'auth_token' not in request.session:
                request.session.flush()
                return HttpResponseRedirect('/login/')
            
            # Check if session is still valid
            if request.session.session_key:
                try:
                    session = Session.objects.get(session_key=request.session.session_key)
                    if session.expire_date < timezone.now():
                        request.session.flush()
                        return HttpResponseRedirect('/login/')
                except Session.DoesNotExist:
                    request.session.flush()
                    return HttpResponseRedirect('/login/')
        
        return None

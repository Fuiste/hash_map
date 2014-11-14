from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SessionView(APIView):
    error_messages = {
        'invalid': 'Invalid username or password',
        'disabled': 'Sorry, this account is suspended',
        }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
            }
        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return Response({'user_id': request.user.id})
        return Response({'user_id': None})

    def post(self, request, *args, **kwargs):
        # Login
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'success': True, 'user_id': user.id})
            return self._error_response('disabled')
        return self._error_response('invalid')

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


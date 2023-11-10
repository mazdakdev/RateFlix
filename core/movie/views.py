from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list top rated movies.

    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
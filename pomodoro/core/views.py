from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TaskCreateAPIView(APIView):
    def post(self, request):
        return Response({
            "uid": "be10032a-b65f-4cac-ab89-a2851afd7518",
            "description": "Criando task de teste",
            "created_at": "2022-05-03T17:48:00"
        }, status=status.HTTP_201_CREATED)

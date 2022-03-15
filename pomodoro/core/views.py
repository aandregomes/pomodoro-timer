from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pomodoro.core.serializers import TaskSerializer


class TaskCreateAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.initial_data["uid"] = "bfb1ea03-3d54-4832-b9f3-cb1b5da1e46b"
        serializer.initial_data["created_at"] = "2022-03-14T22:12:00"

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.initial_data, status=status.HTTP_201_CREATED)

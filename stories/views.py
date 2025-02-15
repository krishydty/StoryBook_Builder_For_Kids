from rest_framework import generics, permissions
from .models import Story
from .serializers import StorySerializer

class StoryListView(generics.ListCreateAPIView):
    """API endpoint to list all stories and create new ones"""
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Assign the logged-in user as the author"""
        serializer.save(author=self.request.user)


class StoryDetailView(generics.RetrieveAPIView):
    """API endpoint to retrieve a single story"""
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

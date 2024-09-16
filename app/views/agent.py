from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from app.models import Agent
from app.serializers.agent import AgentSerializer

# we handle Agent views.
class CreateAgentView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def perform_create(self, serializer):
        agent = serializer.save()
        detail_serializer = AgentSerializer(agent)
        return Response(detail_serializer.data)

class ListAgentView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name')
    
    def get_queryset(self):
        # Return only the agents associated with the current authenticated user
        return Agent.objects.filter(user=self.request.user)


class RetrieveDestroyUpdateAgentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_url_kwarg = 'id'
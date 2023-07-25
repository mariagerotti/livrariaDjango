from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import  LivroDetailSerializer,LivroListSerializer, LivroSerializer



class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    serializer_classes = {
        "list": LivroListSerializer,
        "retrieve": LivroDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivroSerializer)
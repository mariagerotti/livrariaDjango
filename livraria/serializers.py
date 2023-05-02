from rest_framework.serializers import ModelSerializer

from livraria.models import Autor, Categoria, Editora, Livro


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
        
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco"]

# class LivroListSerializer(ModelSerializer):
#      class Meta:
#          model = Livro
#          fields = ['titulo', 'preco']
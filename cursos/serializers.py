"""
    O serializer pega os objetos python e transforma em json
    Também transforma json em objetos python
"""
from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


def validate_avaliacao(valor):
    if valor in range(1, 6):
        return valor
    raise serializers.ValidationError('Aavaliação precisa ser um inteiro entre 1 e 5')


# Nome padronizado: Nome do Objeto + Serializer
class AvaliacaoSerializer(serializers.ModelSerializer):  # Herda ModelSerializer

    class Meta:
        # Indica que o email não será apresentado ao consultar avaliações
        # Somente escrita/gravação
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao  # Modelo que será serializado
        # Campos do modelo que serão apresentados
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship - Somente viável em caso de poucos dados a trafegar
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field - a view_name = avaliacao-detail deve ser escrita assim, pois é o padrão
    # Pois a rota foi criada automaticamente
    # Retorna um link para cada avaliação referente ao curso
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field - Retorna todos ids das avaliacoes
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2

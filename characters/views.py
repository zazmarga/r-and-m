from random import choice

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.filters import CharacterFilter
from characters.models import Character
from characters.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)  # flat=True  return LIST of id
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    #   SPOSOB  1 - ex.  -  api/characters/?name=rick
    # serializer_class = CharacterSerializer
    #
    # def get_queryset(self) -> QuerySet:
    #     queryset = Character.objects.all()
    #     name = self.request.query_params.get("name")
    #     if name is not None:
    #         queryset = queryset.filter(name__icontains=name)
    #     return queryset

    # SPOSOB  2  standart DRF - Setting filter backends  (import django_filters.rest_framework)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter

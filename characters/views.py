from random import choice

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.filters import CharacterFilter
from characters.models import Character
from characters.serializers import CharacterSerializer


def get_random_character() -> Character:
    pks = Character.objects.values_list("pk", flat=True)  # flat=True  return LIST of id
    random_pk = choice(pks)
    return Character.objects.get(pk=random_pk)


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    """Get a random character from Rick & Morty world"""
    random_character = get_random_character()
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

    #  dlia SPOSOB 1  nuzhno perenaznachit metod "list"
    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(
    #             name="name",
    #             description="Filter by name insensitive contains",
    #             required=False,
    #             type=str,
    #         ),
    #     ]
    # )
    #  dlia dvuh SPOSOBOV  - chtoby bylo OPIDANIE endpointa
    def get(self, request: Request, *args, **kwargs) -> Response:
        """List characters with filter by name"""
        return super().get(request, *args, **kwargs)

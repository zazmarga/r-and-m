from django.urls import path

from characters.views import (
    get_random_character_view,
    get_random_character_view,
    CharacterListView,
)

app_name = "characters"

urlpatterns = [
    path("characters/random/", get_random_character_view, name="random_character"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]

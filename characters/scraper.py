from sqlite3 import IntegrityError

import requests
from django.conf import settings

from characters.models import Character


def scrape_characters() -> list[Character]:

    next_url_to_scrape = (
        settings.RICK_AND_MORTY_API_CHARACTER_URL
    )  #  endpoint needed api: character

    characters = []

    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()

        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )

        next_url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        if character.api_id not in Character.objects.values_list("api_id", flat=True):
            character.save()
        else:
            print(f"Character {character.api_id} already exists")


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)

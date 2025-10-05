import json
import os
import re

import click

from polarbadge.service.geekevents import get_client
from polarbadge.service.config import get_config
from polarbadge.service.render import render_card, render_to_image
from .spec import design

_client = get_client()
_config = get_config()

REGEX_UUID = re.compile(r"^[0-9a-f\-]{30,50}$")

def everyone():
    generate_badges()

@click.option("--user", "-u", multiple=True)
def users(user: list[int]):
    users = list(map(int, user))
    generate_badges(user_ids=users)

def generate_badges(user_ids: list | None = None):
    click.echo("Generating badges...")
    crew_members = _client.get_crew_members()
    if user_ids is not None:
        crew_members = [crew_member for crew_member in crew_members if crew_member.user_id in user_ids]

    number_of_crew_members = len(crew_members)
    click.echo(f"Generating badge for {number_of_crew_members} crew members, output path "
               f"{_config.general.output_path}")
    for i, crew in enumerate(crew_members):
        profile_pic = _client.get_picture(crew.profile_image)
        filename = f"{crew.user_id}-{crew.full_name.replace(' ', '')}"
        file_path = os.path.join(_config.general.output_path, filename)

        crew_name = crew.crew.replace("_", ":").replace(" ", ":").replace("::", ":").replace(":", "\n")

        data = {
            "name": crew.first_name,
            "nick": crew.username,
            "crew": crew_name,
            "profile_picture_content": profile_pic,
            "user_id": crew.user_id,
        }

        if REGEX_UUID.match(crew.username):
            click.secho("\tUser has UUID for nick, using first name as nick", fg="yellow")
            data["name"] = ""
            data["nick"] = crew.first_name

        html = render_card(design=design, **data)
        with open(file_path + ".html", "w") as f:
            f.write(html)

        render_to_image(file_path + ".bmp", design, html)

        click.secho(f"{i+1}/{number_of_crew_members} - Generating badge for {crew.full_name}", fg="blue")

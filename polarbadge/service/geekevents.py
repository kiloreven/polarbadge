from base64 import b64encode

import requests
from urllib.parse import urljoin

from requests.auth import HTTPBasicAuth

from polarbadge.models.geekevents import CrewMember, GEConfig, CrewMemberList
from polarbadge.service.config import get_config

_config = get_config()
_CLIENT = None


class GEClient:
    def __init__(self, config: GEConfig):
        self._user = config.username
        self._secret = config.secret
        self._base_url = config.base_url
        self._party_id = config.party_id
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(self._user, self._secret)

    def request(
            self,
            path: str,
            method: str = "GET",
            headers: dict | None = None,
            params: dict | None = None,
            data: dict | None = None
    ) -> requests.Response:

        _headers = headers or {}
        _headers["User-Agent"] = "polarbadge/v0"
        _headers["Content-Type"] = "application/json"

        response = self._session.request(
            method=method,
            url=urljoin(self._base_url, path),
            headers=_headers,
            # params=params,
            # data=data
        )

        response.raise_for_status()
        return response


    def get_crew_members(self) -> CrewMemberList:
        path = f"/event/{self._party_id}/crew/api/crew-list/"
        response = self.request(path).json()
        return CrewMemberList(members=[CrewMember(**item) for item in response.values()])

    def get_picture(self, path: str) -> bytes:
        response = self.request(path)
        return response.content

def get_client():
    config = _config.geekevents
    if not config:
        raise Exception("No GE config")
    return GEClient(config)

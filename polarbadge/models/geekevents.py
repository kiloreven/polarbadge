from pydantic import BaseModel, PositiveInt


class CrewMember(BaseModel):
    user_id: PositiveInt
    username: str
    email: str
    first_name: str
    last_name: str
    phone: str
    address1: str
    address2: str
    postal_code: str
    postal_name: str
    user_card: str
    profile_image: str
    crew: str
    role: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class GEConfig(BaseModel):
    base_url: str
    username: str
    secret: str
    party_id: int

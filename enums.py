from enum import Enum


class RiotApiRegion(Enum):
    AMERICAS = "americas"
    ASIA = "asia"
    EUROPE = "europe"
    SEA = "sea"


class LolQueue(Enum):
    NORMAL_DRAFT = 400
    RANKED_SOLO = 420
    RANKED_FLEX = 440

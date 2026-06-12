import json

from google import genai
from google.genai import types

import cleaner
import enums
from riot_api_client import RiotApiClient


async def run_prompt(
    riot_api_client: RiotApiClient,
    gemini_client: genai.Client,
    in_game_name: str,
    tag_line: str,
    num_matches: int,
    lol_queue: enums.LolQueue,
    prompt: str,
) -> str:
    puuid = await riot_api_client.get_puuid(in_game_name, tag_line)
    match_ids = await riot_api_client.get_match_ids(puuid, num_matches, lol_queue)
    raw_match_data = await riot_api_client.get_raw_match_data_by_ids(match_ids)

    clean_match_data = [
        cleaner.get_clean_match_data(current_data, puuid)
        for current_data in raw_match_data
        if current_data is not None
    ]

    gemini_response = gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a data-driven League of Legends analyst. Answer the prompt from the user "
            + "using only clean sentences with no emojis, lists, bullet points, media, etc. Your reference data is "
            + f"the users's recent League of Legends matches, which can be found here: {json.dumps(clean_match_data)}"
        ),
    )

    return gemini_response.text

import asyncio
import os

from google import genai
from dotenv import load_dotenv

import enums
import processor
from riot_api_client import RiotApiClient


async def main() -> None:
    load_dotenv()
    riot_api_key = os.getenv("RIOT_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    print()
    print("Welcome to Summoner Intelligence!")
    print()
    print(
        "Summoner Intelligence isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc."
    )
    print()

    in_game_name = input("In-game name: ")
    tag_line = input("Tag line: ")
    riot_api_region = enums.RiotApiRegion[
        input("Riot API region (AMERICAS, EUROPE, ASIA, SEA): ").strip().upper()
    ]

    riot_api_client = RiotApiClient(riot_api_key, riot_api_region)
    gemini_client = genai.Client(api_key=gemini_api_key)

    while True:
        print()
        num_matches = int(input("Number of matches to analyze (or 0 to exit): "))

        if num_matches == 0:
            print()
            print("Good luck on the Rift!")
            print()
            break

        lol_queue = enums.LolQueue[
            input("LoL Queue (NORMAL_DRAFT, RANKED_SOLO, RANKED_FLEX): ")
            .strip()
            .upper()
        ]
        prompt = input("Enter whatever you would like to discuss: ")
        print()

        print("Thinking...")

        print()
        print(
            await processor.run_prompt(
                riot_api_client,
                gemini_client,
                in_game_name,
                tag_line,
                num_matches,
                lol_queue,
                prompt,
            )
        )

    await riot_api_client.close()


if __name__ == "__main__":
    asyncio.run(main())

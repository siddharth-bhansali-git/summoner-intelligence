import asyncio

import aiohttp

import enums


class RiotApiClient:
    def __init__(self, api_key: str, api_region: enums.RiotApiRegion) -> None:
        self._http_client: aiohttp.ClientSession = aiohttp.ClientSession(
            base_url=f"https://{api_region.value}.api.riotgames.com/",
            headers={"X-Riot-Token": api_key},
        )

    async def _call_api(self, endpoint: str, params: dict | None = None) -> dict:
        try:
            async with self._http_client.get(url=endpoint, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            if e.code == 429:
                retry_after = int(e.headers.get("Retry-After", 60))
                await asyncio.sleep(retry_after)
                return await self._call_api(endpoint, params)
            else:
                raise

    async def close(self) -> None:
        await self._http_client.close()

    async def get_puuid(self, in_game_name: str, tag_line: str) -> str:
        endpoint = f"riot/account/v1/accounts/by-riot-id/{in_game_name}/{tag_line}"
        response = await self._call_api(endpoint)
        return response["puuid"]

    async def get_match_ids(
        self, puuid: str, num_matches: int, lol_queue: enums.LolQueue
    ) -> list[str]:
        endpoint = f"lol/match/v5/matches/by-puuid/{puuid}/ids"
        params = {"count": num_matches, "queue": lol_queue.value}
        response = await self._call_api(endpoint, params)
        return response

    async def get_raw_match_data_by_id(self, match_id: str) -> dict:
        endpoint = f"lol/match/v5/matches/{match_id}"
        response = await self._call_api(endpoint)
        return response

    async def get_raw_match_data_by_ids(self, match_ids: list[str]) -> list[dict]:
        tasks = [self.get_raw_match_data_by_id(match_id) for match_id in match_ids]
        return await asyncio.gather(*tasks)

# Summoner Intelligence

Summoner Intelligence is a CLI tool that provides LLM-powered League of Legends advice based on your match history.

<details>
<summary>View example usage</summary>

```text
In-game name: [REDACTED]
Tag line: [REDACTED]
Riot API region (AMERICAS, EUROPE, ASIA, SEA): AMERICAS

Number of matches to analyze (or 0 to exit): 20
LoL Queue (NORMAL_DRAFT, RANKED_SOLO, RANKED_FLEX): RANKED_SOLO
Enter whatever you would like to discuss: Give me some actionable tips on how to improve my Sion gameplay.

Thinking...

Based on an analysis of your recent matches, the most critical area of improvement for your Sion gameplay is your farming and wave management. Sion relies heavily on killing minions to stack permanent maximum health through his Soul Furnace passive, but you are currently averaging between four and five and a half minions per minute. This low farm rate prevents you from achieving the massive health pool that makes Sion an unkillable frontline threat, and it also leaves you at a significant gold disadvantage compared to your lane opponents. To fix this, prioritize securing last hits, utilize your Decimating Smash to clear entire waves efficiently, and aim to raise your average creep score to at least seven minions per minute.

Another essential adjustment is reducing your high death count, as you regularly finish matches with seven to nine deaths. While Sion possesses a powerful zombie passive that can salvage a bad trade, over-relying on it often feeds your lane opponent massive amounts of gold and map pressure. Focus on playing more disciplined during the laning phase, particularly when facing duelists and lane bullies like Garen or Tryndamere who can easily snowball the game out of control if given early kills. Staying alive longer will naturally allow you to catch more minion waves, secure more gold, and scale safely into the mid game.

Lastly, you can greatly increase your survivability and lane control by improving your vision and adapting to your specific role. Your vision score per minute frequently dips below zero point five, which makes you an easy target for enemy junglers and roams. Consistently placing stealth wards in high-traffic river bushes and purchasing control wards will provide the safety you need to farm comfortably. Furthermore, when playing Sion in the mid lane, focus on using your high waveclear to shove the lane and secure map priority for your team, whereas in the top lane, prioritize careful wave management to avoid getting frozen out of farm by aggressive melee champions.
```

</details>

## Features

- Queries an exact number of your recent matches in a given queue type
- Uses concurrency + rate limit handling when hitting Riot's API
- Allows you to ask anything and uses a cleaned version of your match data as grounding context
- Uses Gemini 3.5 Flash for insights

## Usage

Make sure you have Python 3.10+ installed. If on Windows, use Windows Subsystem for Linux.

Initial setup:

1. Clone & enter the repository:
    - `git clone https://github.com/siddharth-bhansali-git/summoner-intelligence.git`
    - `cd summoner-intelligence`

2. Configure the following environment variables (`.env` is supported):
    - `RIOT_API_KEY` (for match history retrieval)
    - `GEMINI_API_KEY` (for LLM insights)

3. Run it:
    - `chmod +x run.sh`
    - `./run.sh`

Once you've completed the initial setup, in the future you will only need to do `./run.sh` (assuming you used `.env` or some other kind of persistent storage for your environment variables).

## Disclaimer

Summoner Intelligence isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
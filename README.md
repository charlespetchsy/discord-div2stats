<p align="center">
  <img width="510" src="https://github.com/charlespetchsy/discord-div2stats/blob/master/media/division-discord-banner.png">
</p>

---

## Requirements
- Python version: [`v3.7.x`](https://www.python.org/downloads/release/python-373/)

## Running on your local machine (CLI)
**Assumption**: Discord bot has OAuth2 already setup and Git is installed.
1) Clone the GitHub Repo
    ```
    git clone https://github.com/charlespetchsy/discord-div2stats.git ; cd discord-div2stats/ 
    ```
2) Install dependencies
    ```
    pip3 install -r requirements.txt
    ```
3) Copy and paste your OAuth2 token in the last line of `main.py`
    ```
    ...
    bot.run('<your_OAuth2_token_here>')
    ```
4) Have fun and feel free to modify the code to your desire!

## Basic Usage:
Retrieve general player stats: <br>
**Note**: Player name is character case agnostic.
```
!shd <player_name>
```
Sample Output for `!shd softbunn`:
```
Username: SOFTBUNN
====================
Gear Score: 507  [ Top 2% ]
====================

Lifetime Stats
---------------------------------------------------------
PvP Kills: 7  [ Top 38% ]
NPC Kills: 5,153  [ Top 46% ]
Skill Kills: 351  [ Top 64% ]
Headshots: 20,207  [ Top 23% ]
Items Looted: 2,356  [ Top 28% ]
E-Credit Balance: 473,516  [ Top 5% ]
Commendations: 51  [ Top 27% ]
Sharpshooter (Specialization) Kills: 3,307  [ Top 14% ]
Survivalist (Specialization) Kills: 0  [ None ]
Demolitionist (Specialization) Kills: 0  [ None ]

PvE Stats
---------------------------------------------------------
PvE XP: 21,979,165  [ Top 30% ]
Time Played: 3d 17h 14m  [ Top 37% ]
Named Kills: 75  [ Top 46% ]
Hyena Kills: 1,430  [ Top 49% ]
OutCasts Kills: 1,177  [ Top 44% ]
Truesons Kills: 1,573  [ Top 43% ]
BlackTusk Kills: 871  [ Top 48% ]

PvP Stats
---------------------------------------------------------
PvP XP: 84,227  [ Top 40% ]
Time Played: 1h 53m 48s  [ Top 47% ]
Rogue Time: 03m 08s  [ Top 52% ]
Rogues Killed: 6  [ Top 15% ]
```

Ping Test with `!shd ping`:
```
pong (0 ms)
```

## Command List:
Help Command with `!shd help`:
```
Get player stats: !shd <player_name>
Bot ping test: !shd ping
```

---
Usage of any "The Division" name, logos and/or images are registered trademarks of Ubisoft.

__author__ = "Charles Petchsy"

__license__ = "MIT"
__maintainer__ = "Charles Petchsy"
__status__ = "Alpha"

import requests
import json
import ast
import time
import discord

from discord.ext import commands
from html.parser import HTMLParser


class Lifetime(HTMLParser):
    """ Parse requirements:
    Each entry will include the rank percentile of the player.
    PvP Kills
    NPC Kills
    Skill Kills
    Headshots
    Items Looted
    E-Credit Balance
    Commendations
    Curr Comm. Score
    Sharpshooter Kills
    Survivalist Kills
    Demolitionist Kills
    -> PvE Stats
    -> PvP Stats
    """
    def handle_data(self, data):
        output = """"""
        separator = "\n---------------------------------------------------------\n"
        if 'window.__INITIAL_STATE__' in data:
            player_data = json.loads(
                ast.literal_eval(
                    repr(data.split(';')[0].split('=')[1])
                    )
                )
            root_key = next(iter(player_data['stats']['standardPlayers']))
            # print(root_key) 

            # get player data
            player_name = root_key.split('|')[2]
            output += "Username: " + player_name.upper() + "\n"

            # get gear score
            output += "====================\n" 
            gear_score = player_data['stats']['standardPlayers'][root_key]['stats']['latestGearScore']['displayValue']
            gear_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['latestGearScore']['displayPercentile'])
            output += "Gear Score: " + gear_score + " " + " [ " + gear_rank + " ]"
            output += "\n====================\n\n"

            output += "Lifetime Stats"
            output += separator

            # get pvp kills
            pvp_kills = player_data['stats']['standardPlayers'][root_key]['stats']['killsPvP']['displayValue']
            pvp_rank = player_data['stats']['standardPlayers'][root_key]['stats']['killsPvP']['displayPercentile']
            output += "PvP Kills: " + pvp_kills + " " + " [ " + pvp_rank + " ]" + "\n"

            # get npc kills 
            npc_kills = player_data['stats']['standardPlayers'][root_key]['stats']['killsNpc']['displayValue']
            npc_rank = player_data['stats']['standardPlayers'][root_key]['stats']['killsNpc']['displayPercentile']
            output += "NPC Kills: " + npc_kills + " " + " [ " + npc_rank + " ]" + "\n"

            # get skill kills 
            skill_kills = player_data['stats']['standardPlayers'][root_key]['stats']['killsSkill']['displayValue']
            skill_rank = player_data['stats']['standardPlayers'][root_key]['stats']['killsSkill']['displayPercentile']
            output += "Skill Kills: " + skill_kills + " " + " [ " + skill_rank + " ]" + "\n"

            # get headshot kills 
            headshot_kills = player_data['stats']['standardPlayers'][root_key]['stats']['headshots']['displayValue']
            headshot_rank = player_data['stats']['standardPlayers'][root_key]['stats']['headshots']['displayPercentile']
            output += "Headshots: " + headshot_kills + " " + " [ " + headshot_rank + " ]"  + "\n"

            # get items looted
            items_looted = player_data['stats']['standardPlayers'][root_key]['stats']['itemsLooted']['displayValue']
            items_rank = player_data['stats']['standardPlayers'][root_key]['stats']['itemsLooted']['displayPercentile']
            output += "Items Looted: " + items_looted + " " + " [ " + items_rank + " ]" + "\n"

            # get credit balance 
            credit_balance = str(player_data['stats']['standardPlayers'][root_key]['stats']['eCreditBalance']['displayValue'])
            balance_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['eCreditBalance']['displayPercentile'])
            output += "E-Credit Balance: " + credit_balance + " " + " [ " + balance_rank + " ]" + "\n"

            # get commendations 
            comm_count = str(player_data['stats']['standardPlayers'][root_key]['stats']['commendationCount']['displayValue'])
            comm_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['commendationCount']['displayPercentile'])
            output += "Commendations: " + comm_count + " " + " [ " + comm_rank + " ]" + "\n"

            # get sharpshooter kills
            sharpshooter_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationSharpshooter']['displayValue'])
            sharpshooter_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationSharpshooter']['displayPercentile'])
            output += "Sharpshooter (Spec) Kills: " + sharpshooter_kills + " " + " [ " + sharpshooter_rank + " ]"  + "\n"

            # get sharpshooter kills 
            survivalist_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationSurvivalist']['displayValue'])
            survivalist_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationSurvivalist']['displayPercentile'])
            output += "Survivalist (Spec) Kills: " + survivalist_kills + " " + " [ " + survivalist_rank + " ]"  + "\n"

            # get sharpshooter kills 
            demolitionist_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationDemolitionist']['displayValue'])
            demolitionist_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsSpecializationDemolitionist']['displayPercentile'])
            output += "Demolitionist (Spec) Kills: " + demolitionist_kills + " " + " [ " + demolitionist_rank + " ]" + "\n\n"

            # get PVE stats
            output += "PvE Stats"
            output += separator

            pve_exp = str(player_data['stats']['standardPlayers'][root_key]['stats']['xPPve']['displayValue'])
            pve_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['xPPve']['displayPercentile'])
            output += "PvE XP: " + pve_exp + " " + " [ " + pve_rank + " ]" + "\n"

            time_played = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayed']['displayValue'])
            time_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayed']['displayPercentile'])
            output += "Time Played: " + time_played + " " + " [ " + time_rank + " ]" + "\n"

            named_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsRoleNamed']['displayValue'])
            named_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsRoleNamed']['displayPercentile'])
            output += "Named Kills: " + named_kills + " " + " [ " + named_rank + " ]" + "\n"

            hyena_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionBlackbloc']['displayValue'])
            hyena_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionBlackbloc']['displayPercentile'])
            output += "Hyena Kills: " + hyena_kills + " " + " [ " + hyena_rank + " ]" + "\n"

            outcast_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionCultists']['displayValue'])
            outcast_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionCultists']['displayPercentile'])
            output += "OutCasts Kills: " + outcast_kills + " " + " [ " + outcast_rank + " ]" + "\n"

            truesons_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionMilitia']['displayValue'])
            truesons_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionMilitia']['displayPercentile'])
            output += "Truesons Kills: " + truesons_kills + " " + " [ " + truesons_rank + " ]" + "\n"

            blacktusk_kills = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionEndgame']['displayValue'])
            blacktusk_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['killsFactionEndgame']['displayPercentile'])
            output += "BlackTusk Kills: " + blacktusk_kills + " " + " [ " + blacktusk_rank + " ]" + "\n\n"

            # get PVP stats
            output += "PvP Stats"
            output += separator

            pvp_exp = str(player_data['stats']['standardPlayers'][root_key]['stats']['xPDZ']['displayValue'])
            pvp_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['xPDZ']['displayPercentile'])
            output += "PvP XP: " + pvp_exp + " " + " [ " + pvp_rank + " ]" + "\n"

            dz_time = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayedDarkZone']['displayValue'])
            dz_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayedDarkZone']['displayPercentile'])
            output += "Time Played: " + dz_time + " " + " [ " + dz_rank + " ]" + "\n"

            rogue_time = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayedRogue']['displayValue'])
            rogue_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['timePlayedRogue']['displayPercentile'])
            output += "Rogue Time: " + rogue_time + " " + " [ " + rogue_rank + " ]" + "\n"

            players_killed = str(player_data['stats']['standardPlayers'][root_key]['stats']['roguesKilled']['displayValue'])
            playerKill_rank = str(player_data['stats']['standardPlayers'][root_key]['stats']['roguesKilled']['displayPercentile'])
            output += "Rogues Killed: " + players_killed + " " + " [ " + playerKill_rank + " ]" + "\n"
        
            self.data = output          


bot = commands.Bot(command_prefix='!')

@bot.command()
async def shd(ctx, arg):
    start_time = round(time.time() * 1000)
    if arg.lower() == "help":
        await ctx.channel.send("Get player stats: !shd <player_name>\nBot ping test: !shd ping")
    elif arg.lower() == "ping":
        end_time = round(time.time() * 1000)
        await ctx.channel.send("pong (%s ms)" % str(end_time - start_time))
    else:
        try:
            r = requests.get('https://division.tracker.gg/division-2/profile/uplay/%s/overview' % arg)
            parser = Lifetime()
            parser.feed(str(r.content))
            await ctx.channel.send(parser.data)
        except (TypeError, KeyError):
            await ctx.channel.send("Player does not exist!")


if __name__ == '__main__':
    bot.run('') # Include token here.

   

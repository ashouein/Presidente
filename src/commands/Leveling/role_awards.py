from discord.ext import commands
from discordLevelingSystem import DiscordLevelingSystem, RoleAward, LevelUpAnnouncement

bot = commands.Bot(...)

main_guild_id = 1497426357628698655

my_awards = {
    main_guild_id : [
        RoleAward(role_id=1510619763464732812, level_requirement=1, role_name='Bagong Lipat'),
        RoleAward(role_id=1510620546293829632, level_requirement=5, role_name='Nangungupahan'),
        RoleAward(role_id=1510619752996012132, level_requirement=10, role_name='Suki sa Kanto'),
        RoleAward(role_id=1510620551083855983, level_requirement=20, role_name='Marites ng Barangay'),
        RoleAward(role_id=1510619732066439258, level_requirement=30, role_name='Player sa Liga'),
        RoleAward(role_id=1510620541189623910, level_requirement=40, role_name='May ari ng Sari-Sari Store'),
        RoleAward(role_id=1510619737116115104, level_requirement=50, role_name='Sikat sa Barangay'),
        RoleAward(role_id=1510619760587444404, level_requirement=60, role_name='Legend ng Barangay'),
        RoleAward(role_id=1510619739993538580, level_requirement=70, role_name='May ari ng Sabungan'),
        RoleAward(role_id=1510618496009240699, level_requirement=80, role_name='Tagapagtatag ng Barangay'),
        RoleAward(role_id=1510619755843813526, level_requirement=90, role_name='Buhay na Monumento'),
        RoleAward(role_id=1510618489696686260, level_requirement=100, role_name='Pambansang Bayani'),
    ]
}

announcement = LevelUpAnnouncement(f'{LevelUpAnnouncement.Member.mention} hoy level {LevelUpAnnouncement.LEVEL} ka na, chismis ka pa para may ambag ka naman ! ')

# DiscordLevelingSystem.create_database_file(r'C:\Users\Defxult\Documents') database file already created
lvl = DiscordLevelingSystem(awards=my_awards, level_up_announcement=announcement)
lvl.connect_to_database_file(r'C:\Users\Defxult\Documents\DiscordLevelingSystem.db')

@bot.event
async def on_message(message):
    await lvl.award_xp(amount=15, message=message)

bot.run(...)

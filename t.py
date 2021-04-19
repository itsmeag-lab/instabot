from instabot import Bot
from time import sleep

bot=Bot()
bot.login(username="your username",password="password")
non_followers=set(bot.following)-set(bot.followers)

for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(5)
    except Exception as e:
        print(e)
        sleep(10)
        
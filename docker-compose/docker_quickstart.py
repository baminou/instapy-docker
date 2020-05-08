from instapy import InstaPy
from instapy.util import smart_run
import os

insta_username = os.environ.get('USERNAME')
insta_password = os.environ.get('PASSWORD')
tags = os.environ.get('TAGS').split(',')


bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
with smart_run(bot):
    #bot.set_smart_hashtags(tags, limit=3, sort='top', log_tags=True)
    bot.set_relationship_bounds(enabled=True,
                                potency_ratio=-1.21,
                                delimit_by_numbers=True,
                                max_followers=4590,
                                max_following=5555,
                                min_followers=45,
                                min_following=77)
    bot.like_by_tags(tags, amount=50)
    bot.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    bot.like_by_tags(tags, amount=int(os.environ.get('HOURLY_LIKES')))
    bot.end()

from mongoengine import *
connect('tinyUrlDataBase')


class TinyUrl(Document):
    """
    This class stores all the links given to the website.
    Each object stores a long url, short url, and a unique id given to each object
    """
    long_url = StringField(required=True)
    short_url = StringField(required=True)
    id = IntField(required=True, primary_key=True)

# Guidelines for CRUD with mongoengine
# Create
# example1 = TinyUrl(long_url = "https://www.youtube.com", short_url = "http://uRshort.us/b", id = 1)
#
# example1.save()
#
# Read
# list_of_urls = TinyUrl.objects
# x = list_of_urls[0]
# print(f'Long url:{x.long_url}\n Short Url:{x.short_url}')
#
# Update
# x.long_url = "https://google.com"
#
# Delete
#
# x.delete()

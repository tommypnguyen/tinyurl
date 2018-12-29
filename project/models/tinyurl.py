import json
from project.app import db

URL_TEMPLATE = "http://uRshort.us/"

class TinyUrl(db.Document):
    """
    This class stores all the links given to the website.
    Each object stores a long url, short url, and a unique id given to each object
    """
    long_url = db.StringField(required=True)
    short_url = db.StringField(required=True)
    id = db.IntField(required=True, primary_key=True)

    def return_dict(self) -> dict:
        """
        This function will return dict of the class attributes
        :return: str
        """

        temp_dict = dict()
        temp_dict["long_url"] = self.long_url
        temp_dict["short_url"] = URL_TEMPLATE + self.short_url
        temp_dict["id"] = self.id

        return temp_dict

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

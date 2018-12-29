from flask import request
from flask import abort
from flask import Blueprint
from flask import redirect
from project.models import TinyUrl
from project.models import Short
import json


tinyurl_api_bp = Blueprint("tinyurl_api", "tinyurl_api")


@tinyurl_api_bp.route('/url/<id>', methods=["GET"])
def redirect_user(id):
    if request.method != "GET":
        abort(400)

    id = "http://www.uRshort.us/" + id
    url = Short.convert_short_to_large(id)
    if url:
        return redirect(url)
    else:
        return "Does not exist"


@tinyurl_api_bp.route('/url', methods=["POST"])
def create_url():
    if request.method != "POST":
        abort(400)

    json_object = request.get_json()

    long_url = json_object["longurl"]

    tiny_url_obj = Short.convert_large_to_short(long_url)

    return json.dumps(tiny_url_obj)
    #
    # long = "https://facebook.com"
    # urlObject = Short()
    # example1 = TinyUrl(long_url = long, short_url = urlObject.convert_large_to_short(long), id = urlObject.count)
    # example1.save()
    # list_of_urls = TinyUrl.objects
    # x = list_of_urls[0]
    # response = dict()
    # response = {
    #     "Long_url": x.long_url,
    #     "short_url": x.short_url,
    #     "id ": x.id
    # }
    # print(f'Long url:{x.long_url}\n Short Url:{x.short_url}')
    # return json.dumps(response)

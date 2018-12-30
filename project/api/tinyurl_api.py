from flask import request
from flask import abort
from flask import Blueprint
from flask import redirect
from project.models import Short
import json


tinyurl_api_bp = Blueprint("tinyurl_api", "tinyurl_api")


@tinyurl_api_bp.route('/<url_id>', methods=["GET"])
def redirect_user(url_id):
    """
    This route will take the url_id and redirect the user to the correct large url
    :param url_id:
    :return: str
    """
    if request.method != "GET":
        abort(400)

    url = Short.convert_short_to_large(url_id)
    if url:
        return redirect(url)
    else:
        return f'Does not exist:{url_id}'


@tinyurl_api_bp.route('/url', methods=["POST"])
def create_url():
    """
    This route will take the users input and create a TinyUrl object of the input
    :return: json
    """
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

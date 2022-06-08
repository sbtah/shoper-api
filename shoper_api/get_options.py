import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# GET https://shop.url/webapi/rest/options
def get_all_options():
    """Return a paginated response with all options in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/options"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res


def get_single_option(option_id):
    """Return a paginated response with all collections in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/options/{option_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res

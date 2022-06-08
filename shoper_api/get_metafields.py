import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# GET https://shop.url/webapi/rest/metafield-values
def get_all_metafields():
    """Return a paginated response with all options in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/metafield-values"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res

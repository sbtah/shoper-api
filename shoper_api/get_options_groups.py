import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# GET https://shop.url/webapi/rest/option-groups
def get_all_options_groups():
    """Return a paginated response with all options groups in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/option-groups"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res

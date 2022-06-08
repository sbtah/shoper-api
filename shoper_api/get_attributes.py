import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# https://shop.url/webapi/rest/attributes
def get_all_attributes():
    """Return a paginated response with all attributes in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/attributes"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res

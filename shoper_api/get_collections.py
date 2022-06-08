import time
import requests
from shoper_api.token import get_token
from shoper_api.token import SHOPER_STORE


TOKEN = get_token()


# https://shop.url/webapi/rest/collections
def get_all_collections():
    """Return a paginated response with all collections in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/collections"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res


def get_single_collection(collection_id):
    """Return a paginated response with all collections in Shoper store."""

    url = f"https://{SHOPER_STORE}/webapi/rest/collections/{collection_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res


# GET https://shop.url/webapi/rest/collections/<collection_id>/products
def get_all_products_for_collection(collection_id):

    url = f"https://{SHOPER_STORE}/webapi/rest/collections/{collection_id}/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    time.sleep(0.5)

    return res

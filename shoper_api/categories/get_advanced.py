import time
import requests
from shoper_api.helpers.get_token import SHOPER_DOMAIN, TOKEN
from shoper_api.helpers.logging import logging


def get_single_category_data(cat_id):
    """
    Sends GET request to Shoper's category API endpoint that returns data for single category.
    Properly selects and cleans data from reponse and stores it the variables.
    Variables are used in dictionary that is returned by this function.
    Used for generating copy data for duplication of category via Shoper API.
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories/{cat_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.3)
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(get_single_product_data) Exception: {e}")
    else:
        i = response.json()

        category_id = i.get("category_id")
        root = i.get("root")
        order = i.get("order")
        translations = i.get("translations")

        return {
            "shoper_id": category_id,
            "root": root,
            "order": order,
            "shoper_category_translations": translations,
        }


def from_response_category(response):
    """
    Parses Category response data.
    Stores data in proper variables and returns dictionary of needed data for Category.
    """
    category_id = response.get("category_id")
    root = response.get("root")
    order = response.get("order")
    translations = response.get("translations")

    return {
        "category_id": category_id,
        "root": root,
        "order": order,
        "translations": translations,
    }


def from_response_translations_for_category(response):
    """
    Given the part of response from get_single_category_data,
    Yield data for all translations for this Category.

    Used to seperate logic of creating Categories and Translations.
    """

    try:
        for translation in response.items():
            print(translation[0])
            # locale = translation
            # shoper_translation_id = translation.get("trans_id")
            # related_category_id = translation.get("category_id")
            # name = translation.get("name")
            # description = translation.get("description")
            # description_bottom = translation.get("description_bottom")
            # seo_title = translation.get("seo_title")
            # seo_description = translation.get("seo_description")
            # seo_keywords = translation.get("seo_keywords")
            # seo_url = translation.get("seo_url")
            # permalink = translation.get("permalink")
            # active = translation.get("active")
            # is_default = translation.get("is_default")
            # lang_id = translation.get("lang_id")
            # items = translation.get("items")
        yield {
            # "locale": locale,
            # "shoper_translation_id": shoper_translation_id,
            # "related_category_id": related_category_id,
            # "name": name,
            # "description": description,
            # "description_bottom": description_bottom,
            # "seo_title": seo_title,
            # "seo_description": seo_description,
            # "seo_keywords": seo_keywords,
            # "seo_url": seo_url,
            # "permalink": permalink,
            # "active": active,
            # "is_default": is_default,
            # "lang_id": lang_id,
            # "items": items,
        }
    except Exception as e:
        logging.error(f"Error while getting response: {e}")

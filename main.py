from gettext import translation
from shoper_api.products.get_basic import (
    get_number_of_products,
    get_number_of_product_pages,
    get_single_product,
    get_all_products,
)
from shoper_api.products.get_medium import (
    get_all_products_data,
    get_all_shoper_product_ids,
    get_all_shoper_product_skus,
)
from shoper_api.products.get_advanced import (
    get_all_shoper_product_ids_for_lang,
    get_all_shoper_product_skus_for_lang,
    get_single_product_data,
    from_response_translations_for_product,
)
from shoper_api.categories.get_basic import (
    get_number_of_categories_pages,
    get_number_of_categories,
)
from shoper_api.categories.get_medium import (
    get_all_category_data,
    get_all_shoper_categories_ids,
)
from shoper_api.categories.get_advanced import (
    get_single_category_data,
    from_response_translations_for_category,
)

if __name__ == "__main__":

    ### TODO:
    ### TASK : Get all categories and translation data from list of IDS.
    ### THIS can be used on list responded from an API or generated from DB.
    ### LONG DISCOVERY TASK : List of IDs is a response from API
    ### SHORTER VALIDATION TASK : List of IDs is a response from local db Category table.
    categories_ids = get_all_shoper_categories_ids()
    for cat_id in categories_ids:
        category = get_single_category_data(cat_id)
        print(category)
        translations = from_response_translations_for_category(
            response=category["shoper_category_translations"]
        )
        for trans in translations:
            print(trans)
    # ### TODO:
    # ### TASK : Visit single product by ID and get update for it and all translations.
    # ### Use builder create_or_update Product in db with data responded in product_datas.
    # # print(get_single_product(122))
    # product_data = get_single_product_data(122)
    # # product = create_or_update(id=product_data["shoper_id"]....)
    # # print(
    # translations = from_response_translations_for_product(
    #     response=product_data["shoper_product_translations"]
    # )
    # for trans in translations:
    #     # trans = create_or_update_translation(shoper_translation_id=trans["shoper_translation_id"])
    #     print(trans["active"])

    ### TODO:
    ### TASK : Get all products and translation data from list of IDS.
    ### THIS can be used on list responded from an API or generated from DB.
    ### LONG DISCOVERY TASK : List of IDs is a response from API
    ### SHORTER VALIDATION TASK : List of IDs is a response from local db Products table.
    # product_ids = get_all_shoper_product_ids()
    # for product_id in product_ids:
    #     product = get_single_product_data(product_id)
    #     translations = from_response_translations_for_product(
    #         response=product["shoper_product_translations"]
    #     )
    #     for trans in translations:
    #         print(trans)

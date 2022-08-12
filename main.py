from gettext import translation
from apiclient.products.get_basic import (
    get_number_of_products,
    get_number_of_product_pages,
    get_single_product,
    get_all_products,
)
from apiclient.products.get_medium import (
    get_all_products_data,
    get_all_shoper_product_ids,
    get_all_shoper_product_skus,
)
from apiclient.products.get_advanced import (
    get_all_shoper_product_ids_for_lang,
    get_all_shoper_product_skus_for_lang,
    get_single_product_data,
    from_response_product,
    from_response_translations_for_product,
    from_response_stock_for_product,
)
from apiclient.categories.get_basic import (
    get_number_of_categories_pages,
    get_number_of_categories,
)
from apiclient.categories.get_medium import (
    get_all_categories_data,
    get_all_shoper_categories_ids,
)
from apiclient.categories.get_advanced import (
    get_single_category_data,
    from_response_translations_for_category,
    from_response_category,
)

if __name__ == "__main__":
    # ### TODO:
    # ## Get all categories and translations.
    # for data in get_all_categories_data():
    #     # print(data)
    #     category = from_response_category(response=data)
    #     # print(category)
    #     translations = from_response_translations_for_category(
    #         response=category["translations"]
    #     )
    #     for trans in translations:
    #         print(trans)
    ### TODO:
    ### TASK : Get all categories and translation data from list of IDS.
    ### THIS can be used on list responded from an API or generated from DB.
    ### LONG DISCOVERY TASK : List of IDs is a response from API
    ### SHORTER VALIDATION TASK : List of IDs is a response from local db Category table.
    # categories_ids = get_all_shoper_categories_ids()
    # for cat_id in categories_ids:
    #     category = get_single_category_data(cat_id)
    #     print(category)
    #     translations = from_response_translations_for_category(
    #         response=category["shoper_category_translations"]
    #     )
    #     for trans in translations:
    #         print(trans)

    # ### TODO:
    # ### TASK : Visit single product by ID and get update for it and all translations.
    # ### Use builder create_or_update Product in db with data responded in product_datas.
    # print(get_single_product(122))
    # product_data = get_single_product_data(122)
    # # product = create_or_update(id=product_data["shoper_id"]....)
    # # print(product_data)
    # stock = from_response_stock_for_product(
    #     response=product_data["shoper_product_stock"]
    # )
    # print(stock)
    # translations = from_response_translations_for_product(
    #     response=product_data["shoper_product_translations"]
    # )
    # for trans in translations:
    #     # trans = create_or_update_translation(shoper_translation_id=trans["shoper_translation_id"])
    #     print(trans["active"])

    ## TODO:
    ## TASK : Get all products and translation data from list of IDS.
    ## THIS can be used on list responded from an API or generated from DB.
    ## LONG DISCOVERY TASK : List of IDs is a response from API
    ## SHORTER VALIDATION TASK : List of IDs is a response from local db Products table.
    # product_ids = get_all_shoper_product_ids()
    # for product_id in product_ids:
    #     product = get_single_product_data(product_id)
    #     translations = from_response_translations_for_product(
    #         response=product["shoper_product_translations"]
    #     )
    #     for trans in translations:
    #         print(trans["locale"])

    ### TODO:
    ### Working products fetch task.
    # products_data = get_all_products_data()
    # for prod in products_data:
    #     product = from_response_product(
    #         response=prod,
    #     )
    #     print(product["shoper_id"])
    #     translations = from_response_translations_for_product(
    #         response=product["shoper_product_translations"],
    #     )
    #     # # print(translations)
    #     for trans in translations:
    #         print(trans["locale"])

    # ### TODO:
    # ### Working categories fetch task.
    # category_data = get_all_categories_data()
    # for cat in category_data:
    #     # print(cat)
    #     print("=======================================")
    #     print(cat["category_id"])
    #     category = from_response_category(
    #         response=cat,
    #     )
    #     # print(category["category_translations"])

    #     translations = from_response_translations_for_category(
    #         response=category["category_translations"],
    #     )

    #     for x in translations:
    #         print(x)

    print(get_single_category_data(84))

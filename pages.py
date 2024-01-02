page_url_template = 'https://spb.vkusvill.ru/goods/{}/?PAGEN_1={}'
categories = [
    "zamorozhennye-produkty",
    "sladosti-i-deserty",
    "gotovaya-eda",
    "orekhi-chipsy-i-sneki",
    "myaso-ptitsa",
    "molochnye-produkty-yaytso",
    "kolbasy-i-myasnye-delikatesy",
    "khleb-i-vypechka",
    "ovoshchi-frukty-yagody-zelen",
    "syry",
    "vegetarianskoe-i-postnoe",

]

def generate_page_for_category(category, page_number):
    return page_url_template.format(category, str(page_number))


from selenium import webdriver
import chromedriver_autoinstaller
import pages
# import csv
import json
import re

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1920, 1080)
proteins_regexp = "белки *\d+[.,]?\d* *"
fats_regexp = "жиры *\d+[.,]?\d* *"
carbs_regexp = "углеводы *\d+[.,]?\d* *"
calories_regexp = "\d+[.,]?\d* *ккал"

def number_helper(input):
    s = "".join(c for c in input if c.isdigit() or "." in c or "," in c)
    s = s.replace(",",".")
    return float(s)

for category in pages.categories:
    goods = []
    page_number = 1
    while True:
        # if page_number > 1:
        #     break
        page_url = pages.generate_page_for_category(category, page_number)
        driver.get(page_url)
        items = driver.find_elements_by_class_name('ProductCard__link')
        if not items:
            break
        hrefs = [item.get_attribute('href') for item in items]
        page_number += 1

        for href in hrefs:
            driver.get(href)
            nutritional_value_selector = "//*[contains(text(), 'ккал')]"
            if not driver.find_elements_by_xpath(nutritional_value_selector):
                print ("No Nutritional value provided")
                continue
            name = driver.find_element_by_class_name('Product__title')
            # innerText returns even hidden by CSS text. The text is hidden on low resolutions.
            nutritional_value = driver.find_element_by_xpath(nutritional_value_selector).get_attribute("innerText")
            try:
                proteins = number_helper(re.search(proteins_regexp, nutritional_value).group(0))
                fats = number_helper(re.search(fats_regexp, nutritional_value).group(0))
                carbs = number_helper(re.search(carbs_regexp, nutritional_value).group(0))
                calories = number_helper(re.search(calories_regexp, nutritional_value).group(0))

                # proteins = int(
                #     ''.join(c for c in nutritional_value.split('белки')[1].split('г')[0].split(',')[0] if c.isdigit()))
                # fats = int(
                #     ''.join(c for c in nutritional_value.split('жиры')[1].split('г')[0].split(',')[0] if c.isdigit()))
                # carbs = int(
                #     ''.join(c for c in nutritional_value.split('углеводы')[1].split('г')[0].split(',')[0] if c.isdigit()))
                # calories = int(
                #     ''.join(c for c in nutritional_value.split('ккал')[0].split(';')[-1].split(',')[0] if c.isdigit()))
                price = int(''.join(c for c in driver.find_element_by_class_name('Price__value').get_attribute("innerText").split('.')[0].split(',')[0] if c.isdigit()))
            except:
                print ("Invalid good")
                continue
            # driver.back()
            goods.append({
                'name': name.text,
                'proteins': proteins,
                'fats': fats,
                'carbs': carbs,
                "calories": calories,
                "price": price,
                'href': href,
            })
    with open('{}.json'.format(category), 'w', encoding='utf-8') as f:
        json.dump(goods, f, ensure_ascii=False)


# goods_sorted = sorted(goods, key=lambda d: d['carbs'])
# print(goods_sorted)
# with open('out.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name', 'Proteins', 'Fats', 'Carbs', 'Calories', 'Href'])
#     for item in goods_sorted:
#         writer.writerow([item["name"].replace(",",""), item["proteins"], item["fats"], item["carbs"], item["calories"], item["href"]])
#         # f.write("%s\n" % item)

import requests
def save_image(url):
    f = open('Flipkart.jpg','wb')
    f.write(requests.get(url).content)
    f.close()
    return 'Flipkart.jpg'

def get_data(url,driver):
    driver.get(url)
    ## For Amazon

    try:
        ## Get Name of Product
        name_path=driver.find_element_by_class_name('_35KyD6')
        product_name = name_path.text
    except:
        product_name = 'Not found'

    ## Get Image Url
    try:
        img_path = driver.find_element_by_class_name('_1Nyybr.Yun65Y.OGBF1g._30XEf0')
        img_url = img_path.get_attribute('src')
        # product_image = save_image(img_url)
        product_image = img_url
    except:
        product_image = 'https://image.shutterstock.com/image-vector/no-image-available-vector-illustration-600w-744886198.jpg'

    ### Get Product Price
    try:
        price_path = driver.find_element_by_class_name('_1vC4OE._3qQ9m1')
        product_price = price_path.text
        product_price = product_price.replace('₹','')
        product_price = product_price.replace(',','')
        product_price = product_price.replace(' ','')
    except:
        product_price = 'Not Found'
    ### Get Product Rating

    try:
        rating_path = driver.find_element_by_class_name('hGSR34')
        product_rating = rating_path.get_attribute("innerHTML")
        product_rating = product_rating[:3]
    except:
        product_rating = 'Not Found'

    return product_name, product_image, product_price, product_rating

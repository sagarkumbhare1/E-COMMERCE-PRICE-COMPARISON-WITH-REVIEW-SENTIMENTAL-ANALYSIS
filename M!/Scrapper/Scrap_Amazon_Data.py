import requests
def save_image(url):
    f = open('Amazon.jpg','wb')
    f.write(requests.get(url).content)
    f.close()
    return 'Amazon.jpg'

def get_data(url,driver):
    driver.get(url)
    ## For Amazon

    try:
        ## Get Name of Product
        name_path=driver.find_element_by_class_name('a-size-large')
        product_name = name_path.text
    except:
        product_name='Not Found'

    try:
        ## Get Image Url
        img_path = driver.find_element_by_id('landingImage')
        img_url = img_path.get_attribute('src')
        # product_image = save_image(img_url)
        product_image = img_url
    except:
        product_image = 'https://image.shutterstock.com/image-vector/no-image-available-vector-illustration-600w-744886198.jpg'

    try:
        ### Get Product Price
        price_path = driver.find_element_by_class_name('a-size-medium.a-color-price')
        product_price = price_path.text
        if product_price =='Currently unavailable.':
            product_price = 'Not Found'
        else:
            product_price = product_price.replace('₹','')
            product_price = product_price.replace(',','')
            product_price = product_price.replace(' ','')

    except:
        product_price = 'Not Found'

    try:
        ### Get Product Rating
        rating_path = driver.find_element_by_class_name('a-icon-alt')
        product_rating = rating_path.get_attribute("innerHTML")
        product_rating = product_rating[:3]
    except:
        product_rating = 'Not Found'


    ## Review Source
    review_code = driver.page_source
    return product_name, product_image, product_price, product_rating, review_code



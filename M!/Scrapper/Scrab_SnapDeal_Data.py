import requests
def save_image(url):
    f = open('SnapDeal.jpg','wb')
    f.write(requests.get(url).content)
    f.close()
    return 'SnapDeal.jpg'

def get_data(url,driver):
    driver.get(url)
    ## For Amazon

    try:
        ## Get Name of Product
        name_path=driver.find_element_by_class_name('pdp-e-i-head')
        product_name = name_path.text
    except:
        product_name = 'Not Found'

    try:
        ## Get Image Url
        img_path = driver.find_element_by_class_name('cloudzoom')
        img_url = img_path.get_attribute('src')
        # product_image = save_image(img_url)
        product_image = img_url
    except:
        product_image = 'https://image.shutterstock.com/image-vector/no-image-available-vector-illustration-600w-744886198.jpg'

    try:
        ### Get Product Price
        price_path = driver.find_element_by_class_name('payBlkBig')
        product_price = price_path.text
        product_price = product_price.replace('₹','')
        product_price = product_price.replace(',','')
    except:
        product_price = 'Not Found'

    try:
        ### Get Product Rating
        rating_path = driver.find_element_by_class_name('avrg-rating')
        product_rating = rating_path.text
        product_rating=product_rating.replace('(','')
        product_rating=product_rating.replace(')','')
    except:
        product_rating = 'Not Found'
    return product_name, product_image, product_price, product_rating




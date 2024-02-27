import Scrapper.Scrap_Review as All_Reviews
import Scrapper.Scrap_Amazon_Data as Amazon
import Scrapper.Scrab_Flipkart_Data as Flipkart
import Scrapper.Scrab_SnapDeal_Data as SnapDeal

# import Scrap_Review as All_Reviews
# import Scrap_Amazon_Data as Amazon
# import Scrab_Flipkart_Data as Flipkart
# import Scrab_SnapDeal_Data as SnapDeal


def start_scrabing_data(amazon_url,flipkart_url,snapdeal_url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")
    # driver = webdriver.Chrome(executable_path='driver.exe',,options=options)
    driver = webdriver.Chrome(executable_path='Scrapper/driver.exe')

    amazon_result = 'Good to buy Product from this Site'
    flipkart_result = 'Good to buy Product from this Site'
    snapdeal_result = 'Good to buy Product from this Site'

    amazon_product_name, amazon_product_image, amazon_product_price, amazon_product_rating, review_code = Amazon.get_data(amazon_url,driver)
    print('Amazon Data scrapped')
    flipkart_product_name, flipkart_product_image, flipkart_product_price, flipkart_product_rating = Flipkart.get_data(flipkart_url,driver)
    print('Flipkart Data scrapped')
    snapdeal_product_name, snapdeal_product_image, snapdeal_product_price, snapdeal_product_rating = 'Not Found','Not Found','Not Found','Not Found'
    # SnapDeal.get_data(snapdeal_url,driver)
    print('Snapdeal Data scrapped')


    ################# ALL Revies Scapping
    all_reviews_result = All_Reviews.scrab_reviews(amazon_url,review_code)
    print('All reviews scrapped')

    ################################################################################
    def get_maximum_price():
        ## Stores all price in list
        price_list = []
        if amazon_product_price!='Not Found':
            price_list.append(int(float(amazon_product_price)))
        if flipkart_product_price!='Not Found':
            price_list.append(int(float(flipkart_product_price)))
        if snapdeal_product_price!='Not Found':
            price_list.append(int(float(snapdeal_product_price)))

        ## Find Highest price
        price_list.sort()
        maximum_price = str(price_list[len(price_list)-1])

        ## Get site Name
        if maximum_price==amazon_product_price:
            maximum_price_site = 'Amazon'
        elif maximum_price==flipkart_product_price:
            maximum_price_site = 'Flipkart'
        elif maximum_price==snapdeal_product_price:
            maximum_price_site = 'Snapdeal'

        return maximum_price,maximum_price_site

    ##################################################################################
    def get_smallest_rating():
        ### Store all rating into list
        rating_list = []
        if amazon_product_rating!='Not Found':# or amazon_product_rating!='Currently unavailable.':
            rating_list.append(float(amazon_product_rating))
        if flipkart_product_rating!='Not Found':
            rating_list.append(float(flipkart_product_rating))
        if snapdeal_product_rating!='Not Found':
            rating_list.append(float(snapdeal_product_rating))

        ## Sort the rating list
        rating_list.sort()
        smallest_rating = str(rating_list[0])

        ## Get site name of smallest rating
        if smallest_rating==amazon_product_rating:
            smallest_rating_site = 'Amazon'
        elif smallest_rating==flipkart_product_rating:
            smallest_rating_site = 'Flipkart'
        elif smallest_rating==snapdeal_product_rating:
            smallest_rating_site = 'Snapdeal'
        return smallest_rating,smallest_rating_site

    print('Amazon : ',amazon_product_name, amazon_product_image, amazon_product_price, amazon_product_rating )
    print('Flipkart : ',flipkart_product_name, flipkart_product_image, flipkart_product_price, flipkart_product_rating)
    print('SnapDeal : ',snapdeal_product_name, snapdeal_product_image, snapdeal_product_price, snapdeal_product_rating )

    maximum_price,maximum_price_site = get_maximum_price()
    smallest_rating,smallest_rating_site= get_smallest_rating()
    print(maximum_price,maximum_price_site)
    print(smallest_rating,smallest_rating_site)

    if maximum_price_site==smallest_rating_site:
        if float(smallest_rating)<=3.9:
            if maximum_price_site == 'Amazon':
                amazon_result = 'Bad to buy Product from this Site'
            elif maximum_price_site == 'Flipkart':
                flipkart_result = 'Bad to buy Product from this Site'
            elif maximum_price_site == 'Snapdeal':
                snapdeal_result = 'Bad to buy Product from this Site'

    if amazon_product_rating!='Not Found':
        if float(amazon_product_rating)<=3.4:
            amazon_result = 'Bad to buy Product from this Site'
    if flipkart_product_rating!='Not Found':
        if float(flipkart_product_rating)<=3.4:
            flipkart_result = 'Bad to buy Product from this Site'
    if snapdeal_product_rating!='Not Found':
        if float(snapdeal_product_rating)<=3.4:
            snapdeal_result = 'Bad to buy Product from this Site'

    if amazon_product_price=='Not Found' and amazon_product_rating=='Not Found':
        amazon_result = 'Reviews Data Not Found'
    elif flipkart_product_price=='Not Found' and flipkart_product_rating=='Not Found':
        flipkart_result = 'Reviews Data Not Found'
    elif snapdeal_product_price=='Not Found' and snapdeal_product_rating=='Not Found':
        snapdeal_result = 'Reviews Data Not Found'


    print(amazon_result)
    print(flipkart_result)
    print(snapdeal_result)
    print(all_reviews_result)

    return amazon_product_image, amazon_product_price, amazon_product_rating , flipkart_product_image, flipkart_product_price, flipkart_product_rating , snapdeal_product_image, snapdeal_product_price, snapdeal_product_rating ,amazon_result,flipkart_result,snapdeal_result




# start_scrabing_data('https://www.amazon.in/Realme-Aurora-Green-128GB-Storage/dp/B09SVBLJBY/ref=sr_1_2?adgrpid=62131588963&ext_vrnc=hi&gclid=Cj0KCQjwgYSTBhDKARIsAB8KuksiTXMOk8uIfOIx6wpGw5s-kYmc0s_7qxEhBklv1VSMYCPqBCqDVm0aAsgYEALw_wcB&hvadid=398059833988&hvdev=c&hvlocphy=1007786&hvnetw=g&hvqmt=e&hvrand=10769818335617936967&hvtargid=kwd-1098179357425&hydadcr=24565_1971419&keywords=realme%2B9%2Bpro%2Bmodel&qid=1650561441&sr=8-2&th=1',
#     'https://www.flipkart.com/realme-9-pro-5g-midnight-black-128-gb/p/itmce357e4a0ca24',
#     'https://www.snapdeal.com/product/sleek-qc10-for-android-apple/5764608164219374704#bcrumbSearch:jbl%20bluetooth%20headphone')
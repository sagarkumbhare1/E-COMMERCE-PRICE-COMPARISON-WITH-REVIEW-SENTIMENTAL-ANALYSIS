from bs4 import BeautifulSoup
import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome
import random
from difflib import SequenceMatcher



def checkProductNameSimilarirty(Product_Search, E_Commerse_Name):

    product_words =  Product_Search.split(' ')
    total_words = int(len(product_words) * 0.6)

    result = False
    
    words_exists_count = 0
    
    try:
        for word in product_words:
            if word.lower() in E_Commerse_Name.lower().split(' '):
                words_exists_count +=1
        
            if words_exists_count >= total_words:
                result = True
                break
        
    except Exception as e:
        result = False
        print(e) 
    
    return result


def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

search_quereies = []

Snapdeal_Names = []
Snapdeal_Prices = []
Snapdeal_imagelinks = []
Snapdeal_Prices_2 = []
Snapdeal_Ratings = []

Flipkart_Names = []
Flipkart_Prices = []
Flipkart_Prices_2 = []
Flipkart_ImageLinks = []
Flipkart_Ratings = []
Flipkart_Reviews = []


Amazon_Names = []
Amazon_Prices = []
Amazon_Prices_2 = []
Amazon_ImageLinks = []
Amazon_Ratings = []
Amazon_Reviews = []



Relience_Names = []
Relience_Prices = []
Relience_Prices_2 = []
Relience_ImageLinks = []
Relience_Ratings = []
 
Amazon_URL = ''
Flipkart_URL = ''
Relience_URL = ''
Snapdeal_URL = ''


def cleanPrice(price:str):
    try:
        return int(price.lower().replace(',','').replace('₹','').replace('rs',''))
    except: return price

def cleanRating(rating:str):
    try:
        if 'out' in rating:
            return float(rating.split(' out')[0])
        if 'ratings' in rating.lower():
            return float(rating.lower().split('ratings')[0].strip())

        return float(rating)
    except: return rating


def cleanReviews(reviews:str):
    try:
        if 'reviews' in reviews.lower():
            return int(reviews.lower().replace(',','').replace('reviews','').strip())
        if 'ratings' in reviews.lower():
            return int(reviews.lower().split('ratings')[0].strip())
    except: return reviews


time_variable = random.uniform(0,0)

def Integrated(Product_search):

    Amazon_Products = []
    Flipkart_Products = []
    Relience_Products = []
    Snapdeal_Products = []

    def Amazon():
        time.sleep(time_variable)
        URL = "https://www.amazon.in/s?k=" + str(Product_search) + "&ref=nb_sb_noss_2"
        Amazon_URL = URL
        headers = {
            'authority': 'www.amazon.in',
            'cache-control': 'max-age=0',
            'rtt': '50',
            'downlink': '10',
            'ect': '4g',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://www.amazon.in/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,nl;q=0.7',
            'cookie': 'session-id=258-1636592-3456905; i18n-prefs=INR; ubid-acbin=257-5529898-5487600; x-wl-uid=1ir5E8+OGhMOBpYNk5vAaB/JiH6qK69EwafO54hquG79/1zQlrhpNsM5nmNrkgP7e/m69DA9SWNY=; lc-acbin=en_IN; session-token=RNXDMxPntpb6YB4qLb/SPv+B2D0zCLft5u0EuG4qsBl5C7QyxS8Vu28Sm2iu9j1LS73JtkQsBpHnu6bYxStohPe6gNbEvpgHsJ7m8ld188mgFVDm8Wtjri7Iaq9R5TvjF4zgFmwEP21zD9hf8zmSmODV/8yDxYZ5lTS5McKbQossGXMLNLHZxSopMuq3jN4A; visitCount=28; session-id-time=2082758401l; csm-hit=tb:s-D9EHD2TB6FW1FS29NDVB|1577817064939&t:1577817066038&adb:adblk_yes',
        }
        time.sleep(time_variable)

        print(URL)

        try:
            recieve = requests.get(URL, headers=headers, timeout=10)
        except:
            "One or more of the websites are unresponsive, please retry later."
            exit()

        soup = BeautifulSoup(recieve.content, 'html.parser')


        def scrape():
            time.sleep(time_variable)
            outlines = soup.findAll("div", {"class": "s-card-container"})
            print(len(outlines)) 
            for x in range(len(outlines)):
                try:
                    outline = outlines[x]
                    identify = outline.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
                    name = identify.text
                    print('Amazon',name,checkProductNameSimilarirty(Product_search,name))

                    if checkProductNameSimilarirty(Product_search,name):

                        identify = outline.find("span", {"class": "a-price-whole"})
                        price = identify.text
    
                        identify = outline.find("img", {"class": "s-image"})
                        image_link = identify['src']

                        rev = outline.find("span",{"class":"a-size-base s-underline-text"})
                        rat = outline.find("span", {"class": "a-icon-alt"})


                        data  = {
                            'Product_Name':name,
                            'Product_Price':price,
                            'Product_Rating':rat.text,
                            'Product_Reviews':rev.text,
                            'Product_ImageLink':image_link
                        }

                        # print(data)

                        Amazon_Products.append(data)


                except Exception as e:
                    print(e)

                else:pass



            if len(Flipkart_Names) is 0:
                outlines_2 = soup.findAll("div", {"class": "_4ddWXP"})

                for y in range(len(outlines_2)):
                    outline_2 = outlines_2[y]
                    identify_2 = outline_2.find("a", {"class": "s1Q9rs"})
                    name_2 = identify_2.text
                    Flipkart_Names.append(name_2)
            else:
                pass

            print(Amazon_Names)

        scrape()

    def Snapdeal():
        print("https://www.snapdeal.com/search?keyword=" + str(Product_search) + "&sort=plrty")
        try:
            retrieve = requests.get(
                        "https://www.snapdeal.com/search?keyword=" + str(Product_search) + "&sort=plrty", timeout=2)
        except:
            "One or more of the websites are unresponsive, please retry later."
            exit()

        retrieve = retrieve.text

        soup = BeautifulSoup(retrieve, 'lxml')

        def scrape():
            time.sleep(time_variable)
            outlines = soup.findAll("div", {"class": "product-tuple-listing"})
            print(len(outlines))

            for x in range(len(outlines)):
                outline = outlines[x]
                identify = outline.find("p", {"class": "product-title"})
                name = identify.text
                print(name)

                if checkProductNameSimilarirty(Product_search,name):

                    try:


                        identify = outline.find("span", {"class": "product-price"})
                        price = identify.text

                        identify = outline.find("picture", {"class": "picture-elem"})
                        image = identify.find("img")
                        image_link = image['data-src']

                        rev = outline.find("p",{"class":"product-rating-count"})
                        if rev==None:
                            rev = 'No Review'
                        else:
                            rev = rev.text
                        
                        
                        data  = {
                            'Product_Name':name,
                            'Product_Price':price,
                            'Product_Rating':random.randint(1,5),
                            'Product_Reviews':rev,
                            'Product_ImageLink':image_link
                        }

                        # print(data)
                        Snapdeal_Products.append(data)


                    except Exception as e:
                        print(e,'\n')

                else:pass

        scrape()

    def Flipkart():
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,nl;q=0.7',
        }

        URL = "https://www.flipkart.com/search?q=" + str(
            Product_search) + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

        print(URL)

        try:
            recieve = requests.get(URL, headers=headers)
            recieve = recieve.text

        except:
            options = Options_Chrome()
            options.headless = True
            browser = webdriver.Chrome(options=options)
            browser.get(URL)
            time.sleep(60)
            recieve = browser.page_source
            browser.close()

        soup = BeautifulSoup(recieve, 'lxml')

        def scrape():
            time.sleep(time_variable)
            outlines = soup.findAll("div", {"class": "_2kHMtA"})
                    
            for x in range(len(outlines)):
                outline = outlines[x]
                identify = outline.find("div", {"class": "_4rR01T"})
                # #print(identify.text)
                name = identify.text

                if checkProductNameSimilarirty(Product_search,name):

                    try:


                        identify = outline.find("div", {"class": "_30jeq3 _1_WHN1"})
                        price = identify.text

                        identify = outline.find("div", {"class": "CXW8mj"})
                        image = identify.find("img")
                        image_link = image['src']

                        rev = outline.find("span",{"class":"_2_R_DZ"})
                        rat = outline.find("div", {"class": "_3LWZlK"})
                        
                        
                        # data  = {

                        #     'Product_Name':name,
                        #     'Product_Price':cleanPrice(price),
                        #     'Product_Rating':cleanRating(rat.text),
                        #     'Product_Reviews':cleanReviews(rev.text),
                        #     'Product_ImageLink':image_link
                        # }

                        data  = {

                            'Product_Name':name,
                            'Product_Price':price,
                            'Product_Rating':rat.text,
                            'Product_Reviews':rev.text,
                            'Product_ImageLink':image_link
                        }


                        # print(data)

                        Flipkart_Products.append(data)


                    except Exception as e:
                        print()

                else:pass

    
            if len(Flipkart_Names) is 0:
                outlines_2 = soup.findAll("div", {"class": "_4ddWXP"})

                for y in range(len(outlines_2)):
                    outline_2 = outlines_2[y]
                    identify_2 = outline_2.find("a", {"class": "s1Q9rs"})
                    name_2 = identify_2.text
                    Flipkart_Names.append(name_2)
            else:
                pass

            print(Flipkart_Names)


        scrape()

    def Relience():
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,nl;q=0.7',
        }

        URL = "https://www.reliancedigital.in/search?q=" + str(Product_search)
        print(URL)

        try:
            recieve = requests.get(URL, headers=headers)
            recieve = recieve.text

        except:

            options = Options_Chrome()
            options.headless = True
            browser = webdriver.Chrome(options=options)
            browser.get(URL)
            time.sleep(60)
            recieve = browser.page_source
            browser.close()

        soup = BeautifulSoup(recieve, 'lxml')
        data = soup


        def scrape():
            time.sleep(time_variable)
            outlines = soup.findAll("div", {"class": "sp grid"})
                    
            for x in range(len(outlines)):
                outline = outlines[x]
                identify = outline.find("p", {"class": "sp__name"})
                name = identify.text

                if checkProductNameSimilarirty(Product_search,name):

                    try:


                        identify = outline.find("span", {"class": "sc-bxivhb dmBTBc"})
                        price = identify.text

                        identify = outline.find("div", {"class": "sp__productbox"})
                        image = identify.find("img")
                        image_link = 'https://www.reliancedigital.in/'+image['data-srcset']


                        rev = outline.find("span",{"class":"sc-bxivhb byshAC"})
                        if rev==None:
                            rev = 'No Raating'
                        else:
                            rev = rev.text
                        
                        
                        data  = {
                            'Product_Name':name,
                            'Product_Price':price,
                            'Product_Rating':random.randint(1,5),
                            'Product_Reviews':rev,
                            'Product_ImageLink':image_link
                        }

                        # print(data)
                        Relience_Products.append(data)


                    except Exception as e:
                        print(e,'\n')

                else:pass

        scrape()

    Amazon()
    Flipkart()
    Relience()
    Snapdeal()

    
    allData = {

    }

    allData['Amazon'] =  Amazon_Products


    allData['Flipkart'] =  Flipkart_Products


    allData['Snapdeal'] =  Snapdeal_Products


    allData['Relience'] =  Relience_Products

    print('Complete Scrapped Data\n\n\n',allData)

    return allData


# Integrated('iphone 12')
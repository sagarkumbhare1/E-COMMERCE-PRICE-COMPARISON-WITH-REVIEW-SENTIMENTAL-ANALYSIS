from NLP_Review_Analyzer.Sentiment_Sentence_Analyzer import SentimentIntensity_Analyzer
# from Sentiment_Sentence_Analyzer import SentimentIntensity_Analyzer
from bs4 import BeautifulSoup
def scrab_reviews(url,driver):
    # driver.get(url)
    soup=BeautifulSoup(driver)
    result = []
    for i in soup.findAll("div",{'data-hook':"review-collapsed"}):
        print('Scrap Review : ',i.text)
        sentimental_result = SentimentIntensity_Analyzer(i.text)
        print('NLP analysis result on review : ',sentimental_result)
        result.append(sentimental_result)

    return result

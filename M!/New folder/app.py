import pandas as pd
from difflib import SequenceMatcher
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from string import punctuation
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
set(stopwords.words('english'))
import DataScrapper
from flask import Flask, url_for, render_template, request, jsonify, flash
import ComparisonAlgorithm

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

## Loading URls
data = pd.read_csv(r"product_url.csv")
product_name = list(data['product_name'].values)
amazon_url = list(data['amazon_url'].values)
flipkart_url = list(data['flipkart_url'].values)
snapdeal_url = list(data['snapdeal_url'].values)

all_product_data = []
for name in product_name:
    all_product_data.append({'value': name,'data': name})

###################################################################--->>>METHOD1
###### CHeck matching ratio of two string
def get_product_index_from_list(product):
    for prod_name in product_name:
        simi = SequenceMatcher(None, product,prod_name).ratio()
        print(simi)
        if simi>=0.7:
            index = product_name.index(prod_name)
            print(index,prod_name)
            return index,prod_name

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home1():
    return render_template("home.html")


@app.route('/sentimental')
def sentimental():
    return render_template('sentimental.html')

@app.route('/sentimental', methods=['POST'])
def sentimental_post():
    stop_words = stopwords.words('english')
    
    #convert to lowercase
    text1 = request.form['text1'].lower()
    
    text_final = ''.join(c for c in text1 if not c.isdigit())
    
    #remove punctuations
    #text3 = ''.join(c for c in text2 if c not in punctuation)
        
    #remove stopwords    
    processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer()
    dd = sa.polarity_scores(text=processed_doc1)
    compound = round((1 + dd['compound'])/2, 2)

    return render_template('sentimental.html', final=compound, text1=text_final,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu'])


@app.route("/search/<string:box>")
def process(box):
    query = request.args.get('query')
    if box == 'names':
        suggestions = all_product_data
    return jsonify({"suggestions":suggestions})
    

@app.route('/login', methods = ['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/search_product', methods = ['GET','POST'])
def search_product():
    if request.method == 'POST':

        try:

            product = request.form['names']

            Amazon_URL = "https://www.amazon.in/s?k=" + str(product) + "&ref=nb_sb_noss_2".replace(' ','%20')
            Snapdeal_URL = "https://www.snapdeal.com/search?keyword=" + str(product) + "&sort=plrty".replace(' ','%20')
            Flipkart_URL = "https://www.flipkart.com/search?q=" + str(product) + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".replace(' ','%20')
            Relience_URL = "https://www.reliancedigital.in/search?q=" + str(product).replace(' ','%20')
            print(
                Amazon_URL,
                Snapdeal_URL,
                Flipkart_URL,
                Relience_URL
            )

            allData =  DataScrapper.Integrated(product)

            print('\n\n\nBest Platform\n')
                       
            Best_Platform = ComparisonAlgorithm.Best_Platform_Identifier_Algorithm(
                allData['Amazon'][0]['Product_Price'],allData['Amazon'][0]['Product_Rating'],
                allData['Flipkart'][0]['Product_Price'],allData['Amazon'][0]['Product_Rating'],
                allData['Snapdeal'],allData['Snapdeal'],
                allData['Relience'],allData['Relience']                                
                )        


            Amazon_Recommended = 'Not Recommended'
            Relience_Recommended = 'Not Recommended'
            Flipkart_Recommended = 'Not Recommended'

            if Best_Platform=='Amazon':
                Amazon_Recommended = "Recommended"
                
            if Best_Platform=='Flipkart':
                Flipkart_Recommended = "Recommended"
            
            if Best_Platform=='Relience':
                Relience_Recommended = "Recommended"
            
            topResult = {

                'Amazon':{
                    'Product_Name':allData['Amazon'][0]['Product_Name'],
                    'Product_Price':allData['Amazon'][0]['Product_Price'],
                    'Product_Rating':allData['Amazon'][0]['Product_Rating'],
                    'Product_Reviews':allData['Amazon'][0]['Product_Reviews'],
                    'Product_ImageLink':allData['Amazon'][0]['Product_ImageLink'],
                    'Recommended':Amazon_Recommended
                },

                'Flipkart':{
                    'Product_Name':allData['Flipkart'][0]['Product_Name'],
                    'Product_Price':allData['Flipkart'][0]['Product_Price'],
                    'Product_Rating':allData['Flipkart'][0]['Product_Rating'],
                    'Product_Reviews':allData['Flipkart'][0]['Product_Reviews'],
                    'Product_ImageLink':allData['Flipkart'][0]['Product_ImageLink'],
                    'Recommended':Flipkart_Recommended
                }
            
            }


            if len(allData['Relience'])>0:
                topResult['Relience']= {
                    'Product_Name':allData['Relience'][0]['Product_Name'],
                    'Product_Price':allData['Relience'][0]['Product_Price'],
                    'Product_Rating':allData['Relience'][0]['Product_Rating'],
                    'Product_Reviews':allData['Relience'][0]['Product_Reviews'],
                    'Product_ImageLink':allData['Relience'][0]['Product_ImageLink'],
                    'Recommended':Relience_Recommended
                }
            else:
                topResult['Relience']= {
                    'Product_Name':"Not Available",
                    'Product_Price':"Not Available",
                    'Product_Rating':"Not Available",
                    'Product_Reviews':0,
                    'Product_ImageLink':"Not Available",
                    'Recommended':Relience_Recommended
                }


            return render_template('table.html',topResult=topResult, allData = allData,
                    Amazon_URL = Amazon_URL,
                    Flipkart_URL = Flipkart_URL,
                    Snapdeal_URL = Snapdeal_URL,
                    Relience_URL = Relience_URL
                )


        except Exception as e:
            print('Error Occur',e)
            flash('Some Error Occur Please with other product!!!!')
            return render_template('home.html')


@app.route('/go_back', methods = ['GET','POST'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run('127.1.1.1',debug=True)



    

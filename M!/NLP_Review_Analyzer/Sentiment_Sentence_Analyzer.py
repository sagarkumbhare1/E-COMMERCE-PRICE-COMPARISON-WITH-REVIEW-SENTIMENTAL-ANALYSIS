######### SentimentIntensityAnalyzer Way
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from NLP_Review_Analyzer.filter_sentence import filter_sentence_method

### Analyzing Method 3
def filter_text(text):
    clean_text = filter_sentence_method(text)
    return clean_text

def SentimentIntensity_Analyzer(text):
    clean_text = filter_text(text)
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(clean_text)
    return sentiment_score


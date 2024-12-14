from transformers import pipeline
import re

model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline('sentiment-analysis', model=model_name)

# Function to check if the message is a question
def is_question(text):
    if text.strip().endswith('?'):
        return True
    
    question_words = ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'can', 'does', 'do', 'is', 'are', 'will', 'did', 'should', 'would']
    text_lower = text.strip().lower()

    for word in question_words:
        if text_lower.startswith(word):
            return True
    
    return False


# Function to analyze sentiment and check if it's a question
def analyze_sentiment(text):
    is_question_text = is_question(text)
    # Analyze sentiment
    result = sentiment_analyzer(text)
    sentiment_label = result[0]['label'] 
    # Determine sentiment as positive, negative, or neutral
    if sentiment_label == 'POSITIVE':
        sentiment = 'positive'
    elif sentiment_label == 'NEGATIVE':
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    # Return both sentiment and whether the message is a question
    return sentiment

# Function to calculate service quality (based on sentiment)
def calculate_service_quality(sentiment):
    if sentiment == 'positive':
        return "Excellent"
    elif sentiment == 'negative':
        return "Poor"
    else:
        return "Neutral"
    
# app.py
from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

# Updated project data with GitHub links
projects = [
    {
        "title": "House Price Prediction",
        "description": "ML model to predict housing prices using advanced regression techniques",
        "image": "HousePricePrediction.jpeg",
        "tags": ["Python", "Machine Learning", "Regression"],
        "github": "https://github.com/AlishbaSoftTeche/housing-price-prediction"
    },
    {
        "title": "Image Resizer",
        "description": "Smart image resizing tool with AI-enhanced quality preservation",
        "image": "image_resizer.jpeg",
        "tags": ["Python", "Image Processing", "AI"],
        "github": "https://github.com/AlishbaSoftTeche/ImageResizer"
    },
    {
        "title": "Spam Classifier",
        "description": "NLP-based email classification system using machine learning",
        "image": "spam_classifer.jpg",
        "tags": ["Python", "NLP", "Machine Learning"],
        "github": "https://github.com/AlishbaSoftTeche/spam-classifier"
    },
    {
        "title": "Weather App",
        "description": "Real-time weather forecasting application with interactive UI",
        "image": "WeatherApp.jpeg",
        "tags": ["Python", "API", "Weather Data"],
        "github": "https://github.com/AlishbaSoftTeche/Weather-App"
    },
    {
        "title": "YouTube Downloader",
        "description": "Efficient YouTube video downloader with format selection",
        "image": "YouTube_Downloader.png",
        "tags": ["Python", "YouTube API", "Video Processing"],
        "github": "https://github.com/AlishbaSoftTeche/YouTube-Downloader"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/redirect/<path:github_url>')
def redirect_to_github(github_url):
    return redirect(github_url)

if __name__ == '__main__':
    app.run(debug=True)
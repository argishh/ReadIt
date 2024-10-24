# ReadIt - Reddit Sentiment Analysis Project

An end-to-end sentiment analysis application that leverages deep learning techniques to analyze the top comments of a Reddit post. The project involves data collection using the Reddit API, extensive exploratory data analysis, advanced text preprocessing, and the deployment of a deep learning model for sentiment classification using Streamlit.

## Table of Contents

- [ReadIt - Reddit Sentiment Analysis Project](#readit---reddit-sentiment-analysis-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [How to Use?](#how-to-use)
  - [Tech Stack](#tech-stack)
  - [Data Collection](#data-collection)
    - [Data Sources](#data-sources)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Modeling](#modeling)
  - [Deployment](#deployment)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Future Enhancements](#future-enhancements)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Project Overview

This project aims to perform sentiment analysis on Reddit comments using a deep learning approach. The application fetches top comments from any Reddit post URL provided by the user, processes the data, performs sentiment classification, and displays the results in a user-friendly web interface built with Streamlit.

## Features

- **Reddit Post Analysis**: Simply paste a Reddit post URL into the application, and it will automatically scrape the top comments from the post using the Reddit API.
- **Sentiment Overview**: The application provides an easy-to-understand overview of public sentiment, classifying comments as positive, negative, or neutral.
- **Interactive Sentiment Visualizations**: View detailed, interactive visualizations that show the sentiment distribution across comments using Plotly.
- **User-Friendly Interface**: The application uses a simple Streamlit-based web interface that makes it accessible for anyone without any technical background.
- **Public Opinion Insights**: Get an immediate snapshot of the community's reaction to a topic or post, helping you understand public opinion trends.

## How to Use?

The project is designed to be straightforward and intuitive:

1. **Paste a Reddit Link**: Users can enter any valid Reddit post URL into the provided input field on the web interface.
2. **Analyze Comments**: The application will fetch the top comments, clean and preprocess the text, and use a pre-trained BERT model to classify each comment’s sentiment.
3. **View Results**: Users receive an overall summary of public sentiment in the form of:
   - A pie chart that shows the percentage of positive, negative, and neutral comments.
   - Detailed comment sentiment scores to dive deeper into the data.
4. **Interactive Experience**: Users can interact with the graphs to explore specific sentiment trends and gain insights into the public's perception of the topic discussed in the Reddit post.

This makes it an excellent tool for social media enthusiasts, content creators, marketers, and researchers who want to quickly gauge the overall sentiment of a Reddit discussion.

## Tech Stack

- **Programming Languages**: Python
- **Libraries**: 
  - `PRAW` (Reddit API wrapper)
  - `PyTorch` (Deep Learning)
  - `Transformers` (Huggingface's BERT)
  - `Plotly` (Interactive visualizations)
  - `Streamlit` (Web app deployment)
  - `pandas` & `numpy` (Data processing)
- **Deployment**: Streamlit, Docker

## Data Collection

Data is collected using the `PRAW` library, which is a Python wrapper for the Reddit API. The tool fetches top comments from the Reddit post provided by the user.

### Data Sources

- **Reddit API**: For real-time data collection.
- **Kaggle & GitHub**: Pre-labeled datasets for fine-tuning the sentiment analysis model. Relevant datasets include:
Datasets Used - 
  - [Twitter and Reddit Sentiment Analysis Dataset](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset)
  - [Sentiment140, Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)
  <!-- - [GoEmotions Dataset](https://github.com/Breadteeth/Reddit-Sentiment-Analysis) for nuanced emotion detection. -->

## Exploratory Data Analysis (EDA)

Thorough analysis of the dataset is performed using interactive Plotly graphs to understand the distribution of sentiment, comment lengths, and comment scores. Key EDA steps include:
- **Distribution of Comment Scores**
- **Comment Length Analysis**
- **Sentiment Distribution Visualization**

## Modeling

The core of the project is built using deep learning techniques:
- **Pre-trained BERT Model**: A transformer-based architecture from Huggingface's `transformers` library is utilized for fine-tuning on sentiment data.
- **Model Training**: Fine-tuned on sentiment-labeled Reddit datasets for accurate classification.
- **Evaluation Metrics**: Accuracy, F1 Score, Precision, and Recall.

## Deployment

The model is deployed using Streamlit, making it easy to interact with the sentiment analysis tool. Features include:
- **User Input**: Provide a Reddit post URL to analyze.
- **Interactive Graphs**: View comment score distributions and sentiment analysis results.
- **API Hosting**: The application is deployed on cloud platforms like AWS, Heroku, or Streamlit’s native platform.

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- Docker (Optional for containerization)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Reddit API**
   - Create a Reddit account and set up an application to get the `client_id` and `client_secret`.
   - Update the credentials in the `config.py` file.

4. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the app using Streamlit.
2. Enter a valid Reddit post URL.
3. View the fetched comments and their sentiment classification.
4. Interact with the visualizations to explore the data.

## Future Enhancements

- **Add Emotion Detection**: Expand beyond basic sentiment analysis to include emotion categories using the GoEmotions dataset.
- **Real-Time Analysis**: Allow for real-time monitoring of subreddits.
- **Model Improvements**: Experiment with other transformer-based models like `RoBERTa` or `XLNet`.
- **Multi-Language Support**: Extend sentiment analysis to multiple languages.
- **User Authentication**: Add OAuth for personalized sentiment analysis.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to improve the code, feel free to create a pull request. Please ensure your contributions adhere to the existing code style and pass all tests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Reddit** community for data sources.
- **Huggingface** for providing the `transformers` library.
- **Streamlit** for the deployment framework.
- **Kaggle** and **GitHub** contributors for pre-labeled datasets.

---

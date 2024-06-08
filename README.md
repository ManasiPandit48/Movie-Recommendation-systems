# Movie Recommendation System

This repository contains various models for creating a movie recommendation system. Each model uses different methods to provide accurate and personalized movie recommendations. The main methods included are:

- **Collaborative Filtering**: Recommends movies based on user interactions.
- **Content-Based Filtering**: Recommends movies similar to those a user has liked in the past.
- **Matrix Factorization**: Uses techniques like Singular Value Decomposition (SVD) to uncover latent factors in user-item interactions.
- **Hybrid Methods**: Combines multiple approaches to enhance recommendation accuracy.

Each method is implemented in its respective subfolder, with detailed documentation and code examples provided.

## Dataset
### MovieLens Dataset
The dataset used for all models is sourced from the MovieLens dataset available on Kaggle. It includes:
- **ratings.csv**: User ratings for movies.
- **movies.csv**: Movie metadata such as titles and genres.

You can find more details about the dataset on its [Kaggle page](https://www.kaggle.com/code/ayushimishra2809/movie-recommendation-system/input).

## Installation
To install the necessary packages, run:
```sh
pip install -r requirements.txt
```

## Usage
To run a specific model, navigate to its subfolder and execute the corresponding script. For example:
```sh
cd collaborative_filtering
python main.py
```
## Acknowledgements
We would like to thank MovieLens for providing the dataset used in this project. Their comprehensive dataset has been invaluable in developing and testing our recommendation models.

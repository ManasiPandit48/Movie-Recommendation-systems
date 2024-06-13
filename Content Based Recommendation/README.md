# Movie Recommendation App with Content-Based Filtering

This project involves creating a movie recommendation system using content-based filtering techniques. The system utilizes the TMDB dataset to recommend movies to users based on their selected movie and genre.

Content-based filtering is a technique used in recommendation systems to predict the preferences of a user for a particular item based on the item's features and the user's past interactions with similar items. In this case, we are using movie overviews and genres to recommend similar movies.

## Requirements

The following packages are required to run this project:

- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit
- matplotlib

You can install the required packages using pip:

```sh
pip install pandas numpy scikit-learn streamlit matplotlib
```

## Download TMDB Dataset

Ensure the TMDB datasets (`tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`) are downloaded and placed in the `datasets` folder under your project directory. You can download the datasets from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

## Running the Movie Recommendation App

The `movie_recommendation.py` script is used to run the movie recommendation app. It reads the TMDB dataset, preprocesses the data, and builds a content-based filtering model using movie overviews and genres. The app then uses Streamlit to display recommendations and movie posters.

### Steps to Run the App:

1. **Navigate to the Project Directory**: Open a terminal and navigate to the directory containing the `app.py` script.

2. **Run the Streamlit App**: Execute the following command to run the app using Streamlit:

    ```sh
    streamlit run movie_recommendation.py
    ```

3. **Interact with the App**: Open the link provided in the terminal to interact with the app in your web browser.

### Features of the App:

- **Movie Recommendations**: Get movie recommendations based on the selected movie title and genre.
- **Popular and High Budget Movies**: Visualize popular and high-budget movies among the recommendations.
- **Movie Posters**: Display movie posters alongside the recommendations.

## UI Screenshots

Below are some screenshots of the user interface to illustrate the app's functionality:
![Screenshot 2024-06-13 152738](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/a2e74d99-14be-44e5-9cd8-c359fbfc5ea9)

![Screenshot 2024-06-13 152651](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/ab37546a-8ba6-4f55-a08d-4bb60ed80778)

![Screenshot 2024-06-13 152707](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/9814c04c-3a1d-43bf-a1d7-552f828f0d59)

![Screenshot 2024-06-13 152721](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/bf632d8a-0cf0-44b2-a051-915f051a9f99)

## Notes

- Ensure the TMDB dataset files (`tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`) are placed correctly in the `datasets` directory.
- The app dynamically updates recommendations and visualizations based on user input.

## Acknowledgments

- The datasets used in this project are provided by TMDB.
- The dataset files were downloaded from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

Feel free to reach out if you have any questions or encounter any issues.

Happy coding!

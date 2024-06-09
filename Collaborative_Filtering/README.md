# Movie Recommendation App With Collaborative Filtering 

This project involves creating a movie recommendation system using collaborative filtering techniques. The system utilizes the MovieLens dataset to recommend movies to users based on their previous ratings.

Collaborative filtering is a technique used in recommendation systems to predict the preferences or ratings of a user for a particular item based on the preferences or ratings of many other users. The fundamental idea behind collaborative filtering is that users who agreed in the past will agree in the future.

## Requirements

The following packages are required to run this project:

- Python 3.7+
- pandas
- numpy
- scikit-learn

You can install the required packages using pip:

```bash
pip install pandas numpy scikit-learn
```

## Download MovieLens Dataset

Download the MovieLens dataset from Kaggle using the following link and place it in the `CollaborativeFiltering/Datasets` folder under your project directory: [Download MovieLens Dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)

## Training and Testing the Recommendation Model

The `movie_recommendation_app.py` script is used to train the movie recommendation model. It reads the MovieLens dataset, preprocesses the data, builds a collaborative filtering model, trains the model on the training data, and saves the trained model.

### Training Steps:

1. **Initialize Data Loaders:** Load the MovieLens dataset and preprocess the data.
2. **Build the Collaborative Filtering Model:** Define the model using user-based collaborative filtering.
3. **Train the Model:** Fit the model using the training data.
4. **Save the Trained Model:** Save the model for later use.

### Running the Script:

To train the model, execute the following command:

```bash
cd CollaborativeFiltering
streamlit run ..path/movie_recommendation_app.py
```

The training process time may vary depending on your hardware.

## UI Screenshots

Below are some screenshots of the user interface to test the model:

![Screenshot 2024-06-09 181110](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/534fe616-dc79-4cf7-b909-8ce000cbcd65)

![Screenshot 2024-06-09 181221](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/7437f8eb-85f1-4d53-b662-6120521d3c2e)

![Screenshot 2024-06-09 181144](https://github.com/ManasiPandit48/Movie-Recommendation-systems/assets/125982196/a07f45c0-d794-4899-9d5e-a57f46ff7339)

----
## Notes

- Ensure the MovieLens dataset is placed correctly in the `CollaborativeFiltering/Datasets` directory.
- The model and other output files should be located in the `CollaborativeFiltering` directory after training.

## Acknowledgments

- The datasets used in this project are provided by [MovieLens](https://grouplens.org/datasets/movielens/).
- The dataset files were downloaded from [Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset).

---

Feel free to reach out if you have any questions or encounter any issues.

Happy coding!

---

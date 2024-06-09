# Movie Recommendation App With Collaborative Filtering 

This project involves creating a movie recommendation system using collaborative filtering techniques. The system utilizes the MovieLens dataset to recommend movies to users based on their previous ratings.

Collaborative filtering is a technique used in recommendation systems to predict the preferences or ratings of a user for a particular item based on the preferences or ratings of many other users. The fundamental idea behind collaborative filtering is that users who agreed in the past will agree in the future
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

## Training the Recommendation Model

The `movie_recommendation_app.py` script is used to train the movie recommendation model. It reads the MovieLens dataset, preprocesses the data, builds a collaborative filtering model, trains the model on the training data, and saves the trained model.

### Training Steps:

1. **Initialize Data Loaders:** Load the MovieLens dataset and preprocess the data.
2. **Build the Collaborative Filtering Model:** Define the model using user-based collaborative filtering.
3. **Train the Model:** Fit the model using the training data.
4. **Save the Trained Model:** Save the model for later use.

### Running the Training Script:

To train the model, execute the following command:

```bash
cd CollaborativeFiltering
python movie_recommendation_app.py
```

The training process time may vary depending on your hardware.

## Testing the Recommendation Model

The `movie_recommendation_app.ipynb` notebook is used to test the trained model. It loads the dataset, preprocesses the data, and uses the trained model to make movie recommendations.

### Testing Steps:

1. **Load the Dataset:** Load and preprocess the MovieLens dataset.
2. **Load the Trained Model:** Load the trained model from the saved files.
3. **Make Recommendations:** Use the model to recommend movies based on user input.

### Running the Testing Notebook:

To test the movie recommendation system interactively, execute the following command:

```bash
cd CollaborativeFiltering
jupyter notebook movie_recommendation_app.ipynb
```

Follow the steps in the notebook to see movie recommendations based on the collaborative filtering model.

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


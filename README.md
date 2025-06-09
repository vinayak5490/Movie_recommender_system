# Movie Recommender System

This project is a **Content-Based Movie Recommender System** built using Python, Jupyter Notebook, and Streamlit. It recommends movies similar to a selected movie based on their content (overview, genres, keywords, cast, and crew).

## Features

- Recommends top 5 similar movies for any selected movie.
- Streamlit web interface for easy interaction.
- Displays recommended movie titles and posters (if available in the dataset).

## Dataset

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Files used: `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`

## How it works

1. **Data Preprocessing:**  
   - Merges movie and credits data.
   - Extracts and cleans features: genres, keywords, cast, crew, and overview.
   - Creates a 'tags' column combining all relevant text features.
   - Applies stemming and vectorization.

2. **Similarity Calculation:**  
   - Uses CountVectorizer and Cosine Similarity to compute similarity between movies.

3. **Recommendation:**  
   - For a selected movie, finds the most similar movies using the similarity matrix.

4. **Web App:**  
   - Built with Streamlit for interactive recommendations.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the data

- Download the TMDB dataset and place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the project directory.
- Run the Jupyter notebook (`movie_recommender_system.ipynb`) to generate `movies.pkl` and `similarity.pkl`.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

## File Structure

```
.
├── app.py                  # Streamlit frontend
├── movie_recommender_system.ipynb  # Data processing and model building
├── movies.pkl              # Pickled movie data (generated)
├── similarity.pkl          # Pickled similarity matrix (generated)
├── tmdb_5000_movies.csv    # Raw dataset
├── tmdb_5000_credits.csv   # Raw dataset
└── requirements.txt        # Python dependencies
```

## Screenshots

_Add screenshots of your Streamlit app here!_

## Credits
![Screenshot 2025-06-09 151927](https://github.com/user-attachments/assets/6c071539-7801-4d44-8771-6f542ace1b5d)

- [TMDB](https://www.themoviedb.org/) for the dataset.

## License

This project is licensed under the MIT License.

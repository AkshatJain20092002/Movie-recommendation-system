# Movie Recommendation System
This is a Movie Recommendation System built using Flask and Python. It uses collaborative filtering and content-based filtering algorithms to recommend similar movies to users. The app allows users to select a movie from a list and get recommendations. Movie posters are fetched from The Movie Database (TMDb) API. The project structure includes the main Flask app file, Jupyter Notebook for the backend, and pickle files for storing data. The app has a user-friendly interface and is easy to use.

### How to Use
Clone the repository and unzip the similarity_movie.pkl file.
Set up a virtual environment and install dependencies from requirements.txt.
Run the Flask app with python app.py.
Access the app in your web browser at http://127.0.0.1:5000/.
Select a movie and click "Recommend" to get similar movie recommendations.
# Project Structure
app.py: Main Flask application file.
movie_recommendation.ipynb: Backend code in Jupyter Notebook.
movies_dict.pkl: Pickle file with movie data (pandas DataFrame).
similarity_movie.pkl: Pickle file with movie similarity data.
templates/: Directory containing HTML templates.
templates/index.html: HTML template for the home page.
templates/recommendation.html: HTML template for recommended movies page.
templates/static/: Directory for CSS and images.
templates/static/styles.css: CSS file for styling the app.
# License
This project is licensed under the MIT License.

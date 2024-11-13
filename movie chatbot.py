
movie_database = [
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "description": "Batman faces the Joker in this action-packed thriller."},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "description": "A thief who steals secrets from the subconscious is given a chance to erase his criminal record."},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "description": "The life story of a slow-witted, kind-hearted man from Alabama who witnesses and unwittingly influences several historical events."},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2, "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
    {"title": "Avengers: Endgame", "genre": "Action", "rating": 8.4, "description": "After the devastating events of Avengers: Infinity War, the Avengers assemble once more in order to reverse Thanos' actions."},
    {"title": "Parasite", "genre": "Thriller", "rating": 8.6, "description": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the poor Kim clan."}
]

# --- Movie Recommendation Function ---
def recommend_movies(genre=None, min_rating=0):
    # Filter movies based on user preferences
    filtered_movies = [
        movie for movie in movie_database 
        if (genre is None or movie['genre'].lower() == genre.lower()) and movie['rating'] >= min_rating
    ]
    
    if not filtered_movies:
        print("No movies found based on your preferences.")
        return

    print(f"\nHere are some recommended {genre if genre else 'movies'} with a rating of {min_rating} or higher:\n")
    for movie in filtered_movies:
        print(f"Title: {movie['title']}")
        print(f"Genre: {movie['genre']}")
        print(f"Rating: {movie['rating']}")
        print(f"Description: {movie['description']}\n")

# --- Example Usage ---
# Set user preferences for recommendations
genre = input("Enter a movie genre (e.g., Action, Drama, Sci-Fi, Thriller): ")
min_rating = float(input("Enter minimum rating (e.g., 7.0): "))

# Call the recommendation function with user preferences
recommend_movies(genre=genre, min_rating=min_rating)

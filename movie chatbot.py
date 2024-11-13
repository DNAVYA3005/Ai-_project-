
movie_database = [
    {"title": "fast and furious decription", "genre": "Action", "rating": 9.0, "description": "The movie is packed with high-speed car chases, thrilling action, and an emphasis on loyalty and family."},
    {"title": "instellar", "genre": "Sci-Fi", "rating": 8.8, "description": "The journey takes them to distant galaxies, where they face time dilation, black holes, and the mysteries of space."},
    {"title": "The Pursuit of Happyness", "genre": "Drama", "rating": 8.8, "description": "  a struggling salesman, tries to create a better life for his son while living in poverty and facing overwhelming odds. A story of resilience, perseverance, and hope."},
    {"title": "passengers", "genre": "Sci-Fi", "rating": 8.7, "description": "Aboard a spaceship traveling to a distant colony planet, two passengers—Jim Preston and Aurora Lane—are awakened from cryosleep 90 years too early due to a malfunction."},
    {"title": "the mole", "genre": "Crime", "rating": 9.2, "description": "n Boston, a mole in the police department and an undercover cop infiltrate each other's organizations. As tensions rise, both men struggle to uncover the other’s identity before it's too late."},
    {"title": "The Social Network ", "genre": "Drama", "rating": 9.3, "description": " The story of Mark Zuckerberg's creation of Facebook and the subsequent legal battles that followed. The film delves into ambition, friendship, betrayal, and the cost of success."},
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

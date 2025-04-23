import random

# List storing movies by genre, rating, and popularity
movie_data = [
    {"genre": "Action", "movie": "Avengers: Endgame", "rating": 8.4, "popularity": 98},
    {"genre": "Action", "movie": "Mad Max: Fury Road", "rating": 8.1, "popularity": 90},
    {"genre": "Comedy", "movie": "The Hangover", "rating": 7.7, "popularity": 85},
    {"genre": "Comedy", "movie": "Superbad", "rating": 7.6, "popularity": 80},
    {"genre": "Horror", "movie": "The Conjuring", "rating": 7.5, "popactularity": 88},
    {"genre": "Horror", "movie": "A Quiet Place", "rating": 7.4, "popularity": 82},
    {"genre": "Drama", "movie": "Forrest Gump", "rating": 8.8, "popularity": 95},
    {"genre": "Drama", "movie": "The Shawshank Redemption", "rating": 9.3, "popularity": 97}
]

# List to track movies already recommended
recommended_movies = []

# Procedure to recommend a movie based on genre and preference
def recommend_movie(user_genre, preference):
    options = []
    for item in movie_data:
        if item["genre"].lower() == user_genre.lower():
            options.append(item)

    if not options:
        return None, "Sorry, no movies found for that genre."

    if preference == "random":
        available = [movie for movie in options if movie["movie"] not in recommended_movies]
        if not available:
            return None, "You've seen all movies in this genre."
        choice = random.choice(available)
        recommended_movies.append(choice["movie"])
        return choice, f"{choice['movie']} 🍿 (Rating: {choice['rating']})"

    elif preference == "highest-rated":
        highest = max(options, key=lambda x: x["rating"])
        return highest, f"{highest['movie']} 🌟 (Rating: {highest['rating']})"

    elif preference == "lowest-rated":
        lowest = min(options, key=lambda x: x["rating"])
        return lowest, f"{lowest['movie']} 💩 (Rating: {lowest['rating']})"

    else:
        return None, "Invalid preference. Choose 'random', 'highest-rated', or 'lowest-rated'."

# Procedure to display the popularity of the recommended movie
def show_movie_popularity(movie):
    return f"The popularity score for {movie['movie']} is {movie['popularity']} 📊."

# Function for terminal styling
def print_with_style(text, style="normal"):
    if style == "bold":
        print(f"\033[1m{text}\033[0m")  # Bold text
    elif style == "green":
        print(f"\033[32m{text}\033[0m")  # Green text
    elif style == "red":
        print(f"\033[31m{text}\033[0m")  # Red text
    elif style == "cyan":
        print(f"\033[36m{text}\033[0m")  # Cyan text
    else:
        print(text)

# Clear screen
print("\033c", end="")

print_with_style("🎬 Welcome to the Movie Recommender! 🎥", "green")
print_with_style("Let's find a movie for you to watch based on your preferences.\n", "cyan")

# Get user input for genre
user_input_genre = input("What movie genre do you like? (Action, Comedy, Horror, Drama): ").capitalize()

# Get user input for preference
print("\nHow would you like your recommendation?")
print("1. 'random' movie 🎲")
print("2. 'highest-rated' movie ⭐")
print("3. 'lowest-rated' movie 💩")
user_input_pref = input("Please type 'random', 'highest-rated', or 'lowest-rated': ").lower()

# Call procedure and store result
chosen_movie, movie_recommendation = recommend_movie(user_input_genre, user_input_pref)

# Output result
if chosen_movie:
    print_with_style(f"\n🎬 Recommendation: {movie_recommendation}", "green")

    # New question: ask if user wants popularity of the recommended movie
    see_popularity = input(f"\nWould you like to see the popularity score for {chosen_movie['movie']}? (yes/no): ").lower()
    if see_popularity == "yes":
        print_with_style(show_movie_popularity(chosen_movie), "cyan")
    else:
        print_with_style("\nAlright, no popularity shown. 🎬", "red")
else:
    print_with_style("\nSorry, no movie found. Please check your genre or preference. 😞", "red")

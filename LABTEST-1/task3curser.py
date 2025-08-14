def collect_movies():
    movies = []
    genres = []
    n = int(input("How many movies do you want to enter? "))
    for i in range(n):
        movie = input(f"Enter the name of movie #{i+1}: ")
        genre = input(f"Enter the genre of '{movie}': ")
        movies.append(movie)
        genres.append(genre)
    return movies, genres

def recommend_movies(movies, genres, preferred_genre):
    recommended = [movie for movie, genre in zip(movies, genres) if genre.lower() == preferred_genre.lower()]
    return recommended

if __name__ == "__main__":
    movies, genres = collect_movies()
    user_genre = input("Enter your preferred genre: ")
    recommendations = recommend_movies(movies, genres, user_genre)
    if recommendations:
        print("Recommended movies for you:")
        for movie in recommendations:
            print("-", movie)
    else:
        print("No movies found for your preferred genre.")

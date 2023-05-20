import requests
import json
import csv

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2QwZDY5MTcyMDJkNzA1OGUzMzU1MDRiZGM4YmYxZiIsInN1YiI6IjY0NjQ2MzU2ZDA1YTAzMDBmYzIxNGJjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.02TPXuZ_3VMR1t9sSTwMMsVXtPgWYYNt5hTsyPww8PY"
BASE_URL = "https://api.themoviedb.org/3"
POPULAR_MOVIES_ENDPOINT = "/movie/popular"

csv_file = open("movie_data_new.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(csv_file)

# Definisikan header
header = [
    "Title",
    "Release Date",
    "Adult",
    "Genre IDs",
    "Overview",
    "Popularity",
    "Vote Average",
    "Vote Count",
    "Original Language",
    "Original Title",
    "Poster Path",
    "Backdrop Path",
    "Video",
    "ID"
]

# Tulis header ke file CSV
csv_writer.writerow(header)

page = 1
while True:
    response = requests.get(BASE_URL + POPULAR_MOVIES_ENDPOINT + "?page=" + str(page), headers={"Authorization": "Bearer " + API_KEY})

    if response.status_code == 200:
        response_data = json.loads(response.content)

        for movie in response_data["results"]:
            title = movie.get("title", "")
            release_date = movie.get("release_date", "")
            adult = movie.get("adult", "")
            genre_ids = movie.get("genre_ids", [])
            overview = movie.get("overview", "")
            popularity = movie.get("popularity", 0)
            vote_average = movie.get("vote_average", 0)
            vote_count = movie.get("vote_count", 0)
            original_language = movie.get("original_language", "")
            original_title = movie.get("original_title", "")
            poster_path = movie.get("poster_path", "")
            backdrop_path = movie.get("backdrop_path", "")
            video = movie.get("video", False)
            id = movie.get("id", "")

            row = [
                title,
                release_date,
                adult,
                genre_ids,
                overview,
                popularity,
                vote_average,
                vote_count,
                original_language,
                original_title,
                poster_path,
                backdrop_path,
                video,
                id
            ]

            csv_writer.writerow(row)

    if "total_pages" in response_data and page < response_data["total_pages"]:
        page += 1
    else:
        break

csv_file.close()

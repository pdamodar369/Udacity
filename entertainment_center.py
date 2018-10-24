import media
import fresh_tomatoes

spyder = media.Movie("Spyder", "Indian Spy and a Hacker Story","27 September 2017", media.Movie.VALID_RATINGS[0],
                        "https://upload.wikimedia.org/wikipedia/en/d/de/Spyder_film_poster.jpg",
                        "https://www.youtube.com/watch?v=og1zP3u0b4k")


#print(toy_story.storyline)

bahubali_2 = media.Movie("Bahubali 2", "Indian Mythological Film", "28 April 2017",media.Movie.VALID_RATINGS[1], 
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                     "https://www.youtube.com/watch?v=G62HrubdD6o")

arjun_reddy = media.Movie('Arjun Reddy', "Medico and his Love Story","25 August 2017", media.Movie.VALID_RATINGS[3],
                   "https://upload.wikimedia.org/wikipedia/en/a/a4/Arjunreddy.jpg",
                   "https://www.youtube.com/watch?v=QE9rxjlYHn4&t=113s")

guru = media.Movie("Guru", "Indian Woman Boxer and her Teacher Story","31 March 2017", media.Movie.VALID_RATINGS[0],
                          "https://upload.wikimedia.org/wikipedia/en/f/f8/Venkatesh%27s_Guru_poster.jpg",
                          "https://www.youtube.com/watch?v=23UiMaJmW5c")

mahanubavudu = media.Movie("Mahanubavudu", "Telugu Love Story","29 September 2017", media.Movie.VALID_RATINGS[0],
                          "https://upload.wikimedia.org/wikipedia/en/d/d9/Mahanubhavudu_poster.jpg",
                          "https://www.youtube.com/watch?v=Nc7sg-gRxAc")

bahubali_1 = media.Movie("Bahubali 1", "Indian Mythological Film","10 July 2015", media.Movie.VALID_RATINGS[1],
                          "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                          "https://www.youtube.com/watch?v=sOEg_YZQsTI")

movies = [spyder, bahubali_2, arjun_reddy, guru, mahanubavudu, bahubali_1]

fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS

#print media.Movie.__module__

#print spyder

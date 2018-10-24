import webbrowser
    
class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """ This is Initialization Function"""
    def __init__(self, movie_title, movie_storyline, movie_release_date, movie_rating, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = movie_release_date
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    """ This is Movie Trailer Function"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



# a contructor to create instances of movies
class Movies(
):

    def __init__(self,
                 title, trailer_youtube_url,
                 poster_image_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.title = title
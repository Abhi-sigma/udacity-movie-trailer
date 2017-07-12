# coding=utf-8

# a contructor to create instances of movies

"""
    a module to display movie objects,attributes and instances
"""


class Movies(object):

    """a class object to store movie information"""
    def __init__(self, title, trailer_youtube_url, poster_image_url):
    	"""
        initializes the instance of the class movie

        :param title:string
        :param trailer_you_tube_url:string
        :param poster_image_url:string

        """
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.title = title

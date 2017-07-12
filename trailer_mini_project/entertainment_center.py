
# importing required modules
from media import Movies
from fresh_tomatoes import open_movies_page


# initializing different instances of movies that I want to use in the
# traler movie website


# instances of the class Movies

# Fast and Furious 1,Trailer URL,Movie Image
fast_and_furious_1 = Movies("Fast and Furious 1",
                            "https://www.youtube.com/watch?v=2TAOizOnNPo",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcT18dHcbyb6cKFIjPsy6g8vgd-E6XfBcJr5NIBYAcmaP9T1wlfn")


# Fast and Furious 2,Trailer URL,Movie Image
fast_and_furious_2 = Movies("Fast and Furious 2",
                            "https://www.youtube.com/watch?v=ZZGkV_xWGw4",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcTQ-0PNL4tdTxg58H50JJs_HIzPi3und4vRh3yOJLKTyZ8Wy3f0")


# Fast and Furious 3,Trailer URL,Movie Image
fast_and_furious_3 = Movies("Fast and Furious 3",
                            "https://www.youtube.com/watch?v=p8HQ2JLlc4E",
                            "http://www.gstatic.com/tv/thumb/movieposters/159790/p159790_p_v8_ag.jpg")


# Fast and Furious 4,Trailer URL,Movie Image
fast_and_furious_4 = Movies("Fast and Furious 4", "https://www.youtube.com/watch?v=YXZjANEY6bA",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReS9bG9ucbcpFGK0i-YFRBeT7KhBMgYQyU8Ttc9GNpcjBWGfKp")


# Fast and Furious 5,Trailer URL,Movie Image
fast_and_furious_5 = Movies("Fast and Furious 5", "https://www.youtube.com/watch?v=OqjeOYeG5_A",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcR9Y8JHdp2nSaGCT7RfryzQtCLmJgDDkV77IHKa1hXnQpaDfpDX")


# Fast and Furious 6,Trailer URL,Movie Image
fast_and_furious_6 = Movies("Fast and Furious 6", "https://www.youtube.com/watch?v=oc_P11PNvRs",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcR4YVpIByidoaq4cAwBQ5QENYgteSTk6jL4AL_iMspQJqYiaFG6")


# Fast and Furious 7,Trailer URL,Movie Image
fast_and_furious_7 = Movies("Fast and Furious 7", "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcReedjA2vJSO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7")


# Fast and Furious 8,Trailer URL,Movie Image
fast_and_furious_8 = Movies("Fast and Furious 8", "https://www.youtube.com/watch?v=NxhEZG0k9_w",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_UY1200_CR64,0,630,1200_AL_.jpg")


# creating a list of instances of movies which is passed to
# function open_movies_pages in fresh_tomtoes.py script


list_of_movies = [fast_and_furious_1, fast_and_furious_2,
                  fast_and_furious_3, fast_and_furious_4,
                  fast_and_furious_5, fast_and_furious_6,
                  fast_and_furious_7, fast_and_furious_8]


# invoking function open_movie_page with list_of_movies as argument
# this function opens the browswer and renders the HTML
open_movies_page(list_of_movies)

"""
How to Document your code using doc string,
        * For the description of the any method or class or any code in program

"""
# E.g 1),
class Song:
    """
    IMPORTANT
    WHAT AND HOW of your class
    Class to represents Songs
    Attributes:
        Title(str): The title of the song
        Artist(Name of Artist): An artist representing song creator
        duration(int): This is the duration of the song
    """
    def __init__(self,title,artist,duration):
        """
        This is song init method
        arg:
        title(str): Initializes the title of the song
        artist: The creator of the song
        """
        self.title = title
        self.artist = artist
        self.duration = duration

help(Song) # for the whole class
# o/p
# Output will be whatever typed into doc string

help(Song.__init__) # for the specific method of the class
# o/p
# Output will be specific function's decription fo the class whatever we mention

# Assigning description after defining method or class any code
Song.__init__.__doc__= """
        This is song init method
        arg:
        title(str): Initializes the title of the song
        artist: The creator of the song """
# o/p
# o/p Output will be specific function's decription fo the class whatever we mention
help(Song.__init__)
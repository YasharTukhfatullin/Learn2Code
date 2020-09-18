# Temporary Song Cloud Database
# (Content refers to songs and playlists)
# Program should be able to:
#     1. Create users
#     2. Login (select user)
#     3. Delete users (and there content)
#     4. Browse content
#         1. Lists all songs
#         2. Lists all songs in user's playlist
#         3. Lists all artists
#         4. Lists all albums
#         5. Lists all genres
#     5. End program

# Users should be able to upload a song:
#     1. Songs should have a title
#     2. Songs should have an artist
#     3. Songs should have an album
#     4. Songs should have a track number

# Users should be able to create playlists
# Associated with a user

# Users should be able to manage playlists:
#     1. Playlists should be able to add songs
#     2. Playlists should be able to remove songs
#     3. Playlists should be able to reorder songs
# -------------------------------------------------
# Updated Database Project:
# In addition to all of the original requirements -
# 1. Use classes where appropriate (I can think of at least two places of use)
# 2. Must error check entire program (unit and system testing)
# 3. Must retain state between program uses (will need file I/O)

# Classes are good way group data(information) together.

"""
Class: Definition of how information will be structured (example: concept of a list).
Constructor: Instructions on how to take data(information) and structure it into an object.
Object: Actual data formatted how the class defines (example: a real grocery shopping list).
(example:  To make a list take an item and put it on a line by itself, repeat until out of information).
"""

"""
Classes - They allow us logically group out data and functions,
in a way that's easy to reuse and also easy to build upon if need be.

When we say data and functions that are associated with specific class,
We call those attributes(fields and mamebers) and methods.

When we say methods, we mean a function that is associated with a class
"""

""" 
Difference between a class and an instance of a class.

-class is basically a blueprint for creating instances and each unique employee,
what we create using our employee class will be an instance of that class 
"""


class User:

    # we use parameters when we dont know the value like name
    def __init__(self, name, email, password):
        # we use self when we craate an oject
        self.name = name
        self.email = email
        self.password = password

    def create_user():
        # TODO: Asking a user to enter name, email, password.
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")
        user_password = input("Enter your password: ")
        return User(user_name, user_email, user_password)  # Create a user object

    def login_user():
        # TODO: define
        pass

    def delete_user():
        # TODO: define
        pass

    def user_dict(self):
        return {
            "user-name": self.name,
            "user-email": self.email,
            "user-password": self.password,
        }


class Song:
    def __init__(self, title, artist, album, track_number, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        self.genre = genre

    def create_song():
        # TODO: define
        title = input("Enter a title: ")
        artist = input("Enter a artist: ")
        album = input("Enter an album: ")
        track_number = input("Enter a track number: ")
        genre = input("Enter a genre: ")
        return Song(title, artist, album, track_number, genre)

    # we dont need a song to create a song but we need song to convert to dictinorie
    def song_dict(self):
        return {
            "title": self.ttile,
            "artist": self.artist,
            "album": self.album,
            "track": self.track_number,
            "genre": self.genre,
        }


class Playlist:  # definition is a blueprint
    def __init__(self, name):  # constructor makes a house from a blueprint
        self.name = name  # object of type
        self.songs = list([])
        self.size = 0

    def create_playlist(name):  # static method (you dont need a house to build a house)
        pass

    def add_song(
        self, song
    ):  # instance method (you do need a house to put something in it)
        self.songs.append(song)
        self.size += 1

    def add_to_playlist():
        pass

    def remove_from_playlist():
        pass

    def reorder_playlist():
        pass


class DataBase:
    pass


if __name__ == "__main__":
    user1 = User("Yashar", "yashar@gmail.com", "Password12345")
    print(user1)

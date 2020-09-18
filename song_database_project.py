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

""" EXAMPLE USER {} 
username {password: value
   laylists: {}}
"""

"""
EXAMPLE PLAYLIST {}
name: {
	songs: []
}
"""

users_dict = {}  # empty dictinories
songs_dict = {}  # empty dictinories
current_users = ""

# 1. Create users
def create_user():
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    users_dict[user_name] = {"password": user_password, "playlist": {}}


# 2. Login (select user)
def login():
    user_name = input("Enter username: ")
    user_password = input("Ennter passwaord: ")
    if users_dict[user_name]["password"] == user_password:
        current_users = user_name
    else:
        print("Invalid options: ")


# 3. Delete users (and there content)
def remove_user(user_name):
    users_dict.pop(user_name)


def create_playlist():
    play_name = input("Enter playlist name: ")
    users_dict[current_users]["playlist"][play_name] = []


def add_to_playlist():
    play_name = input("Enter playlist name: ")
    play_list = users_dict[current_users]["playlists"][play_name]

    song_name = input("Enter song name: ")
    song = songs_dict[song_name]

    play_list.append(song)


def remove_from_playlist():
    play_name = input("Enter playlist name: ")
    play_list = users_dict[current_users]["playlists"][play_name]

    song_name = input("Enter song name: ")
    song = songs_dict[song_name]

    play_list.remove(song)


def reorder_playlist():
    play_name = input("Enter playlist name: ")
    play_list = users_dict[current_users]["playlists"][play_name]

    song_name = input("Enter song name: ")
    song = songs_dict[song_name]

    index = input("Enter where you would like to move the song: ")

    play_list.remove(song)
    play_list.insert(index, song)


"""
EXAMPLE SONG {}
title: value
{
artist: value
album: value
track_number: value
}

"""


def add_song():
    title = input("Enter the song title: ")
    artist = input("Enter the song artist: ")
    album = input("Enter the song album: ")
    track = input("Enter the track number: ")
    songs_dict[title] = {"artist": artist, "album": album, "track_number": track}


def list_song():
    songs = songs_dict.keys()
    for song in songs:
        print(song)


def list_artist():
    artists = songs_dict.values()
    for artist in artists:
        print(artist["artist"])


def list_albums():
    albums = songs_dict.values()
    for album in albums:
        print(album["album"])


# --------------------------------------------------

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


def main_menu():
    print(
        "1.Create User\n"
        "2.Login\n"
        "3.Delter User\n"
        "4.Browse\n"
        "5.Mange Playlist\n"
        "6.Upload song\n"
        "7.Quit"
    )

    choice = int(input("Enter the menu option: "))
    if choice == 1:
        create_user()
    elif choice == 2:
        login()
    elif choice == 3:
        remove_user()
    elif choice == 4:
        browse_menu()
    elif choice == 5:
        playlist_menu()
    elif choice == 6:
        add_song()
    elif choice == 7:
        return False
    else:
        print("Invalid Options:")
    return True


def browse_menu():
    print("1.List all songs\n"
          "2.List all artists\n" 
          "3.List all albums\n"
          )

    choice = int(input("Enter the menu options: "))
    if choice == 1:
        list_song()
    elif choice == 2:
        list_artist()
    elif choice == 3:
        list_albums()
    else:
        print("Invalid the option:")


def playlist_menu():
    print("1.Create playlist\n"
          "2.Add song playlist\n"
          "3.Reorder song in playlist\n"
          )

    choice = int(input("Enter the menu option: "))
    if choice == 1:
        create_playlist()
    elif choice == 2:
        add_to_playlist()
    elif choice == 3:
        reorder_playlist()
    else:
        print("Invalid option: ")


while main_menu():
    print("---------")

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

# Classes are good way make data together.

class User():
	pass
class Songs():
	pass
class PlayLists():
	pass

# Creating a menu:
def create_menu():
	try:
		print(
			"1.Create User:\n"
			"2.Login:\n"
			"3.Delete User:\n"
			"4.Browse:\n"
			"5.Mange Playlist:\n"
			"6.Upload song:\n"
			"7.Exit:\n"
		)

		option = int(input("Enter the menu option: "))

		if option == 1:
			create_user()
		elif option == 2:
			create_login()
		elif option == 3:
			delete_user()
		elif option == 4:
			browse_menu()
		elif option == 5:
			playlist_menu()
		elif option == 6:
			add_song()
		elif option == 7:
			return False
		else:
			print("Incorrect Options:")
	except ValueError:
		print("Please enter a number")
	return True


users_dic = {}  # empty user dict
songs_dic = {}  # empty song dict
current_users = ""  # empty user string


def create_user():
	user_name = input("Enter User-Name: ")
	user_password = input("Enter Passwords:")
	users_dic[user_name] = user_password
	print("User Crated Successfully.")


def create_login():
	user_name = input("Enter User-Name: ")
	user_password = input("Enter Password: ")
	if user_name in users_dic and users_dic[user_name] == user_password:
		current_users = user_name
		print("Valid User-Login")
	else:
		print("Incorrect Option ")


def delete_user():
	# del user_dic[user_name]
	user_name = input("Which user do you want to delete?")
	users_dic.pop(user_name)


def browse_menu():
	print("1.List all songs\n"
		  "2.List all artists\n"
		  "3.List all albums\n"
		  )

	option = int(input("Enter the menu options: "))
	if option == 1:
		list_songs()
	elif option == 2:
		list_artists()
	elif option == 3:
		list_albums()
	else:
		print("Incorrect Option")


def add_song():
	title = input("Enter the song title: ")
	artist = input("Enter the song artist: ")
	album = input("Enter the song album: ")
	track = input("Enter the track number: ")
	songs_dic[title] = artist
	songs_dic[title] = album
	songs_dic[title] = track


def list_songs():
	songs = songs_dic.keys()
	for song in songs:
		print(song)


def list_artists():
	artists = songs_dic.keys()
	for artists in artists:
		print(artists)


def list_albums():
	albums = songs_dic.keys()
	for album in albums:
		print(album)


def playlist_menu():
	print("1.Create playlist\n"
		  "2.Add song playlist\n"
		  "3.Reorder song in playlist\n"
		  )

	option = int(input("Enter the menu option: "))
	if option == 1:
		create_playlist()
	elif option == 2:
		add_to_playlist()
	elif option == 3:
		reorder_playlist()
	else:
		print("Invalid option: ")


def create_playlist():
	play_name = input("Enter playlist name: ")
	users_dic[current_users]["playlist"][play_name] = []


def add_to_playlist():
	play_name = input("Enter playlist name: ")
	play_list = users_dic[current_users]["playlists"][play_name]

	song_name = input("Enter song name: ")
	song = songs_dic[song_name]

	play_list.append(song)


def remove_from_playlist():
	play_name = input("Enter playlist name: ")
	play_list = users_dic[current_users]["playlists"][play_name]

	song_name = input("Enter song name: ")
	song = songs_dic[song_name]

	play_list.remove(song)


def reorder_playlist():
	play_name = input("Enter playlist name: ")
	play_list = users_dic[current_users]["playlists"][play_name]

	song_name = input("Enter song name: ")
	song = songs_dic[song_name]

	index = input("Enter where you would like to move the song: ")

	play_list.remove(song)
	play_list.insert(index, song)


while create_menu():
	print("==================")

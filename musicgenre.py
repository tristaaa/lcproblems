class Solution:
    def favoriteGenre(self, userSongs, songGenres):
        """
        Given a map Map<String, List<String>> userSongs with user names as keys and 
        a list of all the songs that the user has listened to as values.

        Also given a map Map<String, List<String>> songGenres, with song genre as keys and 
        a list of all the songs within that genre as values. The song can only belong to only one genre.

        The task is to return a map Map<String, List<String>>, where the key is a user name and
        the value is a list of the user's favorite genre(s). 
        Favorite genre is the **top most** listened to genre. 
        A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.
        """
        import collections
        song2gen = {song:gen for gen in songGenres if songGenres[gen] for song in songGenres[gen]}; 
        favgen = {}
        for user in userSongs: 
            maxcnt=0
            favgen[user]=[]
            favgencnt=collections.defaultdict(int)
            for song in userSongs[user]:
                if song in song2gen:
                    favgencnt[song2gen[song]]+=1
                    if favgencnt[song2gen[song]]>maxcnt: maxcnt=favgencnt[song2gen[song]]
            for gen in favgencnt:
                if favgencnt[gen]==maxcnt:
                  favgen[user].append(gen)
        return favgen


userSongs = {  
  "David": ["song1", "song2", "song3", "song4", "song8"],
  "Emma":  ["song5", "song6", "song7"],
  "John": []
}
songGenres = {  
  "Rock":    ["song1", "song3"],
  "Dubstep": ["song7"],
  "Techno":  ["song2", "song4"],
  "Pop":     ["song5", "song6"],
  "Jazz":    None,
  "Metal": []
}
# Expected Output: {  
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"],
#    "John":  []
# }

sol = Solution()
print("Given the dict userSongs {k(user):v(list of songs)}: \n",userSongs)
print("\nand the dict songGenres {k(genre):v(list of songs)}: \n",songGenres)
print("\noutput the dict favoriteGenre {k(user):v(list of most favorite genres(s))}: \n",sol.favoriteGenre(userSongs,songGenres))


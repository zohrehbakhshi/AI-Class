playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]


print("Number of songs in Playlist:", len(playlist))

print("First song in Playlist:", playlist[0])
print("Last song in Playlist:", playlist[-1])

playlist.append("Dynamite")
playlist.remove("Believer")

playlist.sort()
print("Sorted Playlist:", playlist)

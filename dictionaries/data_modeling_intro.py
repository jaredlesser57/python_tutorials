playlist = {'title': 'patagonia bus', 
            'author': 'jared lesser',
            'songs': [
                {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
                {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
                {'title': 'meowmix', 'artist': ['kitty', 'djcat'], 'duration': 4.25}
            ] 
        }

total_time = 0
for song in playlist['songs']:
    total_time += song['duration']

print(total_time)

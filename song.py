# List of songs with their durations (in minutes)

from functools import reduce
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), 
('Song 3', 6.55), ('Leave The Door Open', 4.02), 
('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
def more_than_five(playlist):
  return playlist[1]>5.00
def minutes_to_seconds(playlist):
  duration = playlist[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 100
  return minutes*60 + round(seconds)
def add_song(total,duration):
  duration = playlist[1]
  return total+duration
filtered_songs = list(filter(more_than_five, playlist))

convert_to_seconds = list(map(minutes_to_seconds, playlist))

total_playtime = reduce(add_song, playlist, 0)

print(filtered_songs) 
print(convert_to_seconds)
print(total_playtime)
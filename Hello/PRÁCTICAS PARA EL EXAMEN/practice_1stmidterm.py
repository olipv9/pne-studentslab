class Prueba_music:
    def __init__(self, song, genre, rhythm):
        self.song = song
        self.genre = genre
        self.rhythm = rhythm

    def __str__(self):
        return f'The song {self.song} belongs to the genre {self.genre}'

    def rhythm_specify(self):
        return f'It has an {self.rhythm} rhythm.'


class Pop(Prueba_music):
    def __init__(self, song, genre, rhythm):
        super().__init__(song, genre, rhythm)
        self.dance = 'Yes'
        self.artist = ''
    def artist_ask(self):
        artist = input(f'To which artist does "{self.song}" belong to? ')
        self.artist = artist

    def __str__(self):
        return f'You chose a song "{self.song}" which belongs to the Pop genre (Upbeat), precisely to the artist {self.artist}'


music_guess = Pop('Yes and', 'Pop', 'Upbeat')
print(music_guess.rhythm_specify())
music_guess.artist_ask()
print(music_guess)
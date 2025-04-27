class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movies):
        self.movies.append(movies)

class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movies):
        self.movies.append(movies)
        return f'Комедии: {self.movies}'
    
class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movies):
        self.movies.append(movies)
        return f'Драмы: {self.movies}'
    
comedy = Comedy()
drama = Drama()
    
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))
from project.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction=AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)
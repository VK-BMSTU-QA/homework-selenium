from pageobjects.base.moviecardlist import MovieCardListPage


class GenresPage(MovieCardListPage):
    def open(self, url='action'):
        super().open('genres/' + url)

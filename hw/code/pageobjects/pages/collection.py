from pageobjects.base.moviecardlist import MovieCardListPage


class CollectionPage(MovieCardListPage):
    def open(self, num=1):
        super().open('collections/'+str(num))

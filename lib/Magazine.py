class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.all_magazines.append(self)
        self._articles = []

    def name(self):
        return self._name

    def category(self):
        return self._category

    def all(self):
        return Magazine.all_magazines

    def contributors(self):
        return list(set(article.author() for article in self._articles))

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.all_magazines:
            titles.extend(article.title() for article in magazine._articles)
        return titles

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author()
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1
        return [author for author, count in authors_count.items() if count > 2]

#!/usr/bin/env python3
import ipdb
import sys
sys.path.append('lib')


if __name__ == '__main__':

    from Author import Author
    from Magazine import Magazine
    from Article import Article

    # Create some authors
    author1 = Author("Kevin")
    author2 = Author("Moino")

    # Create some magazines
    magazine1 = Magazine("Tech Magazine", "Technology")
    magazine2 = Magazine("Fashion Weekly", "Fashion")

    # Add articles for authors in magazines
    author1.add_article(magazine1, "Intro to Python Programming")
    author1.add_article(magazine2, "Trends in Tech")
    author2.add_article(magazine1, "Artificial Intelligence")

    # Test methods
    print("Author:", author1.name())
    print("Author's articles:", [article.title() for article in author1.articles()])
    print("Author's magazines:", [magazine.name() for magazine in author1.magazines()])
    print("Author's topic areas:", author1.topic_areas())

    print("Magazine:", magazine1.name())
    print("Magazine's contributors:", [author.name() for author in magazine1.contributors()])
    print("Magazine's article titles:", magazine1.article_titles())
    print("Contributing authors with more than 2 articles:", [author.name() for author in magazine1.contributing_authors()])

# DO NOT REMOVE THIS
    ipdb.set_trace()


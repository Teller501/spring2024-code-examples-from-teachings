from datetime import datetime


class Book:
    def __init__(self, title, author, publication_year=None):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_description(self) -> str:
        return f"{self.title} by {self.author}{', published in ' + str(self.publication_year) if self.publication_year else ''}"

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value: int):
        if value is None:
            self._publication_year = value
        elif value < 1450 or value > datetime.now().year:
            raise ValueError(
                "Publication Year cannot be before 1450 or in the future")
        else:
            self._publication_year = value

    @classmethod
    def create_ebook(cls):
        current_year = datetime.now().year
        return Book('E-Book', 'Various Authors', current_year)

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return bool(title)

"""Example models for testing django-model-info."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorQuerySet(models.QuerySet):
    """Example Author queryset."""

    def authors_with_last_name(self, last_name: str):
        """Return authors with the last name."""
        return self.filter(last_name=last_name)

    def authors_with_birth_date(self, birth_date: str):
        """Return authors with the birth date."""
        return self.filter(birth_date=birth_date)


class AuthorManager(models.Manager):
    """Example Author manager."""

    def get_queryset(self):
        """Return the queryset."""
        super().get_queryset().all()


class Author(models.Model):
    """Example Author model."""

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    objects = AuthorManager.from_queryset(AuthorQuerySet)()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Return the full name of the author."""
        return f"{self.first_name} {self.last_name}"



class AuthorProxy(Author):
    """Example Author proxy model."""

    class Meta:
        """Meta options for AuthorProxy."""

        proxy = True
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class UnmanagedAuthor(models.Model):
    """Example UnmanagedAuthor model."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, help_text=_("The last name of the author."))
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Return the full name of the author."""
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    """Example Publisher model."""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    """Example Book model."""

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    def get_authors(self):
        """Return a comma-separated list of authors."""
        return ", ".join([author.full_name for author in self.authors.all()])


class Store(models.Model):
    """Example Store model."""

    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_books(self):
        """Return a comma-separated list of books."""
        return ", ".join([book.title for book in self.books.all()])

    def get_books_with_author(self, author: str):
        """Return a comma-separated list of books with the author."""
        return ", ".join([book.title for book in self.books.filter(authors__first_name=author)])


class Profile(models.Model):
    """Example Profile model."""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    birth_date = models.DateField()
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.user.username

    def _some_private_method(self):
        """A private method."""
        pass

    class Meta:
        """Meta options for Profile."""
        abstract = True

class ConcreteProfile(Profile):
    """Example ConcreteProfile model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for ConcreteProfile."""
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ["user__username"]
        db_table = "profiles"
        db_tablespace = "profiles_tablespace"
        db_table_comment = "Table for storing user profiles"
        abstract = False

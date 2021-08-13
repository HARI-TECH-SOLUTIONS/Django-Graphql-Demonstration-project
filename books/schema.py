from django.db.models import query
import graphene
from graphene_django import DjangoObjectType
from .models import Books
from django.db.models import Q


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        # fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType, search=graphene.String())

    def resolve_all_books(self, info, search=None, **kwargs):
        if search:

            filter = (
                Q(title__icontains=search)
            )

            return Books.objects.filter(filter)

        return Books.objects.all()


schema = graphene.Schema(query=Query)

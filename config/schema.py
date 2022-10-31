# # Graphql needs schema.
# # Create type 1. Query, Mutation
import strawberry
import typing


# @strawberry.type
# class Movie:
#     pk: int
#     title: str
#     year: int
#     rating: int


# movies = [
#     Movie(pk=1, title="GOdfather", year=1990, rating=10),
# ]


# def movies() -> typing.List[Movie]:
#     return movies


# def movie(pk: int) -> Movie:
#     return movies[pk - 1]


# def add_movie(title: str, year: int, rating: int) -> Movie:
#     new_movie = Movie(
#         pk=len(movies) + 1,
#         title=title,
#         year=year,
#         rating=rating,
#     )
#     movies.append(new_movie)
#     return new_movie


# # Type : Query
# @strawberry.type
# # you have to type typing
# class Query:
#     # Strawberry make looks your code, generate schema for you.
#     # @strawberry.field
#     movies: typing.List[Movie] = strawberry.field(resolver=movies)
#     movie: Movie = strawberry.field(resolver=movie)


# @strawberry.type
# class Mutation:
#     add_movie: Movie = strawberry.mutation(resolver=add_movie)


# # Create Schema(Query + Mutation)
# schema = strawberry.Schema(
#     query=Query,
#     mutation=Mutation,
# )
from rooms import schema as rooms_schema


@strawberry.type
class Query(rooms_schema.Query):
    pass


@strawberry.type
class Mutation:
    pass


schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
)

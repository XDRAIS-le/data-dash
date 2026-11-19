import graphene

from .data import USERS, POSTS, COMMENTS


class CommentType(graphene.ObjectType):
    id = graphene.Int()
    author = graphene.String()
    text = graphene.String()


class PostType(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    body = graphene.String()
    likes = graphene.Int()
    comments = graphene.List(CommentType)

    def resolve_comments(parent, info):
        return [c for c in COMMENTS if c["post_id"] == parent["id"]]


class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    city = graphene.String()
    bio = graphene.String()
    joined = graphene.String()
    posts = graphene.List(PostType)

    def resolve_posts(parent, info):
        return [p for p in POSTS if p["user_id"] == parent["id"]]


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_users(root, info):
        return USERS

    def resolve_user(root, info, id):
        return next((u for u in USERS if u["id"] == id), None)


schema = graphene.Schema(query=Query)

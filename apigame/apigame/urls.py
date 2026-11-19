from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from game import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lab/", views.lab, name="lab"),

    # ---------- REST API: one URL per resource ----------
    path("api/users/", views.user_list),
    path("api/users/<int:user_id>/", views.user_detail),
    path("api/users/<int:user_id>/posts/", views.user_posts),
    path("api/posts/<int:post_id>/comments/", views.post_comments),

    # ---------- GraphQL API: ONE endpoint for everything ----------
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

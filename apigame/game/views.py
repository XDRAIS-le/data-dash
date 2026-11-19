from django.http import JsonResponse, Http404
from django.shortcuts import render

from .data import USERS, POSTS, COMMENTS


def index(request):
    """The arcade game (arrow keys)."""
    return render(request, "game/game.html")


def lab(request):
    """The side-by-side REST vs GraphQL lab."""
    return render(request, "game/lab.html")


# ---------------- REST endpoints ----------------
# Each endpoint returns a FIXED shape: the client gets every field,
# whether it needs it or not (over-fetching), and related data needs
# extra requests (under-fetching).

def user_list(request):
    return JsonResponse(USERS, safe=False)


def user_detail(request, user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user is None:
        raise Http404("User not found")
    return JsonResponse(user)


def user_posts(request, user_id):
    return JsonResponse([p for p in POSTS if p["user_id"] == user_id], safe=False)


def post_comments(request, post_id):
    return JsonResponse([c for c in COMMENTS if c["post_id"] == post_id], safe=False)

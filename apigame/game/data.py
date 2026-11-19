"""Fake in-memory database shared by the REST API and the GraphQL API."""

USERS = [
    {"id": 1, "name": "Sara", "email": "sara@uni.edu", "phone": "555-0101", "city": "Cairo",
     "bio": "Backend student who loves APIs and coffee. " * 4, "joined": "2024-01-10"},
    {"id": 2, "name": "Omar", "email": "omar@uni.edu", "phone": "555-0102", "city": "Tunis",
     "bio": "Frontend dev, React fan, part-time gamer. " * 4, "joined": "2024-03-22"},
    {"id": 3, "name": "Lina", "email": "lina@uni.edu", "phone": "555-0103", "city": "Rabat",
     "bio": "Mobile developer building apps for slow networks. " * 4, "joined": "2024-06-05"},
]

POSTS = [
    {"id": 1, "user_id": 1, "title": "Intro to REST", "likes": 12,
     "body": "REST exposes resources at URLs and uses HTTP verbs like GET and POST. " * 6},
    {"id": 2, "user_id": 1, "title": "Why GraphQL?", "likes": 30,
     "body": "GraphQL lets the client ask for exactly the fields it needs in one request. " * 6},
    {"id": 3, "user_id": 1, "title": "SOAP is not dead", "likes": 4,
     "body": "Banks and governments still run on SOAP with strict WSDL contracts. " * 6},
    {"id": 4, "user_id": 2, "title": "React + APIs", "likes": 8,
     "body": "Fetching data in React with fetch, Axios and Apollo Client. " * 6},
    {"id": 5, "user_id": 3, "title": "Saving mobile data", "likes": 21,
     "body": "Every kilobyte matters on a 3G connection. " * 6},
]

COMMENTS = [
    {"id": 1, "post_id": 1, "author": "Ali", "text": "Great intro!"},
    {"id": 2, "post_id": 1, "author": "Mona", "text": "Very clear, thanks."},
    {"id": 3, "post_id": 2, "author": "Omar", "text": "GraphQL for the win."},
    {"id": 4, "post_id": 3, "author": "Lina", "text": "My bank still uses it!"},
    {"id": 5, "post_id": 3, "author": "Ali", "text": "XML everywhere..."},
    {"id": 6, "post_id": 4, "author": "Sara", "text": "Nice examples."},
    {"id": 7, "post_id": 5, "author": "Omar", "text": "So true on 3G."},
]

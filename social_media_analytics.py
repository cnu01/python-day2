# Social media data
posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today!", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun!", "likes": 22, "tags": ["python", "learning"]}
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120}
}

def get_popular_tags():
    all_tags = []
    for post in posts:
        all_tags.extend(post["tags"])
    return list(set(all_tags))


def get_user_posts(username):
    return [post for post in posts if post["user"] == username]

def get_total_likes_for_user(username):
    user_posts = get_user_posts(username)
    return sum(post["likes"] for post in user_posts)



def get_user_stats(username):
    if username not in users:
        return None
    
    stats = {
        "username": username,
        "followers": users[username]["followers"],
        "following": users[username]["following"],
        "total_posts": len(get_user_posts(username)),
        "total_likes": get_total_likes_for_user(username)
    }
    return stats


if __name__ == "__main__":
   
    alice_posts = get_user_posts("alice")
    print(alice_posts)
    
    
    alice_stats = get_user_stats("alice")
    print(alice_stats)
    
   
    tags = get_popular_tags()
    print(tags)

    get_total_likes_for_user = get_total_likes_for_user("bob")
    print('User Likes', get_total_likes_for_user)
import re
BANNED_WORDS = ["bad", "toxic", "hate"]
INPUT_FILE = "posts.txt"
OUTPUT_CLEAN_FILE = "cleaned_posts.txt"
OUTPUT_LINK_FILE = "links_found.txt"
def load_posts(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print("posts.txt not found. Creating sample file...\n")
        sample_posts = [
            "User123: This is a bad post check http://example.com\n",
            "User456: I love learning Python\n",
            "User123: Stop spreading hate visit https://dangerous-link.com\n",
            "User789: This platform is toxic sometimes\n",
            "User456: Visit http://school.edu for notes\n"
        ]

        with open(filename, "w") as file:
            file.writelines(sample_posts)

        return sample_posts

def mask_banned_words(post):
    flagged = False

    for word in BANNED_WORDS:
        pattern = re.compile(r"\b" + word + r"\b", re.IGNORECASE)
        if pattern.search(post):
            flagged = True
        post = pattern.sub("***", post)
    return post, flagged
    
def extract_links(post):
    url_pattern = r"https?://\S+"
    return re.findall(url_pattern, post)
    
def extract_username(post):
    return post.split(":")[0]

def save_to_file(filename, content):
    with open(filename, "w") as file:
        for line in content:
            file.write(line)

def moderate_posts(posts):
    cleaned_posts = []
    all_links = []
    user_violation_count = {}
    flagged_count = 0

    for post in posts:
        username = extract_username(post)
        cleaned_post, flagged = mask_banned_words(post)
        links = extract_links(post)
        all_links.extend(links)
        if username not in user_violation_count:
            user_violation_count[username] = 0
        if flagged:
            flagged_count += 1
            user_violation_count[username] += 1
        cleaned_posts.append(cleaned_post)

    return cleaned_posts, all_links, user_violation_count, flagged_count

def main():
    print("Starting Social Media Content Moderation System...\n")
    posts = load_posts(INPUT_FILE)
    if not posts:
        print("No posts available to process.")
        return
    cleaned_posts, links, user_stats, flagged_total = moderate_posts(posts)

    save_to_file(OUTPUT_CLEAN_FILE, cleaned_posts)

    save_to_file(OUTPUT_LINK_FILE, [link + "\n" for link in links])

    total_posts = len(posts)

    clean_posts = total_posts - flagged_total

    print("Moderation Summary Report\n")
    print("Total Posts Screened :", total_posts)
    print("Clean Posts          :", clean_posts)
    print("Flagged Posts        :", flagged_total)
    print("\nUser Violation Statistics:")
    for user, violations in user_stats.items():
        print(user, "->", violations, "flagged post(s)")
    print("\nCleaned posts saved in :", OUTPUT_CLEAN_FILE)
    print("Extracted links saved in :", OUTPUT_LINK_FILE)

if __name__ == "__main__":
    main()
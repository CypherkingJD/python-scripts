import feedparser

# Define a list of RSS feed URLs
rss_urls = [
    #https://www.itu.int/rss/,
    #https://www.infoworld.com/about/rss/
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    #https://rss.app/blog/top-rss-feeds/38-best-technology-websites-to-get-rss-feeds-from
    #https://www.techradar.com/how-to/techradar-rss add these
    #https://arstechnica.com/rss-feeds/ add these
    "https://www.techrepublic.com/rssfeeds/articles/",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "http://feeds.bbci.co.uk/news/business/rss.xml",
    "http://feeds.bbci.co.uk/news/health/rss.xml",
    "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
    "http://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Space.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml",
    #something in cnn causes an exception
    #
    #"http://rss.cnn.com/rss/cnn_topstories.rss",
    #"http://rss.cnn.com/rss/cnn_world.rss",
    #"http://rss.cnn.com/rss/cnn_us.rss",
    #"http://rss.cnn.com/rss/money_latest.rss",
    #"http://rss.cnn.com/rss/cnn_tech.rss",
    #"http://rss.cnn.com/rss/cnn_health.rss",
    #
    #https://www.cnbc.com/rss-feeds/ add these
    "https://www.wired.com/feed/category/business/latest/rss",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    "https://www.wired.com/feed/category/science/latest/rss",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://www.wired.com/feed/category/backchannel/latest/rss",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://defence-blog.com/feed/",
    "https://www.globalissues.org/news/feed"
    # Add more RSS feed URLs as needed
]

# Define the keyword related to the specific subject of technology
keyword = "AI"

# Initialize counters
total_articles = 0  # Total articles searched
found_articles = 0  # Articles found related to the keyword

# Iterate through the list of RSS feed URLs
for rss_url in rss_urls:
    print(f"Searching in {rss_url}...")

    # Fetch and parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Initialize a flag to check if any articles were found for this source
    articles_found_for_source = False

    # Iterate through the entries and display articles related to the keyword
    for entry in feed.entries:
        total_articles += 1
        if keyword.lower() in entry.title.lower() or keyword.lower() in entry.summary.lower():
            found_articles += 1
            articles_found_for_source = True
            print("Title:", entry.title)
            print("Link:", entry.link)
            #print("Publication Date:", entry.published)
            #print("Description:", entry.summary)

            # Check if source information is available
            #if entry.source:
                #print("Source Title:", entry.source.title)
                #print("Source URL:", entry.source.href)

            print("-" * 50)

    # Check if no articles were found for this source
    if not articles_found_for_source:
        print(f"No articles related to '{keyword}' found in feed.")

# Report the results
if found_articles > 0:
    print(f"Found {found_articles} articles in feed.")
else:
    print(f"No articles related to '{keyword}' found in {total_articles} articles searched.")

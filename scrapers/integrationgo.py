
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}


def scrape_integrationgo_article(blog_url):
    response = requests.get(blog_url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.select_one("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    content = soup.select_one("div.post-content.reveal-content")
    article_text = ""

    if content:
        elements = content.find_all(["h2", "h3", "p"])

        for element in elements:
            text = element.get_text(" ", strip=True)

            if text:
                article_text += text + "\n\n"

    return {
        "title": title,
        "blog_url": blog_url,
        "content": article_text
    }


def scrape_integrationgo():
    url = "https://integrationgo.com/blogs"
    
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the last pagination page
    last_page = 1

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if "/blogs/page/" in href:
            page_number = link.get_text(strip=True)

            if page_number.isdigit():
                last_page = max(last_page, int(page_number))

    print("IntegrationGo last page:", last_page)

    all_blogs = []
    seen_urls = set()

    # Visit every listing page
    for page_number in range(1, last_page + 1):

        if page_number == 1:
            url = url
        else:
            url = f"https://integrationgo.com/blogs/page/{page_number}"

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        print("\nIntegrationGo scraping page:", page_number)

        blogs = soup.find_all("article", class_="blog-card")

        print("Blog cards found:", len(blogs))

        for blog in blogs:
            link = blog.find("a", href=True)

            if not link:
                continue

            blog_url = link["href"].rstrip("/")

            if blog_url in seen_urls:
                continue

            seen_urls.add(blog_url)

            blog_data = scrape_integrationgo_article(blog_url)

            all_blogs.append(blog_data)

            print("Scraped:", blog_data["title"])

    print("\nTotal IntegrationGo blogs:", len(all_blogs))

    return all_blogs

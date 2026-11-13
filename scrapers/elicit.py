
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}


def scrape_blog(blog_url):

    blog_response = requests.get(blog_url, headers=headers, timeout=20)
    blog_response.raise_for_status()

    blog_soup = BeautifulSoup(blog_response.text, "html.parser")

    title_tag = blog_soup.select_one("h1.xpro-post-title")
    title = title_tag.get_text(strip=True) if title_tag else None

    content = blog_soup.select_one(".xpro-elementor-content")
    article_text = ""

    if content:
        elements = content.find_all(["h2", "h3", "p"])

        for element in elements:
            text = element.get_text(" ", strip=True)

            if text:
                article_text += text + "\n\n"

    return {
        "blog_url": blog_url,
        "title": title,
        "content": article_text
    }


def scrape_elicit():

    url = "https://elicittechnology.com/blogs/"

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    last_page = 1

    for link in links:
        href = link["href"]

        if "/blogs/page/" in href:
            page_number = link.get_text(strip=True)

            if page_number.isdigit():
                last_page = max(last_page, int(page_number))

    print("Elicit last page:", last_page)

    all_blogs = []

    for page_number in range(1, last_page + 1):

        if page_number == 1:
            url = "https://elicittechnology.com/blogs/"
        else:
            url = f"https://elicittechnology.com/blogs/page/{page_number}/"

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        print("\nElicit scraping page:", page_number)

        blogs = soup.select("article.uc_post_grid_style_one_item")

        print("Blogs found:", len(blogs))

        for blog in blogs:

            link = blog.find_parent("a")
            blog_url = link.get("href") if link else None

            if not blog_url:
                continue

            article_data = scrape_blog(blog_url)

            blog_data = {
                "title": article_data["title"],
                "blog_url": blog_url,
                "content": article_data["content"]
            }

            all_blogs.append(blog_data)

            print("Scraped:", blog_data["title"])

    print("\nTotal Elicit blogs:", len(all_blogs))

    return all_blogs

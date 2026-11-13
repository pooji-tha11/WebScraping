import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}



def scrape_wisebi_article(blog_url):
    try:
        response = requests.get(blog_url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.select_one("h1.text-xxxl")
        title = title_tag.get_text(strip=True) if title_tag else None

        content = soup.select_one("div.content")
        article_text = content.get_text("\n", strip=True) if content else ""

        return {
            "title": title,
            "blog_url": blog_url,
            "content": article_text
        }

    except requests.exceptions.HTTPError as e:
        print(f"Skipping unavailable article: {blog_url}")
        print(f"Reason: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed for {blog_url}: {e}")
        return None



def scrape_wisebi():
    url = "https://wisebi.com/blogs/"

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

    print("WiseBI last page:", last_page)

    all_blogs = []
    seen_urls = set()

    # Visit every listing page
    for page_number in range(1, last_page + 1):

        if page_number == 1:
            url = url
        else:
            url = f"https://wisebi.com/blogs/page/{page_number}/"

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        print("\nWiseBI scraping page:", page_number)

        # Collect individual blog links
        for link in soup.find_all("a", href=True):
            blog_url = link["href"].rstrip("/")

            if (
                blog_url.startswith("https://wisebi.com/blogs/")
                and "/blogs/page/" not in blog_url
                and blog_url != "https://wisebi.com/blogs"
                and blog_url not in seen_urls
            ):
                seen_urls.add(blog_url)

                blog_data = scrape_wisebi_article(blog_url)
                if blog_data:
                    all_blogs.append(blog_data)
                    print("Scraped:", blog_data["title"])
                else:
                    print("Article skipped.")
    print("\nTotal WiseBI blogs:", len(all_blogs))

    return all_blogs
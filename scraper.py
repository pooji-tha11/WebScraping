from database import save_blogs

from scrapers.elicit import scrape_elicit
from scrapers.wisebi import scrape_wisebi
from scrapers.integrationgo import scrape_integrationgo
from scrapers.carguber import scrape_carguber
from scrapers.sfltech import scrape_sfltech

all_blogs = []

print("\n========== SCRAPING ELICIT ==========")
elicit_blogs = scrape_elicit()
all_blogs.extend(elicit_blogs)

print("\n========== SCRAPING WISEBI ==========")
wisebi_blogs = scrape_wisebi()
all_blogs.extend(wisebi_blogs)

print("\n========== SCRAPING INTEGRATIONGO ==========")
integrationgo_blogs = scrape_integrationgo()
all_blogs.extend(integrationgo_blogs)

print("\n========== SCRAPING CARGUBER ==========")
carguber_blogs = scrape_carguber()
all_blogs.extend(carguber_blogs)

print("\n========== SCRAPING SFLTECH ==========")
sfltech_blogs = scrape_sfltech()
all_blogs.extend(sfltech_blogs)



print("\n========== FINAL SUMMARY ==========")


print("WiseBI:", len(wisebi_blogs))
print("IntegrationGo:", len(integrationgo_blogs))
print("Carguber:", len(carguber_blogs))
print("Elicit:", len(elicit_blogs))
print("SFLTech:", len(sfltech_blogs))

print("-----------------------------")
print("TOTAL BLOGS COLLECTED:", len(all_blogs))



print("\n========== SAVING TO DATABASE ==========")

save_blogs(all_blogs)


# import os
# from dotenv import load_dotenv

# load_dotenv()


# import requests
# from bs4 import BeautifulSoup

# import mysql.connector
# from datetime import datetime

# headers = {"User-Agent": "Mozilla/5.0"}



# def scrape_blog(blog_url):

#     blog_response = requests.get(blog_url, headers=headers, timeout=20)
#     blog_response.raise_for_status()

#     blog_soup = BeautifulSoup(blog_response.text, "html.parser")

#     # Extract title
#     title_tag = blog_soup.select_one("h1.xpro-post-title")
#     title = title_tag.get_text(strip=True) if title_tag else None

#     # Extract article content
#     content = blog_soup.select_one(".xpro-elementor-content")
#     article_text = ""

#     if content:
#         elements = content.find_all(["h2", "h3", "p"])

#         for element in elements:
#             text = element.get_text(" ", strip=True)

#             if text:
#                 article_text += text + "\n\n"


#     return {
#         "blog_url": blog_url,
#         "title": title,
#         "content": article_text
#     }



# def scrape_wisebi(blog_url):

#     response = requests.get(blog_url, headers=headers, timeout=20)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract title
#     title_tag = soup.select_one("h1.text-xxxl")
#     title = title_tag.get_text(strip=True) if title_tag else None

#     # Extract complete article content
#     content = soup.select_one("div.content")

#     article_text = ""

#     if content:
#         article_text = content.get_text("\n", strip=True)

#     return {
#         "title": title,
#         "blog_url": blog_url,
#         "content": article_text
#     }


# url = "https://elicittechnology.com/blogs/"


# response = requests.get(url, headers=headers)
# response.raise_for_status()

# soup = BeautifulSoup(response.text, "html.parser")

# links = soup.find_all("a", href=True)

# last_page = 1

# for link in links:
#     href = link["href"]

#     if "/blogs/page/" in href:
#         page_number = link.get_text(strip=True)

#         if page_number.isdigit():
#             last_page = max(last_page, int(page_number))

# print("Last page:", last_page)

# ##--------Used to find the structure of the Blog cards and the elemts in those Blog cards to extract such as the title, description, image and the ID -----------##
# # print("\nHTML STRUCTURE:")

# # for element in soup.find_all(["article", "h1", "h2"]):

# #     print(
# #         "Tag:", element.name,
# #         "| Class:", element.get("class"),
# #         "| ID:", element.get("id")
# #     )


# # # Find all blog cards

# # blogs = soup.select("article.uc_post_grid_style_one_item")

# # print("Total blogs found:", len(blogs))

# # for blog in blogs:

# #     print("\n--------------------------")

# #     print(blog.prettify())



# # Using CSS Selectors to find all the blogs
# # blogs = soup.select("article.uc_post_grid_style_one_item")


# # # To show the total number of blogs found on the page
# # print("Total blogs:", len(blogs))

# ## ----------- The Blog contet without the actual URL to the Blog page which is wrapped in the parent anchor tag of the Blog card. ---------##
# # Getting each blogs title, desc, image and the ID from the Blog Card
# # for blog in blogs:

# #     # Extract title
# #     title = blog.select_one(".ue_p_title").get_text(strip=True)

# #     # Extract description
# #     description = blog.select_one(".uc_post_text").get_text(strip=True)

# #     # Extract image URL
# #     image = blog.select_one(".uc_post_image img")

# #     image_url = image["src"] if image else None

# #     # Extract WordPress post ID
# #     post_id = blog.get("id")

# #     print("\n----------------------------")
# #     print("Post ID:", post_id)
# #     print("Title:", title)
# #     print("Description:", description)
# #     print("Image:", image_url)
# ##---------------------------------------------------##


# all_blogs = []

# for page_number in range(1, last_page + 1):

#     if page_number == 1:
#         url = "https://elicittechnology.com/blogs/"
#     else:
#         url = f"https://elicittechnology.com/blogs/page/{page_number}/"

#     response = requests.get(url, headers=headers, timeout=20)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")

#     print("\nScraping page:", page_number)

#     # Extract blog cards from the current page
#     blogs = soup.select("article.uc_post_grid_style_one_item")

#     print("Blogs found on this page:", len(blogs))

#     for blog in blogs:

#         title = blog.select_one(".ue_p_title").get_text(strip=True)


#         link = blog.find_parent("a")
#         blog_url = link.get("href") if link else None

#         # Scrape the individual article
#         article_data = scrape_blog(blog_url) if blog_url else {}

#         # Combine all information
#         blog_data = {
#             "title": title,
#             "blog_url": blog_url,
#             "content": article_data.get("content")
#         }

#         all_blogs.append(blog_data)

#         print("Scraped:", title)

# print("\nTotal blogs scraped:", len(all_blogs))




# # first_blog = blogs[0]

# # link = first_blog.find_parent("a")

# # if link:
# #     print("Article URL:", link.get("href"))
# # else:
# #     print("No parent link found")


# ##--------------------- Used to find the URL to the actual blog page which was wrapped in the parent anchor tag of the blog card----------##
# # for blog in blogs:
# #     link = blog.find_parent("a")

# #     if link:
# #         print(link.get("href"))






# ##--------------------Used to find the structure of the actual Blog page using the URL found from the previous step to extract the Different tags and the classes from the first blog --------------##
# # blog_url = "https://elicittechnology.com/blogs/how-can-cargowise-ai-agents-help-freight-forwarders-build-smarter-logistics-operations/"

# # blog_response = requests.get(blog_url, headers=headers, timeout=20)

# # print("Status Code:", blog_response.status_code)

# # blog_soup = BeautifulSoup(blog_response.text, "html.parser")

# # print("Page Title:", blog_soup.title.get_text(strip=True))




# # for tag in blog_soup.find_all(["h1", "h2", "h3", "p"]):
# #     print("Tag:", tag.name)
# #     print("Class:", tag.get("class"))
# #     print("Text:", tag.get_text(strip=True)[:150])
# #     print("--------------------")

# #-------------- Used to find the parent elements of the title and the paragraphs to understand the structure of the HTML and how to navigate.--------# 
# # title = blog_soup.select_one("h1.xpro-post-title")

# # parent = title

# # for i in range(6):
# #     if parent:
# #         print("\nLevel:", i)
# #         print("Tag:", parent.name)
# #         print("Class:", parent.get("class"))
# #         print("ID:", parent.get("id"))

# #         parent = parent.parent

# # first_para = blog_soup.select_one("p.wp-block-paragraph")

# # parent = first_para

# # for i in range(8):
# #     if parent:
# #         print("\nLevel:", i)
# #         print("Tag:", parent.name)
# #         print("Class:", parent.get("class"))
# #         print("ID:", parent.get("id"))

# #         parent = parent.parent

# # Find the main article content container

# #-------------------------------------------#
# ## Finding the main content container using CSS selectors and assigning it as an variable for ease of use
# # content = blog_soup.select_one(".xpro-elementor-content")

# # article_text = ""

# # if content:
# #     elements = content.find_all(["h2", "h3", "p"])

# #     for element in elements:
# #         text = element.get_text(" ", strip=True)

# #         if text:
# #             article_text += text + "\n\n"

# # print(article_text)




# # # Inspect metadata related to author and dates

# # for tag in blog_soup.find_all("meta"):

# #     name = tag.get("name")
# #     property = tag.get("property")
# #     content = tag.get("content")

# #     if name or property:
# #         if any(word in str(name or property).lower()
# #                for word in ["author", "date", "published", "modified"]):

# #             print("Name:", name)
# #             print("Property:", property)
# #             print("Content:", content)
# #             print("--------------------")

# # for tag in blog_soup.find_all(["time", "span", "div"]):

# #     text = tag.get_text(" ", strip=True)

# #     if any(word in text.lower()
# #            for word in ["author", "published", "updated", "by"]):

# #         if text and len(text) < 150:
# #             print("Tag:", tag.name)
# #             print("Class:", tag.get("class"))
# #             print("Text:", text)
# #             print("--------------------")

# # author_section = blog_soup.select_one(".lpm")

# # print(author_section.prettify())

# # Extract author
# # author_tag = blog_soup.select_one(".lpm-author")

# # author = author_tag.get_text(strip=True) if author_tag else None


# # # Extract published and modified dates
# # date_tags = blog_soup.select(".lpm-date time")

# # published_date = date_tags[0].get("datetime") if len(date_tags) > 0 else None

# # modified_date = date_tags[1].get("datetime") if len(date_tags) > 1 else None

# # print("Author:", author)
# # print("Published Date:", published_date)
# # print("Modified Date:", modified_date)

# # # Connect to MySQL
# # connection = mysql.connector.connect(
# #     host=os.getenv("DB_HOST"),
# #     user=os.getenv("DB_USER"),
# #     password=os.getenv("DB_PASSWORD"),
# #     database=os.getenv("DB_NAME")
# # )
# # cursor = connection.cursor()

# # print("Connected to MySQL!")


# # insert_query = """
# # INSERT INTO blogs_new (
# #     title, blog_url, content
# # )
# # VALUES (%s, %s, %s)
# # ON DUPLICATE KEY UPDATE
# #     title = VALUES(title),
# #     content = VALUES(content)
# # """

# # for blog in all_blogs:
# #     values = (
# #         blog["title"],
# #         blog["blog_url"],
# #         blog["content"]
# #     )

# #     cursor.execute(insert_query, values)

# # connection.commit()

# # print("All blogs inserted successfully!")

# # cursor.close()
# # connection.close()

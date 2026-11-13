
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()



def save_blogs(all_blogs):

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = connection.cursor()

    query = """
        INSERT INTO blogs_new (title, blog_url, content)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            content = VALUES(content)
    """

    values = [
        (blog["title"], blog["blog_url"], blog["content"])
        for blog in all_blogs
        if blog.get("title") and blog.get("blog_url") and blog.get("content")
    ]

    cursor.executemany(query, values)
    connection.commit()

    print(f"\n{len(values)} valid articles.")
    print(f"Database affected rows: {cursor.rowcount}")

    cursor.close()
    connection.close()

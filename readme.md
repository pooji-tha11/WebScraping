# Elicit Technology Blog Scraper

A Python-based web scraping project that extracts blog information from the [Elicit Technology website](https://elicittechnology.com/blogs/) and stores it in a MySQL database.

## Features

- Extracts blog titles and descriptions.
- Collects blog image URLs and article links.
- Scrapes author names and published/modified dates.
- Extracts the full article content.
- Stores the scraped data in MySQL.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- MySQL
- MySQL Connector for Python

## Project Structure

```text
ElicitScraper/
├── scraper.py
├── .env
├── .gitignore
└── README.md
```

## Setup and Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ElicitScraper
```

2. Install the required packages:

```bash
pip install requests beautifulsoup4 mysql-connector-python python-dotenv
```

3. Create a `.env` file and add your MySQL credentials:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=elicit_blogs
```

4. Create the MySQL database and `blogs` table.

5. Run the scraper:

```bash
python scraper.py
```

## Database

The scraped blog information is stored in a MySQL table named `blogs`.

## Note

The `.env` file contains database credentials and is excluded from version control using `.gitignore`.

## Purpose

This project was built to explore web scraping using Python, HTML parsing with BeautifulSoup, and storing extracted data in a relational database.
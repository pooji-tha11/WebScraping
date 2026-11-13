# Web Scraping & Blog Data Collection

A Python-based web scraping project that collects blog articles from multiple company websites and stores them in a centralized MySQL database.

The project automates the process of discovering blog URLs, extracting article titles and content, and organizing the collected information in a structured format. Instead of manually visiting different websites and collecting articles, the scraper brings the data together in one place.

## Overview

This project is designed to scrape blog articles from multiple websites using Python and BeautifulSoup, then store the extracted information in MySQL.

Each website has its own scraper module because website structures, HTML elements, pagination systems, and article layouts differ.

The collected data is standardized into a common structure before being inserted into the database.

### Key Features

- **Multi-Website Scraping:** Collects blog articles from multiple company websites.
- **Automated Data Extraction:** Extracts article titles, URLs, and full article content.
- **Website-Specific Scrapers:** Uses separate scraping logic for each website.
- **Pagination Handling:** Navigates through multiple blog listing pages to discover articles.
- **Centralized Database:** Stores all collected articles in a single MySQL table.
- **Duplicate Prevention:** Uses unique blog URLs to prevent duplicate records.
- **Database Updates:** Updates existing records when the same URL is scraped again.
- **Modular Architecture:** Makes it easier to add new websites without changing the entire scraping system.

## Websites Covered

The project currently includes scrapers for the following websites:

| Website | Scraper Module | Collection Method |
|---|---|---|
| Elicit Technology | `elicit.py` | Blog listing and pagination |
| WiseBI | `wisebi.py` | Blog listing and pagination |
| IntegrationGo | `integrationgo.py` | Blog listing and pagination |
| Carguber | `carguber.py` | Blog listing and pagination |
| SFL Tech | `sfltech.py` | Manually collected article URLs |

**Note:** SFL Tech uses a manually maintained list of selected Product Resource URLs to avoid collecting unrelated resource categories such as press releases, videos, and case studies.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to websites |
| BeautifulSoup | Parsing HTML and extracting article information |
| MySQL | Storing the scraped data |
| MySQL Workbench | Database management and querying |
| python-dotenv | Managing environment variables |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
WebScraping/
│
├── scraper.py
│
├── database.py
│
├── scrapers/
│   ├── __init__.py
│   ├── elicit.py
│   ├── wisebi.py
│   ├── integrationgo.py
│   ├── carguber.py
│   └── sfltech.py
│
├── .env
├── .gitignore
└── README.md
```

### File Descriptions

**`scraper.py`**

The main entry point of the project.

- Imports all individual website scraper functions.
- Executes each scraper.
- Collects the returned article data into a common list.
- Displays the number of articles collected from each website.
- Sends the combined data to the database module.

**`database.py`**

Handles communication between Python and MySQL.

- Establishes the database connection.
- Inserts scraped articles into the database.
- Uses the blog URL to identify existing records.
- Updates the title and content of existing records when a duplicate URL is encountered.

**`scrapers/`**

Contains individual modules for each website.

Each module is responsible for extracting article information from its respective website and returning the results in a standardized format.

**`.env`**

Stores database configuration and credentials separately from the source code.

**`.gitignore`**

Prevents sensitive files, including `.env`, and unnecessary generated files from being committed to GitHub.

## Database Structure

**Database Name:** `web_scraping_db`

**Table Name:** `blogs_new`

All scraped articles are stored in a single table.

| Column | Data Type | Description |
|---|---|---|
| `id` | INT | Unique auto-incrementing record ID and primary key |
| `title` | TEXT | Title of the blog article |
| `blog_url` | VARCHAR(768) | Original URL of the article; unique |
| `content` | LONGTEXT | Extracted article content |

### Database Design

- `id` acts as the primary key.
- `blog_url` has a unique constraint to prevent duplicate article URLs.
- `content` uses `LONGTEXT` to accommodate lengthy articles.
- All websites share the same table and column structure.

### Duplicate Handling

The project uses MySQL's `INSERT ... ON DUPLICATE KEY UPDATE` functionality.

When a newly scraped article has a URL that already exists:

- A new duplicate row is not created.
- The existing article title is updated.
- The existing article content is updated.

This allows the scraper to be executed multiple times without unnecessarily duplicating records.

## Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd WebScraping
```

### 2. Set Up a Python Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install requests beautifulsoup4 python-dotenv
```

Install the MySQL Python connector required by the implementation in `database.py` if it is not included in the dependencies above.

### 4. Configure MySQL

Make sure MySQL Server is installed and running.

Create the database:

```sql
CREATE DATABASE web_scraping_db;
```

Select the database:

```sql
USE web_scraping_db;
```

Create the table:

```sql
CREATE TABLE blogs_new (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    blog_url VARCHAR(768) NOT NULL UNIQUE,
    content LONGTEXT
);
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the database credentials using the variable names expected by `database.py`.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=web_scraping_db
```

**Important:** Replace the example credentials with your own. Never upload your `.env` file or expose database passwords in a public repository.

### 6. Run the Scraper

Execute the main Python file:

```bash
python scraper.py
```

The script will:

1. Start the Elicit scraper.
2. Start the WiseBI scraper.
3. Start the IntegrationGo scraper.
4. Start the Carguber scraper.
5. Start the SFL Tech scraper.
6. Combine the results from all websites.
7. Display a summary of the collected articles.
8. Save the articles into the MySQL database.

## How the Scraping Process Works

The overall workflow follows these stages:

```text
          Start
            |
            v
      scraper.py
            |
            v
   Execute Website Scrapers
            |
     +------+------+------+------+------+
     |      |      |      |      |      |
   Elicit WiseBI  IntGo Carguber SFL Tech
     |      |      |      |      |
     +------+------+------+------+------+
            |
            v
   Extract Article Information
            |
            v
   Standardize Article Records
            |
            v
     Combine All Results
            |
            v
       database.py
            |
            v
    Check Unique Blog URL
            |
       +----+----+
       |         |
     Exists   New URL
       |         |
     Update    Insert
       |         |
       +----+----+
            |
            v
      MySQL Database
```

### Standardized Data Format

Each scraper returns article information in the following dictionary format:

```python
{
    "title": "Example Blog Title",
    "blog_url": "https://example.com/blog/example-article",
    "content": "Extracted article content..."
}
```

Using a common structure allows data from different websites to be stored in the same database table.

## Viewing the Collected Data

You can use MySQL Workbench or the MySQL command line to inspect the scraped records.

**View all articles:**

```sql
SELECT * FROM blogs_new;
```

**View the total number of records:**

```sql
SELECT COUNT(*) FROM blogs_new;
```

**Search for articles by title:**

```sql
SELECT *
FROM blogs_new
WHERE title LIKE '%keyword%';
```

**View articles from a particular website:**

```sql
SELECT *
FROM blogs_new
WHERE blog_url LIKE '%elicittechnology.com%';
```

**View a specific article:**

```sql
SELECT *
FROM blogs_new
WHERE id = 672;
```

## Exporting the Data

The collected records can be exported from MySQL Workbench into CSV format.

For large article content containing multiple paragraphs, make sure the CSV is imported using the correct delimiter and double-quote text qualifier.

The resulting data can also be converted into an Excel workbook for easier viewing and analysis.

## Adding a New Website

The modular design allows additional websites to be integrated into the project.

To add another website:

1. Create a new Python file inside the `scrapers/` directory.
2. Inspect the website's blog listing page and identify the HTML elements containing article links.
3. Implement the logic to collect article URLs, including pagination if required.
4. Visit individual article pages and identify the elements containing the title and content.
5. Extract the information and return it using the standardized dictionary structure.
6. Import the new scraper function into `scraper.py`.
7. Execute the function and append its results to `all_blogs`.
8. Add the website to the final summary output.

No changes to the database schema are required as long as the new scraper returns the same three fields.

## Important Considerations

- Website HTML structures can change, which may require updating CSS selectors.
- Some websites may restrict automated requests or return HTTP errors.
- Article URLs that no longer exist may not be retrievable.
- Different websites may contain different content structures and formatting.
- Scraping should be performed responsibly, respecting website terms of service, robots.txt policies, and applicable rules.
- Database credentials should always be kept private.
- Unique URLs help prevent duplicate records, but they do not guarantee that two different URLs contain different articles.

## Future Improvements

Potential improvements for the project include:

- Adding more company websites.
- Improving error handling for unavailable articles and failed requests.
- Adding logging to track scraping activity.
- Automating scheduled scraping.
- Improving article content cleaning and formatting.
- Adding a data analysis layer to explore the collected articles.
- Creating a simple interface to search and filter the collected blog records.

## Project Goal

The goal of this project is to build a centralized collection of blog articles from multiple company websites through automated web scraping.

It demonstrates the use of Python for web scraping, HTML parsing, modular programming, database integration, and structured data management.

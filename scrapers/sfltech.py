import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}

def scrape_sfltech_article(blog_url):
    response = requests.get(blog_url, headers= headers, timeout = 20)
    response.raise_for_status()


    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.select_one("h1.article-hero__title")
    title = title_tag.get_text(strip = True) if title_tag else None

    content_element = soup.select_one("div.rich-text-block-6.article-body.w-richtext")
    
    article_text = (
        content_element.get_text("\n", strip = True) if content_element else None
    )

    return {
        "title": title,
        "blog_url": blog_url,
        "content": article_text
    }

def scrape_sfltech():
    urls = [
        "https://www.sfltech.ai/resources/the-external-dependencies-that-can-delay-your-eadaptor-next-migration",
        "https://www.sfltech.ai/resources/eadaptor-next-the-edi-client-count-behind-your-migration-estimate",
        "https://www.sfltech.ai/resources/your-middleware-has-not-been-tested-for-oauth-2-0-that-is-the-problem",
        "https://www.sfltech.ai/resources/soap-to-rest-rewrites-your-entire-integration-layer",
        "https://www.sfltech.ai/resources/eadaptor-next-the-deadline-is-set-is-your-scope",
        "https://www.sfltech.ai/resources/automating-customs-data-entry-just-got-better",
        "https://www.sfltech.ai/resources/care-by-sfl-tech-structured-cargowise-support-built-for-performance",
        "https://www.sfltech.ai/resources/cargowise-customs-in-brazil-built-for-the-next-phase-of-digital-trade",
        "https://www.sfltech.ai/resources/top-5-features-of-the-business-intelligence-bi-tool-we-offer-you-during-cargowise-project-implementations",
        "https://www.sfltech.ai/resources/document-automation-in-logistics-where-the-productivity-gains-actually-live",
        "https://www.sfltech.ai/resources/sfl-ecosystem-business-process-offshoring-rpa-and-ocr-cargowise-consulting",
        "https://www.sfltech.ai/resources/ai-in-cargowise-what-separates-access-from-operational-value",
        "https://www.sfltech.ai/resources/optimise-your-warehouse-operations-with-robotics-and-your-erp-in-2022",
        "https://www.sfltech.ai/resources/everything-you-need-to-know-about-cargowise-certification-and-partner-accreditation",
        "https://www.sfltech.ai/resources/the-real-state-of-freight-in-2026",
        "https://www.sfltech.ai/resources/why-do-i-need-a-cargowise-service-partner",
        "https://www.sfltech.ai/resources/automate-your-ap-invoices-into-cargowise-cargodoc",
        "https://www.sfltech.ai/resources/why-freight-forwarders-use-cargowise-building-an-operating-model-that-can-scale",
        "https://www.sfltech.ai/resources/denied-party-screening-in-freight-forwarding-what-it-is-why-it-matters-and-how-cargowise-handles-it",
        "https://www.sfltech.ai/resources/new-cargowise-updates-and-features-for-2022",
        "https://www.sfltech.ai/resources/the-partner-behind-the-platform-what-actually-determines-the-return-on-cargowise",
        "https://www.sfltech.ai/resources/why-cargowise",
        "https://www.sfltech.ai/resources/why-the-right-cargowise-partner-changes-everything-",
        "https://www.sfltech.ai/resources/e2e-eadaptor-or-middleware-understanding-the-integration-architecture-behind-a-connected-cargowise-environment-",
        "https://www.sfltech.ai/resources/the-cargowise-updates-that-actually-change-how-you-operate-"
    ]

    all_blogs = []

    for url in urls:

        blog_data = scrape_sfltech_article(url)
        all_blogs.append(blog_data)
    return all_blogs







import argparse
import WebScraper as ws

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Wikipedia Scraper")
    
    parser.add_argument("--max_recurse", type=int, default=10, help="Max recursion depth for crawling")
    parser.add_argument("--num_articles", type=int, default=4, help="Number of articles to scrape")
    parser.add_argument("--max_length", type=int, default=500, help="Max words per article")
    parser.add_argument("--desired_lang", type=str, default="hi", help="Desired language (e.g., 'hi' for Hindi)")
    parser.add_argument("--root_url", type=str, default="https://en.wikipedia.org", help="Root URL to start scraping")
    parser.add_argument("--csv_path", type=str, default="scraped_data.csv", help="Path to save the scraped data")

    args = parser.parse_args()

    
    my_scraper = ws.scraper(
        max_recurse=args.max_recurse,
        num_articles=args.num_articles,
        max_article_length=args.max_length,
        desired_lang=args.desired_lang,
        root_url=args.root_url,
        csv_path=args.csv_path
    )

    my_scraper.fire()

# Use the command to run 
# python data_scraper.py --max_recurse 1000 --num_articles 1000 --max_length 500 --desired_lang "hi" --root_url https://hi.wikipedia.org/wiki/%E0%A4%B9%E0%A5%88%E0%A4%A6%E0%A4%B0%E0%A4%BE%E0%A4%AC%E0%A4%BE%E0%A4%A6_%E0%A4%95%E0%A5%87_%E0%A4%A8%E0%A4%BF%E0%A4%9C%E0%A4%BC%E0%A4%BE%E0%A4%AE --csv_path "../GeneratedDatasets/hindi_scrapped_processed.csv"
# python data_scraper.py --max_recurse 1000 --num_articles 1000 --max_length 500 --desired_lang "hi" --root_url https://en.wikipedia.org/wiki/Eilat --csv_path "../GeneratedDatasets/eng.csv"
# python data_scraper.py --max_recurse 1000 --num_articles 1 --max_length 500 --desired_lang "te" --root_url https://te.wikipedia.org/wiki/%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B1%81%E0%B0%97%E0%B1%81_%E0%B0%95%E0%B0%A5 --csv_path "./te.csv"
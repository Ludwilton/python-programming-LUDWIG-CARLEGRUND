import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Base URL for the Letterboxd page
base_url = "https://letterboxd.com/lddec/films/page/"

# Function to fetch the average user rating using Selenium
def fetch_average_user_rating(film_page_url):
    options = Options()
    options.headless = True  # Run in headless mode (no UI)

    with webdriver.Chrome(service=Service(), options=options) as driver:
        driver.get(film_page_url)
        time.sleep(2) 

        try:
            # Locate the average rating in the sidebar
            avg_rating_tag = driver.find_element(By.CSS_SELECTOR, 'section.ratings-histogram-chart span.average-rating a')
            avg_rating_value = avg_rating_tag.text.strip()  # Extract the rating value (e.g., "3.2")
            avg_rating_text = avg_rating_tag.get_attribute('data-original-title')  # Full text for additional details
            
            # Keep only the numerical part of the average rating
            avg_rating_number = avg_rating_value.split()[0]  # Extract just the number (e.g., "3.66")
            print(f"Average rating for {film_page_url}: {avg_rating_text} ({avg_rating_number})")
            return avg_rating_number, avg_rating_text  # Return just the number
            
        except Exception as e:
            print(f"Average rating for {film_page_url}: No Rating (No Rating), Error: {e}")
            return "No Rating", "No Rating"



# Function to scrape film ratings, genres, and average user rating
def scrape_letterboxd(url, single_film=False):
    response = requests.get(url)
    response.raise_for_status()  
    print(f"Fetched page: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    

    films = soup.find_all('li', class_='poster-container')
    print(f"Found {len(films)} films on this page.")

    film_data = []
    
    for index, film in enumerate(films):
        if single_film and index >= 1:
            break


        film_div = film.find('div', class_='really-lazy-load')
        
        if film_div:

            film_slug = film_div.get('data-film-slug')
            film_link = film_div.get('data-target-link')

            if not film_slug or not film_link:
                print("Missing film slug or target link, skipping this film.")
                continue


            film_page_url = f"https://letterboxd.com{film_link}"
            print(f"Fetching genres and average rating for {film_slug}...")

            # Fetch genres
            film_response = requests.get(film_page_url)
            film_response.raise_for_status()  # Check for request errors
            
            film_soup = BeautifulSoup(film_response.text, 'html.parser')


            genres = film_soup.find_all('a', class_='text-slug')
            film_genres = [genre.text.strip() for genre in genres if genre.has_attr('href') and 'genre' in genre['href']]
            
            # Fetch the average user rating using the new function
            avg_rating_value, avg_rating_text = fetch_average_user_rating(film_page_url)

            # Poster rating extraction
            rating = film.find('p', class_='poster-viewingdata').find('span', class_='rating')
            film_rating = rating.text.strip() if rating else "No Rating"

            film_data.append({
                'name': film_slug,
                'rating': film_rating,
                'genres': ', '.join(film_genres),
                'avg_user_rating': avg_rating_value  # Only numerical value now
            })

    return film_data



def save_to_csv(film_data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'rating', 'genres', 'avg_user_rating'])
        writer.writeheader()
        for film in film_data:
            writer.writerow(film)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    all_films = []
    
    option = input("Enter 'single' to scrape a single film or 'all' to scrape all films across pages: ").strip().lower()

    if option == 'single':
        url = f"{base_url}1/"  # Scrape the first page
        films_info = scrape_letterboxd(url, single_film=True)
        all_films.extend(films_info)
    elif option == 'all':
        for page in range(1, 7):
            url = f"{base_url}{page}/"
            films_info = scrape_letterboxd(url)
            all_films.extend(films_info)

    if all_films:
        save_to_csv(all_films, 'letterboxd_films.csv')
    else:
        print("No films found.")

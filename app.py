import streamlit as st
import requests
from bs4 import BeautifulSoup

# Scraper functies
def scrape_gamma(ean):
    zoek_url = f"https://www.gamma.nl/assortiment?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product = soup.find('div', class_='product-teaser')
    if product:
        naam = product.find('h3').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.gamma.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_praxis(ean):
    zoek_url = f"https://www.praxis.nl/zoek?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-teaser')
    if product:
        naam = product.find('h3').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.praxis.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_bouwmaat(ean):
    zoek_url = f"https://www.bouwmaat.nl/search?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-tile')
    if product:
        naam = product.find('h2').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.bouwmaat.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_karwei(ean):
    zoek_url = f"https://www.karwei.nl/zoek/{ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-teaser')
    if product:
        naam = product.find('h3').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.karwei.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_hornbach(ean):
    zoek_url = f"https://www.hornbach.nl/shop/{ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-detail')
    if product:
        naam = product.find('h1').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.hornbach.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_gereedschapcentrum(ean):
    zoek_url = f"https://www.gereedschapcentrum.nl/search/{ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-item')
    if product:
        naam = product.find('h3').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.gereedschapcentrum.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_toolnation(ean):
    zoek_url = f"https://www.toolnation.nl/search/?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-grid-item')
    if product:
        naam = product.find('h2').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.toolnation.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_toolstation(ean):
    zoek_url = f"https://www.toolstation.nl/search?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-grid-item')
    if product:
        naam = product.find('h2').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.toolstation.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

def scrape_verfwinkel(ean):
    zoek_url = f"https://www.verfwinkel.nl/search?q={ean}"
    response = requests.get(zoek_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find('div', class_='product-teaser')
    if product:
        naam = product.find('h3').get_text(strip=True)
        prijs = product.find('span', class_='price').get_text(strip=True).replace('€', '').replace(',', '.')
        link = "https://www.verfwinkel.nl" + product.find('a')['href']
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    return []

# Streamlit gebruikersinterface
def main():
    st.title("EAN Prijschecker")

    # Vraag de gebruiker om het EAN-nummer in te voeren (één zoekbalk)
    ean = st.text_input("Voer het EAN-nummer in:")

    if ean:
        resultaten = []

        # Roep je scrapers aan
        resultaten += scrape_gamma(ean)
        resultaten += scrape_praxis(ean)
        resultaten += scrape_bouwmaat(ean)
        resultaten += scrape_karwei(ean)
        resultaten += scrape_hornbach(ean)
        resultaten += scrape_gereedschapcentrum(ean)
        resultaten += scrape_toolnation(ean)
        resultaten += scrape_toolstation(ean)
        resultaten += scrape_verfwinkel(ean)

        # Als er resultaten zijn, toon ze
        if len(resultaten) > 0:
            # Sorteer de resultaten op prijs
            resultaten.sort(key=lambda x: x['prijs'])
            
            # Toon de top 3 resultaten
            for i, item in enumerate(resultaten[:3], start=1):
                st.markdown(f"**{i}. {item['naam']}**")
                st.markdown(f"💰 Prijs: €{item['prijs']:.2f}")
                st.markdown(f"[🔗 Naar webshop]({item['link']})")
        else:
            st.write("Geen producten gevonden met dit EAN-nummer.")

# Start de app
if __name__ == "__main__":
    main()

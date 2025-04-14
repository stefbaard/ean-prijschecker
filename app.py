import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Selenium instellen
def start_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)

# Scrapers
def scrape_gamma(driver, ean):
    try:
        driver.get(f"https://www.gamma.nl/assortiment?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-tile")
        naam = product.find_element(By.TAG_NAME, "h3").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_praxis(driver, ean):
    try:
        driver.get(f"https://www.praxis.nl/zoek?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-tile")
        naam = product.find_element(By.TAG_NAME, "h3").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_karwei(driver, ean):
    try:
        driver.get(f"https://www.karwei.nl/zoek/{ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-tile")
        naam = product.find_element(By.TAG_NAME, "h3").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_hornbach(driver, ean):
    try:
        driver.get(f"https://www.hornbach.nl/shop/search.html?search={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product")
        naam = product.find_element(By.TAG_NAME, "h2").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_bouwmaat(driver, ean):
    try:
        driver.get(f"https://www.bouwmaat.nl/search?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-tile")
        naam = product.find_element(By.TAG_NAME, "h2").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_gereedschapcentrum(driver, ean):
    try:
        driver.get(f"https://www.gereedschapcentrum.nl/search/{ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-item")
        naam = product.find_element(By.TAG_NAME, "h3").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_toolnation(driver, ean):
    try:
        driver.get(f"https://www.toolnation.nl/search/?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-grid-item")
        naam = product.find_element(By.TAG_NAME, "h2").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_toolstation(driver, ean):
    try:
        driver.get(f"https://www.toolstation.nl/search?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-grid-item")
        naam = product.find_element(By.TAG_NAME, "h2").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

def scrape_verfwinkel(driver, ean):
    try:
        driver.get(f"https://www.verfwinkel.nl/search?q={ean}")
        time.sleep(2)
        product = driver.find_element(By.CLASS_NAME, "product-tile")
        naam = product.find_element(By.TAG_NAME, "h3").text
        prijs = product.find_element(By.CLASS_NAME, "price").text.replace('€', '').replace(',', '.')
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        return [{"naam": naam, "prijs": float(prijs), "link": link}]
    except:
        return []

# Streamlit-app
def main():
    st.title("EAN Prijschecker")

    ean = st.text_input("🔍 Voer het EAN-nummer in:")

    if ean:
        with st.spinner("Bezig met zoeken..."):
            driver = start_driver()
            resultaten = []
            scrapers = [
                scrape_gamma,
                scrape_praxis,
                scrape_karwei,
                scrape_hornbach,
                scrape_bouwmaat,
                scrape_gereedschapcentrum,
                scrape_toolnation,
                scrape_toolstation,
                scrape_verfwinkel
            ]

            for scraper in scrapers:
                try:
                    resultaten += scraper(driver, ean)
                except Exception as e:
                    print(f"Fout bij scraper {scraper.__name__}: {e}")

            driver.quit()

        if resultaten:
            resultaten.sort(key=lambda x: x['prijs'])
            st.subheader("Top 3 goedkoopste opties:")
            for i, item in enumerate(resultaten[:3], start=1):
                st.markdown(f"**{i}. {item['naam']}**")
                st.markdown(f"💰 Prijs: €{item['prijs']:.2f}")
                st.markdown(f"[🔗 Naar webshop]({item['link']})")
        else:
            st.warning("Geen resultaten gevonden voor dit EAN-nummer.")

# Run de app
if __name__ == "__main__":
    main()

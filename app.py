import streamlit as st

# Demo-data (later vervangen we dit met live scraping)
demo_resultaten = [
    {"naam": "Product A", "prijs": 84.99, "link": "https://voorbeeldwinkel1.nl"},
    {"naam": "Product B", "prijs": 87.00, "link": "https://voorbeeldwinkel2.nl"},
    {"naam": "Product C", "prijs": 89.99, "link": "https://voorbeeldwinkel3.nl"},
]

st.title("🔎 EAN Prijschecker")

ean = st.text_input("Voer het EAN-nummer in:", "")

if ean:
    st.subheader("Top 3 goedkoopste opties:")
    for i, item in enumerate(demo_resultaten, start=1):
        st.markdown(f"**{i}. {item['naam']}**")
        st.markdown(f"💰 Prijs: €{item['prijs']:.2f}")
        st.markdown(f"[🔗 Naar webshop]({item['link']})")
        st.markdown("---")

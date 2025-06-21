import streamlit as st

# Streamlit setup
st.set_page_config(page_title="🍛 Cooking Chatbot", page_icon="🍽️")
st.title("🍛 Step-by-Step Cooking Chatbot (English + Tamil)")
st.markdown("Ask for a recipe (e.g., `idly`) or a cooking term (e.g., `what is urad dal`) 👩‍🍳")

# Recipe steps
recipes = {
    "idly": [
        """1. Wash 2 cups of idly rice and 1 cup of urad dal separately.
2. Soak them for 4 to 6 hours.
3. Grind urad dal until fluffy. Then grind rice to a coarse paste.
4. Mix both, add salt, and allow it to ferment overnight.
5. Grease idly plates and pour batter.
6. Steam for 10-12 minutes.
7. Serve hot with chutney or sambar.""",
        """1. 2 கப் இட்லி அரிசி மற்றும் 1 கப் உளுந்தை தனித்தனியாக கழுவவும்.
2. 4-6 மணி நேரம் ஊற வைக்கவும்.
3. உளுந்தை நன்கு அரைத்து, அரிசியை தட்டையாக அரைக்கவும்.
4. இரண்டும் கலந்து உப்பு சேர்த்து, இரவு முழுக்க புளிக்க வைக்கவும்.
5. இட்லி தட்டில் எண்ணெய் தடவி மாவை ஊற்றவும்.
6. 10-12 நிமிடங்கள் ஆவியில் வேகவைக்கவும்.
7. சட்னி அல்லது சாம்பாருடன் பரிமாறவும்."""
    ],
    "dosa": [
        """1. Use the same idly batter, but ferment it a little longer.
2. Heat a non-stick tawa and pour a ladle of batter.
3. Spread it in a circular motion.
4. Drizzle oil on sides and cook till golden brown.
5. Flip if needed, then serve hot.""",
        """1. இட்லி மாவை சற்று அதிக நேரம் புளிக்க வைக்கவும்.
2. தவாவை காயவைத்து ஒரு கரண்டி மாவை ஊற்றவும்.
3. சுற்று சுற்றாக பரப்பவும்.
4. எண்ணெய் விடவும், தங்க நிறமாக வேகவைக்கவும்.
5. தேவைப்பட்டால் திருப்பி வேகவைத்து பரிமாறவும்."""
    ],
    "curd rice": [
        """1. Cook rice until soft.
2. Cool it and mash lightly.
3. Add curd and salt.
4. In a small pan, heat oil, mustard, curry leaves, and green chilies.
5. Add this tempering to rice.
6. Mix and serve with pickle or fryums.""",
        """1. சாதத்தை நன்கு வேகவைக்கவும்.
2. குளிர விட்டு மெதுவாக நுரைக்கவும்.
3. தயிர் மற்றும் உப்பு சேர்க்கவும்.
4. சிறிய வாணலியில் எண்ணெய், கடுகு, கருவேப்பிலை, பச்சை மிளகாய் வதக்கவும்.
5. அதை சாதத்தில் ஊற்றி கலக்கவும்.
6. ஊறுகாய் அல்லது வதைக்கல் உடன் பரிமாறவும்."""
    ]
}

# Term explanations
definitions = {
    "urad dal": [
        "Urad dal is black gram. It’s a type of lentil used in South Indian dishes like idli and dosa.",
        "உளுந்து என்பது இட்லி, தோசை போன்றவற்றில் பயன்படுத்தப்படும் பருப்பு வகை."
    ],
    "fermentation": [
        "Fermentation is the process where batter is left overnight to rise due to helpful bacteria.",
        "புளிப்பு என்பது மாவை இரவு முழுக்க வைத்திருப்பதால் நிகழும் இயற்கையான செயல்முறை."
    ],
    "tempering": [
        "Tempering is when spices are fried in oil to release their aroma before adding to food.",
        "தாளிக்குதல் என்பது எண்ணெயில் மசாலா பொருட்களை வதக்கி உணவில் சேர்க்கும் செயல்."
    ],
    "tawa": [
        "Tawa is a flat pan used for making dosa, chapati, or roti.",
        "தவா என்பது தோசை, சப்பாத்தி செய்ய பயன்படுத்தப்படும் சமையல் தட்டு."
    ]
}

# Input box
user_input = st.text_input("Enter a dish or term:")

# Output logic
if user_input:
    query = user_input.strip().lower()
    
    if query in recipes:
        en, ta = recipes[query]
        st.subheader("🍽️ Recipe Steps (English):")
        st.markdown(en)
        st.subheader("🍽️ செய்முறை (தமிழ்):")
        st.markdown(ta)

    elif query.startswith("what is") or query.startswith("explain"):
        keyword = query.replace("what is", "").replace("explain", "").strip()
        if keyword in definitions:
            en, ta = definitions[keyword]
            st.subheader("📘 English Meaning:")
            st.write(en)
            st.subheader("📗 தமிழ் விளக்கம்:")
            st.write(ta)
        else:
            st.warning("Sorry, I don't have that explanation yet.")
    else:
        st.warning("Sorry, I don’t have that recipe or term yet. Try 'idly', 'curd rice', or 'what is urad dal'.")


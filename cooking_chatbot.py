import streamlit as st
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Streamlit setup
st.set_page_config(page_title="Step-by-Step Cooking Chatbot", page_icon="🍛")
st.title("🍛 Step-by-Step Cooking Chatbot (English + Tamil)")
st.markdown("Ask me how to cook a dish. I'll guide you step by step in English and Tamil! 👩‍🍳")

# Detailed recipe database
recipes = {
    "idly": [
        """1. Wash 2 cups of idly rice and 1 cup of urad dal separately.\n2. Soak them for 4 to 6 hours.\n3. Grind urad dal until fluffy. Then grind rice to a coarse paste.\n4. Mix both, add salt, and allow it to ferment overnight.\n5. Grease idly plates and pour batter.\n6. Steam for 10-12 minutes.\n7. Serve hot with chutney or sambar.""",
        """1. 2 கப் இட்லி அரிசி மற்றும் 1 கப் உளுந்தை தனித்தனியாக கழுவவும்.\n2. 4-6 மணி நேரம் ஊற வைக்கவும்.\n3. உளுந்தை நன்கு அரைத்து, அரிசியை தட்டையாக அரைக்கவும்.\n4. இரண்டும் கலந்து உப்பு சேர்த்து, இரவு முழுக்க புளிக்க வைக்கவும்.\n5. இட்லி தட்டில் எண்ணெய் தடவி மாவை ஊற்றவும்.\n6. 10-12 நிமிடங்கள் ஆவியில் வேகவைக்கவும்.\n7. சட்னி அல்லது சாம்பாருடன் பரிமாறவும்."""
    ],
    "dosa": [
        """1. Use the same idly batter, but ferment it a little longer.\n2. Heat a non-stick tawa and pour a ladle of batter.\n3. Spread it in a circular motion.\n4. Drizzle oil on sides and cook till golden brown.\n5. Flip if needed, then serve hot.""",
        """1. இட்லி மாவை சற்று அதிக நேரம் புளிக்க வைக்கவும்.\n2. தவாவை காயவைத்து ஒரு கரண்டி மாவை ஊற்றவும்.\n3. சுற்று சுற்றாக பரப்பவும்.\n4. எண்ணெய் விடவும், தங்க நிறமாக வேகவைக்கவும்.\n5. தேவைப்பட்டால் திருப்பி வேகவைத்து பரிமாறவும்."""
    ],
    "curd rice": [
        """1. Cook rice until soft.\n2. Cool it and mash lightly.\n3. Add curd and salt.\n4. In a small pan, heat oil, mustard, curry leaves, and green chilies.\n5. Add this tempering to rice.\n6. Mix and serve with pickle or fryums.""",
        """1. சாதத்தை நன்கு வேகவைக்கவும்.\n2. குளிர விட்டு மெதுவாக நுரைக்கவும்.\n3. தயிர் மற்றும் உப்பு சேர்க்கவும்.\n4. சிறிய வாணலியில் எண்ணெய், கடுகு, கருவேப்பிலை, பச்சை மிளகாய் வதக்கவும்.\n5. அதை சாதத்தில் ஊற்றி கலக்கவும்.\n6. ஊறுகாய் அல்லது வதைக்கல் உடன் பரிமாறவும்."""
    ],
    "ice cream": [
        """1. Mix 2 cups of cream and 1 cup condensed milk.\n2. Add vanilla extract and beat until fluffy.\n3. Pour into a container and cover.\n4. Freeze for at least 6 hours.\n5. Scoop and serve cold.""",
        """1. 2 கப் கிரீம் மற்றும் 1 கப் கன்சென்ஸ் பால் கலந்து விடவும்.\n2. வெணிலா எசென்ஸ் சேர்த்து நன்கு அடித்துக் கொள்ளவும்.\n3. ஒரு பெட்டியில் ஊற்றி மூடி வைக்கவும்.\n4. குறைந்தது 6 மணி நேரம் உறையவைக்கவும்.\n5. ஸ்கூப் செய்து பரிமாறவும்."""
    ]
}

# Cooking Term Definitions
definitions = {
    "urad dal": [
        "Urad dal is black gram. It’s a type of lentil used in South Indian dishes like idli and dosa.",
        "உளுந்து என்பது இட்லி, தோசை போன்றவற்றில் பயன்படுத்தப்படும் பருப்பு வகை."
    ],
    "fermentation": [
        "Fermentation is the natural process where batter is left overnight to rise due to helpful bacteria.",
        "புளிப்பு என்பது மாவை இரவு முழுக்க வைத்திருப்பதால் நிகழும் இயற்கையான செயல்முறை. இது மாவை நன்கு எழும்ப வைக்கும்."
    ],
    "tempering": [
        "Tempering is when spices are fried in oil to release their aroma before adding to food.",
        "தாளிக்குதல் என்பது எண்ணெயில் மசாலா பொருட்களை வதக்கி உணவில் சேர்க்கும் செயல்."
    ],
    "tawa": [
        "Tawa is a flat pan used for making dosa, chapati, or roti.",
        "தவா என்பது தோசை, சப்பாத்தி செய்ய பயன்படுத்தப்படும் சமையல் தட்டு."
    ],
    "grind": [
        "Grinding means making something into a paste using a grinder or stone.",
        "அரைக்கும் என்பது பருப்பு அல்லது அரிசியை மையமாக அரைக்கும் செயல்முறை."
    ]
}

# User input
user_input = st.text_input("Which recipe or term do you want?")

if user_input:
    query = user_input.lower().strip()
    if query in recipes:
        en_steps, ta_steps = recipes[query]
        st.markdown(f"**English Steps:**\n\n{en_steps}")
        st.markdown("---")
        st.markdown(f"**தமிழ் படிகள்:**\n\n{ta_steps}")
        engine.say("Here is the step by step process")
        engine.runAndWait()

    elif query.startswith("what is") or query.startswith("explain"):
        keyword = query.replace("what is", "").replace("explain", "").strip()
        if keyword in definitions:
            en_def, ta_def = definitions[keyword]
            st.markdown(f"**English Meaning:** {en_def}")
            st.markdown(f"**தமிழ் விளக்கம்:** {ta_def}")
            engine.say(en_def)
            engine.runAndWait()
        else:
            st.warning("Sorry, I don’t have that explanation yet. Ask about common terms like 'urad dal', 'tawa', etc.")
            engine.say("Term not found")
            engine.runAndWait()

    else:
        st.warning("Sorry, I don't have that recipe yet. Try 'idly', 'dosa', 'curd rice', or 'ice cream'.")
        engine.say("Recipe not found")
        engine.runAndWait()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ to guide every home cook!")

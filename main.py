import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, numbers, characters):
    new = string.ascii_letters
    if numbers:
        new += string.digits
    if characters:
        new += string.punctuation
    return ''.join(random.choice(new) for _ in range(length))

# Initialize session state for password visibility
if "password" not in st.session_state:
    st.session_state.password = ""
if "show_password" not in st.session_state:
    st.session_state.show_password = False

# Apply Custom CSS for Animated Background and Styling
animated_bg = """
<style>
    /* Smooth Background Animation */
    [data-testid="stAppViewContainer"] {
        background: url(''https://storyblok-cdn.photoroom.com/f/191576/768x432/5d72c4f216/spring_backgrounds_cover.webp') no-repeat center center fixed;
        background-size: cover;
        animation: fadeIn 3s ease-in-out;
        filter: brightness(0.9) contrast(1.1);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

   /* Apply Black Text Globally */
     * {
         color: black !important;
     }

    /* Styling for Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 20px;
    }

    /* Custom Button Style */
    .stButton > button {
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white !important;
        border: none;
        padding: 10px 20px;
        border-radius: 20px;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        transform: scale(1.05);
    }
    
    /* Password Display Box */
    .password-box {
        font-size: 18px;
        font-weight: bold;
        background: white !important;
        color: black;
        padding: 10px;
        border-radius: 10px;
        display: inline-block;
    }
</style>
"""

st.markdown(animated_bg, unsafe_allow_html=True)

# App Title
st.title('🔐 Password Generator')

# Password Length Slider
length = st.slider('Password Length', min_value=15, max_value=50, value=20)

# Checkbox options
numbers = st.checkbox('Include Numbers', value=True)
characters = st.checkbox('Include Special Characters', value=True)
upper = st.checkbox('Include Uppercase Letters', value=True)
lower = st.checkbox('Include Lowercase Letters', value=True)

# Generate password on button click
if st.button('Generate Password'):
    st.session_state.password = generate_password(length, numbers, characters)

# Toggle Visibility Button (Eye Icon)
col1, col2 = st.columns([0.9, 0.1])  # Create two columns for text and button
with col1:
    if st.session_state.password:
        password_display = (
            st.session_state.password
            if st.session_state.show_password
            else "•" * len(st.session_state.password)  # Hide password with dots
        )
        st.markdown(f'<p class="password-box">{password_display}</p>', unsafe_allow_html=True)

with col2:
    if st.session_state.password:
        if st.button("👁️"):
            st.session_state.show_password = not st.session_state.show_password  # Toggle visibility

st.markdown("✅ **Password generated successfully!**")

st.markdown('<p style="text-align: center;">Made With ♥️ By <b>Shan-E-Zehra</b></p>', unsafe_allow_html=True)

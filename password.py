import streamlit as st  # type: ignore
import random
import string

# Set up Streamlit's dark theme
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# Custom CSS for the dark theme
st.markdown(
    """
    <style>
        .reportview-container {
            background-color: #121212;
        }
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
        }
      
        h1, h2, h3, h4, h5, h6 {
            color: #FF8C00;  /* Orange color for headings */
        }
        .stButton>button {
            background-color: #FF8C00;  /* Orange color for buttons */
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            background-color: #333;
            color: #FF8C00;
            border: 2px solid #FF8C00;
            border-radius: 8px;
        }
        .stTextInput>label {
            color: #FF8C00;
        }
        .stMarkdown {
            color: white;
        }
        .stAlert {
            background-color: #333;
            border: 2px solid #FF8C00;
        }
    </style>
    """, unsafe_allow_html=True
)

# App Title and Subheader
st.title("🔐 Password Strength Checker")
st.markdown("""
    ## Protect Your Data with Strong Passwords 🔒
  Check your password's strength and get personalized tips to make it **more secure** and **uncrackable**! 🛡️  
    Follow these simple steps to build a **bulletproof password** 💪
""")

# Function to generate a random password based on the specified criteria
def generate_random_password():
    characters = string.ascii_lowercase + string.digits + "!@#$%&*"  # Lowercase + digits + special characters
    length = random.randint(12, 16)  # Password length between 12 and 16 characters
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
    return password

# Button to generate a random password
if st.button("Generate Random Password 🎲"):
    random_password = generate_random_password()
    st.text_input("Your Random Password", value=random_password, key="generated_password", type="password")

# Password input field for the user to type their password
password = st.text_input("Enter your password 🔑", type="password")

# List to collect feedback
feedback = []

# Initialize score as integer (0)
score = 0

# Checking password conditions and adding feedback
if password:
    # Check length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check if both uppercase and lowercase characters are present
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain lowercase characters.")
    
    # Check if there is at least one digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check if there is at least one special character
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (e.g., !@#$%&*).")
    
    # Provide feedback based on score
    if score == 4:
        feedback.append("✅ Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🟡 Your password has medium strength. It could be stronger.")
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")
    
    # Display feedback
    if feedback:
        st.markdown("## Improvement Suggestions")
        for hint in feedback:
            st.write(hint)
else:
    st.info("Please enter your password to get started.")

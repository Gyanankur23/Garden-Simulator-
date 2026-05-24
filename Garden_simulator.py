import streamlit as st
import random

st.set_page_config(page_title="Magic Garden Simulator", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_index=True)

st.title("🌿 Magic Garden Simulator")
st.caption("Plant seeds, sing to them, water them, and watch them sprout into life!")

if "garden" not in st.session_state:
    st.session_state.garden = []  

# Helper to determine plant emoji based on growth stage
def get_plant_emoji(growth_level):
    if growth_level == 0: return "🌱"
    elif growth_level < 3: return "🌿"
    elif growth_level < 6: return "🪴"
    elif growth_level < 10: return "🌻"
    else: return "🌳"

# Sidebar Actions (Planting Panel)
with st.sidebar:
    st.header("🎒 Gardener's Toolbelt")
    
    plant_name = st.text_input("What seed are you planting?", placeholder="e.g., Sunflower, Rose, Tomato")
    
    if st.button("✨ Plant Seed", use_container_width=True):
        if plant_name.strip():
            # Check for duplicates to prevent confusion
            if any(p['name'].lower() == plant_name.strip().lower() for p in st.session_state.garden):
                st.warning(f"You already have a '{plant_name}' in your garden!")
            else:
                st.session_state.garden.append({
                    "name": plant_name.strip(),
                    "growth": 0
                })
                st.toast(f"🎉 {plant_name} seed tucked safely into the soil!", icon="🌱")
        else:
            st.error("Please name your seed first!")

    st.divider()
    
    # Global Actions
    if st.button("💧 Water All Plants", use_container_width=True):
        if st.session_state.garden:
            for plant in st.session_state.garden:
                plant["growth"] += 1
            st.balloons()
            st.toast("Your plants gulp down the refreshing water!", icon="💦")
        else:
            st.warning("The watering can is full, but your garden is empty!")
            
    if st.button("🎶 Sing to Garden", use_container_width=True):
        if st.session_state.garden:
            for plant in st.session_state.garden:
                # Random chance to boost growth with music
                if random.choice([True, False]):
                    plant["growth"] += 1
            st.toast("🎵 Your beautiful singing voice cheered up the plants!", icon="🎶")
        else:
            st.warning("You are singing beautifully, but to an empty patch of dirt.")

    if st.button("🗑️ Clear Garden", type="secondary", use_container_width=True):
        st.session_state.garden = []
        st.toast("Garden cleared. Time for a fresh start!", icon="🧹")

# Main Display: The Visual Garden Grid
st.subheader("🏡 Your Visual Garden Patch")

if not st.session_state.garden:
    st.info("Your garden patch is bare dirt right now. Use the sidebar toolbelt to plant your very first seed! 👇")
else:
    # Arrange plants in a dynamic clean grid layout (3 items per row)
    cols = st.columns(3)
    
    for idx, plant in enumerate(st.session_state.garden):
        col = cols[idx % 3]
        
        with col:
            emoji = get_plant_emoji(plant["growth"])
            
            with st.container(border=True):
                st.markdown(f"<h1 style='text-align: center; margin:0;'>{emoji}</h1>", unsafe_html=True)
                st.markdown(f"<h3 style='text-align: center; margin:0;'>{plant['name']}</h3>", unsafe_html=True)
                
                # Dynamic growth badge labels
                if plant["growth"] == 0:
                    stage_name = "Just Planted"
                elif plant["growth"] < 3:
                    stage_name = "Sprout"
                elif plant["growth"] < 6:
                    stage_name = "Growing Vine"
                elif plant["growth"] < 10:
                    stage_name = "Blooming Flower"
                else:
                    stage_name = "Mega Tree!"
                    
                st.markdown(f"<p style='text-align: center; color: gray;'>Stage: {stage_name}<br>Growth Level: <b>{plant['growth']}</b></p>", unsafe_html=True)
                
                # Individual plant care button
                if st.button(f"💧 Water {plant['name']}", key=f"water_{idx}", use_container_width=True):
                    plant["growth"] += 1
                    st.rerun()

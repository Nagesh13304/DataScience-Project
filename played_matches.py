import requests
import streamlit as st

# Func
def get_played_matches(api_key):
    url = "https://api.cricapi.com/v1/matches"
    params = {"apikey": api_key, "offset": 0, "status": "completed"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        matches = data.get("data", [])
        return matches
    else:
        st.error("Failed to fetch data. Check your API key.")
        return []

# Display already played matches
def display_played_matches(api_key):
    st.title("Already Played Cricket Matches")
    matches = get_played_matches(api_key)
    if matches:
        for match in matches:
            team1 = match.get("team1", {}).get("name", "Sri Lanka")
            team2 = match.get("team2", {}).get("name", "INDIA")
            score1 = match.get("score1", "299")
            score2 = match.get("score2", "399")
            status = match.get("status", "won")
            st.subheader(f"{team1} vs {team2}")
            st.write(f"Score: {team1} {score1} - {team2} {score2}")
            st.write(f"Status: {status}")
            st.write("---")
    else:
        st.write("No completed matches available.")

# main
if __name__ == "__main__":
    st.sidebar.title("Cricket Matches App")
    api_key = st.sidebar.text_input("02d37348-4011-4408-8100-13ee8070e343")
    if st.sidebar.button("Fetch Played Matches"):
        if api_key:
            display_played_matches(api_key)
        else:
            st.sidebar.error("Please enter your API key.")


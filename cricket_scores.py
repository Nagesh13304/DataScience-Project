import requests
import streamlit as st

# Function to fetch live cricket scores
def get_cricket_scores(api_key):
    url = "https://cricapi.com/api/matches"  # CricAPI matches endpoint
    params = {"apikey": api_key}
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        matches = data.get("matches", [])
        return matches
    else:
        st.error("Failed to fetch data. Check your API key.")
        return []

# Display cricket scores
def display_scores(api_key):
    st.title("Live Cricket Scores")
    matches = get_cricket_scores(api_key)
    if matches:
        for match in matches:
            if match.get("matchStarted"):
                # Only display live matches
                team1 = match.get("team-1", "N/A")
                team2 = match.get("team-2", "N/A")
                toss = match.get("toss_winner_team", "N/A")
                match_type = match.get("type", "N/A")
                winner = match.get("winner_team", "N/A")
                st.subheader(f"{team1} vs {team2}")
                st.write(f"Match Type: {match_type}")
                st.write(f"Toss Winner: {toss}")
                st.write(f"Winner: {winner if winner else 'Match in Progress'}")
                st.write("---")
    else:
        st.write("No live matches available.")

# Main function
if __name__ == "__main__":
    st.sidebar.title("Cricket Score App")
    api_key = "02d37348-4011-4408-8100-13ee8070e343"  # Your API key
    if st.sidebar.button("Fetch Scores"):
        if api_key:
            display_scores(api_key)
        else:
            st.sidebar.error("Please enter your API key.")


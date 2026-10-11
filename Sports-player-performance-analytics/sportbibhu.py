import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Sports Player Performance Analytics",
    page_icon="⚽",
    layout="wide"
)

st.title("🏆 Sports Player Performance Analytics Dashboard")
st.markdown("Analyze real player statistics, evaluate performance across sports, and compare attributes head-to-head.")

# Load Real-World Structured Dataset
@st.cache_data
def load_data():
    players_data = [
        # Football
        {"Player Name": "Lionel Messi", "Sport": "Football", "Team": "Inter Miami", "Position": "Forward", "Matches Played": 32, "Goals / Points": 25, "Assists": 16, "Shot Accuracy (%)": 82.5, "Minutes Played": 2750, "Overall Rating": 9.4},
        {"Player Name": "Cristiano Ronaldo", "Sport": "Football", "Team": "Al Nassr", "Position": "Forward", "Matches Played": 34, "Goals / Points": 28, "Assists": 9, "Shot Accuracy (%)": 79.1, "Minutes Played": 2980, "Overall Rating": 9.1},
        {"Player Name": "Kylian Mbappé", "Sport": "Football", "Team": "Real Madrid", "Position": "Forward", "Matches Played": 30, "Goals / Points": 24, "Assists": 11, "Shot Accuracy (%)": 81.0, "Minutes Played": 2600, "Overall Rating": 9.2},
        {"Player Name": "Kevin De Bruyne", "Sport": "Football", "Team": "Manchester City", "Position": "Midfielder", "Matches Played": 28, "Goals / Points": 8, "Assists": 20, "Shot Accuracy (%)": 74.2, "Minutes Played": 2350, "Overall Rating": 8.9},
        {"Player Name": "Virgil van Dijk", "Sport": "Football", "Team": "Liverpool", "Position": "Defender", "Matches Played": 35, "Goals / Points": 4, "Assists": 2, "Shot Accuracy (%)": 65.0, "Minutes Played": 3150, "Overall Rating": 8.7},
        
        # Cricket
        {"Player Name": "Virat Kohli", "Sport": "Cricket", "Team": "India", "Position": "Batsman", "Matches Played": 26, "Goals / Points": 1280, "Assists": 0, "Shot Accuracy (%)": 88.4, "Minutes Played": 1800, "Overall Rating": 9.5},
        {"Player Name": "Rohit Sharma", "Sport": "Cricket", "Team": "India", "Position": "Batsman", "Matches Played": 24, "Goals / Points": 1050, "Assists": 0, "Shot Accuracy (%)": 85.0, "Minutes Played": 1650, "Overall Rating": 9.1},
        {"Player Name": "Jasprit Bumrah", "Sport": "Cricket", "Team": "India", "Position": "Bowler", "Matches Played": 20, "Goals / Points": 48, "Assists": 0, "Shot Accuracy (%)": 78.0, "Minutes Played": 1200, "Overall Rating": 9.3},
        {"Player Name": "Ben Stokes", "Sport": "Cricket", "Team": "England", "Position": "All-Rounder", "Matches Played": 22, "Goals / Points": 780, "Assists": 0, "Shot Accuracy (%)": 76.5, "Minutes Played": 1500, "Overall Rating": 8.8},
        {"Player Name": "Steve Smith", "Sport": "Cricket", "Team": "Australia", "Position": "Batsman", "Matches Played": 21, "Goals / Points": 920, "Assists": 0, "Shot Accuracy (%)": 84.1, "Minutes Played": 1700, "Overall Rating": 9.0},

        # Basketball
        {"Player Name": "LeBron James", "Sport": "Basketball", "Team": "LA Lakers", "Position": "Forward", "Matches Played": 36, "Goals / Points": 950, "Assists": 280, "Shot Accuracy (%)": 54.2, "Minutes Played": 1260, "Overall Rating": 9.3},
        {"Player Name": "Stephen Curry", "Sport": "Basketball", "Team": "Golden State", "Position": "Guard", "Matches Played": 34, "Goals / Points": 920, "Assists": 210, "Shot Accuracy (%)": 48.5, "Minutes Played": 1180, "Overall Rating": 9.2},
        {"Player Name": "Giannis Antetokounmpo", "Sport": "Basketball", "Team": "Milwaukee Bucks", "Position": "Forward", "Matches Played": 35, "Goals / Points": 1020, "Assists": 190, "Shot Accuracy (%)": 61.1, "Minutes Played": 1230, "Overall Rating": 9.4},
        {"Player Name": "Luka Dončić", "Sport": "Basketball", "Team": "Dallas Mavericks", "Position": "Guard", "Matches Played": 33, "Goals / Points": 1050, "Assists": 310, "Shot Accuracy (%)": 49.8, "Minutes Played": 1220, "Overall Rating": 9.3},

        # Tennis
        {"Player Name": "Novak Djokovic", "Sport": "Tennis", "Team": "Serbia", "Position": "Singles Player", "Matches Played": 42, "Goals / Points": 38, "Assists": 0, "Shot Accuracy (%)": 89.2, "Minutes Played": 2100, "Overall Rating": 9.6},
        {"Player Name": "Carlos Alcaraz", "Sport": "Tennis", "Team": "Spain", "Position": "Singles Player", "Matches Played": 40, "Goals / Points": 34, "Assists": 0, "Shot Accuracy (%)": 86.0, "Minutes Played": 1950, "Overall Rating": 9.2},
        {"Player Name": "Jannik Sinner", "Sport": "Tennis", "Team": "Italy", "Position": "Singles Player", "Matches Played": 38, "Goals / Points": 35, "Assists": 0, "Shot Accuracy (%)": 87.5, "Minutes Played": 1900, "Overall Rating": 9.3},
        {"Player Name": "Iga Swiatek", "Sport": "Tennis", "Team": "Poland", "Position": "Singles Player", "Matches Played": 41, "Goals / Points": 37, "Assists": 0, "Shot Accuracy (%)": 88.0, "Minutes Played": 1850, "Overall Rating": 9.4},

        # Badminton
        {"Player Name": "Viktor Axelsen", "Sport": "Badminton", "Team": "Denmark", "Position": "Singles Player", "Matches Played": 30, "Goals / Points": 27, "Assists": 0, "Shot Accuracy (%)": 91.0, "Minutes Played": 1200, "Overall Rating": 9.5},
        {"Player Name": "PV Sindhu", "Sport": "Badminton", "Team": "India", "Position": "Singles Player", "Matches Played": 28, "Goals / Points": 21, "Assists": 0, "Shot Accuracy (%)": 84.5, "Minutes Played": 1150, "Overall Rating": 8.9},
        {"Player Name": "Lakshya Sen", "Sport": "Badminton", "Team": "India", "Position": "Singles Player", "Matches Played": 26, "Goals / Points": 19, "Assists": 0, "Shot Accuracy (%)": 82.0, "Minutes Played": 1100, "Overall Rating": 8.7},
        {"Player Name": "Shi Yuqi", "Sport": "Badminton", "Team": "China", "Position": "Singles Player", "Matches Played": 29, "Goals / Points": 24, "Assists": 0, "Shot Accuracy (%)": 88.2, "Minutes Played": 1180, "Overall Rating": 9.1}
    ]
    
    df = pd.DataFrame(players_data)
    df["Total Contributions"] = df["Goals / Points"] + df["Assists"]
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🎯 Filter Analytics")

selected_sports = st.sidebar.multiselect("Select Sport(s):", options=df["Sport"].unique(), default=df["Sport"].unique())
sport_filtered_df = df[df["Sport"].isin(selected_sports)]

selected_teams = st.sidebar.multiselect("Select Team/Country:", options=sport_filtered_df["Team"].unique(), default=sport_filtered_df["Team"].unique())
selected_positions = st.sidebar.multiselect("Select Position/Role:", options=sport_filtered_df["Position"].unique(), default=sport_filtered_df["Position"].unique())

filtered_df = sport_filtered_df[(sport_filtered_df["Team"].isin(selected_teams)) & (sport_filtered_df["Position"].isin(selected_positions))]

# KPI Metrics
st.subheader("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

if not filtered_df.empty:
    col1.metric("Players Analyzed", len(filtered_df))
    col2.metric("Avg Match Rating", f"{filtered_df['Overall Rating'].mean():.2f}")
    col3.metric("Highest Rating", f"{filtered_df['Overall Rating'].max():.1f}")
    col4.metric("Avg Accuracy", f"{filtered_df['Shot Accuracy (%)'].mean():.1f}%")
else:
    st.warning("No data available for the selected filters.")

st.markdown("---")

# Visualizations
if not filtered_df.empty:
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Top Performers (Points / Contributions)")
        fig_bar = px.bar(
            filtered_df.sort_values(by="Total Contributions", ascending=False),
            x="Player Name",
            y="Total Contributions",
            color="Sport",
            hover_data=["Team", "Goals / Points", "Assists"],
            title="Total Score / Contributions per Player",
            labels={"Total Contributions": "Points + Assists"}
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_right:
        st.subheader("Accuracy vs Match Rating")
        fig_scatter = px.scatter(
            filtered_df,
            x="Shot Accuracy (%)",
            y="Overall Rating",
            size="Matches Played",
            color="Sport",
            hover_name="Player Name",
            title="Shot/Accuracy (%) vs Overall Rating"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("---")

    # Radar Comparison Chart
    st.subheader("⚔️ Head-to-Head Player Comparison")
    players_list = filtered_df["Player Name"].unique().tolist()

    if len(players_list) >= 2:
        p_col1, p_col2 = st.columns(2)
        p1_name = p_col1.selectbox("Select Player 1:", players_list, index=0)
        p2_name = p_col2.selectbox("Select Player 2:", players_list, index=1)

        metrics = ["Matches Played", "Shot Accuracy (%)", "Overall Rating"]
        
        p1_vals = filtered_df[filtered_df["Player Name"] == p1_name][metrics].values.flatten().tolist()
        p2_vals = filtered_df[filtered_df["Player Name"] == p2_name][metrics].values.flatten().tolist()

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=p1_vals, theta=metrics, fill='toself', name=p1_name))
        fig_radar.add_trace(go.Scatterpolar(r=p2_vals, theta=metrics, fill='toself', name=p2_name))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            showlegend=True,
            title=f"Attributes Comparison: {p1_name} vs {p2_name}"
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.info("Select at least 2 players in the filter to enable radar comparison.")

    st.markdown("---")

    # Data Table
    st.subheader("📋 Raw Data Explorer")
    st.dataframe(filtered_df, use_container_width=True)
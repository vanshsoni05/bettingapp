
import streamlit as st
import math

st.title("Betting Odds Calculator")
type = st.selectbox("What type of bet?",("Single Bet", "Parlay"))
wager = float(st.text_input("Enter wager ($)","10"))

if(type) == "Single Bet":
    odds = int(st.text_input("Enter odds (+) or (-)", "+110"))

odds_list = [] # this list has all odds that are in parlay
decimal_odds = [] #decimal odds all in the parlay

if (type) == "Parlay":
    q = (st.number_input("How many legs",min_value = 2, max_value = None, value = 2, step = 1))
    st.subheader("Enter odds for each leg")
    for i in range(q):
        p_odds = st.number_input(f"Leg {i+1}",value = 110, step = 1)
        #p_odds = int(st.text_input(f"Leg {i+1}", key = f"odds_list{i}"))
        odds_list.append(p_odds)
        ##
        #list index : odds already in number
        #0:1
        #1:2
        #2:3
        #3:4
        #4:5
        #5:6
        #american to decimal = odds/100 + 1, negative = 100/odds + 1

# This for loop calculates the american odds into decimal odds
decimal_odds = []
for i in odds_list:
    if i > 0:
        d_odds = (i/100)  + 1
        decimal_odds.append(d_odds)
    elif i < 0:
        d_odds = (100/abs(i)) + 1
        decimal_odds.append(d_odds)


result = 1
for j in decimal_odds:
    result *= j
######
if "a_odds" not in st.session_state:
    st.session_state.a_odds = 0
if (type == "Parlay"):
    if (st.button("Calculate Parlay Odds")):
        for i in decimal_odds:
            if i >= 2:
                st.session_state.a_odds = (result - 1) * 100
            if 1.01 <= i <= 1.99:
               st.session_state. a_odds = (-100/(result - 1))
        if st.session_state.a_odds > 0:
            st.write(f'+{st.session_state.a_odds:.0f}')
        else:
            st.write(f"{st.session_state.a_odds:.0f}")

# if single bet keep my if statement below
# if parlayed write the new calculation

# - = odds/ odds +100           +=  100/100 + odds



if (type == "Single Bet"):
    if (st.button("Calculate Payout")):
        if odds > 0:
            st.write(f'Payout: ${((odds/100) * wager) + wager:.2f}')
        elif odds < 0:
            st.write(f'Payout: ${((100/abs(odds)) * wager) + wager:.2f}')
    
    if(st.button("Calculate Probability")):
        if odds > 0:
            st.write(f'The probability sportbooks are giving is {(100/(100+ odds))*100:.2f}%')
        elif(odds < 0):
            st.write(f'The probability sportbooks are giving is {(abs(odds)/(100+ abs(odds)))*100:.2f}%')


elif(type == "Parlay"):
    if (st.button("Parlay Payout")):
        if st.session_state.a_odds > 0:
            st.write(f'Payout: ${((st.session_state.a_odds/100) * wager) + wager:.2f}')
        elif st.session_state.a_odds < 0:
            st.write(f'Payout: ${((100/abs(st.session_state.a_odds)) * wager) + wager:.2f}')
    if (st.button("Calculate Parlay Probability")):
        if st.session_state.a_odds > 0:
            st.write(f'The probability sportbooks are giving is {(100/(100+ st.session_state.a_odds))*100:.2f}%')
        elif(st.session_state.a_odds < 0):
            st.write(f'The probability sportbooks are giving is {(abs(st.session_state.a_odds)/(100+ abs(st.session_state.a_odds)))*100:.2f}%')

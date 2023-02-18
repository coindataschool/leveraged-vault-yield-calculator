import streamlit as st

# set_page_config() can only be called once per app, and must be called as the 
# first Streamlit command in your script.
st.set_page_config(page_title='leveraged-vault-yield-calculator', 
    layout='wide', page_icon='🔔') 

# user inputs    
st.header("Enter your numbers:")
c1, c2 = st.columns(2)
with c1:
    capital = st.number_input('Collateral ($)', min_value=100, value=10_000)
    borrow_mult = st.number_input('Borrow Multiple', min_value=1, value=5)
    dur = st.number_input('Duration (month)', min_value=1, value=1)
        
with c2:
    rate_get = st.number_input('Supply Yield (APR, %)', min_value=5, value=10)
    rate_pay = st.number_input('Borrow Rate (APR, %)', min_value=1, value=7)

# calculate effective yield
borrow = capital * borrow_mult
deposit = capital + borrow
monthly_rate_get = rate_get/100/12
monthly_rate_pay = rate_pay/100/12
earnings = deposit * (1 + monthly_rate_get*dur) - borrow * (1 + monthly_rate_pay*dur)
effective_yield = (earnings / capital - 1) / dur * 12

# display
st.header("Your Expected Yield (APR):")
st.title('{:.2%}'.format(effective_yield))


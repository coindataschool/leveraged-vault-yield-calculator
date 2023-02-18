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
    rate_pay = st.number_input('Borrow Rate (APR, %)', min_value=1, value=7)
    dur = st.number_input('Duration (month)', min_value=1, value=1)
with c2:
    stETH_yield = st.number_input('stETH Yield (APR, %)', min_value=1.0, value=10.0)
    swap_fees = st.number_input('Balancer wstETH/WETH Pool Swap Fees (APR, %)', min_value=0.1, value=0.5)
    bal_rewards = st.number_input('Bal Incentives (APR, %)', min_value=0.0, value=5.0)
    lido_rewards = st.number_input('Lido Incentives (APR, %)', min_value=0.0, value=0.5, step=0.1)
    aura_rewards = st.number_input('Aura Incentives (APR, %)', min_value=0.0, value=12.5, step=0.1) 
    
# calculate effective yield
borrow = capital * borrow_mult
deposit = capital + borrow
monthly_rate_get = (stETH_yield+swap_fees+bal_rewards+lido_rewards+aura_rewards)/100/12
monthly_rate_pay = rate_pay/100/12
earnings = deposit * monthly_rate_get * dur - borrow * monthly_rate_pay * dur # assume no compounding
effective_yield = (earnings / capital) / dur * 12

# display
st.header("Your Expected Yield (APR):")
st.title('{:.2%}'.format(effective_yield))
st.text('assuming no compounding')

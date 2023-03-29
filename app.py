import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import time

st.set_page_config(layout='wide')

df=pd.read_csv('startup_cleaned.csv')

st.sidebar.title('Startup Funding analysis')

df['date'] = pd.to_datetime(df['date'],errors= 'coerce')

df['year']=df['date'].dt.year
df['month']= df['date'].dt.month
def load_overall_analysis():
    st.title('Overall Analysis')
    col1, col2, col3, col4= st.columns(4)

    with col1:
        # Total amount invested in startups
        total_investment= round(df['amount'].sum())
        st.metric('Total Investment', str(total_investment) + ' Cr')

    with col2:
        # Max amount invested in startup
        max_investment= df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1)[0]
        st.metric('Maximum Investment', str(max_investment) + ' Cr')

    with col3:
        # Avg investment on an indian Startup
        avg_investment= round(df.groupby('startup')['amount'].sum().mean())
        st.metric('Avg Investment', str(avg_investment) + ' Cr')

    with col4:
        # Total No. of Funded Startups

        total_no_startups= df['startup'].nunique()
        st.metric('Total Invested startups', total_no_startups)


    st.header('Month on Month Investment Graph')
    select_option= st.selectbox('Select type', ['Total', 'Count'])
    if select_option=='Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '_' + temp_df['year'].astype('str')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig5)



def get_investor_details(investor):
    st.title(investor)

    # display last 5 investments details of investor

    last_5_df= df[df['investor'].str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last_5_df)

    # Biggest investments of investor

    col1, col2 = st.columns(2)
    with col1:
        big_invt_series  = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader('Biggest Investments')
        st.dataframe(big_invt_series)

        # Ploting a Bar Graph for Biggest investments of investor

        fig , ax = plt.subplots()
        ax.bar(big_invt_series.index, big_invt_series.values)

        st.pyplot(fig)
    with col2:
        investment_sector_series= df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Sectors Invested In')
        st.dataframe(investment_sector_series)

        # Plot pie chart of investment sector

        fig1, ax1 = plt.subplots()
        ax1.pie(investment_sector_series,autopct='%0.01f%%',labels= investment_sector_series.index)
        st.pyplot(fig1)

    # Top Cities Inevested In

    top_city_series= df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum().head(5).sort_values(ascending=False)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader('Top Cities Investor Inevested In')
        st.dataframe(top_city_series)

    # pie chart of Top Cities Inevested In
    with col4:
        st.subheader('Pie Chart of Top Cities Investor Inevested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(top_city_series, autopct='%0.01f%%', labels=top_city_series.index)
        st.pyplot(fig2)

    # year on year investments
    yoy_series= df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('Year on Year Investments')
    fig3, ax3 = plt.subplots()
    ax3.plot(yoy_series.index, yoy_series.values)
    st.pyplot(fig3)



options = st.sidebar.selectbox('Select Any One Analysis', ['Overall Analysis', 'Startup analysis', 'Investor Analysis'])

if options =='Overall Analysis':
    load_overall_analysis()
elif options == 'Startup analysis':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1= st.sidebar.button('Find Startup Details')
    st.title('Startup analysis')
else:
    selected_investor= st.sidebar.selectbox('Select Investor', sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        get_investor_details(selected_investor)


    

























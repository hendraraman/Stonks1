import streamlit as st
from datetime import date
import yfinance as yf
from prophet.plot import plot_plotly
from prophet import Prophet
import plotly.graph_objs as go
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start,today)
    data.reset_index(inplace = True)
    return data

st.write ("Opened")

start = "2015-01-01"
today = date.today().strftime("%Y-%m-%d")

st.title("Welcome eyyy")
st.header("This is our Stock Price prediction APP ")

stonks = ("AAPL","GOOG","MSFT")
selected = st.selectbox("Select the stock for prediction",stonks)
default_value = 3

num_years = st.slider("Predict for how many months?",1,12,default_value)
period = num_years*30
data_load_state = st.text("Load dataaaa")
data = load_data(selected)
data_load_state.text("Loading dataaaw...overeyyy")

st.subheader("Raw data")
st.write(data.tail())

# plotting the raw data
def plot_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['Date'],y = data["Open"],name = "Stock_open"))
    fig.add_trace(go.Scatter(x = data['Date'],y = data["Close"],name = "Stock_close"))
    fig.layout.update(title_text = "This is a time series data of "+selected,xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)
plot_data()

# here is where forcastring is done
# prediction
st.write("Prediction ... In progress")

# st.write(data.columns)  
df_train = data[["Date","Close"]]
df_train =  df_train.rename(columns = {"Date":"ds","Close":"y"})
m = Prophet()

m.fit(df_train)

upcoming = m.make_future_dataframe(periods = period)
st.write("We're almost there")
prediction = m.predict(upcoming)


 
st.subheader("Here is the prediction:")
st.write(prediction.tail())

st.subheader("Plotting the forecasted data")
plot1 = plot_plotly(m, prediction)
st.plotly_chart(plot1)

st.subheader("Forecasting the Trends for "+selected)
plot2 = m.plot_components(prediction)
st.write(plot2)
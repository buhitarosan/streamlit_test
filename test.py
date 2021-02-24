import streamlit as st
import plotly.graph_objs as go

animals = ['giraffes', 'orangutans', 'monkeys']
populations = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

st.plotly_chart(fig, use_container_width=True)

"Hello World"

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

option = st.selectbox(
    'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


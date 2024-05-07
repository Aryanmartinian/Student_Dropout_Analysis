import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Student Dropout Analysis")
# 1 --> Dropout and 0 --> No Dropout
df = pd.read_csv('data/data.csv')
st.subheader('Summary Statistics')
st.write(df.describe())

st.subheader('Correlation Matrix')
corr_matrix = df.corr()
st.write(corr_matrix)

cols = df.columns.tolist()
selected_cols = st.multiselect('Select Attributes',cols) # for multiple columns
st.metric(label= 'Average Dropout Students',value=round(df['Unemployment_rate'].mean()),
          delta = round(df['Unemployment_rate'].std()))

for col in selected_cols:
    st.subheader(f'Mean {col}')
    try:
        st.metric(label=f'Mean {col}',
                value=round(df[col].mean()),
                delta=round(df[col].std()))
        st.line_chart(df[col],use_container_width=True)
    except:
        st.error(f'Cannot display{col} numeric data')


# Allow the user to select two variables
variable1 = st.selectbox("Select Variable 1", df.columns)
variable2 = st.selectbox("Select Variable 2", df.columns)

# Calculate frequencies or counts of unique values for the selected variables
variable1_counts = df[variable1].value_counts()
variable2_counts = df[variable2].value_counts()

# Create a pie chart using Matplotlib
fig, ax = plt.subplots(1, 2, figsize=(15, 10))

ax[0].pie(variable1_counts, labels=variable1_counts.index, autopct='%1.1f%%', startangle=140)
ax[0].set_title(f'Pie Chart for {variable1}')
ax[0].axis('equal')

ax[1].pie(variable2_counts, labels=variable2_counts.index, autopct='%1.1f%%', startangle=140)
ax[1].set_title(f'Pie Chart for {variable2}')
ax[1].axis('equal')

# Display the pie charts in the Streamlit app
st.pyplot(fig)


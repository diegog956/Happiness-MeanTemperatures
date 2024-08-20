import pandas as pd
import streamlit as st
import seaborn as sns
import flagpy as fl
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

sources = ['https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021', 'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature']

df = pd.read_csv('data/data_happiness_meantemperature.csv', index_col =0)

st.image('data/winter_vs_summer.jpg')

st.title('Analyzing Happiness by Temperature: Does Warm Weather Make Us Happier?')

st.page_link('https://github.com/diegog956', label="github.com/diegog956", icon=":material/link:")

st.text("""It's widely believed that people tend to be happier during the summer, while 
winter is often associated with sadness.
        
Let's explore the data from the 2021 World Happiness Report alongside the average
yearly temperatures of countries around the world to see what insights we can 
uncover.\n""")

st.markdown('<u>*Disclaimer:</u> This report is intented to be test of streamlit as a tool.*', unsafe_allow_html=True)

st.page_link(sources[0], label='World Happiness Report 2021', icon=":material/captive_portal:")
st.page_link(sources[1], label='List of countries by average yearly temperature', icon=":material/captive_portal:")

st.text("""After extracting data from both sources and cleaning and parsing the dataset,
we come across this DataFrame:""")

df1=df.copy()
df1.rename(columns={'Temperature':'Temperature (ºC)'}, inplace=True)
st.dataframe(df1)

st.text("""Reading tabular data might be boring and you can get dizzy.
Let's build a scatterplot instead with thier proper flags:
""")

lista_img = []
country_list = fl.get_country_list()
for country in df.Country:
  if country in country_list:
    lista_img.append(fl.get_flag_img(country))

figure = plt.figure(figsize=(10, 6), dpi=200)
sns.scatterplot(data=df,x='Score', y='Temperature', s=0);
plt.ylabel('Mean annual Temperature (ºC)')
plt.xlabel('Happiness Score (0-10)')
plt.yticks(list(range(-5,31, 5)))

for i in range(len(df)):
    img = lista_img[i]
    imagebox = OffsetImage(img, zoom=0.07)
    ab = AnnotationBbox(imagebox, (df['Score'][i], df['Temperature'][i]), frameon=True, pad=0.05)
    plt.gca().add_artist(ab)

plt.grid(color='gray', linestyle='--', linewidth=0.5)

st.pyplot(figure)

st.text("""We found an interesting thing to point out as a conclusion:
    
People's hypotesis of strong correlation between Happiness and warm weather might
not be accurate due to the fact, as the plot is pointing out, that there's no cold
weather countries whose happiness score drops below 5 while seems to be the mean 
in warm countries.
        
We can't also jump into conclusion that is the other way around giving the fact 
that other different indicators play an important role in humanity well being as well.

""")

st.markdown("""*For further investigation about the subject i recommend take a deep look into
the 2021 world happiness report to extract more meaningful data.*""")

st.text("Thank you!")

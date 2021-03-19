import streamlit as st
import numpy as np
import pandas as pd


ORDERED_KEYS = pd.read_csv('data/ordered_keys.csv')

@st.cache
def get_combination_percentage():
    return pd.read_csv('data/combination_percentage_01.csv', compression='infer', storage_options=None)
COMBINATION_PERCENTAGE = get_combination_percentage()

def get_combinations(search_word, range_start, range_end):
    word_index = ORDERED_KEYS[ORDERED_KEYS['replaced'] == search_word[0]].index[0]
    ingredient_row = COMBINATION_PERCENTAGE.iloc[word_index,:].T.sort_values(ascending=False)
    top_results = []
    for position in range(range_start,range_end):
        ingr_id = int(ingredient_row.index[position])
        name = ORDERED_KEYS['replaced'].iloc[ingr_id]
        top_results.append(name)
    return top_results

# def print_combinations(selectByuser):
#     for i in selectByuser:
#         print(i)
#         st.write(COMBINATION_PERCENTAGE[ORDERED_KEYS['replaced']==i][['replaced', 'id']])
#     print(selectByuser)

# def app():
#     st.title('Aproveite para desfrutar de uma das maiores base de Dados de ingredientes.Faça uma busca com os ingredientes que deseja.')
#     selectByuser = st.multiselect('Escolha uma das funcionalidades:', 
#                 ORDERED_KEYS['replaced'].unique())
#     get_combinations(selectByuser)

st.title('Ingredient matcher')
st.markdown('''### Aproveite para desfrutar de uma das maiores base de Dados de ingredientes.Faça uma busca com os ingredientes que deseja.''')

selectByuser = st.multiselect('Escolha seus ingredientes:', 
                ORDERED_KEYS['replaced'].unique())
st.title('Top results')
st.write(get_combinations(selectByuser,1,21))
st.title('Arte ou merda')
st.write(get_combinations(selectByuser,50,60))
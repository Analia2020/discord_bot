import numpy as numpy
import pandas as pd
from bs4 import BeautifulSoup 
import requests

def concatenate_query(key_concepts):
    concepts_list = [str(concept) for concept in key_concepts]
    concept = '+'.join(concepts_list)
    return concept
# def concatenate_query(key_concepts):
#     concepts_list = key_concepts.split()
#     concept = '+'.join(concepts_list)
#     return concept

def get_bvsalud(query):
    url = f'https://pesquisa.bvsalud.org/portal/?output=site&lang=en&from=1&sort=YEAR_DESC&format=summary&count=20&fb=&page=1&skfp=true&index=&q={query}&search_form_submit='
    content = requests.get(url).content
    output_data = []
    soup = BeautifulSoup(content, features="html.parser")
    for row in soup.find_all('div', {'class':'box1'}):
        row_dict = {}
        for div in row.find_all('div'):
            div_class = div ['class'][0]
            row_dict[div_class] = div.text.strip()
        output_data.append(row_dict)
    df=pd.DataFrame(output_data).reset_index(drop= True)
    columns = ['Title', 'Author', 'Journal', 'Abstract']
    df= df[['titleArt', 'author', 'reference', 'reference-detail']]
    df.columns = columns
    return df.loc[:4]

# manos = concatenate_query('cancer de higado')
# print(manos)
# df = get_bvsalud(manos)
# print(df.columns)

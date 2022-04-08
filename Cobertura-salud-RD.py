# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:11:32 2022

@author: Familia Ramirez
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
##############################################################################################################################################################
# que abarque todo el ancho de la página
st.set_page_config(layout='wide')
# Definir el título del dashboard y su estilo
st.markdown("<h1 style = 'text-align:center;color:cyan;'> Cobertura de salud en República Dominicana👩‍⚕️️ ⚕️</h1>", unsafe_allow_html=True)

###############################################################################
# Correr dato mediante una función
# @st.cache(persist = True) #permite que quede la info almacenada si se corre una vez
# def load_data(url):

cober2015 = pd.read_csv('Bases/Cobertura2015.csv', sep=';')
cober2016 = pd.read_csv('Bases/Cobertura2016.csv', sep=';')
cober2017 = pd.read_csv('Bases/Cobertura2017.csv', encoding= 'unicode_escape', sep=';')
cober2018 = pd.read_csv('Bases/Cobertura2018.csv', sep=';')
cober2019 = pd.read_csv('Bases/Cobertura2019.csv', encoding= 'unicode_escape', sep=';')
cober2020 = pd.read_csv('Bases/Cobertura2020.csv', encoding= 'unicode_escape', sep=';')

##############################################################################################################################################################
st.sidebar.markdown("### República Dominicana")
from PIL import Image
image = Image.open('playa.jpeg')
st.sidebar.image(image, caption='Playas República Dominicana')
st.sidebar.markdown("Es un país ubicado en la zona central del caribe americano, sobre la zona centro de las Antillas, su proporción ocupa la parte oriental y central de la isla la española, compartida con el país de Haití por el Oeste. República Dominicana tiene la novena economía más grande de América Latina y la primera de América Central y el Caribe y ocupa la séptima posición en ingreso per cápita en América Latina, superada por Puerto Rico, Panamá, Chile, Uruguay, Argentina y México.")
st.sidebar.markdown("Datos importantes:")
st.sidebar.markdown("*Tiene aproximadamente 10 millones de habitantes y su capital es Santo Domingo.")
st.sidebar.markdown("*Es el destino más visitado del Caribe.")
st.sidebar.markdown("*Durante todo el año los campos de golf del país se encuentran entre las principales atracciones de la isla.")
st.sidebar.markdown("*Tiene una amplia diversidad biológica.")
st.sidebar.markdown("*Tiene una temperatura promedio de 27 °C.")
##############################################################################################################################################################
pd.options.display.float_format = '{:.0f}'.format # organizar los decimales
# Funciones

def graf(base, row=1, col=1):
    """
    Gráficas del análisis Población usuaria vs Cantidad servicios cuando se 
    escoge un años en específica. 
    """
    fig = go.Figure()
    fig = make_subplots(rows=1,cols=1)
    base1 = orden_mes(base)
    fig.add_trace(go.Scatter(x = base1['Mes'], y = base1['Poblacion usuaria'],mode = 'lines+markers' , name = 'Poblacion usuaria',
                             line=dict(color="red")),row=row,col=col)
    fig.add_trace(go.Scatter(x = base1['Mes'], y = base1['Cantidad servicios'],mode = 'lines+markers', name = 'Cantidad de servicios',
                             line=dict(color="blue")),row=row,col=col)
    fig.update_layout(width = 1280, height = 450)
    st.plotly_chart(fig)
def make_graf(base,row=1, col=1, legend = False):
    """
    Gráficas del análisis Población usuaria vs Cantidad servicios cuando se 
    escoge observar todos los años.
    
    """
    base1 = orden_mes(base)
    fig.add_trace(go.Scatter(x = base1['Mes'], y = base1['Cantidad servicios'],mode = 'lines+markers', name = 'Cantidad de servicios', showlegend = legend,
                             line=dict(color="blue")),row=row,col=col)
    fig.add_trace(go.Scatter(x = base1['Mes'], y = base1['Poblacion usuaria'],mode = 'lines+markers' , name = 'Poblacion usuaria', showlegend = legend,
                             line=dict(color="red")),row=row,col=col)
    fig.update_layout(width = 1280, height = 800)#, showlegend = False)
def orden_mes(x):
    """
    Función para organizar en orden los meses del año
    """
    x['Mes1'] = x.Mes.replace({'Enero':1,'Febrero':2,'Marzo':3,'Abril':4,'Mayo':5,'Junio':6,
                               'Julio':7,'Agosto':8,'Septiembre':9,'Octubre':10,'Noviembre':11,'Diciembre':12})
    x = x.sort_values('Mes1').reset_index(drop=True)
    x.drop(['Mes1'], axis = 1, inplace = True)
    return x
def unir(df1,df2):
    """
    Función para unir dataframes
    """
    return pd.merge(df1, df2, on = ['Provincia'], how='left')

##############################################################################################################################################################
# Punto 2

# eliminar espacios en blanco
cober2018['Mes'] = cober2018['Mes'].apply(lambda x: x.strip())
cober2020['Mes'] = cober2020['Mes'].apply(lambda x: x.strip())
cober_pobla_usu2015 = cober2015[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()
cober_pobla_usu2016 = cober2016[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()
cober_pobla_usu2017 = cober2017[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()
cober_pobla_usu2018 = cober2018[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()
cober_pobla_usu2019 = cober2019[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()
cober_pobla_usu2020 = cober2020[['Poblacion usuaria','Cantidad servicios', 'Mes']].groupby(['Mes'])[['Poblacion usuaria','Cantidad servicios']].sum().reset_index()

# organizar valores año 2015
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].astype('str')
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].str.replace(',','')
cober2015['Valor Autorizado (RD$)'] = pd.to_numeric(cober2015['Valor Autorizado (RD$)'])
##############################################################################################################################################################

st.markdown("<h4 style = 'text-align:center;color:red;'> Frecuencia con la que una persona va a los especialistas </h4>", unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns((1,1,1,1,1,1))

c1.markdown("<h4 style = 'text-align:left;color:white;'> 2015</h4>", unsafe_allow_html=True)
frec_2015 = round(cober_pobla_usu2015['Cantidad servicios'].sum()/cober_pobla_usu2015['Poblacion usuaria'].sum(),2)
c1.text(frec_2015)

c2.markdown("<h4 style = 'text-align:left;color:white;'> 2016</h4>", unsafe_allow_html=True)
frec_2016 = round(cober_pobla_usu2016['Cantidad servicios'].sum()/cober_pobla_usu2016['Poblacion usuaria'].sum(),2)
c2.text(frec_2016)

c3.markdown("<h4 style = 'text-align:left;color:white;'> 2017</h4>", unsafe_allow_html=True)
frec_2017 = round(cober_pobla_usu2017['Cantidad servicios'].sum()/cober_pobla_usu2017['Poblacion usuaria'].sum(),2)
c3.text(frec_2017)

c4.markdown("<h4 style = 'text-align:left;color:white;'> 2018</h4>", unsafe_allow_html=True)
frec_2018 = round(cober_pobla_usu2018['Cantidad servicios'].sum()/cober_pobla_usu2018['Poblacion usuaria'].sum(),2)
c4.text(frec_2018)

c5.markdown("<h4 style = 'text-align:left;color:white;'> 2019</h4>", unsafe_allow_html=True)
frec_2019 = round(cober_pobla_usu2019['Cantidad servicios'].sum()/cober_pobla_usu2019['Poblacion usuaria'].sum(),2)
c5.text(frec_2019)

c6.markdown("<h4 style = 'text-align:left;color:white;'> 2020</h4>", unsafe_allow_html=True)
frec_2020 = round(cober_pobla_usu2020['Cantidad servicios'].sum()/cober_pobla_usu2020['Poblacion usuaria'].sum(),2)
c6.text(frec_2020)

# st.checkbox('Gráfico de torta'):
fig = go.Figure()
fig.add_trace(go.Pie(labels = ['2015','2016','2017','2018','2019','2020'], values = [frec_2015,frec_2016,frec_2017,frec_2018,frec_2019,frec_2020], pull=[0, 0, 0, 0, 0, 0.2]))
fig.update_layout(template = 'simple_white')
c2.plotly_chart(fig)

##############################################################################################################################################################
st.markdown("<h4 style = 'text-align:center;color:red;'> Análisis de la evolución por meses de la población usuaria vs la cantidad de servicios ofrecidos en cada año</h4>", unsafe_allow_html=True)

anio = st.selectbox("Año a observar", [2015, 2016, 2017, 2018, 2019, 2020,'Todos'], index=0)

if anio == 2015:
    graf(cober_pobla_usu2015)
elif anio == 2016:
    graf(cober_pobla_usu2016)
elif anio == 2017:
    graf(cober_pobla_usu2017)
elif anio == 2018:
    graf(cober_pobla_usu2018)
elif anio == 2019:
    graf(cober_pobla_usu2019)
elif anio == 2020:
    graf(cober_pobla_usu2020)
else:
    fig = make_subplots(rows=3,cols=2, subplot_titles = ('<b>2015<b>','<b>2016<b>','<b>2017<b>','<b>2018<b>','<b>2019<b>','<b>2020<b>'))
    make_graf(cober_pobla_usu2015, 1, 1, True)
    make_graf(cober_pobla_usu2016, 1, 2)
    make_graf(cober_pobla_usu2017, 2, 1)
    make_graf(cober_pobla_usu2018, 2, 2)
    make_graf(cober_pobla_usu2019, 3, 1)
    make_graf(cober_pobla_usu2020, 3, 2)
    st.plotly_chart(fig)
##############################################################################################################################################################
# Punto 4

st.markdown("<h4 style = 'text-align:center;color:red;'> Top 6 de provincias donde más dinero se invierte en cada año</h4>", unsafe_allow_html=True)

# 2015
cober2015_valor = cober2015.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2015'}).head(6)
# 2016
cober2016_valor = cober2016.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2016'}).head(6)
# 2017
cober2017_valor = cober2017.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2017'}).head(6)
# 2018
cober2018_valor = cober2018.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2018'}).head(6)
# 2019
cober2019_valor = cober2019.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2019'}).head(6)
# 2020
cober2020_valor = cober2020.groupby(['Provincia'])[['Valor Autorizado (RD$)']].sum().reset_index().sort_values('Valor Autorizado (RD$)', ascending = False).rename(columns = {'Valor Autorizado (RD$)':'2020'}).head(6)

provincias = pd.DataFrame({'Provincia':['SANTO DOMINGO','DISTRITO NACIONAL','SANTIAGO DE LOS CABALLEROS','SAN CRISTOBAL','LA VEGA','DUARTE']})

df1 = unir(provincias, cober2015_valor)
df2 = unir(df1, cober2016_valor)
df3 = unir(df2, cober2017_valor)
df4 = unir(df3, cober2018_valor)
df5 = unir(df4, cober2019_valor)
df6 = unir(df5, cober2020_valor)

df8 = df6.copy()
df8['color'] = ['rgb(170, 68, 153)','rgb(136, 204, 238)', 'rgb(51, 34, 136)', 'rgb(17, 119, 51)', 'rgb(221, 204, 119)', 'rgb(204, 102, 119)']

fig = go.Figure(data = [go.Table(
    header = dict(values=list(df6.columns), # encabezado
                  fill_color = 'black',
                  line_color = 'darkslategray',
                  font=dict(size=16)),
    
    cells = dict(values = [df6['Provincia'], df6['2015'], df6['2016'],df6['2017'],df6['2018'],df6['2019'],df6['2020']], height=30,
                 format = ["",",.0f"],
                 fill_color = [df8.color],
                 line_color = 'lightgrey',
                 font=dict(size=14)))
    ])
fig.update_layout(width = 1280)

st.write(fig)


df7 = pd.pivot_table(df6, values = ['2015','2016','2017','2018','2019','2020'], columns = ['Provincia'])

fig = px.area(df7, x = ['2015','2016','2017','2018','2019','2020'], y = ['DUARTE', 'LA VEGA', 'SAN CRISTOBAL','SANTIAGO DE LOS CABALLEROS','DISTRITO NACIONAL',  'SANTO DOMINGO'], 
               color_discrete_sequence = ['rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)', 'rgb(51, 34, 136)','rgb(136, 204, 238)',  'rgb(170, 68, 153)'])

fig.update_layout(
    xaxis_title = '<b>Años<b>',
    yaxis_title = '<b>Valor autorizado<b>',
    legend_title = '<b>Distritos<b>',
    template = 'simple_white',
    width = 1280, height = 500,
    legend=dict(
      orientation='h',
      yanchor="bottom",
      y=1.09,
      xanchor="right",
      x=1))

fig.update_xaxes(tickfont=dict(family='Rockwell', size=16))
fig.update_yaxes(tickfont=dict(family='Rockwell', size=16))
st.plotly_chart(fig)


##############################################################################################################################################################
# Punto 6
# ¿Cuál es la cantidad de Especialidades solicitada por mes de los últimos 3 años?
st.markdown("<h4 style = 'text-align:center;color:red;'> Cantidad de Especialidades solicitada por mes de los últimos 3 años \n\n Elija el gráfico de su preferencia</h4>", unsafe_allow_html=True)

# sacar los datos para analziar
cober2018_espe = cober2018[['Especialidad','Mes']]
cober2018_espe = cober2018_espe.groupby(['Mes'])[['Especialidad']].count().reset_index()
cober2018_espe = orden_mes(cober2018_espe)

cober2019_espe = cober2019[['Especialidad','Mes']]
cober2019_espe = cober2019_espe.groupby(['Mes'])[['Especialidad']].count().reset_index()
cober2019_espe = orden_mes(cober2019_espe)

cober2020_espe = cober2020[['Especialidad','Mes']]
cober2020_espe  = cober2020_espe .groupby(['Mes'])[['Especialidad']].count().reset_index()
cober2020_espe  = orden_mes(cober2020_espe )


st.markdown("<h5 style = 'text-align:center;color:white;'> Año 2018 </h5>", unsafe_allow_html=True)
c1,c2 = st.columns([1,1])
# se definide gráfico de torta
if c1.checkbox('Gráfico de torta 2018',True):
    base = cober2018_espe
    fig = go.Figure()
    fig.add_trace(go.Pie(labels = base['Mes'], values = base['Especialidad'], pull=[0, 0, 0, 0,0, 0, 0.2, 0,0, 0, 0, 0]))
    fig.update_layout(template = 'simple_white',legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01),
                      title_text = '<b>Porcentaje de especialidades solicitadas por mes en 2018<b>',title_x = 0.5)
    fig.update_traces(marker=dict(colors=['#FD3216', '#00FE35', '#6A76FC', '#FED4C4', '#FE00CE', '#0DF9FF', '#F6F926', '#FF9616', '#479B55', '#EEA6FB', '#DC587D', '#D626FF']))
    c1.plotly_chart(fig)
# se definide gráfico de barras
if c2.checkbox('Gráfico de barras 2018',True):
    base = cober2018_espe
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x = base['Mes'], y = base['Especialidad'], marker_color=px.colors.qualitative.Light24))
    fig2.update_layout(title_text = '<b>Cantidad de especialidades solicitadas por mes en 2018<b>',template = 'simple_white',title_x = 0.5)
    c2.plotly_chart(fig2)
#########################################################################
st.markdown("<h5 style = 'text-align:center;color:white;'> Año 2019 </h5>", unsafe_allow_html=True)
c1,c2 = st.columns([1,1])
# se definide gráfico de torta
if c1.checkbox('Gráfico de torta 2019',True):
    base = cober2019_espe
    fig = go.Figure()
    fig.add_trace(go.Pie(labels = base['Mes'], values = base['Especialidad'], pull=[0, 0, 0, 0,0, 0, 0.2, 0,0, 0, 0, 0]))
    fig.update_layout(template = 'simple_white',legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01),
                      title_text = '<b>Porcentaje de especialidades solicitadas por mes en 2019<b>',title_x = 0.5) 
    fig.update_traces(marker=dict(colors=['#FD3216', '#00FE35', '#6A76FC', '#FED4C4', '#FE00CE', '#0DF9FF', '#F6F926', '#FF9616', '#479B55', '#EEA6FB', '#DC587D', '#D626FF']))
    c1.plotly_chart(fig)
# se definide gráfico de barras
if c2.checkbox('Gráfico de barras 2019',True):
    base = cober2019_espe
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x = base['Mes'], y = base['Especialidad'], marker_color=px.colors.qualitative.Light24))
    fig2.update_layout(title_text = '<b>Cantidad de especialidades solicitadas por mes en 2019<b>',template = 'simple_white',title_x = 0.5)
    c2.plotly_chart(fig2)
#########################################################################
st.markdown("<h5 style = 'text-align:center;color:white;'> Año 2020 </h5>", unsafe_allow_html=True)
c1,c2 = st.columns([1,1])
# se definide gráfico de torta
if c1.checkbox('Gráfico de torta 2020',True):
    base = cober2020_espe
    fig = go.Figure()
    fig.add_trace(go.Pie(labels = base['Mes'], values = base['Especialidad'], pull=[0.2, 0.2, 0, 0,0, 0, 0, 0,0, 0, 0, 0]))
    fig.update_layout(template = 'simple_white',legend=dict(yanchor="top",y=0.9,xanchor="left",x=-0.1),
                      title_text = '<b>Porcentaje de especialidades solicitadas por mes en 2020<b>',title_x = 0.5)
    fig.update_traces(marker=dict(colors=['#FD3216', '#00FE35', '#6A76FC', '#FED4C4', '#FE00CE', '#0DF9FF', '#F6F926', '#FF9616', '#479B55', '#EEA6FB', '#DC587D', '#D626FF']))
    c1.plotly_chart(fig)
# se definide gráfico de barras
if c2.checkbox('Gráfico de barras 2020',True):
    base = cober2020_espe
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x = base['Mes'], y = base['Especialidad'], marker_color=px.colors.qualitative.Light24))
    fig2.update_layout(title_text = '<b>Cantidad de especialidades solicitadas por mes en 2020<b>',template = 'simple_white',title_x = 0.5)
    c2.plotly_chart(fig2)
##############################################################################################################################################################




cober2020.rename(columns = {'sistemas':'Sistema'}, inplace = True)

# se eliminan valores nulos
cober2016.dropna(inplace = True)
cober2017.dropna(inplace = True)
cober2018.dropna(inplace = True)
cober2020.dropna(inplace = True)


# función para eliminar datos 'No especificados' o 'No indicados' de una columna especificada
def drop_noespe(df,col):
  df[col] = df[col].apply(lambda x: np.nan if x[:2] == 'No' else x)
  df.dropna(inplace = True)

# función para reemplazar valores extraños
def reempla(df,c, v, n):
  df[c] = df[c].replace({v:n})

# se usa la función anterior
drop_noespe(cober2015,'Especialidad')
drop_noespe(cober2016,'Especialidad')
drop_noespe(cober2016,'Provincia')
drop_noespe(cober2017,'Especialidad')
drop_noespe(cober2018,'Especialidad')
drop_noespe(cober2019,'Especialidad')
drop_noespe(cober2019, 'Provincia')
drop_noespe(cober2020,'Especialidad')
drop_noespe(cober2020,'Provincia')

reempla(cober2017,'Provincia','ELIAS PI\x84A','ELIAS PINA')
reempla(cober2017,'Provincia','MONSE\x84OR NOUEL','MONSENOR NOUEL')
reempla(cober2018,'Provincia','MONSEnOR NOUEL','MONSENOR NOUEL')
reempla(cober2018,'Provincia','ELIAS PInA','ELIAS PINA')
reempla(cober2019,'Provincia','ELIAS PInA','ELIAS PINA')
reempla(cober2019,'Provincia','ELIAS PIÑA','ELIAS PINA')
reempla(cober2019,'Provincia','MONSEnOR NOUEL','MONSENOR NOUEL')
reempla(cober2019,'Provincia','MONSEÑOR NOUEL','MONSENOR NOUEL')
reempla(cober2020,'Provincia','ELIAS PInA','ELIAS PINA')
reempla(cober2020,'Provincia','ELIAS PIÑA','ELIAS PINA')
reempla(cober2020,'Provincia','MONSEnOR NOUEL','MONSENOR NOUEL')
reempla(cober2020,'Provincia','MONSEÑOR NOUEL','MONSENOR NOUEL')


# organizar valores
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].astype('str')
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2015['Valor Autorizado (RD$)'] = cober2015['Valor Autorizado (RD$)'].str.replace(',','')
cober2015['Valor Autorizado (RD$)'] = pd.to_numeric(cober2015['Valor Autorizado (RD$)'])

cober2016['Valor Autorizado (RD$)'] = cober2016['Valor Autorizado (RD$)'].astype('str')
cober2016['Valor Autorizado (RD$)'] = cober2016['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2016['Valor Autorizado (RD$)'] = cober2016['Valor Autorizado (RD$)'].str.replace(',','')
cober2016['Valor Autorizado (RD$)'] = pd.to_numeric(cober2016['Valor Autorizado (RD$)'])

cober2017['Valor Autorizado (RD$)'] = cober2017['Valor Autorizado (RD$)'].astype('str')
cober2017['Valor Autorizado (RD$)'] = cober2017['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2017['Valor Autorizado (RD$)'] = cober2017['Valor Autorizado (RD$)'].str.replace(',','')
cober2017['Valor Autorizado (RD$)'] = pd.to_numeric(cober2017['Valor Autorizado (RD$)'])

cober2018['Valor Autorizado (RD$)'] = cober2018['Valor Autorizado (RD$)'].astype('str')
cober2018['Valor Autorizado (RD$)'] = cober2018['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2018['Valor Autorizado (RD$)'] = cober2018['Valor Autorizado (RD$)'].str.replace(',','')
cober2018['Valor Autorizado (RD$)'] = pd.to_numeric(cober2018['Valor Autorizado (RD$)'])

cober2019['Valor Autorizado (RD$)'] = cober2019['Valor Autorizado (RD$)'].astype('str')
cober2019['Valor Autorizado (RD$)'] = cober2019['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2019['Valor Autorizado (RD$)'] = cober2019['Valor Autorizado (RD$)'].str.replace(',','')
cober2019['Valor Autorizado (RD$)'] = pd.to_numeric(cober2019['Valor Autorizado (RD$)'])

cober2020['Valor Autorizado (RD$)'] = cober2020['Valor Autorizado (RD$)'].astype('str')
cober2020['Valor Autorizado (RD$)'] = cober2020['Valor Autorizado (RD$)'].apply(lambda x: x.strip())
cober2020['Valor Autorizado (RD$)'] = cober2020['Valor Autorizado (RD$)'].str.replace(',','')
cober2020['Valor Autorizado (RD$)'] = pd.to_numeric(cober2020['Valor Autorizado (RD$)'])





Base_general = pd.concat([cober2015, cober2016, cober2017, cober2018, cober2019,cober2020])
Base_general.drop(['Unnamed: 10'], axis = 1, inplace = True)





###Base_general['Mes'] = Base_general['Mes'].replace({'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06',
                              #### 'Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'})
Base_general['Mes'] = Base_general['Mes'].replace({'Mes':'No '})                             

Base_general['Sistema'] = Base_general['Sistema'].replace(['Autorizaciones ','Autorizaciones'], 'AUTORIZACIONES')
Base_general['Sistema'] = Base_general['Sistema'].replace(['Sirs'], 'SIRS')
Base_general['Provincia'] = Base_general['Provincia'].replace(['MONSENOR NOUEL'], 'MONSEÑOR NOUEL')


drop_noespe(Base_general,'Mes') # CON LA FUNCION CREADA, ELIMINAR EL DATO EERADO QUE DICE MES EN VEZ DEL MES COMO TAL

Base_general['Mes'] = Base_general['Mes'].replace({'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06',
                               'Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'})


### se conviertes los datos de 'mes' y 'dia' a string
Base_general['Mes'] = Base_general['Mes'].astype('str')
Base_general['Ano'] = Base_general['Ano'].astype('str')

Base_general['fecha'] = Base_general[['Ano','Mes']].apply(lambda x: '-'.join(x), axis = 1)

##Base_general['fecha'] = pd.to_datetime(Base_general['fecha'], format = '%Y-%m')

pd.to_datetime(Base_general['fecha'], format = '%Y-%m')
##########################st.write(Base_general)



Base_general22=Base_general.groupby(['fecha'])[['Poblacion usuaria']].sum().reset_index()
Base_general1=Base_general.groupby(['fecha'])[['Cantidad servicios']].sum().reset_index()
data_0= pd.merge(Base_general22,Base_general1, how = 'left', on = 'fecha')
data_0[['Usuarios acum','Servicios acum']] = data_0.iloc[:,[1,2]].cumsum()

fig2 = px.line(data_0, x = 'fecha', y = ['Servicios acum','Usuarios acum'], title = '<b>Cantidas servicios y usuarios  acum <b>', color_discrete_sequence = px.colors.qualitative.G10)
fig1 = px.line(data_0, x = 'fecha', y = ['Cantidad servicios','Poblacion usuaria'], title = '<b>Cantidas servicios y usuarios del sistema <b>', color_discrete_sequence = px.colors.qualitative.G10)

Base_general_esp=Base_general.groupby(['Especialidad'])[['Cantidad servicios']].sum().reset_index()
b1 = Base_general_esp.sort_values('Cantidad servicios',ascending=False)
b1=b1.iloc[0:20,:]
fig20 = px.bar(b1, x = 'Especialidad', y = ['Cantidad servicios'], title = '<b>Cantidad de consultas por especilidas <b>', color_discrete_sequence = px.colors.qualitative.G10)



b1 = Base_general_esp.sort_values('Cantidad servicios',ascending=False)

Base_general200= Base_general.groupby(['Region'])[['Valor Autorizado (RD$)']].sum().reset_index()
b2 = Base_general200.sort_values('Valor Autorizado (RD$)',ascending=False)                                
fig23 = px.bar(b2, x = 'Region', y = ['Valor Autorizado (RD$)'], title = '<b> Cantidad de dinero autorizado por regiones <b>', color_discrete_sequence = px.colors.qualitative.G10)




st.markdown("<h5 style = 'text-align:center;color:red;'> Comportamiento general de los servicios </h5>", unsafe_allow_html=True)
c3,c4 = st.columns((1,1/1.5))
c3.plotly_chart(fig1)
c4.plotly_chart(fig2)

st.markdown("<h4 style = 'text-align:center;color:red;'> Especialidades mas consultadas por los dominicanos entre 2015 y 2020 </h4>", unsafe_allow_html=True)
st.write(fig20)

from PIL import Image
image2= Image.open('regiones.jpeg')


st.markdown("<h4 style = 'text-align:center;color:red;'> Gasto total del sistema por regiones </h4>", unsafe_allow_html=True)
c5,c6 = st.columns((1,1/1.5))
c5.plotly_chart(fig23)
c6.image(image2) 


###############################

##¿Cual es el top 5 de provincias que mayor poblacion atienden? 
##¿Este analisis cambia si se relaciona la poblacion total de cada provincia con
##la poblacion usuaria?
st.markdown("<h3 style = 'text-align:center;color:red;'>Top de las 5 provincias con mayor atención</h3>", unsafe_allow_html=True)

c1, c2 = st.columns((1,1))

provincia_mayor = Base_general[['Provincia','Poblacion usuaria']]
provincia_mayorg = provincia_mayor.groupby(['Provincia'])[['Poblacion usuaria']].count().reset_index()
provincia_mayorg = provincia_mayorg.sort_values(by = 'Poblacion usuaria', ascending = False) 
fig1 = px.bar(provincia_mayorg.head(5), x="Provincia", y="Poblacion usuaria", color="Provincia", title="Relacion poblacion usuaria con Provincia", barmode = 'stack',width = 600)
c1.write(fig1)

provincia_mayor = Base_general[['Provincia','Poblacion usuaria']]
provincia_mayorg = provincia_mayor.groupby(['Provincia'])[['Poblacion usuaria']].count().reset_index()
provincia_mayorg['Poblacion total'] = pd.Series([256981,118987,226898,67887,1484789,384789,115889,70589,390478,89578,103974,54785,335677,330587,420478,140784,201474,200454,135710,38941,298747,490733,168265,859741,82458,300476,418850,157457,1833451,164941,2995211,207447])
atencion_mayor =((provincia_mayorg['Poblacion usuaria']/provincia_mayorg['Poblacion total'])*100)
provincia_mayorg['Tasa de atendidos'] = atencion_mayor
provincia_mayorg = provincia_mayorg.sort_values(by = 'Tasa de atendidos', ascending = False)
fig1 = px.bar(provincia_mayorg.head(5), x="Provincia", y="Tasa de atendidos", color="Provincia", title="Proporcion de la publacion usuaria vs la poblacion total por provincia", barmode = 'stack', width = 600, height = 450)
c2.write(fig1)

#################
#¿Cual es el sistema de salud de replublica dominicana que mas especialidades atiende en cada región?

st.markdown("<h3 style = 'text-align:center;color:red;'>¿Cual es el sistema de salud que más especialidades atiende en cada región?</h3>", unsafe_allow_html=True)
especialidad = Base_general[['Sistema','Especialidad','Region']]
especialidad_sis = especialidad.groupby(['Sistema','Region'])[['Especialidad',]].count().reset_index()
fig = px.bar(especialidad_sis, x="Region", y="Especialidad", color="Sistema", title="Especialidades atendidas en cada sistema segun la especialidad región", barmode = 'group', width = 1200)
st.write(fig)

#############################

#¿Cual es el top 5 de las region que menos valor autoriza? ¿este cambia si se hace el analisis dependiendo del año?
st.markdown("<h3 style = 'text-align:center;color:red;'>Cual es el top 5 de las region que menos valor autoriza? ¿este cambia si se hace el analisis dependiendo del año?</h3>", unsafe_allow_html=True)

c1, c2 = st.columns((1,1/1.5))
#se arma una nueva tabla con los datos desde base general
valoraut = Base_general[['Region','Valor Autorizado (RD$)']]
valorautorizado = valoraut.groupby(['Region'])[['Valor Autorizado (RD$)']].sum().reset_index()
valorautorizado = valorautorizado.sort_values(by = 'Valor Autorizado (RD$)', ascending = True)
#Se aplica grafica de barras
fig = px.bar(valorautorizado, x="Region", y="Valor Autorizado (RD$)", color= "Region", title="Valor autorizado por region acumulado en todos los años", width = 600)
c1.write(fig)

#Analisis añadiendo el año
if c2.checkbox('Analisis agregando el año',True):
    valoraut2 = Base_general[['Region','Valor Autorizado (RD$)','Ano']]
    valorautorizado2 = valoraut2.groupby(['Region','Ano'])[['Valor Autorizado (RD$)']].sum().reset_index()
    valorautorizado2 = valorautorizado2.sort_values(by = 'Valor Autorizado (RD$)', ascending = True)
    c2.write(valorautorizado2.head(5))
    

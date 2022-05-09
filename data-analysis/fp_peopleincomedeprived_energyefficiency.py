# -*- coding: utf-8 -*-
"""
%PeopleIncomeDeprived >= 25% and energyEfficiency <= 80 %
by Phoebe Chen 05/2022 
"""

!pip install plotly

import json
import pandas as pd
import plotly.io as pio
import plotly.express as px



# GeoJSON data of Glasgow Region
with open("Glasgow.geojson", "r") as geojson_g:
  glasgow_areas = json.load(geojson_g)

glasgow_districts_map = {}
for feature in glasgow_areas["features"]:
    feature["area_name"] = feature["properties"]["description"]
    glasgow_districts_map[feature["properties"]["name"]] = feature["area_name"]


glasgow_districts_map_byname = {}
for feature in glasgow_areas["features"]:
  for i in feature["properties"]["description"].split(", "):
    glasgow_districts_map_byname[i] = feature["properties"]["name"]


# EPC 
with open('D_EPC_data_2020_Q1_extract_0721.csv') as epc2020q1, open('D_EPC_data_2020_Q2_extract_0721.csv') as epc2020q2, open('D_EPC_data_2020_Q3_extract_0721.csv') as epc2020q3, open('D_EPC_data_2020_Q4_extract_0721.csv') as epc2020q4, open('D_EPC_data_2021_Q1_extract_0721.csv') as epc2021q1, open('D_EPC_data_2021_Q2_extract_0721.csv') as epc2021q2:
  all_epc2020_q1_df =  pd.read_csv(epc2020q1, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q2_df =  pd.read_csv(epc2020q2, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q3_df =  pd.read_csv(epc2020q3, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q4_df =  pd.read_csv(epc2020q4, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2021_q1_df =  pd.read_csv(epc2021q1, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2021_q2_df =  pd.read_csv(epc2021q2, skiprows=1,encoding = "ISO-8859-1", engine='python')     

# SIMD MSOA dataset
with open("SIMD_MSOA_domestic_gas_elec_2020.xlsx", mode='rb') as simd_msoa:
  msoa2020_gas_df = pd.read_excel(simd_msoa, "MSOA GAS 2020") #MSOA_domestic_gas_2010-20.xlsx
  msoa2020_elec_df = pd.read_excel(simd_msoa, "MSOA ELEC 2020") #MSOA_domestic_elec_2010-20.xlsx 
  simd2020_df = pd.read_excel(simd_msoa, "SIMD 2020") #simd2020_withinds.csv


# get EPC 2020 Q1 dataframe
glasgow_epc2020_q1 = all_epc2020_q1_df.loc[all_epc2020_q1_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2020_q1["district_code"] = glasgow_epc2020_q1["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q1["district_name"] = glasgow_epc2020_q1["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q1["theyear"] = 2020
glasgow_epc2020_q1["theq"] = 'Q1'

# get EPC 2020 Q2 dataframe
glasgow_epc2020_q2 = all_epc2020_q2_df.loc[all_epc2020_q2_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2020_q2["district_code"] = glasgow_epc2020_q2["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q2["district_name"] = glasgow_epc2020_q2["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q2["theyear"] = 2020
glasgow_epc2020_q2["theq"] = 'Q2'

# get EPC 2020 Q3 dataframe
glasgow_epc2020_q3 = all_epc2020_q3_df.loc[all_epc2020_q3_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2020_q3["district_code"] = glasgow_epc2020_q3["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q3["district_name"] = glasgow_epc2020_q3["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q3["theyear"] = 2020
glasgow_epc2020_q3["theq"] = 'Q3'

# get EPC 2020 Q4 dataframe
glasgow_epc2020_q4 = all_epc2020_q4_df.loc[all_epc2020_q4_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2020_q4["district_code"] = glasgow_epc2020_q4["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q4["district_name"] = glasgow_epc2020_q4["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q4["theyear"] = 2020
glasgow_epc2020_q4["theq"] = 'Q4'


# get EPC 2021 Q1 dataframe
glasgow_epc2021_q1 = all_epc2021_q1_df.loc[all_epc2021_q1_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2021_q1["district_code"] = glasgow_epc2021_q1["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2021_q1["district_name"] = glasgow_epc2021_q1["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2021_q1["theyear"] = 2021
glasgow_epc2021_q1["theq"] = 'Q1'

# get EPC 2021 Q2 dataframe
glasgow_epc2021_q2 = all_epc2021_q2_df.loc[all_epc2021_q2_df['POSTCODE'].str[0:1] =='G', ['POSTCODE','LOCAL_AUTHORITY_LABEL','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','3_YR_ENERGY_COST_CURRENT']]
glasgow_epc2021_q2["district_code"] = glasgow_epc2021_q2["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2021_q2["district_name"] = glasgow_epc2021_q2["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2021_q2["theyear"] = 2021
glasgow_epc2021_q2["theq"] = 'Q2'


# Calculate average energy Efficiency
glasgow_epc_all = pd.concat([glasgow_epc2020_q1, glasgow_epc2020_q2,glasgow_epc2020_q3,glasgow_epc2020_q4, glasgow_epc2021_q1, glasgow_epc2021_q2], axis=0)
glasgow_epc_all_new = glasgow_epc_all.copy()
glasgow_epc_all_grouped= glasgow_epc_all.groupby('district_code')['CURRENT_ENERGY_EFFICIENCY'].mean()
glasgow_epc_all_grouped= glasgow_epc_all_grouped.reset_index()


# Calculate % of income deprived
glasgow_simd2020 = simd2020_df[simd2020_df['Council_area'] == 'Glasgow City']
glasgow_simd2020_copy = glasgow_simd2020.copy()
glasgow_simd2020_copy['postcode_district'] = glasgow_simd2020_copy['Intermediate_Zone'].apply(lambda x: glasgow_districts_map_byname[x])
glasgow_simd2020_byarea_sum = glasgow_simd2020_copy.groupby(by=['postcode_district'])[['Total_population','income_count']].sum()
glasgow_simd2020_byarea_sum = glasgow_simd2020_byarea_sum.reset_index()
glasgow_simd2020_byarea_sum['percent_income_deprived'] = glasgow_simd2020_byarea_sum['income_count'] / glasgow_simd2020_byarea_sum['Total_population'] * 100


# Merge average energe efficiency and % of income deprived datasets into one
glasgow_ee_incomedeprivated = glasgow_epc_all_grouped.merge(glasgow_simd2020_byarea_sum,how='left', left_on='district_code', right_on='postcode_district')
glasgow_ee_incomedeprivated["district_name"] = glasgow_ee_incomedeprivated["district_code"].apply(lambda x: glasgow_districts_map[x])

# Filter % % income deprived >=25% and average energy Efficiency <= 80%
filt = (glasgow_ee_incomedeprivated['CURRENT_ENERGY_EFFICIENCY'] <= 80) & (glasgow_ee_incomedeprivated['percent_income_deprived']>=25)
filtered_df = glasgow_ee_incomedeprivated.loc[(glasgow_ee_incomedeprivated['CURRENT_ENERGY_EFFICIENCY']<=80.000000) & (glasgow_ee_incomedeprivated['percent_income_deprived']>=25.000000),['district_code','CURRENT_ENERGY_EFFICIENCY','postcode_district','Total_population','income_count','percent_income_deprived','district_name']]



# Prepare for the data to show on Choropleth map
glasgow_areas_copy = glasgow_areas.copy()
target_states = filtered_df['district_code'].tolist()
glasgow_areas_copy['features'] = [f for f in glasgow_areas_copy['features'] if f['properties']['name'] in target_states]

# Function to create a Choropleth map: needed to update to pass in parameters in the future
def basemap():
  fig = px.choropleth_mapbox(
      filtered_df,
      locations="district_code",
      geojson=glasgow_areas_copy,
      color="percent_income_deprived",
      color_continuous_scale=[[0, 'rgb(250,218,94)'],[0.05, 'rgb(154,205,50)'],[0.1, 'rgb(255,140,0)'],[0.20, 'rgb(255,0,255)'],[1, 'rgb(138,43,226)']],
      hover_name="district_name",
      hover_data=["CURRENT_ENERGY_EFFICIENCY","percent_income_deprived", "Total_population","income_count"],
      featureidkey="properties.name",
      title="% Glasgow pop who are >=25% income deprived & <=80% Energy efficiency (2020-2021)",
      mapbox_style="carto-positron",
      center={"lat": 56, "lon": -4},
      zoom=8,
      opacity=0.9,
  )    
  fig.update_geos(fitbounds="locations",visible=True)
  fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
  return fig

# Show the map
basemap()




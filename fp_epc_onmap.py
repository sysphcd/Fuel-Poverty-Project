# -*- coding: utf-8 -*-
"""fp_EPC_onMap.ipynb

Glasgow Districts Median Energy Efficiency and Median Energy Consumption current (2020 Q1-Q4, 2021 Q1-Q2) on Plotly Choropleth Map
by Phoebe chen 05/2022
"""

!pip install plotly

import json
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.io as pio

import matplotlib.pyplot as plt
import seaborn as sns

# EPC data
with open('D_EPC_data_2020_Q1_extract_0721.csv') as epc2020q1, open('D_EPC_data_2020_Q2_extract_0721.csv') as epc2020q2, open('D_EPC_data_2020_Q3_extract_0721.csv') as epc2020q3, open('D_EPC_data_2020_Q4_extract_0721.csv') as epc2020q4, open('D_EPC_data_2021_Q1_extract_0721.csv') as epc2021q1, open('D_EPC_data_2021_Q2_extract_0721.csv') as epc2021q2:
  all_epc2020_q1_df =  pd.read_csv(epc2020q1, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q2_df =  pd.read_csv(epc2020q2, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q3_df =  pd.read_csv(epc2020q3, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2020_q4_df =  pd.read_csv(epc2020q4, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2021_q1_df =  pd.read_csv(epc2021q1, skiprows=1,encoding = "ISO-8859-1", engine='python') 
  all_epc2021_q2_df =  pd.read_csv(epc2021q2, skiprows=1,encoding = "ISO-8859-1", engine='python')


# Glasgow GeoJSON data
with open("Glasgow.geojson", "r") as geojson_g:  
  glasgow_areas = json.load(geojson_g)

glasgow_districts_map = {}
for feature in glasgow_areas["features"]:
    feature["area_name"] = feature["properties"]["description"]
    glasgow_districts_map[feature["properties"]["name"]] = feature["area_name"]


# EPC 2020 Q1
glasgow_epc2020_q1 = all_epc2020_q1_df.loc[all_epc2020_q1_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2020_q1["district_code"] = glasgow_epc2020_q1["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q1["district_name"] = glasgow_epc2020_q1["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q1["theyear"] = 2020
glasgow_epc2020_q1["theq"] = "Q1"

# EPC 2020 Q2
glasgow_epc2020_q2 = all_epc2020_q2_df.loc[all_epc2020_q2_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2020_q2["district_code"] = glasgow_epc2020_q2["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q2["district_name"] = glasgow_epc2020_q2["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q2["theyear"] = 2020
glasgow_epc2020_q2["theq"] = "Q2"
# EPC 2020 Q3
glasgow_epc2020_q3 = all_epc2020_q3_df.loc[all_epc2020_q3_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2020_q3["district_code"] = glasgow_epc2020_q3["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q3["district_name"] = glasgow_epc2020_q3["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q3["theyear"] = 2020
glasgow_epc2020_q3["theq"] = "Q3"
# EPC 2020 Q4
glasgow_epc2020_q4 = all_epc2020_q4_df.loc[all_epc2020_q4_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2020_q4["district_code"] = glasgow_epc2020_q4["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2020_q4["district_name"] = glasgow_epc2020_q4["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2020_q4["theyear"] = 2020
glasgow_epc2020_q4["theq"] = "Q4"

# EPC 2021 Q1
glasgow_epc2021_q1 = all_epc2021_q1_df.loc[all_epc2021_q1_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2021_q1["district_code"] = glasgow_epc2021_q1["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2021_q1["district_name"] = glasgow_epc2021_q1["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2021_q1["theyear"] = 2021
glasgow_epc2021_q1["theq"] = "Q1"
# EPC 2021 Q2
glasgow_epc2021_q2 = all_epc2021_q2_df.loc[all_epc2021_q2_df['POSTCODE'].str[0:1] =='G', ['POST_TOWN','POSTCODE','LOCAL_AUTHORITY_LABEL','INSPECTION_DATE','ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY',	'CURRENT_ENERGY_RATING','HEATING_COST_CURRENT','LIGHTING_COST_CURRENT','SPACE_HEATING_DEMAND','WATER_HEATING_DEMAND','BUILT_FORM',	'PROPERTY_TYPE']]
glasgow_epc2021_q2["district_code"] = glasgow_epc2021_q2["POSTCODE"].apply(lambda x: x.split(" ")[0])
glasgow_epc2021_q2["district_name"] = glasgow_epc2021_q2["district_code"].apply(lambda x: glasgow_districts_map[x])
glasgow_epc2021_q2["theyear"] = 2021
glasgow_epc2021_q2["theq"] = "Q2"

# Concatenate all epc dataframes
glasgow_epc_all = pd.concat([glasgow_epc2020_q1, glasgow_epc2020_q2,glasgow_epc2020_q3,glasgow_epc2020_q4, glasgow_epc2021_q1, glasgow_epc2021_q2], axis=0)

# Calculate the median of energy consumption and energy efficiency
glasgow_epc_all_median = glasgow_epc2020_q1.groupby(['district_code'])['ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY'].median()
groupedmedian_glasgow_epc_all = pd.DataFrame(glasgow_epc_all_median)
groupedmedian_glasgow_epc_all = groupedmedian_glasgow_epc_all.reset_index()
groupedmedian_glasgow_epc_all["district_name_median"] = groupedmedian_glasgow_epc_all["district_code"].apply(lambda x: glasgow_districts_map[x])
groupedmedian_glasgow_epc_all.rename(columns = {'ENERGY_CONSUMPTION_CURRENT':'median_ENERGY_CONSUMPTION_CURRENT', 'CURRENT_ENERGY_EFFICIENCY':'median_CURRENT_ENERGY_EFFICIENCY'}, inplace = True)

# Calculate the average of energy consumption and energy efficiency
glasgow_epc_all_mean = glasgow_epc2020_q1.groupby(['district_code'])['ENERGY_CONSUMPTION_CURRENT','CURRENT_ENERGY_EFFICIENCY'].mean()
groupedmean_glasgow_epc_all = pd.DataFrame(glasgow_epc_all_mean)
groupedmean_glasgow_epc_all = groupedmean_glasgow_epc_all.reset_index()
groupedmean_glasgow_epc_all["district_name_mean"] = groupedmean_glasgow_epc_all["district_code"].apply(lambda x: glasgow_districts_map[x])
groupedmean_glasgow_epc_all.rename(columns = {'ENERGY_CONSUMPTION_CURRENT':'mean_ENERGY_CONSUMPTION_CURRENT', 'CURRENT_ENERGY_EFFICIENCY':'mean_CURRENT_ENERGY_EFFICIENCY'}, inplace = True)

# Merge Median and Average energy consumption and energy efficiency dataframe
glasgow_allepc_meanmedian_merge = groupedmedian_glasgow_epc_all.merge(groupedmean_glasgow_epc_all,how='left', left_on='district_code', right_on='district_code')

# Create a Glasgow Districts Median Current Energy Efficiency (2020-2021) Plotly Choropleth Map with Plotly.express
fig = px.choropleth_mapbox(
    glasgow_allepc_meanmedian_merge,
    locations="district_code",
    geojson=glasgow_areas,
    color="median_CURRENT_ENERGY_EFFICIENCY",
    hover_name="district_name_median",
    hover_data=["median_ENERGY_CONSUMPTION_CURRENT","median_CURRENT_ENERGY_EFFICIENCY"],
    featureidkey="properties.name",
    title="Glasgow Districts Median current energy efficiency (2020 Q1-Q4, 2021 Q1-Q2)",
    mapbox_style="carto-positron",
    center={"lat": 56, "lon": -4},
    zoom=8,
    opacity=0.5,
) 
fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0},)
fig.show()

# Create a Glasgow Districts  Current Energy Consumption (2020-2021) Plotly Choropleth Map with Plotly.express
fig = px.choropleth_mapbox(
    glasgow_allepc_meanmedian_merge,
    locations="district_code",
    geojson=glasgow_areas,
    color="median_ENERGY_CONSUMPTION_CURRENT",
    hover_name="district_name_median",
    hover_data=["median_ENERGY_CONSUMPTION_CURRENT","median_CURRENT_ENERGY_EFFICIENCY"],
    featureidkey="properties.name",
    title="Glasgow Districts Median Energy Consumption current (2020 Q1-Q4, 2021 Q1-Q2)",
    mapbox_style="carto-positron",
    center={"lat": 56, "lon": -4},
    zoom=8,
    opacity=0.5,
) 
fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0},)
fig.show()
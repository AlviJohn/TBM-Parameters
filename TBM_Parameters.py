# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:33:42 2022

@author: alvi
"""
import streamlit as st
import numpy as np
import pandas as pd
from chart_studio import plotly as py
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from itertools import product
from datetime import datetime
from PIL import Image



#######Setting the Basics for the Page
st.set_page_config(page_title="TBM_Parameters", page_icon="muscleman.jpg", layout="wide", initial_sidebar_state="auto")
st.title('TBM Parameters')
TBM_parameter_dataset = pd.read_csv('TBMParameter_Analyticaldataset.csv',encoding="cp1252") 


def RFPP_only(x):
        if (x['Non_Uniformity_RFPP'] ==1): return 'Rejected Tyre'
        else: return 'Not Rejected Tyre'        
TBM_parameter_dataset['Rejection_RFPP_Only'] =TBM_parameter_dataset.apply(RFPP_only, axis=1)

def Imbalance_only(x):
        if (x['Non_Uniformity_Imbalance'] ==1): return 'Rejected Tyre'
        else: return 'Not Rejected Tyre'        
TBM_parameter_dataset['Rejection_Imbalance_Only'] =TBM_parameter_dataset.apply(Imbalance_only, axis=1)





TBM_parameter_dataset_1sttest = TBM_parameter_dataset.loc[TBM_parameter_dataset['timeperiod'].isin(['Test 1','Control 1']),:]
TBM_parameter_dataset_2ndtest = TBM_parameter_dataset.loc[TBM_parameter_dataset['timeperiod'].isin([ 'Test 2','Control 2']),:]




Variables = ['Belt1_length_deviation', 'Belt2_length_deviation',
       'TD_length_deviation', 'IL_length_deviation', 'PLY1_length_deviation',
       'PLY2_length_deviation', 'Belt1_width_deviation',
       'Belt2_width_deviation', 'TD_width_deviation', 'PLY_Width_deviation',
       '1BPR_CYCLE_MAT_AT_FRONT', '1BPR_CYCLE_TOTAL',
       '2BPR_CYCLE_MAT_AT_FRONT', '2BPR_CYCLE_TOTAL', 'BP1_TOTAL_SCRAP_CUTOUT',
       'BP2_TOTAL_SCRAP_CUTOUT', 'BPPR_BP1_CYCLE_REST', 'BPPR_BP2_CYCLE_REST',
       'BR1_LE_ANGLE_MEASURED', 'BR1_TE_ANGLE_MEASURED',
       'BR2_LE_ANGLE_MEASURED', 'BR2_TE_ANGLE_MEASURED', 'BR2_WIDTH_MEASURED',
       'BTPR_CYCLE_TIME_WAIT_CC', 'DR_SHAPE_PRESSURE_MAX',
       'DR_STITCH_TD_PRESSURE_MAX', 'DR_TURNUP_PRESSURE_MAX',
       'PR_CYCLE_TIME_1PAP', 'PR_CYCLE_TIME_PAAP', 'PR_CYCLE_TIME_STITCH_PA',
       'ISDS_AMOUNT_SPLICES_BP1', 'ISDS_AMOUNT_SPLICES_BP2',
       'PA_ANGLE_MEASURED', 'PA_WIDTH_MEASURED', 'PAPR_CYCLE_MAT_AT_FRONT',
       'PAPR_CYCLE_TOTAL', 'TDPR_CYCLE_MAT_AT_FRONT', 'TDPR_CYCLE_TOTAL']



option = st.selectbox(
     'Please Select the Variable',Variables)

metric_option = st.selectbox('Select the Metric',['RFPP Only', 'Imbalance only','Imbalance & RFPP'])

if metric_option=='RFPP Only':
    var1='Rejection_RFPP_Only'
elif metric_option=='Imbalance only':
    var1='Rejection_Imbalance_Only'
elif metric_option=='Imbalance & RFPP':
    var1='Rejection_RFPP_Imbalance'




##########Charts#########################
var = option
fig = px.violin(TBM_parameter_dataset_1sttest, y=var, x="timeperiod",color=var1 ,box=True)
fig.update_layout(title_text= str(var) +  " VS Rejection (Test-24Apr to 1May,Control-17Apr to 23Apr(7days))")
st.plotly_chart(fig,use_container_width=True)

fig = px.violin(TBM_parameter_dataset_2ndtest, y=var, x="timeperiod",color=var1 ,box=True)
fig.update_layout(title_text= str(var) + " VS Rejection (Test-30Mar to 1Apr,Control-25Mar to 29Mar(5days))")
st.plotly_chart(fig,use_container_width=True)

st.write(TBM_parameter_dataset_1sttest.groupby(['timeperiod',var1])['BARCODE'].count())
st.write(TBM_parameter_dataset_2ndtest.groupby(['timeperiod',var1])['BARCODE'].count())



















































#col1, col2 = st.sidebar.columns(2)
#with col1:
#    start_date = st.date_input('Start date', min_date)
#with col2:
#        end_date = st.date_input('End date', max_date)
#        
#if start_date > end_date:
#    st.error('Error: End date must fall after start date.')
#        
#RC_with_DR = RC_with_DR[(RC_with_DR['Createddate'] >= start_date) & (RC_with_DR['Createddate'] <= end_date)]
#
#
#
####Select Rim Sizes
#rim_choices = RC_with_DR['Rim_Size_new'].unique().tolist()
#rim_choices.insert(0,"ALL")
#rim_make_choice = st.sidebar.multiselect("Select one or more Rim Sizes:",rim_choices,'ALL')
#if "ALL" in rim_make_choice:
#    rim_make_choice_final = rim_choices
#else:
#    rim_make_choice_final = rim_make_choice
#
#RC_with_DR=RC_with_DR.loc[(RC_with_DR['Rim_Size_new'].isin(rim_make_choice_final))]
#####First Chart
#RC_with_DR = RC_with_DR.dropna()
#
#
#
####Select Aspect Ratio
#ar_choices = RC_with_DR['aspect_ratio'].unique().tolist()
#ar_choices.insert(0,"ALL")
#ar_make_choice = st.sidebar.multiselect("Select one or more Aspect Ratios:",ar_choices,'ALL')
#if "ALL" in ar_make_choice:
#    ar_make_choice_final = ar_choices
#else:
#    ar_make_choice_final = ar_make_choice
#RC_with_DR=RC_with_DR.loc[(RC_with_DR['aspect_ratio'].isin(ar_make_choice_final))]
#
#
####Select Capcompound
#cap_choices = RC_with_DR['CapCompound'].unique().tolist()
#cap_choices.insert(0,"ALL")
#cap_make_choice = st.sidebar.multiselect("Select one or more Cap Compounds:",cap_choices,'ALL')
#if "ALL" in cap_make_choice:
#    cap_make_choice_final = cap_choices
#else:
#    cap_make_choice_final = cap_make_choice
#
#
#RC_with_DR=RC_with_DR.loc[(RC_with_DR['CapCompound'].isin(cap_make_choice_final))]
#
#####Removing Duplicates
#RC_with_DR = RC_with_DR.dropna()
#st.write("After filtering",RC_with_DR.shape[0], " observations were filtered for the dashboard" )
#
#csv= RC_with_DR.to_csv().encode('utf-8')
#st.download_button(
#   "Click to Download Data",
#    csv,
#   "RRC Data.csv",
#   "text/csv",
#   key='download-csv'
#   )
#
#
#image = Image.open('muscle_man2.png')
#st.sidebar.image(image)
#
#
#
#
########################################################Charts
#####First Chart
#fig = go.Figure()
#
#fig = px.scatter(RC_with_DR, x="Createddate", y="CRR", color='CapCompound')
#st.plotly_chart(fig,use_container_width=True)
#






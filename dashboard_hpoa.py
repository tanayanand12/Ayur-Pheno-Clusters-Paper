# -*- coding: utf-8 -*-
"""Dashboard_HPOA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fxFPzKAqlPUcpNcgcTxA4QFh90sWrz_5
"""

# !pip install gradio

# import gradio as gr

import numpy
import pandas
import pickle

from collections import defaultdict

def pickle_load(file_path):
    with open(file_path, 'rb') as handle:
        b = pickle.load(handle)
    return b

# loading dicts
disease_hpo_dict = pickle_load('/content/drive/MyDrive/HPO Dataset/Dashboard/disease_hpo_dict.pickle')
disease_name_dict =  pickle_load('/content/drive/MyDrive/HPO Dataset/Dashboard/disease_name_dict.pickle')
hpid_descriptions_dict =  pickle_load('/content/drive/MyDrive/HPO Dataset/Dashboard/hpid_descriptions_dict.pickle')
hpid_vpk_label_dict =  pickle_load('/content/drive/MyDrive/HPO Dataset/Dashboard/hpid_vpk_label_dict.pickle')
hpo_disease_dict =  pickle_load('/content/drive/MyDrive/HPO Dataset/Dashboard/hpo_disease_dict.pickle')

def fetch_hpids(disease_id):
  temp_hpid_name_dict = defaultdict(list)
  hpid_list = disease_hpo_dict[disease_id]
  for i in hpid_list:
    # print(i, '\t', hpid_descriptions_dict[i], '\n')
    # print(hpid_descriptions_dict[i], '\n')
    temp_hpid_name_dict[i].append(hpid_descriptions_dict[i])
  # print(temp_hpid_name_dict)
  return temp_hpid_name_dict

#test
# type(fetch_hpids('OMIM:301040'))

def fetch_disease_name(disease_id):
  disease_name = disease_name_dict[disease_id]
  return disease_name

# test
# type(fetch_disease_name('OMIM:301040'))

def fetch_hpid_descriptions(hpid):
  hpid_description = hpid_descriptions_dict[hpid]
  return hpid_description

def fetch_hpid_vpk_label(hpid):
  hpid_vpk_label_list = hpid_vpk_label_dict[hpid]
  return hpid_vpk_label_list

# test
# type(fetch_hpid_vpk_label("HP:0004840"))

def fetch_corresp_diseases(hpid):
  disease_list = hpo_disease_dict[hpid]
  temp_disease_name_dict = defaultdict(list)
  for i in disease_list:
    temp_disease_name_dict[i].append(disease_name_dict[i])
  return temp_disease_name_dict

# test
# fetch_corresp_diseases("HP:0004840")

def disease_details(disease_id):
  a = disease_id
  hpid_list = fetch_hpids(a) # dict id to name mapping
  disease_name = fetch_disease_name(a)
  disease_vpk_count_list = []
  return hpid_list, disease_name, disease_vpk_count_list

def hpid_details(hpid):
  a = hpid
  disease_list = fetch_corresp_diseases(a) # dict disease id to name mapping
  hpid_description = fetch_hpid_descriptions(a)
  hpid_vpk_label = fetch_hpid_vpk_label(a)
  return disease_list, hpid_description, hpid_vpk_label

# # Define the dropdown options
# function_options = ["Disease Info", "Phenotype Info"]

# # Define the Gradio interface
# def dashboard(function, input_data):
#     if function == "Disease Info":
#         output1, output2, output3 = disease_details(input_data)
#     elif function == "Phenotype Info":
#         output1, output2, output3 = hpid_details(input_data)

#     return {"Output 1": output1, "Output 2": output2, "Output 3": output3}

# inputs = [
#     gr.inputs.Dropdown(function_options, label="Select a function:"),
#     gr.inputs.Textbox(label="Input data:")
# ]

# # outputs = ["json", "list", "list"]

# output1_component = gr.outputs.HTML(label="Output 1")
# output2_component = gr.outputs.Textbox(label="Output 2")
# output3_component = gr.outputs.Label(label="Output 3")

# iface = gr.Interface(fn=dashboard, inputs=inputs, outputs=[output1_component, output2_component, output3_component], title="HPOA Dashboard")
# iface.launch(share=True)

# !pip install streamlit

# %%streamlit

import streamlit as st

def main():
  # Define the dropdown options
  function_options = ["Disease Info", "Phenotype Info"]


  # Set page title
  st.set_page_config(page_title="Function Dashboard")

  # Create dashboard layout
  st.title("Function Dashboard")

  # User inputs
  selected_function = st.selectbox("Select a function:", function_options)
  input_data = st.number_input("Input data:")

  # Compute outputs based on selected function
  if selected_function == "Disease Info":
      output1, output2, output3 = disease_details(input_data)
  elif selected_function == "Phenotype Info":
      output1, output2, output3 = hpid_details(input_data)

  # if function == "Disease Info":
  #     output1, output2, output3 = disease_details(input_data)
  # elif function == "Phenotype Info":
  #     output1, output2, output3 = hpid_details(input_data)

  # Display outputs
  st.subheader("Output 1")
  st.write(output1)

  st.subheader("Output 2")
  st.write(output2)

  st.subheader("Output 3")
  st.write(output3)

if __name__ == '__main__':
    main()

# !pip install pyngrok

# from pyngrok import ngrok
# from streamlit import _is_running_with_streamlit

# # Check if running with Streamlit
# if _is_running_with_streamlit():
#     # Start ngrok tunnel
#     public_url = ngrok.connect(port='8501')
#     public_url


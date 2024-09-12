import pickle
import pandas as pd 
import numpy as np

def pickle_load(file_path):
    with open(file_path, 'rb') as handle:
        b = pickle.load(handle)
    return b

# loading dicts #tanay path
disease_hpo_dict = pickle_load('disease_hpo_dict_V_110923.pickle')
disease_name_dict =  pickle_load('disease_name_dict_V_110923.pickle')
hpid_descriptions_dict =  pickle_load('hpid_descriptions_dict_V_110923.pickle')
hpid_vpk_label_dict =  pickle_load('hpid_vpk_label_dict_V_110923.pickle')
hpo_disease_dict =  pickle_load('hpo_disease_dict_V_110923.pickle')
disease_vpk_count_dict = pickle_load('disease_vpk_count_dict_V_110923.pickle')

def retrive_diseases(phenotypes_df, hpo_disease_dict= hpo_disease_dict):
    main_disease_list = []
    res_hpid_column_list = []
    suspicious_pid_list = []

    count = 0
    for p_id in phenotypes_df['Phenotype_ID']:
        temp_disease_list  = hpo_disease_dict[p_id]
        if (temp_disease_list == []):
            suspicious_pid_list.append(p_id)  # Stroring pid's which ain't associated with any of the diseases
        # temp_hpid_list = np.full((len(temp_disease_list)), p_id)
        temp_hpid_list = []
        given_value= p_id
        temp_hpid_list.extend([given_value for i in range(len(temp_disease_list))])
        # print('len of disease list: ', len(temp_disease_list))
        # print("length of temp HPID LIST: ",len(temp_hpid_list))
        main_disease_list.append(temp_disease_list)
        res_hpid_column_list.append(temp_hpid_list)
        # print('length of res: ',len(res_hpid_column_list), "\n\n\n")
        # print(res_hpid_column_list)
        # if (count == 10):
        #     break
        
        # count += 1

    temp_disease_list.clear()
    temp_hpid_list.clear()

    main_disease_list = [i for row in main_disease_list for i in row]
    res_hpid_column = [i for row in res_hpid_column_list for i in row]
    # print(len(res_hpid_column))
    # main_disease_list = np.unique(main_disease_list)
    # len(main_disease_list)

    disease_name_list = []  # making disease name list
    for disease_id in main_disease_list:
        disease_name_list.append(disease_name_dict[disease_id])

    return_df = pd.DataFrame(columns=['Disease_ID', 'Disease_Name', 'HP_ID'])

    return_df['Disease_ID'] = main_disease_list
    return_df['Disease_Name'] = disease_name_list
    return_df['HP_ID'] = res_hpid_column

    return return_df


def retrive_phenotypes(disease_df, disease_hpo_dict = hpo_disease_dict):
    main_phenotype_list = []
    res_disease_id_column_list = []
    suspicious_disease_id_list = []

    for did in disease_df['Disease_ID']:
        temp_phenotype_list = disease_hpo_dict[did]

        if (temp_phenotype_list == []):
            suspicious_disease_id_list.append(did)

        temp_disease_id_list = []
        given_value = did
        temp_disease_id_list.extend([given_value for i in range(len(temp_phenotype_list))])

        main_phenotype_list.append(temp_phenotype_list)
        res_disease_id_column_list.append(temp_disease_id_list)

    temp_phenotype_list.clear()
    temp_disease_id_list.clear()

    main_phenotype_list = [i for row in maim_disaese_list for i in row]
    res_disease_id_column = [i for row in res_disease_id_column_list for i in row]

    phenotype_name_list = []
    for phenotype_id in main_phenotype_list:
        phenotype_name_list.append(hpid_descriptions_dict[phenotype_id])

    retrun_df = pd.DataFrame(columns=['Phenotype_ID', 'Phenotype_Name', 'Disease_ID'])

    retrun_df['Phenotype_ID'] = main_phenotype_list
    return_df['Phenotype_Name'] = phenotype_name_list
    return_df['Disease_ID'] = res_disease_id_column

    return return_df


def find_list_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    difference = list(set1.symmetric_difference(set2))

    return difference

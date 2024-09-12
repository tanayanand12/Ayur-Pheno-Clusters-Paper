import pandas as pd 
import numpy as np 

def count_vpk_proportions(vpk_label_df, disease_df, disease_hpo_dict, disease_name_dict):
    final_concencous_hpo_vpk_label_df = vpk_label_df
    disease_name_dict = disease_name_dict
    
    try:    # dropping description column
        final_concencous_hpo_vpk_label_df = final_concencous_hpo_vpk_label_df.drop(['Description'], axis=1)
    except Exception as e:
        print('Exception Occured')
        print(e)
    # df

    # print('item type: ', type(final_concencous_hpo_vpk_label_df.iloc[2, 4]))

    # encodeing v, p and k into 0 & 1
    for i in range(0, len(final_concencous_hpo_vpk_label_df)):
        if((final_concencous_hpo_vpk_label_df.iloc[i, 1] == 'V') | (final_concencous_hpo_vpk_label_df.iloc[i, 1] == 'v')):
            final_concencous_hpo_vpk_label_df.iloc[i, 1] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 1] = int(0)

        if((final_concencous_hpo_vpk_label_df.iloc[i, 2] == 'P') | (final_concencous_hpo_vpk_label_df.iloc[i, 2] == 'p')):
            final_concencous_hpo_vpk_label_df.iloc[i, 2] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 2] = int(0)

        if((final_concencous_hpo_vpk_label_df.iloc[i, 3] == 'K') | (final_concencous_hpo_vpk_label_df.iloc[i, 3] == 'k')):
            final_concencous_hpo_vpk_label_df.iloc[i, 3] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 3] = int(0)

        if((final_concencous_hpo_vpk_label_df.iloc[i, 4] == 'NV') | (final_concencous_hpo_vpk_label_df.iloc[i, 4] != 0)):
            final_concencous_hpo_vpk_label_df.iloc[i, 4] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 4] = int(0)

        if((final_concencous_hpo_vpk_label_df.iloc[i, 5] == 'NP') | (final_concencous_hpo_vpk_label_df.iloc[i, 5] != 0)):
            final_concencous_hpo_vpk_label_df.iloc[i, 5] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 5] = int(0)

        if((final_concencous_hpo_vpk_label_df.iloc[i, 6] == 'NK') | (final_concencous_hpo_vpk_label_df.iloc[i, 6] != 0)):
            final_concencous_hpo_vpk_label_df.iloc[i, 6] = int(1)
        else:
            final_concencous_hpo_vpk_label_df.iloc[i, 6] = int(0)

    # print(final_concencous_hpo_vpk_label_df.head(30))

    term_df = final_concencous_hpo_vpk_label_df.iloc[:,1]
    term_df.drop_duplicates()
    # term_df

    disease_vpk_count_df = pd.DataFrame(columns = ['disease_id', 'disease_name', 'v_count', 'p_count', 'k_count', 'nv_count', 'np_count', 'nk_count'])
    disease_vpk_count_df

    temp_vpk_list = []

    disease_count = 0
    no_success_count = 0

    main_list = []

    for x in disease_df: # for vpk counting
        # print('x: ', x)
        try:
            v_count = 0
            p_count = 0
            k_count = 0
            nv_count = 0
            np_count = 0
            nk_count = 0
            val_list = disease_hpo_dict[x]
            empty_disease_list = []
            if(val_list == []):
                empty_disease_list.append(x)
            # print(val_list)
            for y in val_list:
                if (y == 'HP:0004495'):
                    continue
                # print(df[df['Term']== y].index.values)
                # print(y)


                # if not df[df['Term']== y].index.values:# print('for H# _ID\t', y, '\thandling NAN values from the list')
                #     continue

                index_number = final_concencous_hpo_vpk_label_df[final_concencous_hpo_vpk_label_df['HP_Terms']== y].index.values[0]
                # print('index_number= ', index_number)
                # print(df.iloc[index_number, :])

                # try:
                # only considering v, p and k columns for the calculation.
                
                v_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 1]
                # print(type(v_count))
                # print(v_count)
                # print('length of v count: ', len(v_count))
                # print('v: ', final_concencous_hpo_vpk_label_df.iloc[index_number, 1])
                # print('\tv count: ', v_count, '\n')
                p_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 2]
                # print(type(p_count))
                # print('p: ', final_concencous_hpo_vpk_label_df.iloc[index_number, 2])
                # print('\tp count: ', v_count, '\n')
                k_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 3]
                # print(type(k_count))
                # print('k: ', final_concencous_hpo_vpk_label_df.iloc[index_number, 3])
                # print('\tk count: ', v_count, '\n\n\n')
                nv_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 4]
                # print("NV value: ", final_concencous_hpo_vpk_label_df.iloc[index_number, 4])
                # print("NV count: ", nv_count)
                np_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 5]
                # print("NP value: ", final_concencous_hpo_vpk_label_df.iloc[index_number, 5])
                # print("NP count", np_count)
                nk_count += final_concencous_hpo_vpk_label_df.iloc[index_number, 6]
                # print("NP value: ", final_concencous_hpo_vpk_label_df.iloc[index_number, 6])
                # print("NK count: ", nk_count)
                


        except Exception as e :
            print(final_concencous_hpo_vpk_label_df.iloc[index_number,:])
            print("Error:",e,"occured")
            print(y)
            break


        temp_vpk_list.append(x)
        temp_disease_description = disease_name_dict[x]
        temp_vpk_list.append(temp_disease_description)
        temp_vpk_list.append(v_count)
        # print('v count ', v_count)
        temp_vpk_list.append(p_count)
        # print('p count ', p_count)
        temp_vpk_list.append(k_count)
        # print('k count ', k_count)
        temp_vpk_list.append(nv_count)
        temp_vpk_list.append(np_count)
        temp_vpk_list.append(nk_count)
        # print('loaded', temp_vpk_list)
        # print('shape of temp vpk list at present index', len(temp_vpk_list))

        # append to disease_vpk df and/or array
        disease_vpk_count_df.loc[len(disease_vpk_count_df)] = temp_vpk_list

        temp_vpk_list.clear()
        # print('clear', temp_vpk_list)


        disease_count += 1

        # except Exception as e :
        #     no_success_count += 1
        #     # continue
        #     print(y, "\t", e)
        # break
    
    return disease_vpk_count_df, disease_count, empty_disease_list


uname= "6209254"
pwd="6209254"

project_id="ENQ-23-09-01-00"
# DEND_Crn_Petal_type_Params_incld_allwnc={

#     "N":"XX",
#     "PETLWT1":"XXXXX",
#     "PETEL_MATERIAL":"XXXXXX",
#     "SURFACE_AREA":"XXXXXX"
# }


CRN_AND_PETEL_OP_PARMS_WITH_ALLWNC={
    "N":00,
    "A":00,
    "B":00,
    "TL":00,
    "SL":00,
    "PETELAREA":00,
    "PETELWT":00,
    "MATERIAL":"XXX"
}

master_mat_list=['SA516Gr.60','SA516Gr.60(N)','SA516GR.60(NACE)','SA516Gr.60(NACE+HIC)','SA516Gr.60(NACE)+CLAD','SA516Gr.70',
                'SA105','SA105(NACE)','SA105(CLAD)','SA106Gr.B','SA106Gr.B(NACE)','SA106Gr.B(CLAD)','SA234Gr.WPB',
                'SA234Gr.WPB+CLAD','SA240TP304L','IS2062Gr.B']
Inner_plate_mat_list=['SA516Gr.60','SA516Gr.60(N)','SA516GR.60(NACE)','SA516Gr.60(NACE+HIC)','SA516Gr.60(NACE)+CLAD','SA516Gr.70',
                      'SA105','SA105(NACE)','SA105(CLAD)','SA106Gr.B','SA106Gr.B(NACE)','SA106Gr.B(CLAD)','SA234Gr.WPB',
                      'SA234Gr.WPB+CLAD','SA240TP304L','IS2062Gr.B']

NPS_list=[3,6,10,15,20,25,40,50,65,80,90,100,125,150,200,250,300,350,400,450,500,550,600]
Schedule_list=[5, 10, 20, 30, 40, 60, 80, 100, 120, 140, 160, 'Std.', 'Ext. Strong', 'Dbl. Ext Strong']
avl_plate_width_for_DEND=list(map(str,[x for x in range(2500,13500,500)]))


#Will Save Estimation and Surface Area in a List
Estimation_Schema={
    "item":"XXXX",    
    "Wt":"00",
    "Material":"XXXX"
}
Estimation_Dict={
    "Desc_of_the_Item":Estimation_Schema,
}

Surface_Area_Schema={
    "Item_desc":"XXX",
    "Surface_Area":"00"
}
Surface_Area_List=[]






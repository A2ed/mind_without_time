"""dictionary to contain the columns of interest for the models.
These have been broken down into different data types.
"""

columns_to_rename = {### these data are volumetric estimates from the UCSF
                     ### longitudinal dataset
                     # Left hippocampus
                     'ST29SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_hippocampus_l',
                     # right hippocampus
                     'ST88SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_hippocampus_r',
                     # Intracranial volume ICV
                     'ST10CV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_icv',
                     # Left entorhinal cortex volume
                     'ST24CV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_entorhinal_l',
                     # Left entorhinal cortex thickness
                     'ST24TA_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_entorhinal_l_thick',
                     # Right entorhinal cortex volume
                     'ST83CV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_entorhinal_r',
                     # Right entorhinal cortex thickness
                     'ST83TA_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_entorhinal_r_thick',
                     # Third ventricle
                     'ST127SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_third_ventricle',
                     # Left inferior lateral ventricle
                     'ST30SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_il_ventricle_l',
                     # Left lateral ventricle
                     'ST37SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_l_ventricle_l',
                     # Right inferior lateral ventricle
                     'ST89SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_il_ventricle_r',
                     # Fifth ventricle
                     'ST8SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_fifth_ventricle',
                     # Right lateral ventricle
                     'ST96SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_l_ventricle_r',
                     # fourth ventricle
                     'ST9SV_UCSFFSL_02_01_16_UCSFFSL51ALL_08_01_16' : 'l_fourth_ventricle',
                     ### These are from the cross sectional UCSF dataset
                     # Left hippocampus
                     'ST29SV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_hippocampus_l',
                     # Right hippocampus
                     'ST88SV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_hippocampus_r',
                     # Left entorhinal cortex volume
                     'ST24CV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_entorhinal_l',
                     # Left entorhinal cortex thickness
                     'ST24TA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_entorhinal_l_thick',
                     # Right entorhinal cortex volume
                     'ST83CV_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_entorhinal_r',
                     # Right entorhinal cortex thickness
                     'ST83TA_UCSFFSX_11_02_15_UCSFFSX51_08_01_16' : 'x_entorhinal_r_thick',
                     ### These are from PET
                     # Hippocampus FDG measure
                     'FNEHC2_BAIPETNMRC_09_12_16' : 'fdg_hippocampus',
                     # Left hippocampus AV45
                     'LEFT_HIPPOCAMPUS_UCBERKELEYAV45_10_17_16' : 'av45_hippocampus_l',
                     # Right hippocampus AV45
                     'RIGHT_HIPPOCAMPUS_UCBERKELEYAV45_10_17_16' : 'av45_hippocampus_r',
                     # Left entorhinal cortex AV45
                     'CTX_LH_ENTORHINAL_UCBERKELEYAV45_10_17_16' : 'av45_entorhinal_l',
                     # Right entorhinal cortex AV45
                     'CTX_RH_ENTORHINAL_UCBERKELEYAV45_10_17_16' : 'av45_entorhinal_r',
                     # Left hippocampus AV1451
                     'LEFT_HIPPOCAMPUS_UCBERKELEYAV1451_10_17_16' : 'av1451_hippocampus_l',
                     # Right hippocampus AV1451
                     'RIGHT_HIPPOCAMPUS_UCBERKELEYAV1451_10_17_16' : 'av1451_hippocampus_r',
                     # Left entorhinal cortex AV1451
                     'CTX_LH_ENTORHINAL_UCBERKELEYAV1451_10_17_16' : 'av1451_entorhinal_l',
                     # Right entorhinal cortex AV1451
                     'CTX_RH_ENTORHINAL_UCBERKELEYAV1451_10_17_16' : 'av1451_entorhinal_r',
                     ### These are from DTI
                     # Left hippocampus fractional anisotropy
                     'FA_CGH_L_DTIROI_04_30_14' : 'fa_hippocampus_l',
                     # Right hippocampus fractional anisotropy
                     'FA_CGH_R_DTIROI_04_30_14' : 'fa_hippocampus_r',
                     # Left hippocampus mean diffusivity
                     'MD_CGH_L_DTIROI_04_30_14' : 'md_hippocampus_l',
                     # Right hippocampus mean diffusivity
                     'MD_CGH_R_DTIROI_04_30_14' : 'md_hippocampus_r'
}

metadata = {'demographic':
                          # Participant roster ID
                          ['RID',
                          # Visit code where bl is baseline
                          'VISCODE',
                          # Dataset that the record belongs to
                          'D1',
                          'D2',
                          # Baseline diagnosis
                          'DX_bl',
                          # Diagnosis change coded as
                          # 1=Stable:NL to NL, 2=Stable:MCI to MCI, 3=Stable:AD to AD,
                          # 4=Conv:NL to MCI, 5=Conv:MCI to AD, 6=Conv:NL to AD,
                          # 7=Rev:MCI to NL, 8=Rev:AD to MCI, 9=Rev:AD to NL,
                          # -1=Not available
                          'DXCHANGE',
                          # Age at baseline
                          'AGE',
                          # Gender
                          'PTGENDER',
                          # Education
                          'PTEDUCAT',
                          # Ethnicity
                          'PTETHCAT',
                          # Marital status at baseline
                          'PTMARRY'],
            'cognitive_tests':
                          # Clinical Dementia Rating Scale Sum of Boxes Scores
                          ### NOTE that bl denotes baseline assessment and != bl
                          ### denotes visit measurement
                          ['CDRSB_bl',
                          'CDRSB',
                          # Alzheimer's Disease Assessment Scale 13
                          'ADAS13_bl',
                          'ADAS13',
                          # Mini mental state examination
                          'MMSE_bl',
                          'MMSE',
                          # Montreal cognitive assessment
                          'MOCA_bl',
                          'MOCA'],
            'ECog':
                          # Ecog measurement memory
                          ['EcogPtMem_bl',
                          'EcogPtMem',
                          # Ecog measurement visual spatial
                          'EcogPtVisspat_bl',
                          'EcogPtVisspat'],
            'MRI':
                          # Hippocampus longitudinal
                          ['l_hippocampus_l',
                          'l_hippocampus_r',
                          # Hippocampus cross sectional
                          'x_hippocampus_l',
                          'x_hippocampus_r',
                          # Entorhinal cortex volume longitudinal
                          'l_entorhinal_l',
                          'l_entorhinal_r',
                          # Entorhinal cortex thickness longitudinal
                          'l_entorhinal_l_thick',
                          'l_entorhinal_r_thick',
                          # Entorhinal cortex volume cross sectional
                          'x_entorhinal_l',
                          'x_entorhinal_r',
                          # Entorhinal cortex thickness longitudinal
                          'x_entorhinal_l_thick',
                          'x_entorhinal_r_thick'],
            'fMRI':
                          # anterior DMN
                          ['ADMNRV',
                          # posterior DMN
                          'PDMNRV',
                          # anterior vs posterior DMN ratio
                          'DMNRVR'],
            'PET':
                          # Average FDG from angular, temporal, and posterior cingulate
                          ['FDG',
                          # FDG baseline
                          'FDG_bl',
                          # Hippocampus FDG
                          'fdg_hippocampus',
                          # Average PIB from frontal cortex, anterior cingulate, precuneus cortex, and parietal cortex
                          'PIB',
                          # Baseline PIB
                          'PIB_bl',
                          # Average AV45 from frontal, anterior cingulate, precuneus, and parietal cortex relative to the cer
                          'AV45',
                          'AV45_bl',
                          # Left hippocampus AV45
                          'av45_hippocampus_l',
                          # Right hippocampus AV45
                          'av45_hippocampus_r',
                          # Left entorhinal cortex AV45
                          'av45_entorhinal_l',
                          # Right entorhinal cortex AV45
                          'av45_entorhinal_r',
                          # Left hippocampus AV1451
                          'av1451_hippocampus_l',
                          # Right hippocampus AV1451
                          'av1451_hippocampus_r',
                          # Left entorhinal cortex AV1451
                          'av1451_entorhinal_l',
                          # Right entorhinal cortex AV1451
                          'av1451_entorhinal_r'],
            'DTI':
                         # Left hippocampus fractional anisotropy
                         ['fa_hippocampus_l',
                         # Right hippocampus fractional anisotropy
                         'fa_hippocampus_r',
                         # Left hippocampus mean diffusivity
                         'md_hippocampus_l',
                         # Right hippocampus mean diffusivity
                         'md_hippocampus_r'],
            'Genetic':
                         # APOE E4
                         ['APOE4']
                          }

dx_change_ids = {1 : 'Stable:NL to NL',
                 2 : 'Stable:MCI to MCI',
                 3 : 'Stable:AD to AD',
                 4 : 'Conv:NL to MCI',
                 5 : 'Conv:MCI to AD',
                 6 : 'Conv:NL to AD',
                 7 : 'Rev:MCI to NL',
                 8 : 'Rev:AD to MCI',
                 9 : 'Rev:AD to NL', 
                 -1 : 'Not available'
                 }

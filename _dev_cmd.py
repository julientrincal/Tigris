# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import argparse

from Tigris import command

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# command(['--convert', 'Porflow', r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Porflow/Porflow_Simple/ITER_CSA_OG_AlvExp_Ref3.inp", '-name', "test_cmd"])
command(['convert', 'Min3P', r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/Benchmark_SergioBea_dtmax2000s/atm_carbon_dtdiv100.dat", '-name', "test_cmd"])
# command(['convert', 'Hytec', r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Hytec/Carb_bench_cas2_473mag5FVaqueous_SA_TM_6", '-name', "test_cmd"])
# command(['convert', 'Crunch', r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Crunch/Problem-eauCO2-UNIX-REFERENCE/eauCO2.in", '-name', "test_cmd"])

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





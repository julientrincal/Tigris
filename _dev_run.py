# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
#------------------------------------------------------------------------------
from PyQt5.QtWidgets import QApplication
#------------------------------------------------------------------------------
from Tigris import Tigris
from Graph import Graph_Config
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#---- TEST
#==============================================================================
def add_graph(prog, gtype, dimensions) :
    gc = Graph_Config(gtype, dimensions)
    page = prog.pages_manager.add_page(gc=gc)
    return page.graphs[0]
    
#==============================================================================
def test_porflow(prog) :
    #--------------------------------------------------------------------------
    nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Porflow/Porflow_Simple/ITER_CSA_OG_AlvExp_Ref3.nc"
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Porflow/Porflow_Complexe/test.nc"
    
    #--------------------------------------------------------------------------
    calcul = prog.files_manager.load_file(nc_path)
    
    #--------------------------------------------------------------------------
    # graph = add_graph(prog, '1D', ['X'])
    # graph = add_graph(prog, '1D', ['T'])
    # graph = add_graph(prog, '2D', ['X','Y'])
    graph = add_graph(prog, '2D', ['X','T'])
    # graph = add_graph(prog, '3D', ['X','Y','Z'])
    
    #--------------------------------------------------------------------------
    # graph.add_element(file=calcul, path=['2-ZONES', 'Primaire','DOMAINE'])
    # graph.add_element(file=calcul, path=['2-ZONES', 'Primaire','SABLES'])
    # graph.add_element(file=calcul, path=['2-ZONES', 'Secondaire','COLIS'])
    # graph.add_element(file=calcul, path=['2-ZONES', 'Secondaire','C1PG'])
    # graph.add_element(file=calcul, path=['2-ZONES', 'Finale'])
    graph.add_element(file=calcul, path=['4-RESULTS', 'SAVE', 'ITER_CSA_OG_AlvExp_Hydrau.sav', 'P'])
    
    # graph.save_image()
    
#==============================================================================
def test_min3p(prog) :
    #--------------------------------------------------------------------------
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/CERIB_NonReactif_ParamHR62opt/test.nc"
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/CERIB_NonReactif_ParamHR62opt_Phases12_1/test.nc"
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Porflow/Porflow_Complexe/test.nc"
    
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/Test_MQ_a2b4.2_Ref/test.nc"
    
    # nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/Test_MQ_a2b4.2_Ref/test.nc"
    
    
    
    nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/MIN3P/Benchmark_SergioBea_dtmax2000s/test.nc"
    
    #--------------------------------------------------------------------------
    calcul = prog.files_manager.load_file(nc_path)
    
    #--------------------------------------------------------------------------
    # graph = add_graph(prog, '1D', ['X'])
    # graph = add_graph(prog, '1D', ['T'])
    # graph = add_graph(prog, '2D', ['X','T'])
    # graph = add_graph(prog, '3D', ['X','Y','Z'])
    
    #--------------------------------------------------------------------------
    # graph.add_element(file=calcul, path=['4-RESULTS', 'gsp'], field='s_a')
    # graph.add_element(file=calcul, path=['4-RESULTS', 'gsp'], field='s_a')
    # graph.add_element(file=calcul, path=['4-RESULTS', 'gsp'], field='s_g')
    # graph.add_element(file=calcul, path=['4-RESULTS', 'vel'], field='vx')
    
#==============================================================================
def test_crunch(prog) :
    #--------------------------------------------------------------------------
    nc_path = r"C:/Users/jt250258/Documents/Developpement/Python/TIGRIS/_Calculs/Crunch/CB_son68_ep-tous-poles-ssespsec-ssphasesec-1m3-SV7636-surf_const-verif-v2020\test.nc"
    calcul = prog.files_manager.load_file(nc_path)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~q
#---- PROGRAMME
#==============================================================================
if __name__ == '__main__' :
    #--------------------------------------------------------------------------
    app = QApplication(sys.argv)
    
    #--------------------------------------------------------------------------
    prog = Tigris(mode='dev')
    # prog = Tigris()
    
    prog.show()
    
    # test_porflow(prog)
    # test_min3p(prog)
    test_crunch(prog)
    
    app.exec_()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


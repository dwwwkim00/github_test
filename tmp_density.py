from pymatgen import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.io.vasp import Poscar
from pymatgen.io.vasp.outputs import BSVasprun
from pymatgen.io.vasp import inputs
from pymatgen.analysis.elasticity.strain import DeformedStructureSet, Strain
from pymatgen.analysis.elasticity.stress import Stress
from pymatgen.analysis.elasticity.elastic import ElasticTensor
from pymatgen.core.tensors import symmetry_reduce, Tensor
from numpy import arange, array
import os
import time


# yeonghun

print("Start")
start = time.time()

currentPath = os.getcwd()
print(currentPath)

# Retrieve the relaxed structure
# currentPath = 'E:/2_ETRI_coworks/1_LiCMC/1_model/2_LiCMC/4_multi_slab_from_NaCMC/1_same_direction/1_relax_isif_3'
# currentPath = 'E:/2_ETRI_coworks/1_LiCMC/1_model/2_LiCMC/4_multi_slab_from_NaCMC/1_same_direction/1_relax_isif_3/ivdw_10'
# currentPath = 'E:/2_ETRI_coworks/1_LiCMC/1_model/2_LiCMC/4_multi_slab_from_NaCMC/1_same_direction/1_relax_isif_3/ivdw_11'
# currentPath = 'E:/2_ETRI_coworks/1_LiCMC/1_model/3_NaCMC/2_multi_slab_from_one_slab_from_LiCMC/1_same_direction/2_relax_isif_3/ivdw_10'
currentPath = 'E:/2_ETRI_coworks/1_LiCMC/1_model/3_NaCMC/2_multi_slab_from_one_slab_from_LiCMC/1_same_direction/2_relax_isif_3/ivdw_11'
# structure = Poscar.from_file(currentPath + '/POSCAR')

vasprun = BSVasprun(currentPath + '/vasprun.xml')

print("Bulk density")
# print(structure.structure.density)
print(vasprun.final_structure.density)

print("time :", time.time() - start)
print("end")

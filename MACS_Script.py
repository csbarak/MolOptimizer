import os

PATH_OF_SCRIPT = r"D:\Samuel\WebServer\UPLOADS_ALIGN"
os.chdir(PATH_OF_SCRIPT)
def make_it_run(ref_file, lig_db):
    import sys
    from rdkit import Chem
    from rdkit.Chem import AllChem
    from rdkit.Chem import rdFMCS
    from rdkit.Chem.rdMolAlign import AlignMol
    #from rdkit.Chem.rdMolTransforms import GetDihedralDeg, SetDihedralDeg


    """Script taking a single reference molecule and a set of ligands 
       The MCS between each molecule and the reference is identified and if more than x% of the reference molecule match 
       then the common atom ids of the set of ligands are written to the output SDF.
       If no MCS is found ligands are written into another output file. 
       Both output SD files can be easily used for constrained or free docking with rdock.
    
       If you want you can adapt the code very easily also to do tethered minimization of 3D molecules. 
    """




    ratioThreshold=0.5 	#minimum portion of the reference molecule that should be found as common substructure to consider it for tethered minimization: 0.0-1.0

    reference = Chem.MolFromMolFile(ref_file, removeHs=True)
    ligands = Chem.SDMolSupplier(lig_db,removeHs=True)

    w=Chem.SDWriter("aligned.sdf")	#output ligands with constrained atoms
    wnt=Chem.SDWriter("output_nontethered.sdf")	#output of ligands without constraints (no MCS with reference ligand)

    for mol in ligands:
        if mol == None:
            continue
        else:
            print(mol)
            mols=[reference,mol]
            mcsResult=rdFMCS.FindMCS(mols,threshold=0.1,completeRingsOnly=False)    #find the maximum common substructure

            if mcsResult.smartsString and len(mcsResult.smartsString)>0 :
                patt = Chem.MolFromSmarts(mcsResult.smartsString,mergeHs=True)
                #keep only the core of the reference molecule
                ref=AllChem.ReplaceSidechains(reference,patt)
                if ref:
                    core=AllChem.DeleteSubstructs(ref,Chem.MolFromSmiles('*'))
                    core.UpdatePropertyCache()
                    newmol=Chem.Mol(mol)    #create a new instance of the ligand, as we will change the coordinates
                    try:
                        AllChem.ConstrainedEmbed(newmol,core)    #constrained minimization of newmol versus the core of the referenc
                        tethered_atom_ids=newmol.GetSubstructMatches(patt)    #that's to get the atom ids only
                        t=tethered_atom_ids[0]
                        t1=map(lambda x:x+1, list(t))
                        ta=','.join(str(el) for el in t1)
                        nm=Chem.AddHs(newmol, addCoords=True)    #create a new 3D molecule  and add the TETHERED ATOMS property
                        nm.SetProp('TETHERED ATOMS',ta)
                        w.write(nm)
                    except ValueError as ve:
                        print(ve)
                        pass
                        #write to an sd file
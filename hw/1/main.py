from rdkit import Chem


def substructure_search(molecule_list, substructure_smiles):
    found_substructure = Chem.MolFromSmiles(substructure_smiles)
    matching_molecules = []

    for smiles in molecule_list:
        molecule = Chem.MolFromSmiles(smiles)
        if molecule.HasSubstructMatch(found_substructure):
            matching_molecules.append(smiles)

    return matching_molecules


if __name__ == "__main__":
    smiles_list = ["CCO", "c1ccccc1", "CC(=O)O", "CC(=O)Oc1ccccc1C(=O)O"]
    substructure = "c1ccccc1"
    result = substructure_search(smiles_list, substructure)
    print(result)

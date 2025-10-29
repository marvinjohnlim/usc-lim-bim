import ifcopenshell
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")

#3 
print("IFC file loaded:", ifc_file.schema)

#4 
project = ifc_file.by_type("IfcProject")[0] 
project_name = project.Name or "Unnamed Project"
print(f"Project: {project_name}")

#5
stairs = ifc_file.by_type("IFCStair")
print(f"Number of stairs: {len(stairs)}")
for stair in stairs:
	print(stair.GlobalId, stair.Name)   

#6
slabs = ifc_file.by_type("IFCSlab")
print(f"Number of slabs: {len(slabs)}")
for slab in slabs:
	print(slab.GlobalId, slab.Name)   

#7
slabs = ifc_file.by_type("IfcSlab")
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated slab: {slab.GlobalId} → {slab.Name}")

#8
for site in project.IsDecomposedBy[0].RelatedObjects:
	for building in site.IsDecomposedBy[0].RelatedObjects:
		for storey in building.IsDecomposedBy[0].RelatedObjects:
			print("Storey", storey.Name, "Elevation", storey.Elevation)

#9
types = set(el.is_a() for el in ifc_file) 
print("Object types in file:", types)

#10

ifc_file.write("AC20-FZK-Haus_renamed.ifc")

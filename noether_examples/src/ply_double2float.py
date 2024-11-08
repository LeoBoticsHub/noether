from plyfile import PlyData

data = PlyData.read('noether/noether_examples/data/raw_mesh.ply')

new_types = {
    'x': 'double',
    'y': 'double',
    'z': 'double',
}

for prop in data['vertex'].properties:
    if prop.name in new_types:
        prop.val_dtype = new_types[prop.name]


print(data['vertex'].data)
print(data['vertex'].data.dtype)

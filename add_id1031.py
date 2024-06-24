#Add id
#id 추가하기

_ID_FIELD = 'grid_id'
name = 'grid_id'
type = QVariant.Int

# Add new FIELD
def create_new_field(name,type):
    layer = iface.activeLayer()
    ##<<  Create new field and initialization  >>
    layer_provider = layer.dataProvider()
    layer_provider.addAttributes([QgsField(name, type)])
    layer.updateFields()
    print('Processing complete. _create_new_field')

# give id
def give_id():
    layer= iface.activeLayer()
    layer.startEditing()

    # Create a dictionary of all features
    feature_dict = {f.id(): f for f in layer.getFeatures()}

    id =0
    # Loop through all features and give id
    for f in feature_dict.values():
        f[_ID_FIELD] = id
        id +=1
        layer.updateFeature(f)

    layer.commitChanges()
    print('Processing complete. _give_id')


create_new_field(name,type)
give_id()

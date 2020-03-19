import xml.etree.cElementTree as ET

tree = ET.parse('hk.xml')
root = tree.getroot()

for module in root.iter('Module'):
    print(module.get('ID')+'\tSG '+module.get('NameKey')+'\t'+module.get('ModulePquid'))

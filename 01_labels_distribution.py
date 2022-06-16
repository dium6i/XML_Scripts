import os
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

xml_path = 'Your_XMLs_Path'

label_count = {}

for xml in os.listdir(xml_path):
    tree = ET.parse(xml_path + '/' + xml)
    root = tree.getroot()

    for obj in root.iter('object'):
        name = obj.find('name').text
        if name not in label_count.keys():
            label_count[name] = 1
        else:
            label_count[name] += 1

print(label_count)

x = [i for i in label_count.keys()]
y = [j for j in label_count.values()]

plt.bar(x, y)
for a,b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom')
plt.savefig('Your_img_save_path/.labels_distribution.jpg', bbox_inches='tight', dpi=200, pad_inches=0.1)

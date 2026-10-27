import os
import xml.etree.ElementTree as ET
from collections import Counter

ANNOTATION_DIR = "annotations"
class_counts = Counter()

for filename in os.listdir(ANNOTATION_DIR):
    if filename.lower().endswith(".xml"):
        xml_path = os.path.join(ANNOTATION_DIR, filename)

        try:
            root = ET.parse(xml_path).getroot()

            for obj in root.findall("object"):
                label = obj.findtext("name")

                if label:
                    class_counts[label.strip()] += 1

        except ET.ParseError:
            print("Invalid XML:", filename)

print("\n========== TRAFFIC SIGN CLASSES ==========")

for class_name, count in sorted(class_counts.items()):
    print(f"{class_name}: {count} objects")

print("\nTotal classes:", len(class_counts))
print("Total annotated objects:", sum(class_counts.values()))
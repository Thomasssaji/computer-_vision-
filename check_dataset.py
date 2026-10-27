import os
import xml.etree.ElementTree as ET

IMAGE_DIR = "images"
ANNOTATION_DIR = "annotations"

image_files = {
    os.path.splitext(f)[0]
    for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
}

annotation_files = {
    os.path.splitext(f)[0]
    for f in os.listdir(ANNOTATION_DIR)
    if f.lower().endswith(".xml")
}

matched = image_files & annotation_files

print("========== DATASET SUMMARY ==========")
print("Total images:", len(image_files))
print("Total annotations:", len(annotation_files))
print("Matched pairs:", len(matched))
print("Images without annotations:", len(image_files - annotation_files))
print("Annotations without images:", len(annotation_files - image_files))

print("\n========== SAMPLE ANNOTATION ==========")

if matched:
    sample_name = sorted(matched)[0]
    xml_path = os.path.join(ANNOTATION_DIR, sample_name + ".xml")

    root = ET.parse(xml_path).getroot()

    print("Image:", sample_name)
    print("XML filename:", root.findtext("filename"))
    print("Width:", root.findtext("size/width"))
    print("Height:", root.findtext("size/height"))

    for obj in root.findall("object"):
        label = obj.findtext("name")
        box = obj.find("bndbox")

        if box is not None:
            print("Traffic sign:", label)
            print(
                "Bounding box:",
                box.findtext("xmin"),
                box.findtext("ymin"),
                box.findtext("xmax"),
                box.findtext("ymax"),
            )
else:
    print("No matching image-annotation pairs found.")
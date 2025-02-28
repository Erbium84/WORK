import os
from collections import Counter

LABELS_FOLDER ="/labels-20250212T103318Z-001/labels/labels_hd"


labels_per_image = []

for filename in os.listdir(LABELS_FOLDER):
    if filename.endswith(".txt"):  
        file_path = os.path.join(LABELS_FOLDER, filename)
        

        with open(file_path, "r") as file:
            num_labels = sum(1 for _ in file)
            labels_per_image.append(num_labels)


total_instances = sum(labels_per_image)
label_distribution = Counter(labels_per_image)


print(f"Total Solar Panel Instances in Dataset: {total_instances}")


print("\nValue Counts of Labels per Image:")
ans=0
for num_labels, count in sorted(label_distribution.items()):
    print(f"{count} images have {num_labels} solar panel(s)")
    ans+=count*num_labels
print(f"Total {ans} solar panels in the labels_hd dataset")

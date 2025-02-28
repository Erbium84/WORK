import os
import numpy as np
import matplotlib.pyplot as plt


PIXEL_RESOLUTION = 0.31  
IMAGE_SIZE = 416  
LABELS_FOLDER = "/labels-20250212T103318Z-001/labels/labels_hd"

all_areas = []


for filename in os.listdir(LABELS_FOLDER):
    if filename.endswith(".txt"):  
        file_path = os.path.join(LABELS_FOLDER, filename)
        
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split()
                
                _, _, _, width, height = map(float, data)
                
                width_px = width * IMAGE_SIZE
                height_px = height * IMAGE_SIZE

                area_m2 = (width_px * PIXEL_RESOLUTION) * (height_px * PIXEL_RESOLUTION)
                all_areas.append(area_m2)

total_instances = len(all_areas)
mean_area = np.mean(all_areas)
std_area = np.std(all_areas)

print(f"Total Solar Panel Instances: {total_instances}")
print(f"Mean Solar Panel Area: {mean_area:.2f} m²")
print(f"Standard Deviation of Area: {std_area:.2f} m²")

plt.hist(all_areas, bins=15, edgecolor='black')
plt.xlabel("Solar Panel Area (m²)")
plt.ylabel("Frequency")
plt.title("Histogram of Solar Panel Areas (All Files)")
plt.show()

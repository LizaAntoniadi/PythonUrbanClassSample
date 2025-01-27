# -*- coding: utf-8 -*-
"""Task_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16iJmjMtoudRbnAgxZBPJa1-PCuEgCYrF
"""

class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
         self.territory_name = territory_name
         self.territory_area = territory_area
         self.green_zones = green_zones

         self.green_index = self.calculate_green_index()

    def calculate_green_index(self):
        
        green_index = sum(self.green_zones) / self.territory_area

        return round(green_index * 100,2)

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

list_gr_index=[]

for city_dict in list_territories:
    territory_name = city_dict.get("territory_name")
    territory_area = city_dict.get("territory_area")
    green_zones = city_dict.get("green_zones")

    index_unv = GreenZoneIndex(territory_name, territory_area,green_zones)
    index_unv.green_index

    list_gr_index.append(index_unv.green_index)
    print("Индекс озеленения территории {index_unv.territory_name} равен {index_unv.green_index}%")

print(list_gr_index)
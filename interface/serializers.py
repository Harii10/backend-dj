from .models import Materials, Bmaterials
from typing import Iterable, List, Dict, Any


def serialize_interface(interface: Iterable[Materials]) -> List[Dict[str, Any]]:
    data = []
    for info in interface:
        data.append({
            'Name' : info.Name,
            'Cost_per_Unit' : info.Cost_per_Unit,
            'Durability' : info.Durability,
            'Strength' : info.Strength,
            'Resistance' : info.Resistance,
            'Performance' : info.Performance,
            'Pressure' : info.Pressure,
            'Construction_Cost_Over_Time_Years' : info.Construction_Cost_Over_Time_Years,
            'Area_Measurements' : info.Area_Measurements,
            'Risk_Score' : info.Risk_Score,
            'Material_Score' : info.Material_Score
        })
    return data


def serialize_data(interface : Iterable[Bmaterials]) -> List[Dict[str, Any]]:
    data = []
    for s_info in interface:
        data.append({
            'Name' : s_info.Name,
            'Cost_per_Unit' : s_info.Cost_per_Unit,
            'Durability' : s_info.Durability,
            'Strength' : s_info.Strength,
            'Resistance' : s_info.Resistance,
            'Performance' : s_info.Performance,
            'Pressure' : s_info.Pressure,
            'Construction_Cost_Over_Time_Years' : s_info.Construction_Cost_Over_Time_Years,
            'Area_Measurements' : s_info.Area_Measurements,
            'Risk_Score' : s_info.Risk_Score,
            'Material_Score' : s_info.Material_Score
        })
    return data

def serialize_nested_data(interface : Iterable[Bmaterials]) -> List[Dict[str, Any]]:
    data = []
    for n_info in interface:
        nested_item = {
            f"Name: {n_info.Name}" : {
                    'Cost_per_Unit' : n_info.Cost_per_Unit,
            'Durability' : n_info.Durability,
            'Strength' : n_info.Strength,
            'Resistance' : n_info.Resistance,
            'Performance' : n_info.Performance,
            'Pressure' : n_info.Pressure,
            'Construction_Cost_Over_Time_Years' : n_info.Construction_Cost_Over_Time_Years,
            'Area_Measurements' : n_info.Area_Measurements,
            'Risk_Score' : n_info.Risk_Score,
            'Material_Score' : n_info.Material_Score
            },
            'Cost_per_Unit' : n_info.Cost_per_Unit,
            'Durability' : n_info.Durability,
            'Strength' : n_info.Strength,
            'Resistance' : n_info.Resistance,
            'Performance' : n_info.Performance,
            'Pressure' : n_info.Pressure,
            'Construction_Cost_Over_Time_Years' : n_info.Construction_Cost_Over_Time_Years,
            'Area_Measurements' : n_info.Area_Measurements,
            'Risk_Score' : n_info.Risk_Score,
            'Material_Score' : n_info.Material_Score
        }
        data.append(nested_item)
    return data










        
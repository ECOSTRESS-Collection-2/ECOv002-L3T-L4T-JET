# ECOSTRESS Collection 2 Level-1-2-3-4 Gridded and Tiled Data Products User Guide

**Version 2**<br>
**May 13, 2026**

## Authors
* **Gregory Halverson**: ECOSTRESS Science Team, Jet Propulsion Laboratory, California Institute of Technology
* **Kerry Cawse-Nicholson**: ECOSTRESS Science Team, Jet Propulsion Laboratory, California Institute of Technology
* **Margaret Johnson**: ECOSTRESS Science Team, Jet Propulsion Laboratory, California Institute of Technology

---

## 1. Introduction
This user guide describes the ECOSTRESS Collection 2 gridded and tiled products. ECOSTRESS acquires data within an orbit, divided into scenes roughly 400 x 400 km in size. Collection 2 products are distributed in two formats:
1.  **Orbit/Scene**: Hierarchical Data Format 5 (HDF5)
2.  **Orbit/Scene/Tile**: Cloud-Optimized GeoTIFF (COG)

### Table 1: Listing of ECOSTRESS Collection 2 gridded and tiled products and their swath equivalents.

| Product | Swath (Orbit/Scene HDF5) | Gridded (Orbit/Scene HDF5) | Tiled (Orbit/Scene Tile GeoTIFF) |
| :--- | :--- | :--- | :--- |
| Radiance | L1B RAD | L1CG RAD | L1CT RAD |
| Surface Temperature | L2 LSTE | L2G LSTE | L2T LSTE |
| Cloud | L2 CLOUD | L2G CLOUD | - |
| STARS NDVI/Albedo | - | - | L2T STARS |
| Surface Energy Balance | - | L3G SEB | L3T SEB |
| Soil Moisture | - | L3G SM | L3T SM |
| Meteorology | - | L3G MET | L3T MET |
| Evapotranspiration Ensemble | - | L3G JET | L3T JET |
| DisALEXI-JPL Evapotranspiration | - | L3G ET ALEXI | L3T ET ALEXI |
| Evaporative Stress Index | - | L4G ESI | L4T ESI |
| DisALEXI-JPL Evaporative Stress Index | - | L4G ESI ALEXI | L4T ESI ALEXI |
| Water Use Efficiency | - | L4G WUE | L4T WUE |

---

## 2. Change History Log

| Revision | Effective Date | Prepared by | Description of Changes |
| :--- | :--- | :--- | :--- |
| Draft | 8/24/2022 | Gregory Halverson, Kerry Cawse-Nicholson | User Guide first draft |
| Draft | 12/15/2022 | Margaret Johnson, Kerry Cawse-Nicholson | STARS Description |
| Draft | 12/15/2022 | Gregory Halverson | L1C Processing |
| Draft | 01/12/2023 | Gregory Halverson | Editing for URS submission |
| Version 1 | 4/13/2023 | Kerry Cawse-Nicholson | Version approved for release |

---

## 3. Contacts
Readers seeking additional information may contact:
* **Gregory Halverson**: gregory.h.halverson@jpl.nasa.gov
* **Kerry Cawse-Nicholson**: Kerry-anne.cawse-nicholson@jpl.nasa.gov
* **Margaret Johnson**: maggie.johnson@jpl.nasa.gov
---

## 4. Technical Details

### 4.1 HDF-EOS5 Orbit/Scene Gridded Products
The HDF-EOS5 format (files ending in `.h5`) is used for long-term archiving but is not recommended for end-user analysis. All raster layers are projected to a globally snapped 0.0006° grid in WGS84 (approx. 70 m resolution).

### 4.2 Cloud-Optimized GeoTIFF (COG) Tiled Products
To provide analysis-ready data, ECOSTRESS Collection 2 products are distributed in a tiled form using the COG format. The system uses the modified Military Grid Reference System (MGRS) scheme used by Sentinel 2, dividing UTM zones into square tiles 109,760 m across. Each tile consists of 1568 rows by 1568 columns (70 m pixels).

### 4.3 Quality Flags
Two high-level quality flags (unsigned 8-bit integer) are provided:
* **Cloud Layer**: 0 = absent, 1 = presence (from L2 CLOUD).
* **Water Layer**: 0 = absent, 1 = presence (from SRTM DEM).

---

## 5. Product Descriptions

### 5.1 Level 1 Radiance (L1CG RAD / L1CT RAD)
Distributes top-of-atmosphere radiance in units of $W~m^{-2}sr^{-1}m^{-1}$.

| Name | Type | Units |
| :--- | :--- | :--- |
| radiance 1-5 | float32 | $W~m^{-2}sr^{-1}m^{-1}$ |
| data_quality_1-5 | uint16 | quality flag |
| cloud / water | uint8 | mask |

### 5.2 Level 2 Surface Temperature (L2G LSTE / L2T LSTE)
Distributes bottom-of-atmosphere land-surface temperature (LST) in Kelvin.

| Name | Type | Units |
| :--- | :--- | :--- |
| LST | float32 | Kelvin |
| LST err | float32 | Kelvin |
| EmisWB | float32 | unitless (0 to 1) |
| height | float32 | meters |
| view zenith | float32 | degrees |
| QC | uint16 | quality flag |

### 5.3 L2T STARS NDVI and Albedo
Estimates NDVI and albedo at 70 m resolution by fusing Harmonized Landsat Sentinel (HLS) with Suomi NPP VIIRS data.

| Name | Type | Units |
| :--- | :--- | :--- |
| NDVI | float32 | index: -1 to 1 |
| NDVI-UQ | float32 | index: -1 to 1 |
| albedo | float32 | proportion: 0 to 1 |
| albedo-UQ | float32 | proportion: 0 to 1 |

---

## 6. JPL Evapotranspiration Ensemble (JET)
The JET product combines ECOSTRESS ST/emissivity with STARS NDVI/albedo and downscaled GEOS-5 FP meteorology.

### 6.1 Evapotranspiration Components

| Name | Description | Units |
| :--- | :--- | :--- |
| ETdaily | Integrated ET between sunrise and sunset | mm/day |
| ETinstUncertainty | Standard deviation between ensemble estimates | $W~m^{-2}$ |
| PTJPLSMinst | Priestley-Taylor JPL Soil Moisture model ET | $W~m^{-2}$ |
| STICinst | Surface Temperature Initiated Closure model ET | $W~m^{-2}$ |
| MOD16inst | Penman-Monteith based ET | $W~m^{-2}$ |
| BESSinst | Breathing Earth System Simulator ET | $W~m^{-2}$ |

---

## 7. Water Use Efficiency and Stress Index

| Name | Type | Units |
| :--- | :--- | :--- |
| ESI | float32 | ratio: 0 to 1 (actual ET / PET) |
| PET | float32 | $W~m^{-2}$ (Potential ET) |
| WUE | float32 | $g~C~kg^{-1}~H_2O$ |
| GPP | float32 | μmol $m^{-2}s^{-1}$ (Gross Primary Production) |

---

## 8. Acknowledgements
Special thanks to Joshua Fisher (initial science lead), Adam Purdy (PT-JPL-SM), Kaniska Mallick (STIC), and Martha Anderson (DisALEXI-JPL).

---
*Reference: ECOSTRESS Collection 2 Level-1-2-3-4 Gridded and Tiled Data Products User Guide, Version 2, 2026.*

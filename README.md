# ECOSTRESS Collection 2 JPL Evapotranspiration (JET) Product Generating Executable (PGE)

This software package has been refactored from the [ECOSTRESS Collection 2 Gridded & Tiled Products Generator](https://github.com/ECOSTRESS-Collection-2/ECOSTRESS-Collection-2) as an independent product pipeline for the ECOSTRESS Collection 2 JPL Evapotranspiration (JET), Evaporative Stress Index (ESI), and Water-Use Efficiency (WUE) products. This software package will serve as an ECOSTRESS Collection 2 reference for the development of the [ECOSTRESS Collection 3 JET PGE](https://github.com/ECOSTRESS-Collection-3/ECOv003-L3T-L4T-JET) and the [SBG Collection 1 JET PGE](https://github.com/sbg-tir/SBG-TIR-L4-JET).

[Gregory H. Halverson](https://github.com/gregory-halverson-jpl) (they/them)<br>
[gregory.h.halverson@jpl.nasa.gov](mailto:gregory.h.halverson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 321H

[Kerry Cawse-Nicholson](https://github.com/kcawse) (she/her)<br>
[kerry-anne.cawse-nicholson@jpl.nasa.gov](mailto:kerry-anne.cawse-nicholson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 321H

[Madeleine Pascolini-Campbell](https://github.com/madeleinepc) (she/her)<br>
[madeleine.a.pascolini-campbell@jpl.nasa.gov](mailto:madeleine.a.pascolini-campbell@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 321E

[Evan Davis](https://github.com/evandjpl) (he/him)<br>
[evan.w.davis@jpl.nasa.gov](mailto:evan.w.davis@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 341F

[Claire Villanueva-Weeks](https://github.com/clairesvw) (she/her)<br>
[claire.s.villanueva-weeks@jpl.nasa.gov](mailto:claire.s.villanueva-weeks@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory

## Authentication

This package requires an [EarthData](https://urs.earthdata.nasa.gov/) account and reads EarthData credentials from `~/.netrc` in the following format:

```
machine urs.earthdata.nasa.gov
login <USERNAME>
password <PASSWORD>
```

## Environment

On macOS, there are issues with installing `pykdtree` using pip, so it's better to use a mamba environment and install the `pykdtree` mamba package.

```
mamba create -y -n ECOv002-L3T-L4T-JET -c conda-forge python=3.11 jupyter pykdtree 
mamba activate ECOv002-L3T-L4T-JET
```

## Installation

Install this package from PyPi using the name `ECOv002-L3T-L4T-JET` with dashes:

```
pip install ECOv002-L3T-L4T-JET
```

You can also install development versions of this package directly from a clone of this repository:

```
pip install .
```

## Usage

Import this package with the name `ECOv002_L3T_L4T_JET` with underscores:

```
import ECOv002_L3T_L4T_JET
```

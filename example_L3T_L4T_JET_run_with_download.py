import logging

import numpy as np

import colored_logging as cl

from ECOv002_CMR import download_ECOSTRESS_granule
from ECOv002_L3T_L4T_JET import generate_L3T_L4T_JET_runconfig, L3T_L4T_JET

logger = logging.getLogger(__name__)

working_directory = "~/data/ECOSTRESS_example"
static_directory = "~/data/L3T_L4T_static"

logger.info("acquiring L2T LSTE granule")

L2T_LSTE_granule = download_ECOSTRESS_granule(
    product="L2T_LSTE", 
    orbit=35698,
    scene=14,
    tile="11SPS", 
    aquisition_date="2024-10-22",
    parent_directory=working_directory

logger.info("acquiring L2T STARS granule")

L2T_STARS_granule = download_ECOSTRESS_granule(
    product="L2T_STARS", 
    tile="11SPS", 
    aquisition_date="2024-10-22",
    parent_directory=working_directory
)

logger.info("generating L3T L4T JET runconfig")

runconfig_filename = generate_L3T_L4T_JET_runconfig(
    L2T_LSTE_filename=L2T_LSTE_granule.product_filename,
    L2T_STARS_filename=L2T_STARS_granule.product_filename,
    working_directory=working_directory,
    static_directory=static_directory
)

with open(runconfig_filename, "r") as f:
    print(f.read())

logger.info("running L3T L4T JET")

exit_code = L3T_L4T_JET(runconfig_filename=runconfig_filename)

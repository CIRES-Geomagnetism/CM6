import os
import numpy as np
from functools import lru_cache
from DIFI import SwarmL2_F107_Read, SwarmL2_MIO_SHA_Read_v2
from typing import Optional, Union




@lru_cache(maxsize=1)
def load_swarm_CM6() -> dict:
    """
    This function is called in this file to import 
    DIFI7 coefficients
    """
    baseDir = os.path.dirname(__file__)
    filename_DIFI = os.path.join(baseDir, "coefs", "MIO_CM6.DBL.txt")
    swarm_data = SwarmL2_MIO_SHA_Read_v2.SwarmL2_MIO_SHA_Read_v2(filename_DIFI)

    return swarm_data


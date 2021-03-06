# -*- coding: utf-8 -*-
"""
    hazus
    ~~~~~

    FEMA developed module for analzying risk and loss from natural hazards.

    :copyright: © 2019 by FEMA's Natural Hazards and Risk Assessment Program.
    :license: cc, see LICENSE for more details.
    :author: James Raines; james.rainesii@fema.dhs.gov
"""

__version__ = '0.0.1'
__all__ = [
    'GeneralBuildingStock',
    'UserDefinedFacilities'
    ]

from .general_building_stock import GeneralBuildingStock
from .user_defined_facilities import UserDefinedFacilities

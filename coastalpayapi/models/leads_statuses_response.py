# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.category_with_statuses import CategoryWithStatuses
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class LeadsStatusesResponse(object):

    """Implementation of the 'Leads Statuses Response' model.

    TODO: type model description here.

    Attributes:
        data (list of CategoryWithStatuses): A list of lead statuses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data'
    }

    _optionals = [
        'data',
    ]

    def __init__(self,
                 data=APIHelper.SKIP):
        """Constructor for the LeadsStatusesResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        data = None
        if dictionary.get('data') is not None:
            data = [CategoryWithStatuses.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(data)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        file_name = os.path.basename(__file__).removesuffix(".py")
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__), file_name)).is_valid(val)

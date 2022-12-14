# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class LeadsResponse(object):

    """Implementation of the 'Leads Response' model.

    TODO: type model description here.

    Attributes:
        lead_id (int): Lead Id
        message (string): Result message

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lead_id": 'leadId',
        "message": 'message'
    }

    _optionals = [
        'lead_id',
        'message',
    ]

    def __init__(self,
                 lead_id=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the LeadsResponse class"""

        # Initialize members of the class
        if lead_id is not APIHelper.SKIP:
            self.lead_id = lead_id 
        if message is not APIHelper.SKIP:
            self.message = message 

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

        lead_id = dictionary.get("leadId") if dictionary.get("leadId") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(lead_id,
                   message)

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

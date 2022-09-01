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


class Recipient5(object):

    """Implementation of the 'Recipient5' model.

    TODO: type model description here.

    Attributes:
        field_id (int): Lead Field Id with email address
        email (string): Recipient Email
        name (string): Recipient Name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field_id": 'fieldId',
        "email": 'email',
        "name": 'name'
    }

    _optionals = [
        'field_id',
        'email',
        'name',
    ]

    def __init__(self,
                 field_id=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Recipient5 class"""

        # Initialize members of the class
        if field_id is not APIHelper.SKIP:
            self.field_id = field_id 
        if email is not APIHelper.SKIP:
            self.email = email 
        if name is not APIHelper.SKIP:
            self.name = name 

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

        field_id = dictionary.get("fieldId") if dictionary.get("fieldId") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(field_id,
                   email,
                   name)

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

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


class LeadFieldTab(object):

    """Implementation of the 'LeadFieldTab' model.

    TODO: type model description here.

    Attributes:
        id (int): Tab Id
        active (ActiveEnum): Active tab
        position (PositionEnum): Tab position
        mclass (ClassEnum): Tab class
        name (string): Tab class
        order (int): Tab order

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "position": 'position',
        "mclass": 'class',
        "name": 'name',
        "order": 'order',
        "id": 'id',
        "active": 'active'
    }

    _optionals = [
        'id',
        'active',
    ]

    def __init__(self,
                 position=1,
                 mclass=None,
                 name=None,
                 order=None,
                 id=APIHelper.SKIP,
                 active=APIHelper.SKIP):
        """Constructor for the LeadFieldTab class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if active is not APIHelper.SKIP:
            self.active = active 
        self.position = position 
        self.mclass = mclass 
        self.name = name 
        self.order = order 

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

        position = dictionary.get("position") if dictionary.get("position") else 1
        mclass = dictionary.get("class") if dictionary.get("class") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        order = dictionary.get("order") if dictionary.get("order") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        active = dictionary.get("active") if dictionary.get("active") else APIHelper.SKIP
        # Return an object of this model
        return cls(position,
                   mclass,
                   name,
                   order,
                   id,
                   active)

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

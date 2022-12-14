# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.label import Label
from coastalpayapi.models.tab import Tab
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class Datum3(object):

    """Implementation of the 'Datum3' model.

    TODO: type model description here.

    Attributes:
        id (string): Document Id
        name (string): Name
        size (string): Size
        tab (Tab): TODO: type description here.
        label (Label): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "size": 'size',
        "tab": 'tab',
        "label": 'label'
    }

    _optionals = [
        'id',
        'name',
        'size',
        'tab',
        'label',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 size=APIHelper.SKIP,
                 tab=APIHelper.SKIP,
                 label=APIHelper.SKIP):
        """Constructor for the Datum3 class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if size is not APIHelper.SKIP:
            self.size = size 
        if tab is not APIHelper.SKIP:
            self.tab = tab 
        if label is not APIHelper.SKIP:
            self.label = label 

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

        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        tab = Tab.from_dictionary(dictionary.get('tab')) if 'tab' in dictionary.keys() else APIHelper.SKIP 
        label = Label.from_dictionary(dictionary.get('label')) if 'label' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(id,
                   name,
                   size,
                   tab,
                   label)

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

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


class Meta(object):

    """Implementation of the 'Meta' model.

    TODO: type model description here.

    Attributes:
        current_page (int): The current page number of a data set
        mfrom (int): The current position of a data set
        last_page (string): The last page of a data set
        path (string): API path
        per_page (int): A number of records per page
        to (int): The last position in a data set
        total (int): Total number of records in a data set

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current_page": 'current_page',
        "mfrom": 'from',
        "last_page": 'last_page',
        "path": 'path',
        "per_page": 'per_page',
        "to": 'to',
        "total": 'total'
    }

    _optionals = [
        'current_page',
        'mfrom',
        'last_page',
        'path',
        'per_page',
        'to',
        'total',
    ]

    def __init__(self,
                 current_page=APIHelper.SKIP,
                 mfrom=APIHelper.SKIP,
                 last_page=APIHelper.SKIP,
                 path=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 to=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the Meta class"""

        # Initialize members of the class
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if last_page is not APIHelper.SKIP:
            self.last_page = last_page 
        if path is not APIHelper.SKIP:
            self.path = path 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if to is not APIHelper.SKIP:
            self.to = to 
        if total is not APIHelper.SKIP:
            self.total = total 

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

        current_page = dictionary.get("current_page") if dictionary.get("current_page") else APIHelper.SKIP
        mfrom = dictionary.get("from") if dictionary.get("from") else APIHelper.SKIP
        last_page = dictionary.get("last_page") if dictionary.get("last_page") else APIHelper.SKIP
        path = dictionary.get("path") if dictionary.get("path") else APIHelper.SKIP
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        to = dictionary.get("to") if dictionary.get("to") else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(current_page,
                   mfrom,
                   last_page,
                   path,
                   per_page,
                   to,
                   total)

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

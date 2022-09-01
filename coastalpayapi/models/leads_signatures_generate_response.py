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


class LeadsSignaturesGenerateResponse(object):

    """Implementation of the 'Leads Signatures Generate Response' model.

    TODO: type model description here.

    Attributes:
        message (string): Result message
        hash (string): E-Sign hash
        url (string): E-Sign URL

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "hash": 'hash',
        "url": 'url'
    }

    _optionals = [
        'message',
        'hash',
        'url',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 hash=APIHelper.SKIP,
                 url=APIHelper.SKIP):
        """Constructor for the LeadsSignaturesGenerateResponse class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if hash is not APIHelper.SKIP:
            self.hash = hash 
        if url is not APIHelper.SKIP:
            self.url = url 

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

        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        hash = dictionary.get("hash") if dictionary.get("hash") else APIHelper.SKIP
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   hash,
                   url)

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

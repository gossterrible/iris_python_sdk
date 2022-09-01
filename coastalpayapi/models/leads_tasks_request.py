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


class LeadsTasksRequest(object):

    """Implementation of the 'Leads Tasks Request' model.

    TODO: type model description here.

    Attributes:
        priority (PriorityEnum): Priority
        date (string): Date in ISO 8601 format (Y-m-d\TH:i:sP)
        date_end (string): End date in ISO 8601 format (Y-m-d\TH:i:sP)
        text (string): Task description
        set_by (string): Task set by user (user Id)
        set_for (string): Task set for user (user Id)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "priority": 'priority',
        "date": 'date',
        "date_end": 'date_end',
        "text": 'text',
        "set_by": 'set_by',
        "set_for": 'set_for'
    }

    def __init__(self,
                 priority=None,
                 date=None,
                 date_end=None,
                 text=None,
                 set_by=None,
                 set_for=None):
        """Constructor for the LeadsTasksRequest class"""

        # Initialize members of the class
        self.priority = priority 
        self.date = date 
        self.date_end = date_end 
        self.text = text 
        self.set_by = set_by 
        self.set_for = set_for 

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

        priority = dictionary.get("priority") if dictionary.get("priority") else None
        date = dictionary.get("date") if dictionary.get("date") else None
        date_end = dictionary.get("date_end") if dictionary.get("date_end") else None
        text = dictionary.get("text") if dictionary.get("text") else None
        set_by = dictionary.get("set_by") if dictionary.get("set_by") else None
        set_for = dictionary.get("set_for") if dictionary.get("set_for") else None
        # Return an object of this model
        return cls(priority,
                   date,
                   date_end,
                   text,
                   set_by,
                   set_for)

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
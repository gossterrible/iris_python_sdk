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


class StatusActivity(object):

    """Implementation of the 'StatusActivity' model.

    TODO: type model description here.

    Attributes:
        id (int): Activity Id
        changed_by (int): User Id
        changed_at (datetime): Deleted date (Y-m-d\TH:i:sP)
        old_status (string): Old status
        old_status_id (int): Old Status Id
        new_status (string): New status
        new_status_id (int): New Status Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "changed_by": 'changedBy',
        "changed_at": 'changedAt',
        "old_status": 'oldStatus',
        "old_status_id": 'old_status_id',
        "new_status": 'newStatus',
        "new_status_id": 'new_status_id'
    }

    _optionals = [
        'id',
        'changed_by',
        'changed_at',
        'old_status',
        'old_status_id',
        'new_status',
        'new_status_id',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 changed_by=APIHelper.SKIP,
                 changed_at=APIHelper.SKIP,
                 old_status=APIHelper.SKIP,
                 old_status_id=APIHelper.SKIP,
                 new_status=APIHelper.SKIP,
                 new_status_id=APIHelper.SKIP):
        """Constructor for the StatusActivity class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if changed_by is not APIHelper.SKIP:
            self.changed_by = changed_by 
        if changed_at is not APIHelper.SKIP:
            self.changed_at = APIHelper.RFC3339DateTime(changed_at) if changed_at else None 
        if old_status is not APIHelper.SKIP:
            self.old_status = old_status 
        if old_status_id is not APIHelper.SKIP:
            self.old_status_id = old_status_id 
        if new_status is not APIHelper.SKIP:
            self.new_status = new_status 
        if new_status_id is not APIHelper.SKIP:
            self.new_status_id = new_status_id 

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
        changed_by = dictionary.get("changedBy") if dictionary.get("changedBy") else APIHelper.SKIP
        changed_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("changedAt")).datetime if dictionary.get("changedAt") else APIHelper.SKIP
        old_status = dictionary.get("oldStatus") if dictionary.get("oldStatus") else APIHelper.SKIP
        old_status_id = dictionary.get("old_status_id") if dictionary.get("old_status_id") else APIHelper.SKIP
        new_status = dictionary.get("newStatus") if dictionary.get("newStatus") else APIHelper.SKIP
        new_status_id = dictionary.get("new_status_id") if dictionary.get("new_status_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   changed_by,
                   changed_at,
                   old_status,
                   old_status_id,
                   new_status,
                   new_status_id)

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

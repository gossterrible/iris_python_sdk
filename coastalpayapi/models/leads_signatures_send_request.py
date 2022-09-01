# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.recipient import Recipient
from coastalpayapi.models.recipient_1 import Recipient1
from coastalpayapi.models.recipient_5 import Recipient5
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class LeadsSignaturesSendRequest(object):

    """Implementation of the 'Leads Signatures Send Request' model.

    TODO: type model description here.

    Attributes:
        recipients (list of Recipient5): TODO: type description here.
        expire (bool): Expire the previously generated application

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipients": 'recipients',
        "expire": 'expire'
    }

    _optionals = [
        'recipients',
        'expire',
    ]

    def __init__(self,
                 recipients=APIHelper.SKIP,
                 expire=APIHelper.SKIP):
        """Constructor for the LeadsSignaturesSendRequest class"""

        # Initialize members of the class
        if recipients is not APIHelper.SKIP:
            self.recipients = recipients 
        if expire is not APIHelper.SKIP:
            self.expire = expire 

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
        if dictionary.get('recipients') is not None:
            if isinstance(dictionary.get('recipients'), list):
                recipients = []
                for x in dictionary.get('recipients'):
                    if Recipient.validate(x):
                        recipients.append(Recipient.from_dictionary(x))
                    elif Recipient1.validate(x):
                        recipients.append(Recipient1.from_dictionary(x))
                    else:
                        raise ValidationError("The value provided doesn't validate against the schema")
        elif 'recipients' not in dictionary.keys():
            recipients = APIHelper.SKIP
        expire = dictionary.get("expire") if "expire" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(recipients,
                   expire)

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

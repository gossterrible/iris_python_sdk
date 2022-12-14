# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.copy import Copy
from coastalpayapi.models.dropdown import Dropdown
from coastalpayapi.models.zipcode_autocomplete import ZipcodeAutocomplete
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class Options(object):

    """Implementation of the 'Options' model.

    TODO: type model description here.

    Attributes:
        dropdown (Dropdown): Add new list item
        dupecheck (bool): Enable dupecheck
        contactid (string): Id of contact field
        mask (MaskEnum): Field mask
        copy (Copy): Copy button properties
        hyperlink (bool): Enable hyperlink
        sms (bool): Enable SMS
        dialer (bool): Enable dialer
        googlemaps (object): Google Maps search properties
        zip_code_field (int): Zip code field ID for TimeZone field only
        zipcode_autocomplete (ZipcodeAutocomplete): ZIP Code autofill
            properties

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dropdown": 'dropdown',
        "dupecheck": 'dupecheck',
        "contactid": 'contactid',
        "mask": 'mask',
        "copy": 'copy',
        "hyperlink": 'hyperlink',
        "sms": 'sms',
        "dialer": 'dialer',
        "googlemaps": 'googlemaps',
        "zip_code_field": 'zip_code_field',
        "zipcode_autocomplete": 'zipcode_autocomplete'
    }

    _optionals = [
        'dropdown',
        'dupecheck',
        'contactid',
        'mask',
        'copy',
        'hyperlink',
        'sms',
        'dialer',
        'googlemaps',
        'zip_code_field',
        'zipcode_autocomplete',
    ]

    def __init__(self,
                 dropdown=APIHelper.SKIP,
                 dupecheck=APIHelper.SKIP,
                 contactid=APIHelper.SKIP,
                 mask=APIHelper.SKIP,
                 copy=APIHelper.SKIP,
                 hyperlink=APIHelper.SKIP,
                 sms=APIHelper.SKIP,
                 dialer=APIHelper.SKIP,
                 googlemaps=APIHelper.SKIP,
                 zip_code_field=APIHelper.SKIP,
                 zipcode_autocomplete=APIHelper.SKIP):
        """Constructor for the Options class"""

        # Initialize members of the class
        if dropdown is not APIHelper.SKIP:
            self.dropdown = dropdown 
        if dupecheck is not APIHelper.SKIP:
            self.dupecheck = dupecheck 
        if contactid is not APIHelper.SKIP:
            self.contactid = contactid 
        if mask is not APIHelper.SKIP:
            self.mask = mask 
        if copy is not APIHelper.SKIP:
            self.copy = copy 
        if hyperlink is not APIHelper.SKIP:
            self.hyperlink = hyperlink 
        if sms is not APIHelper.SKIP:
            self.sms = sms 
        if dialer is not APIHelper.SKIP:
            self.dialer = dialer 
        if googlemaps is not APIHelper.SKIP:
            self.googlemaps = googlemaps 
        if zip_code_field is not APIHelper.SKIP:
            self.zip_code_field = zip_code_field 
        if zipcode_autocomplete is not APIHelper.SKIP:
            self.zipcode_autocomplete = zipcode_autocomplete 

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

        dropdown = Dropdown.from_dictionary(dictionary.get('dropdown')) if 'dropdown' in dictionary.keys() else APIHelper.SKIP 
        dupecheck = dictionary.get("dupecheck") if "dupecheck" in dictionary.keys() else APIHelper.SKIP
        contactid = dictionary.get("contactid") if dictionary.get("contactid") else APIHelper.SKIP
        mask = dictionary.get("mask") if dictionary.get("mask") else APIHelper.SKIP
        copy = Copy.from_dictionary(dictionary.get('copy')) if 'copy' in dictionary.keys() else APIHelper.SKIP 
        hyperlink = dictionary.get("hyperlink") if "hyperlink" in dictionary.keys() else APIHelper.SKIP
        sms = dictionary.get("sms") if "sms" in dictionary.keys() else APIHelper.SKIP
        dialer = dictionary.get("dialer") if "dialer" in dictionary.keys() else APIHelper.SKIP
        googlemaps = dictionary.get("googlemaps") if dictionary.get("googlemaps") else APIHelper.SKIP
        zip_code_field = dictionary.get("zip_code_field") if dictionary.get("zip_code_field") else APIHelper.SKIP
        zipcode_autocomplete = ZipcodeAutocomplete.from_dictionary(dictionary.get('zipcode_autocomplete')) if 'zipcode_autocomplete' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(dropdown,
                   dupecheck,
                   contactid,
                   mask,
                   copy,
                   hyperlink,
                   sms,
                   dialer,
                   googlemaps,
                   zip_code_field,
                   zipcode_autocomplete)

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

# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.options import Options
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class LeadsFieldsRequest(object):

    """Implementation of the 'Leads Fields Request' model.

    TODO: type model description here.

    Attributes:
        id (int): Field Id
        tab (int): Field tab Id
        label (string): Field label
        mtype (TypeEnum): Field type
        length (int): Field size
        default (string): Field default value
        alignment (AlignmentEnum): Field alignment
        searchable (SearchableEnum): Searchable field
        special (SpecialEnum): Field special value
        options (Options): TODO: type description here.
        order (int): TODO: type description here.
        read_only (bool): Whether the field is read only
        required (bool): Whether the field is required
        override (bool): Flag for overriding existing special field

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tab": 'tab',
        "label": 'label',
        "mtype": 'type',
        "id": 'id',
        "length": 'length',
        "default": 'default',
        "alignment": 'alignment',
        "searchable": 'searchable',
        "special": 'special',
        "options": 'options',
        "order": 'order',
        "read_only": 'readOnly',
        "required": 'required',
        "override": 'override'
    }

    _optionals = [
        'id',
        'length',
        'default',
        'alignment',
        'searchable',
        'special',
        'options',
        'order',
        'read_only',
        'required',
        'override',
    ]

    def __init__(self,
                 tab=None,
                 label=None,
                 mtype=None,
                 id=APIHelper.SKIP,
                 length=APIHelper.SKIP,
                 default=APIHelper.SKIP,
                 alignment=APIHelper.SKIP,
                 searchable=APIHelper.SKIP,
                 special=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 order=APIHelper.SKIP,
                 read_only=APIHelper.SKIP,
                 required=APIHelper.SKIP,
                 override=APIHelper.SKIP):
        """Constructor for the LeadsFieldsRequest class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.tab = tab 
        self.label = label 
        self.mtype = mtype 
        if length is not APIHelper.SKIP:
            self.length = length 
        if default is not APIHelper.SKIP:
            self.default = default 
        if alignment is not APIHelper.SKIP:
            self.alignment = alignment 
        if searchable is not APIHelper.SKIP:
            self.searchable = searchable 
        if special is not APIHelper.SKIP:
            self.special = special 
        if options is not APIHelper.SKIP:
            self.options = options 
        if order is not APIHelper.SKIP:
            self.order = order 
        if read_only is not APIHelper.SKIP:
            self.read_only = read_only 
        if required is not APIHelper.SKIP:
            self.required = required 
        if override is not APIHelper.SKIP:
            self.override = override 

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

        tab = dictionary.get("tab") if dictionary.get("tab") else None
        label = dictionary.get("label") if dictionary.get("label") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        length = dictionary.get("length") if dictionary.get("length") else APIHelper.SKIP
        default = dictionary.get("default") if dictionary.get("default") else APIHelper.SKIP
        alignment = dictionary.get("alignment") if dictionary.get("alignment") else APIHelper.SKIP
        searchable = dictionary.get("searchable") if dictionary.get("searchable") else APIHelper.SKIP
        special = dictionary.get("special") if dictionary.get("special") else APIHelper.SKIP
        options = Options.from_dictionary(dictionary.get('options')) if 'options' in dictionary.keys() else APIHelper.SKIP 
        order = dictionary.get("order") if dictionary.get("order") else APIHelper.SKIP
        read_only = dictionary.get("readOnly") if "readOnly" in dictionary.keys() else APIHelper.SKIP
        required = dictionary.get("required") if "required" in dictionary.keys() else APIHelper.SKIP
        override = dictionary.get("override") if "override" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(tab,
                   label,
                   mtype,
                   id,
                   length,
                   default,
                   alignment,
                   searchable,
                   special,
                   options,
                   order,
                   read_only,
                   required,
                   override)

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

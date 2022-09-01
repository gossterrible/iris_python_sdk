# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from coastalpayapi.api_helper import APIHelper
from coastalpayapi.models.duplicate import Duplicate
import os
from coastalpayapi.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError


class Info(object):

    """Implementation of the 'Info' model.

    TODO: type model description here.

    Attributes:
        field_name (string): Field name
        field_type (FieldTypeEnum): Field type
        left (int): Padding from left
        right (int): Padding from right
        top (int): Padding from top
        bottom (int): Padding from bottom
        field_height (int): Height of field
        field_width (int): Width of field
        page_number (int): Page number
        page_height (int): Page height
        page_width (int): Page width
        page_rotation (int): Page rotation
        export_value (string): Export value
        tooltip (string): Field tooltip
        duplicates (list of Duplicate): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field_name": 'field_name',
        "field_type": 'field_type',
        "left": 'left',
        "right": 'right',
        "top": 'top',
        "bottom": 'bottom',
        "field_height": 'field_height',
        "field_width": 'field_width',
        "page_number": 'page_number',
        "page_height": 'page_height',
        "page_width": 'page_width',
        "page_rotation": 'page_rotation',
        "export_value": 'export_value',
        "tooltip": 'tooltip',
        "duplicates": 'duplicates'
    }

    _optionals = [
        'field_name',
        'field_type',
        'left',
        'right',
        'top',
        'bottom',
        'field_height',
        'field_width',
        'page_number',
        'page_height',
        'page_width',
        'page_rotation',
        'export_value',
        'tooltip',
        'duplicates',
    ]

    def __init__(self,
                 field_name=APIHelper.SKIP,
                 field_type=APIHelper.SKIP,
                 left=APIHelper.SKIP,
                 right=APIHelper.SKIP,
                 top=APIHelper.SKIP,
                 bottom=APIHelper.SKIP,
                 field_height=APIHelper.SKIP,
                 field_width=APIHelper.SKIP,
                 page_number=APIHelper.SKIP,
                 page_height=APIHelper.SKIP,
                 page_width=APIHelper.SKIP,
                 page_rotation=APIHelper.SKIP,
                 export_value=APIHelper.SKIP,
                 tooltip=APIHelper.SKIP,
                 duplicates=APIHelper.SKIP):
        """Constructor for the Info class"""

        # Initialize members of the class
        if field_name is not APIHelper.SKIP:
            self.field_name = field_name 
        if field_type is not APIHelper.SKIP:
            self.field_type = field_type 
        if left is not APIHelper.SKIP:
            self.left = left 
        if right is not APIHelper.SKIP:
            self.right = right 
        if top is not APIHelper.SKIP:
            self.top = top 
        if bottom is not APIHelper.SKIP:
            self.bottom = bottom 
        if field_height is not APIHelper.SKIP:
            self.field_height = field_height 
        if field_width is not APIHelper.SKIP:
            self.field_width = field_width 
        if page_number is not APIHelper.SKIP:
            self.page_number = page_number 
        if page_height is not APIHelper.SKIP:
            self.page_height = page_height 
        if page_width is not APIHelper.SKIP:
            self.page_width = page_width 
        if page_rotation is not APIHelper.SKIP:
            self.page_rotation = page_rotation 
        if export_value is not APIHelper.SKIP:
            self.export_value = export_value 
        if tooltip is not APIHelper.SKIP:
            self.tooltip = tooltip 
        if duplicates is not APIHelper.SKIP:
            self.duplicates = duplicates 

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

        field_name = dictionary.get("field_name") if dictionary.get("field_name") else APIHelper.SKIP
        field_type = dictionary.get("field_type") if dictionary.get("field_type") else APIHelper.SKIP
        left = dictionary.get("left") if dictionary.get("left") else APIHelper.SKIP
        right = dictionary.get("right") if dictionary.get("right") else APIHelper.SKIP
        top = dictionary.get("top") if dictionary.get("top") else APIHelper.SKIP
        bottom = dictionary.get("bottom") if dictionary.get("bottom") else APIHelper.SKIP
        field_height = dictionary.get("field_height") if dictionary.get("field_height") else APIHelper.SKIP
        field_width = dictionary.get("field_width") if dictionary.get("field_width") else APIHelper.SKIP
        page_number = dictionary.get("page_number") if dictionary.get("page_number") else APIHelper.SKIP
        page_height = dictionary.get("page_height") if dictionary.get("page_height") else APIHelper.SKIP
        page_width = dictionary.get("page_width") if dictionary.get("page_width") else APIHelper.SKIP
        page_rotation = dictionary.get("page_rotation") if dictionary.get("page_rotation") else APIHelper.SKIP
        export_value = dictionary.get("export_value") if dictionary.get("export_value") else APIHelper.SKIP
        tooltip = dictionary.get("tooltip") if dictionary.get("tooltip") else APIHelper.SKIP
        duplicates = None
        if dictionary.get('duplicates') is not None:
            duplicates = [Duplicate.from_dictionary(x) for x in dictionary.get('duplicates')]
        else:
            duplicates = APIHelper.SKIP
        # Return an object of this model
        return cls(field_name,
                   field_type,
                   left,
                   right,
                   top,
                   bottom,
                   field_height,
                   field_width,
                   page_number,
                   page_height,
                   page_width,
                   page_rotation,
                   export_value,
                   tooltip,
                   duplicates)

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
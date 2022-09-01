"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete)  ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.   # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from iriscrm.api_client import ApiClient, Endpoint as _Endpoint
from iriscrm.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from iriscrm.model.lead_field import LeadField
from iriscrm.model.lead_field_order import LeadFieldOrder
from iriscrm.model.lead_field_tab import LeadFieldTab
from iriscrm.model.leads_campaigns_get200_response import LeadsCampaignsGet200Response
from iriscrm.model.leads_emails_templates_get200_response import LeadsEmailsTemplatesGet200Response
from iriscrm.model.leads_fields_field_id_order_patch200_response import LeadsFieldsFieldIdOrderPatch200Response
from iriscrm.model.leads_fields_get200_response import LeadsFieldsGet200Response
from iriscrm.model.leads_fields_get_request import LeadsFieldsGetRequest
from iriscrm.model.leads_fields_tabs_get200_response import LeadsFieldsTabsGet200Response
from iriscrm.model.leads_file_labels_get200_response import LeadsFileLabelsGet200Response
from iriscrm.model.leads_get200_response import LeadsGet200Response
from iriscrm.model.leads_get200_response1 import LeadsGet200Response1
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_get_request import LeadsGetRequest
from iriscrm.model.leads_groups_get200_response import LeadsGroupsGet200Response
from iriscrm.model.leads_lead_id_activity_campaign_get200_response import LeadsLeadIdActivityCampaignGet200Response
from iriscrm.model.leads_lead_id_activity_deletion_get200_response import LeadsLeadIdActivityDeletionGet200Response
from iriscrm.model.leads_lead_id_activity_duplicates_get200_response import LeadsLeadIdActivityDuplicatesGet200Response
from iriscrm.model.leads_lead_id_activity_links_get200_response import LeadsLeadIdActivityLinksGet200Response
from iriscrm.model.leads_lead_id_activity_source_get200_response import LeadsLeadIdActivitySourceGet200Response
from iriscrm.model.leads_lead_id_activity_status_get200_response import LeadsLeadIdActivityStatusGet200Response
from iriscrm.model.leads_lead_id_applications_application_id_populate_post200_response import LeadsLeadIdApplicationsApplicationIdPopulatePost200Response
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
from iriscrm.model.leads_lead_id_appointments_get200_response import LeadsLeadIdAppointmentsGet200Response
from iriscrm.model.leads_lead_id_appointments_get200_response1 import LeadsLeadIdAppointmentsGet200Response1
from iriscrm.model.leads_lead_id_appointments_get_request import LeadsLeadIdAppointmentsGetRequest
from iriscrm.model.leads_lead_id_documents_get200_response import LeadsLeadIdDocumentsGet200Response
from iriscrm.model.leads_lead_id_emails_template_id_post200_response import LeadsLeadIdEmailsTemplateIdPost200Response
from iriscrm.model.leads_lead_id_emails_template_id_post_request import LeadsLeadIdEmailsTemplateIdPostRequest
from iriscrm.model.leads_lead_id_get200_response import LeadsLeadIdGet200Response
from iriscrm.model.leads_lead_id_get200_response1 import LeadsLeadIdGet200Response1
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_get_request import LeadsLeadIdGetRequest
from iriscrm.model.leads_lead_id_notes_get200_response import LeadsLeadIdNotesGet200Response
from iriscrm.model.leads_lead_id_notes_get200_response1 import LeadsLeadIdNotesGet200Response1
from iriscrm.model.leads_lead_id_notes_get_request import LeadsLeadIdNotesGetRequest
from iriscrm.model.leads_lead_id_records_cat_id_record_id_delete200_response import LeadsLeadIdRecordsCatIdRecordIdDelete200Response
from iriscrm.model.leads_lead_id_sms_template_id_post200_response import LeadsLeadIdSmsTemplateIdPost200Response
from iriscrm.model.leads_lead_id_sms_template_id_post_request import LeadsLeadIdSmsTemplateIdPostRequest
from iriscrm.model.leads_lead_id_tabs_tab_id_fields_get200_response import LeadsLeadIdTabsTabIdFieldsGet200Response
from iriscrm.model.leads_lead_id_tasks_get200_response import LeadsLeadIdTasksGet200Response
from iriscrm.model.leads_lead_id_tasks_get200_response1 import LeadsLeadIdTasksGet200Response1
from iriscrm.model.leads_lead_id_tasks_get_request import LeadsLeadIdTasksGetRequest
from iriscrm.model.leads_lead_id_users_get200_response import LeadsLeadIdUsersGet200Response
from iriscrm.model.leads_lead_id_users_get200_response1 import LeadsLeadIdUsersGet200Response1
from iriscrm.model.leads_lead_id_users_get_request import LeadsLeadIdUsersGetRequest
from iriscrm.model.leads_lead_id_users_user_id_delete200_response import LeadsLeadIdUsersUserIdDelete200Response
from iriscrm.model.leads_pricing_templates_get200_response import LeadsPricingTemplatesGet200Response
from iriscrm.model.leads_sms_templates_get200_response import LeadsSmsTemplatesGet200Response
from iriscrm.model.leads_sources_get200_response import LeadsSourcesGet200Response
from iriscrm.model.leads_statuses_get200_response import LeadsStatusesGet200Response


class LeadsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.leads_campaigns_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsCampaignsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/campaigns',
                'operation_id': 'leads_campaigns_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_emails_templates_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsEmailsTemplatesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/emails/templates',
                'operation_id': 'leads_emails_templates_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_fields_field_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadField,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/{fieldId}',
                'operation_id': 'leads_fields_field_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'field_id',
                ],
                'required': [
                    'field_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'field_id':
                        (int,),
                },
                'attribute_map': {
                    'field_id': 'fieldId',
                },
                'location_map': {
                    'field_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_fields_field_id_order_patch_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsFieldsFieldIdOrderPatch200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/{fieldId}/order',
                'operation_id': 'leads_fields_field_id_order_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'field_id',
                    'lead_field_order',
                ],
                'required': [
                    'field_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'field_id':
                        (int,),
                    'lead_field_order':
                        (LeadFieldOrder,),
                },
                'attribute_map': {
                    'field_id': 'fieldId',
                },
                'location_map': {
                    'field_id': 'path',
                    'lead_field_order': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_fields_field_id_patch_endpoint = _Endpoint(
            settings={
                'response_type': (LeadField,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/{fieldId}',
                'operation_id': 'leads_fields_field_id_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'field_id',
                    'leads_fields_get_request',
                ],
                'required': [
                    'field_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'field_id':
                        (int,),
                    'leads_fields_get_request':
                        (LeadsFieldsGetRequest,),
                },
                'attribute_map': {
                    'field_id': 'fieldId',
                },
                'location_map': {
                    'field_id': 'path',
                    'leads_fields_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_fields_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsFieldsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields',
                'operation_id': 'leads_fields_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_fields_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadField,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields',
                'operation_id': 'leads_fields_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'leads_fields_get_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'leads_fields_get_request':
                        (LeadsFieldsGetRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'leads_fields_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_fields_tabs_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsFieldsTabsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/tabs',
                'operation_id': 'leads_fields_tabs_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_fields_tabs_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadFieldTab,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/tabs',
                'operation_id': 'leads_fields_tabs_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_field_tab',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_field_tab':
                        (LeadFieldTab,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'lead_field_tab': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_fields_tabs_tab_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadFieldTab,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/tabs/{tabId}',
                'operation_id': 'leads_fields_tabs_tab_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tab_id',
                ],
                'required': [
                    'tab_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tab_id':
                        (int,),
                },
                'attribute_map': {
                    'tab_id': 'tabId',
                },
                'location_map': {
                    'tab_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_fields_tabs_tab_id_patch_endpoint = _Endpoint(
            settings={
                'response_type': (LeadFieldTab,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/fields/tabs/{tabId}',
                'operation_id': 'leads_fields_tabs_tab_id_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'tab_id',
                    'lead_field_tab',
                ],
                'required': [
                    'tab_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tab_id':
                        (int,),
                    'lead_field_tab':
                        (LeadFieldTab,),
                },
                'attribute_map': {
                    'tab_id': 'tabId',
                },
                'location_map': {
                    'tab_id': 'path',
                    'lead_field_tab': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_file_labels_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsFileLabelsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/file_labels',
                'operation_id': 'leads_file_labels_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads',
                'operation_id': 'leads_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                    'sort_by',
                    'sort_dir',
                    'group',
                    'mid',
                    'campaign',
                    'source',
                    'status',
                    'category',
                    'user',
                    'date_filter',
                    'start_date',
                    'end_date',
                    'email',
                    'fields',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                    'sort_by',
                    'sort_dir',
                    'date_filter',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                    ('sort_by',): {

                        "ID": "id",
                        "MID": "mid",
                        "NAME": "name",
                        "CREATED": "created",
                        "MODIFIED": "modified"
                    },
                    ('sort_dir',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                    ('date_filter',): {

                        "CREATED": "created",
                        "MODIFIED": "modified",
                        "LAST_NOTE": "last_note",
                        "LAST_STATUS": "last_status",
                        "LAST_TASK": "last_task",
                        "LAST_TASK_DUE": "last_task_due",
                        "LAST_APPOINTMENT": "last_appointment",
                        "LAST_APPOINTMENT_DUE": "last_appointment_due"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort_by':
                        (str,),
                    'sort_dir':
                        (str,),
                    'group':
                        (int,),
                    'mid':
                        (int,),
                    'campaign':
                        (int,),
                    'source':
                        (int,),
                    'status':
                        (int,),
                    'category':
                        (int,),
                    'user':
                        (int,),
                    'date_filter':
                        (str,),
                    'start_date':
                        (datetime,),
                    'end_date':
                        (datetime,),
                    'email':
                        (str,),
                    'fields':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                    'sort_by': 'sort_by',
                    'sort_dir': 'sort_dir',
                    'group': 'group',
                    'mid': 'mid',
                    'campaign': 'campaign',
                    'source': 'source',
                    'status': 'status',
                    'category': 'category',
                    'user': 'user',
                    'date_filter': 'date_filter',
                    'start_date': 'start_date',
                    'end_date': 'end_date',
                    'email': 'email',
                    'fields': 'fields',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                    'sort_by': 'query',
                    'sort_dir': 'query',
                    'group': 'query',
                    'mid': 'query',
                    'campaign': 'query',
                    'source': 'query',
                    'status': 'query',
                    'category': 'query',
                    'user': 'query',
                    'date_filter': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'email': 'query',
                    'fields': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_groups_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsGroupsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/groups',
                'operation_id': 'leads_groups_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'status',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'status':
                        (int,),
                },
                'attribute_map': {
                    'status': 'status',
                },
                'location_map': {
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_campaign_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivityCampaignGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/campaign',
                'operation_id': 'leads_lead_id_activity_campaign_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_deletion_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivityDeletionGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/deletion',
                'operation_id': 'leads_lead_id_activity_deletion_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_duplicates_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivityDuplicatesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/duplicates',
                'operation_id': 'leads_lead_id_activity_duplicates_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_links_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivityLinksGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/links',
                'operation_id': 'leads_lead_id_activity_links_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_source_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivitySourceGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/source',
                'operation_id': 'leads_lead_id_activity_source_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_activity_status_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdActivityStatusGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/activity/status',
                'operation_id': 'leads_lead_id_activity_status_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_applications_application_id_populate_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdApplicationsApplicationIdPopulatePost200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/applications/{applicationId}/populate',
                'operation_id': 'leads_lead_id_applications_application_id_populate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'application_id',
                ],
                'required': [
                    'lead_id',
                    'application_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'application_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'application_id': 'applicationId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'application_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_appointments_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdAppointmentsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/appointments',
                'operation_id': 'leads_lead_id_appointments_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'set_for',
                    'set_by',
                    'modified_by',
                    'confirmed_by',
                    'rescheduled_by',
                    'seen_by',
                    'rescheduled_count',
                    'done',
                    'per_page',
                    'sort_by',
                    'sort_dir',
                    'date_filter',
                    'start_date',
                    'end_date',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                    'sort_by',
                    'sort_dir',
                    'date_filter',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                    ('sort_by',): {

                        "ID": "id",
                        "SET_FOR": "set_for",
                        "SET_AT": "set_at",
                        "SET_BY": "set_by",
                        "MODIFIED": "modified",
                        "MODIFIED_BY": "modified_by",
                        "DATE": "date",
                        "DATE_END": "date_end",
                        "CONFIRMED": "confirmed",
                        "CONFIRMED_BY": "confirmed_by",
                        "SEEN": "seen",
                        "SEEN_BY": "seen_by",
                        "RESCHEDULED": "rescheduled",
                        "RESCHEDULED_BY": "rescheduled_by",
                        "RESCHEDULED_BY": "rescheduled_by"
                    },
                    ('sort_dir',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                    ('date_filter',): {

                        "DATE": "date",
                        "SET_AT": "set_at",
                        "MODIFIED": "modified",
                        "CONFIRMED": "confirmed",
                        "RESCHEDULED": "rescheduled",
                        "SEEN": "seen"
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'set_for':
                        (int,),
                    'set_by':
                        (int,),
                    'modified_by':
                        (int,),
                    'confirmed_by':
                        (int,),
                    'rescheduled_by':
                        (int,),
                    'seen_by':
                        (int,),
                    'rescheduled_count':
                        (int,),
                    'done':
                        (bool,),
                    'per_page':
                        (int,),
                    'sort_by':
                        (str,),
                    'sort_dir':
                        (str,),
                    'date_filter':
                        (str,),
                    'start_date':
                        (date,),
                    'end_date':
                        (date,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'set_for': 'set_for',
                    'set_by': 'set_by',
                    'modified_by': 'modified_by',
                    'confirmed_by': 'confirmed_by',
                    'rescheduled_by': 'rescheduled_by',
                    'seen_by': 'seen_by',
                    'rescheduled_count': 'rescheduled_count',
                    'done': 'done',
                    'per_page': 'per_page',
                    'sort_by': 'sort_by',
                    'sort_dir': 'sort_dir',
                    'date_filter': 'date_filter',
                    'start_date': 'start_date',
                    'end_date': 'end_date',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'set_for': 'query',
                    'set_by': 'query',
                    'modified_by': 'query',
                    'confirmed_by': 'query',
                    'rescheduled_by': 'query',
                    'seen_by': 'query',
                    'rescheduled_count': 'query',
                    'done': 'query',
                    'per_page': 'query',
                    'sort_by': 'query',
                    'sort_dir': 'query',
                    'date_filter': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_appointments_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdAppointmentsGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/appointments',
                'operation_id': 'leads_lead_id_appointments_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'leads_lead_id_appointments_get_request',
                ],
                'required': [
                    'lead_id',
                    'leads_lead_id_appointments_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'leads_lead_id_appointments_get_request':
                        (LeadsLeadIdAppointmentsGetRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'leads_lead_id_appointments_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_documents_document_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/documents/{documentId}',
                'operation_id': 'leads_lead_id_documents_document_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'document_id',
                ],
                'required': [
                    'lead_id',
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'document_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'document_id': 'documentId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'document_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_documents_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdDocumentsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/documents',
                'operation_id': 'leads_lead_id_documents_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_documents_post_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/documents',
                'operation_id': 'leads_lead_id_documents_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'tab',
                    'label',
                    'filename',
                    'notify_users',
                    'body',
                ],
                'required': [
                    'lead_id',
                    'tab',
                    'label',
                    'filename',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'tab':
                        (int,),
                    'label':
                        (int,),
                    'filename':
                        (str,),
                    'notify_users':
                        (str,),
                    'body':
                        (file_type,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'tab': 'tab',
                    'label': 'label',
                    'filename': 'filename',
                    'notify_users': 'notify_users',
                },
                'location_map': {
                    'lead_id': 'path',
                    'tab': 'query',
                    'label': 'query',
                    'filename': 'query',
                    'notify_users': 'query',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json'
                ],
                'content_type': [
                    'application/octet-stream'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_emails_template_id_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdEmailsTemplateIdPost200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/emails/{templateId}',
                'operation_id': 'leads_lead_id_emails_template_id_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'template_id',
                    'leads_lead_id_emails_template_id_post_request',
                ],
                'required': [
                    'lead_id',
                    'template_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'template_id':
                        (int,),
                    'leads_lead_id_emails_template_id_post_request':
                        (LeadsLeadIdEmailsTemplateIdPostRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'template_id': 'templateId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'template_id': 'path',
                    'leads_lead_id_emails_template_id_post_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}',
                'operation_id': 'leads_lead_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_mailbox_email_id_attachment_attachment_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId}',
                'operation_id': 'leads_lead_id_mailbox_email_id_attachment_attachment_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'email_id',
                    'attachment_id',
                ],
                'required': [
                    'lead_id',
                    'email_id',
                    'attachment_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'email_id':
                        (int,),
                    'attachment_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'email_id': 'emailId',
                    'attachment_id': 'attachmentId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'email_id': 'path',
                    'attachment_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_notes_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdNotesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/notes',
                'operation_id': 'leads_lead_id_notes_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_notes_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdNotesGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/notes',
                'operation_id': 'leads_lead_id_notes_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'leads_lead_id_notes_get_request',
                ],
                'required': [
                    'lead_id',
                    'leads_lead_id_notes_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'leads_lead_id_notes_get_request':
                        (LeadsLeadIdNotesGetRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'leads_lead_id_notes_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_patch_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}',
                'operation_id': 'leads_lead_id_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'leads_lead_id_get_request',
                ],
                'required': [
                    'lead_id',
                    'leads_lead_id_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'leads_lead_id_get_request':
                        (LeadsLeadIdGetRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'leads_lead_id_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_records_cat_id_record_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdRecordsCatIdRecordIdDelete200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/records/{catId}/{recordId}',
                'operation_id': 'leads_lead_id_records_cat_id_record_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'cat_id',
                    'record_id',
                ],
                'required': [
                    'lead_id',
                    'cat_id',
                    'record_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'cat_id':
                        (int,),
                    'record_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'cat_id': 'catId',
                    'record_id': 'recordId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'cat_id': 'path',
                    'record_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_sms_template_id_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdSmsTemplateIdPost200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/sms/{templateId}',
                'operation_id': 'leads_lead_id_sms_template_id_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'template_id',
                    'leads_lead_id_sms_template_id_post_request',
                ],
                'required': [
                    'lead_id',
                    'template_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'template_id':
                        (int,),
                    'leads_lead_id_sms_template_id_post_request':
                        (LeadsLeadIdSmsTemplateIdPostRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'template_id': 'templateId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'template_id': 'path',
                    'leads_lead_id_sms_template_id_post_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_tabs_tab_id_fields_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdTabsTabIdFieldsGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/tabs/{tabId}/fields',
                'operation_id': 'leads_lead_id_tabs_tab_id_fields_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'tab_id',
                ],
                'required': [
                    'lead_id',
                    'tab_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'tab_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'tab_id': 'tabId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'tab_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_tasks_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdTasksGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/tasks',
                'operation_id': 'leads_lead_id_tasks_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_tasks_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdTasksGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/tasks',
                'operation_id': 'leads_lead_id_tasks_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'leads_lead_id_tasks_get_request',
                ],
                'required': [
                    'lead_id',
                    'leads_lead_id_tasks_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'leads_lead_id_tasks_get_request':
                        (LeadsLeadIdTasksGetRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'leads_lead_id_tasks_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_users_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdUsersGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/users',
                'operation_id': 'leads_lead_id_users_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'page',
                    'per_page',
                ],
                'required': [
                    'lead_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100,
                        "500": 500,
                        "1000": 1000
                    },
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'lead_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_lead_id_users_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdUsersGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/users',
                'operation_id': 'leads_lead_id_users_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'leads_lead_id_users_get_request',
                ],
                'required': [
                    'lead_id',
                    'leads_lead_id_users_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'leads_lead_id_users_get_request':
                        (LeadsLeadIdUsersGetRequest,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'leads_lead_id_users_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_lead_id_users_user_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdUsersUserIdDelete200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/{leadId}/users/{userId}',
                'operation_id': 'leads_lead_id_users_user_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'lead_id',
                    'user_id',
                ],
                'required': [
                    'lead_id',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lead_id':
                        (int,),
                    'user_id':
                        (int,),
                },
                'attribute_map': {
                    'lead_id': 'leadId',
                    'user_id': 'userId',
                },
                'location_map': {
                    'lead_id': 'path',
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_post_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsGet200Response1,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads',
                'operation_id': 'leads_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'leads_get_request',
                ],
                'required': [
                    'leads_get_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'leads_get_request':
                        (LeadsGetRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'leads_get_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.leads_pricing_templates_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsPricingTemplatesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/pricing_templates',
                'operation_id': 'leads_pricing_templates_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_sms_templates_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsSmsTemplatesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/sms/templates',
                'operation_id': 'leads_sms_templates_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_sources_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsSourcesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/sources',
                'operation_id': 'leads_sources_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_statuses_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsStatusesGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/statuses',
                'operation_id': 'leads_statuses_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group':
                        (int,),
                },
                'attribute_map': {
                    'group': 'group',
                },
                'location_map': {
                    'group': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.leads_users_get_endpoint = _Endpoint(
            settings={
                'response_type': (LeadsLeadIdUsersGet200Response,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/leads/users',
                'operation_id': 'leads_users_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'per_page',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'per_page',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('per_page',): {

                        "10": 10,
                        "25": 25,
                        "50": 50,
                        "100": 100
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'per_page': 'per_page',
                },
                'location_map': {
                    'page': 'query',
                    'per_page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def leads_campaigns_get(
        self,
        **kwargs
    ):
        """Get a list of available campaigns  # noqa: E501

        Get a list of available campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_campaigns_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsCampaignsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_campaigns_get_endpoint.call_with_http_info(**kwargs)

    def leads_emails_templates_get(
        self,
        **kwargs
    ):
        """Get a list of email templates  # noqa: E501

        Get list of available email templates for a lead email  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_emails_templates_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsEmailsTemplatesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_emails_templates_get_endpoint.call_with_http_info(**kwargs)

    def leads_fields_field_id_get(
        self,
        field_id,
        **kwargs
    ):
        """Get a lead field  # noqa: E501

        Get a lead field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_field_id_get(field_id, async_req=True)
        >>> result = thread.get()

        Args:
            field_id (int): Field Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadField
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['field_id'] = \
            field_id
        return self.leads_fields_field_id_get_endpoint.call_with_http_info(**kwargs)

    def leads_fields_field_id_order_patch(
        self,
        field_id,
        **kwargs
    ):
        """Update a lead field order position  # noqa: E501

        Update a lead field order position for the current Lead. You can send value equal to 0 and type 'increment' or 'decrement' to set the field as first or last in the field list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_field_id_order_patch(field_id, async_req=True)
        >>> result = thread.get()

        Args:
            field_id (int): Field Id

        Keyword Args:
            lead_field_order (LeadFieldOrder): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsFieldsFieldIdOrderPatch200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['field_id'] = \
            field_id
        return self.leads_fields_field_id_order_patch_endpoint.call_with_http_info(**kwargs)

    def leads_fields_field_id_patch(
        self,
        field_id,
        **kwargs
    ):
        """Update a lead field  # noqa: E501

        Update a field for the current lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_field_id_patch(field_id, async_req=True)
        >>> result = thread.get()

        Args:
            field_id (int): Field Id

        Keyword Args:
            leads_fields_get_request (LeadsFieldsGetRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadField
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['field_id'] = \
            field_id
        return self.leads_fields_field_id_patch_endpoint.call_with_http_info(**kwargs)

    def leads_fields_get(
        self,
        **kwargs
    ):
        """Get a list of available lead fields  # noqa: E501

        Get a list of available lead fields  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsFieldsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_fields_get_endpoint.call_with_http_info(**kwargs)

    def leads_fields_post(
        self,
        **kwargs
    ):
        """Create a new lead field  # noqa: E501

        Create a new lead field  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            leads_fields_get_request (LeadsFieldsGetRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadField
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_fields_post_endpoint.call_with_http_info(**kwargs)

    def leads_fields_tabs_get(
        self,
        **kwargs
    ):
        """Get a list of all lead field tabs  # noqa: E501

        Get a list of all lead field tabs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_tabs_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsFieldsTabsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_fields_tabs_get_endpoint.call_with_http_info(**kwargs)

    def leads_fields_tabs_post(
        self,
        **kwargs
    ):
        """Create a lead field tab  # noqa: E501

        Create a lead field tab  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_tabs_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            lead_field_tab (LeadFieldTab): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadFieldTab
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_fields_tabs_post_endpoint.call_with_http_info(**kwargs)

    def leads_fields_tabs_tab_id_get(
        self,
        tab_id,
        **kwargs
    ):
        """Get a lead field tab  # noqa: E501

        Get a lead field tab  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_tabs_tab_id_get(tab_id, async_req=True)
        >>> result = thread.get()

        Args:
            tab_id (int): Lead field tab Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadFieldTab
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['tab_id'] = \
            tab_id
        return self.leads_fields_tabs_tab_id_get_endpoint.call_with_http_info(**kwargs)

    def leads_fields_tabs_tab_id_patch(
        self,
        tab_id,
        **kwargs
    ):
        """Update a lead field tab  # noqa: E501

        Update a lead field tab  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_fields_tabs_tab_id_patch(tab_id, async_req=True)
        >>> result = thread.get()

        Args:
            tab_id (int): Lead field tab Id

        Keyword Args:
            lead_field_tab (LeadFieldTab): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadFieldTab
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['tab_id'] = \
            tab_id
        return self.leads_fields_tabs_tab_id_patch_endpoint.call_with_http_info(**kwargs)

    def leads_file_labels_get(
        self,
        **kwargs
    ):
        """Get a list of available document labels  # noqa: E501

        Get a list of all document labels available when uploading and downloading files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_file_labels_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsFileLabelsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_file_labels_get_endpoint.call_with_http_info(**kwargs)

    def leads_get(
        self,
        **kwargs
    ):
        """Get a list of leads  # noqa: E501

        Get a list of leads  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            sort_by (str): Sorting of leads by the field value. [optional]
            sort_dir (str): Direction of sorting. [optional] if omitted the server will use the default value of "asc"
            group (int): Filter leads by a group id. [optional]
            mid (int): Filter leads by a merchant id. [optional]
            campaign (int): Filter leads by a campaign id. [optional]
            source (int): Filter leads by a source id. [optional]
            status (int): Filter leads by a status id. [optional]
            category (int): Filter leads by a status category id. [optional]
            user (int): Filter leads by a user id. [optional]
            date_filter (str): Filtering leads by a date range depends on this filter. [optional]
            start_date (datetime): Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**). [optional]
            end_date (datetime): Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**). [optional]
            email (str): Filter leads by using an email address. [optional]
            fields (str): Filter leads by searching any lead field values. Search multiple values as an AND operation. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_get_endpoint.call_with_http_info(**kwargs)

    def leads_groups_get(
        self,
        **kwargs
    ):
        """Get a list of available groups  # noqa: E501

        Get a list of available groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_groups_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            status (int): Status Id. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsGroupsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_groups_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_campaign_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead campaign activity  # noqa: E501

        Get a list of all lead campaign activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_campaign_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivityCampaignGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_campaign_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_deletion_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead deletion activity  # noqa: E501

        Get a list of all lead deletion activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_deletion_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivityDeletionGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_deletion_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_duplicates_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead duplicate activity  # noqa: E501

        Get a list of all lead duplicate activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_duplicates_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivityDuplicatesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_duplicates_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_links_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead links activity  # noqa: E501

        Get a list of all lead links activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_links_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivityLinksGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_links_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_source_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead source activity  # noqa: E501

        Get a list of all lead source activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_source_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivitySourceGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_source_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_activity_status_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of all lead status activity  # noqa: E501

        Get a list of all lead status activity  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_activity_status_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdActivityStatusGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_activity_status_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_applications_application_id_populate_post(
        self,
        lead_id,
        application_id,
        **kwargs
    ):
        """Populate PDF Document  # noqa: E501

        Populate a PDF document from a lead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_applications_application_id_populate_post(lead_id, application_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            application_id (int): Application Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdApplicationsApplicationIdPopulatePost200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['application_id'] = \
            application_id
        return self.leads_lead_id_applications_application_id_populate_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_appointments_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get lead appointments  # noqa: E501

        Get lead appointments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_appointments_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            set_for (int): Filter by the user for who appointment was created. [optional]
            set_by (int): Filter by the user for who have created an appointment. [optional]
            modified_by (int): Filter by the user for who have modified an appointment. [optional]
            confirmed_by (int): Filter by the user for who have confirmed an appointment. [optional]
            rescheduled_by (int): Filter by the user for who have rescheduled an appointment. [optional]
            seen_by (int): Filter by the user for who have mark an appointment as seen. [optional]
            rescheduled_count (int): Filter by the count of rescheduling. [optional]
            done (bool): Filter by the done flag. [optional]
            per_page (int): Count of records per page. [optional]
            sort_by (str): Sort appointments by columns. [optional]
            sort_dir (str): Sort direction. [optional]
            date_filter (str): Filtering appointments by a date range depends on this filter. [optional]
            start_date (date): Filter appointments by a date in format Y-m-d. [optional]
            end_date (date): Filter leads by a date in format Y-m-d. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdAppointmentsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_appointments_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_appointments_post(
        self,
        lead_id,
        leads_lead_id_appointments_get_request,
        **kwargs
    ):
        """Create a lead appointment  # noqa: E501

        Create a lead appointment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_appointments_post(lead_id, leads_lead_id_appointments_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            leads_lead_id_appointments_get_request (LeadsLeadIdAppointmentsGetRequest): Create a lead appointment

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdAppointmentsGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['leads_lead_id_appointments_get_request'] = \
            leads_lead_id_appointments_get_request
        return self.leads_lead_id_appointments_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_documents_document_id_get(
        self,
        lead_id,
        document_id,
        **kwargs
    ):
        """Download a document  # noqa: E501

        Download a document  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_documents_document_id_get(lead_id, document_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            document_id (int): Document Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['document_id'] = \
            document_id
        return self.leads_lead_id_documents_document_id_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_documents_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of available documents  # noqa: E501

        Get a list of available documents  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_documents_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdDocumentsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_documents_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_documents_post(
        self,
        lead_id,
        tab,
        label,
        filename,
        **kwargs
    ):
        """Upload a document  # noqa: E501

        Upload a document  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_documents_post(lead_id, tab, label, filename, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            tab (int): Tab Id
            label (int): Label Id
            filename (str): File name

        Keyword Args:
            notify_users (str): Comma separated list of user ids to notify or `all_assigned` to notify all users assigned to the lead. [optional]
            body (file_type): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['tab'] = \
            tab
        kwargs['label'] = \
            label
        kwargs['filename'] = \
            filename
        return self.leads_lead_id_documents_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_emails_template_id_post(
        self,
        lead_id,
        template_id,
        **kwargs
    ):
        """Send an email to lead with template  # noqa: E501

        Send an email to lead with template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_emails_template_id_post(lead_id, template_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            template_id (int): Template Id

        Keyword Args:
            leads_lead_id_emails_template_id_post_request (LeadsLeadIdEmailsTemplateIdPostRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdEmailsTemplateIdPost200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['template_id'] = \
            template_id
        return self.leads_lead_id_emails_template_id_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get detailed lead information  # noqa: E501

        Get detailed lead information. If field has a default value, the `uid` field will be `null`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_mailbox_email_id_attachment_attachment_id_get(
        self,
        lead_id,
        email_id,
        attachment_id,
        **kwargs
    ):
        """Download a mailbox email attachment  # noqa: E501

        Download a mailbox email attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_mailbox_email_id_attachment_attachment_id_get(lead_id, email_id, attachment_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            email_id (int): Email Id
            attachment_id (int): Attachment Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['email_id'] = \
            email_id
        kwargs['attachment_id'] = \
            attachment_id
        return self.leads_lead_id_mailbox_email_id_attachment_attachment_id_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_notes_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get lead notes  # noqa: E501

        Get lead notes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_notes_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdNotesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_notes_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_notes_post(
        self,
        lead_id,
        leads_lead_id_notes_get_request,
        **kwargs
    ):
        """Create a lead note  # noqa: E501

        Create a lead note  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_notes_post(lead_id, leads_lead_id_notes_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            leads_lead_id_notes_get_request (LeadsLeadIdNotesGetRequest): Create a lead note

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdNotesGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['leads_lead_id_notes_get_request'] = \
            leads_lead_id_notes_get_request
        return self.leads_lead_id_notes_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_patch(
        self,
        lead_id,
        leads_lead_id_get_request,
        **kwargs
    ):
        """Update a lead  # noqa: E501

        Update a lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_patch(lead_id, leads_lead_id_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            leads_lead_id_get_request (LeadsLeadIdGetRequest): Lead changes (send only fields you want to change)

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['leads_lead_id_get_request'] = \
            leads_lead_id_get_request
        return self.leads_lead_id_patch_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_records_cat_id_record_id_delete(
        self,
        lead_id,
        cat_id,
        record_id,
        **kwargs
    ):
        """Delete record from a lead record set  # noqa: E501

        The method allows deleting records from lead tabs with the type \"set\". Values of `catId` and `recordId` can be obtained by request [Get detailed lead information](#/paths/~1leads~1{leadId}/get) (`details.id` = `catId`, `details.record` = `recordId`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_records_cat_id_record_id_delete(lead_id, cat_id, record_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            cat_id (int): Record category ID
            record_id (int): Record ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdRecordsCatIdRecordIdDelete200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['cat_id'] = \
            cat_id
        kwargs['record_id'] = \
            record_id
        return self.leads_lead_id_records_cat_id_record_id_delete_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_sms_template_id_post(
        self,
        lead_id,
        template_id,
        **kwargs
    ):
        """Send an SMS to lead with selected SMS template  # noqa: E501

        Send an SMS to lead with selected SMS template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_sms_template_id_post(lead_id, template_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            template_id (int): Template Id

        Keyword Args:
            leads_lead_id_sms_template_id_post_request (LeadsLeadIdSmsTemplateIdPostRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdSmsTemplateIdPost200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['template_id'] = \
            template_id
        return self.leads_lead_id_sms_template_id_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_tabs_tab_id_fields_get(
        self,
        lead_id,
        tab_id,
        **kwargs
    ):
        """Get lead information from a specific tab  # noqa: E501

        Get lead information from a specific tab. If field has a default value, the `uid` field will be `null`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_tabs_tab_id_fields_get(lead_id, tab_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            tab_id (int): Lead field tab Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdTabsTabIdFieldsGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['tab_id'] = \
            tab_id
        return self.leads_lead_id_tabs_tab_id_fields_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_tasks_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get lead tasks  # noqa: E501

        Get lead tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_tasks_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdTasksGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_tasks_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_tasks_post(
        self,
        lead_id,
        leads_lead_id_tasks_get_request,
        **kwargs
    ):
        """Create a lead task  # noqa: E501

        Create a lead task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_tasks_post(lead_id, leads_lead_id_tasks_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            leads_lead_id_tasks_get_request (LeadsLeadIdTasksGetRequest): Create a lead task

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdTasksGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['leads_lead_id_tasks_get_request'] = \
            leads_lead_id_tasks_get_request
        return self.leads_lead_id_tasks_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_users_get(
        self,
        lead_id,
        **kwargs
    ):
        """Get a list of assigned users  # noqa: E501

        Get a list of assigned users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_users_get(lead_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id

        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdUsersGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        return self.leads_lead_id_users_get_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_users_post(
        self,
        lead_id,
        leads_lead_id_users_get_request,
        **kwargs
    ):
        """Assign a user  # noqa: E501

        Assign a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_users_post(lead_id, leads_lead_id_users_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            leads_lead_id_users_get_request (LeadsLeadIdUsersGetRequest): Create a lead task

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdUsersGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['leads_lead_id_users_get_request'] = \
            leads_lead_id_users_get_request
        return self.leads_lead_id_users_post_endpoint.call_with_http_info(**kwargs)

    def leads_lead_id_users_user_id_delete(
        self,
        lead_id,
        user_id,
        **kwargs
    ):
        """Unassign a user from a lead  # noqa: E501

        Unassign a user from a lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_lead_id_users_user_id_delete(lead_id, user_id, async_req=True)
        >>> result = thread.get()

        Args:
            lead_id (int): Lead Id
            user_id (int): User Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdUsersUserIdDelete200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['lead_id'] = \
            lead_id
        kwargs['user_id'] = \
            user_id
        return self.leads_lead_id_users_user_id_delete_endpoint.call_with_http_info(**kwargs)

    def leads_post(
        self,
        leads_get_request,
        **kwargs
    ):
        """Create a lead  # noqa: E501

        Create a lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_post(leads_get_request, async_req=True)
        >>> result = thread.get()

        Args:
            leads_get_request (LeadsGetRequest): Lead details

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsGet200Response1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['leads_get_request'] = \
            leads_get_request
        return self.leads_post_endpoint.call_with_http_info(**kwargs)

    def leads_pricing_templates_get(
        self,
        **kwargs
    ):
        """Get pricing templates  # noqa: E501

        Get pricing templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_pricing_templates_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsPricingTemplatesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_pricing_templates_get_endpoint.call_with_http_info(**kwargs)

    def leads_sms_templates_get(
        self,
        **kwargs
    ):
        """Get list of SMS templates  # noqa: E501

        Get list of available SMS templates for sending SMS to a lead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_sms_templates_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsSmsTemplatesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_sms_templates_get_endpoint.call_with_http_info(**kwargs)

    def leads_sources_get(
        self,
        **kwargs
    ):
        """Get a list of available sources  # noqa: E501

        Get a list of available sources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_sources_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsSourcesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_sources_get_endpoint.call_with_http_info(**kwargs)

    def leads_statuses_get(
        self,
        **kwargs
    ):
        """Get a list of available statuses  # noqa: E501

        Get a list of available statuses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_statuses_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            group (int): Group Id. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsStatusesGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_statuses_get_endpoint.call_with_http_info(**kwargs)

    def leads_users_get(
        self,
        **kwargs
    ):
        """Get a list of available users  # noqa: E501

        Get a list of available users for assigning  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_users_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number. [optional]
            per_page (int): Count of records per page. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LeadsLeadIdUsersGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.leads_users_get_endpoint.call_with_http_info(**kwargs)


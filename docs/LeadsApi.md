# iriscrm.LeadsApi

All URIs are relative to *https://www.mycoastalpay.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_campaigns_get**](LeadsApi.md#leads_campaigns_get) | **GET** /leads/campaigns | Get a list of available campaigns
[**leads_emails_templates_get**](LeadsApi.md#leads_emails_templates_get) | **GET** /leads/emails/templates | Get a list of email templates
[**leads_fields_field_id_get**](LeadsApi.md#leads_fields_field_id_get) | **GET** /leads/fields/{fieldId} | Get a lead field
[**leads_fields_field_id_order_patch**](LeadsApi.md#leads_fields_field_id_order_patch) | **PATCH** /leads/fields/{fieldId}/order | Update a lead field order position
[**leads_fields_field_id_patch**](LeadsApi.md#leads_fields_field_id_patch) | **PATCH** /leads/fields/{fieldId} | Update a lead field
[**leads_fields_get**](LeadsApi.md#leads_fields_get) | **GET** /leads/fields | Get a list of available lead fields
[**leads_fields_post**](LeadsApi.md#leads_fields_post) | **POST** /leads/fields | Create a new lead field
[**leads_fields_tabs_get**](LeadsApi.md#leads_fields_tabs_get) | **GET** /leads/fields/tabs | Get a list of all lead field tabs
[**leads_fields_tabs_post**](LeadsApi.md#leads_fields_tabs_post) | **POST** /leads/fields/tabs | Create a lead field tab
[**leads_fields_tabs_tab_id_get**](LeadsApi.md#leads_fields_tabs_tab_id_get) | **GET** /leads/fields/tabs/{tabId} | Get a lead field tab
[**leads_fields_tabs_tab_id_patch**](LeadsApi.md#leads_fields_tabs_tab_id_patch) | **PATCH** /leads/fields/tabs/{tabId} | Update a lead field tab
[**leads_file_labels_get**](LeadsApi.md#leads_file_labels_get) | **GET** /leads/file_labels | Get a list of available document labels
[**leads_get**](LeadsApi.md#leads_get) | **GET** /leads | Get a list of leads
[**leads_groups_get**](LeadsApi.md#leads_groups_get) | **GET** /leads/groups | Get a list of available groups
[**leads_lead_id_activity_campaign_get**](LeadsApi.md#leads_lead_id_activity_campaign_get) | **GET** /leads/{leadId}/activity/campaign | Get a list of all lead campaign activity
[**leads_lead_id_activity_deletion_get**](LeadsApi.md#leads_lead_id_activity_deletion_get) | **GET** /leads/{leadId}/activity/deletion | Get a list of all lead deletion activity
[**leads_lead_id_activity_duplicates_get**](LeadsApi.md#leads_lead_id_activity_duplicates_get) | **GET** /leads/{leadId}/activity/duplicates | Get a list of all lead duplicate activity
[**leads_lead_id_activity_links_get**](LeadsApi.md#leads_lead_id_activity_links_get) | **GET** /leads/{leadId}/activity/links | Get a list of all lead links activity
[**leads_lead_id_activity_source_get**](LeadsApi.md#leads_lead_id_activity_source_get) | **GET** /leads/{leadId}/activity/source | Get a list of all lead source activity
[**leads_lead_id_activity_status_get**](LeadsApi.md#leads_lead_id_activity_status_get) | **GET** /leads/{leadId}/activity/status | Get a list of all lead status activity
[**leads_lead_id_applications_application_id_populate_post**](LeadsApi.md#leads_lead_id_applications_application_id_populate_post) | **POST** /leads/{leadId}/applications/{applicationId}/populate | Populate PDF Document
[**leads_lead_id_appointments_get**](LeadsApi.md#leads_lead_id_appointments_get) | **GET** /leads/{leadId}/appointments | Get lead appointments
[**leads_lead_id_appointments_post**](LeadsApi.md#leads_lead_id_appointments_post) | **POST** /leads/{leadId}/appointments | Create a lead appointment
[**leads_lead_id_documents_document_id_get**](LeadsApi.md#leads_lead_id_documents_document_id_get) | **GET** /leads/{leadId}/documents/{documentId} | Download a document
[**leads_lead_id_documents_get**](LeadsApi.md#leads_lead_id_documents_get) | **GET** /leads/{leadId}/documents | Get a list of available documents
[**leads_lead_id_documents_post**](LeadsApi.md#leads_lead_id_documents_post) | **POST** /leads/{leadId}/documents | Upload a document
[**leads_lead_id_emails_template_id_post**](LeadsApi.md#leads_lead_id_emails_template_id_post) | **POST** /leads/{leadId}/emails/{templateId} | Send an email to lead with template
[**leads_lead_id_get**](LeadsApi.md#leads_lead_id_get) | **GET** /leads/{leadId} | Get detailed lead information
[**leads_lead_id_mailbox_email_id_attachment_attachment_id_get**](LeadsApi.md#leads_lead_id_mailbox_email_id_attachment_attachment_id_get) | **GET** /leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId} | Download a mailbox email attachment
[**leads_lead_id_notes_get**](LeadsApi.md#leads_lead_id_notes_get) | **GET** /leads/{leadId}/notes | Get lead notes
[**leads_lead_id_notes_post**](LeadsApi.md#leads_lead_id_notes_post) | **POST** /leads/{leadId}/notes | Create a lead note
[**leads_lead_id_patch**](LeadsApi.md#leads_lead_id_patch) | **PATCH** /leads/{leadId} | Update a lead
[**leads_lead_id_records_cat_id_record_id_delete**](LeadsApi.md#leads_lead_id_records_cat_id_record_id_delete) | **DELETE** /leads/{leadId}/records/{catId}/{recordId} | Delete record from a lead record set
[**leads_lead_id_sms_template_id_post**](LeadsApi.md#leads_lead_id_sms_template_id_post) | **POST** /leads/{leadId}/sms/{templateId} | Send an SMS to lead with selected SMS template
[**leads_lead_id_tabs_tab_id_fields_get**](LeadsApi.md#leads_lead_id_tabs_tab_id_fields_get) | **GET** /leads/{leadId}/tabs/{tabId}/fields | Get lead information from a specific tab
[**leads_lead_id_tasks_get**](LeadsApi.md#leads_lead_id_tasks_get) | **GET** /leads/{leadId}/tasks | Get lead tasks
[**leads_lead_id_tasks_post**](LeadsApi.md#leads_lead_id_tasks_post) | **POST** /leads/{leadId}/tasks | Create a lead task
[**leads_lead_id_users_get**](LeadsApi.md#leads_lead_id_users_get) | **GET** /leads/{leadId}/users | Get a list of assigned users
[**leads_lead_id_users_post**](LeadsApi.md#leads_lead_id_users_post) | **POST** /leads/{leadId}/users | Assign a user
[**leads_lead_id_users_user_id_delete**](LeadsApi.md#leads_lead_id_users_user_id_delete) | **DELETE** /leads/{leadId}/users/{userId} | Unassign a user from a lead
[**leads_post**](LeadsApi.md#leads_post) | **POST** /leads | Create a lead
[**leads_pricing_templates_get**](LeadsApi.md#leads_pricing_templates_get) | **GET** /leads/pricing_templates | Get pricing templates
[**leads_sms_templates_get**](LeadsApi.md#leads_sms_templates_get) | **GET** /leads/sms/templates | Get list of SMS templates
[**leads_sources_get**](LeadsApi.md#leads_sources_get) | **GET** /leads/sources | Get a list of available sources
[**leads_statuses_get**](LeadsApi.md#leads_statuses_get) | **GET** /leads/statuses | Get a list of available statuses
[**leads_users_get**](LeadsApi.md#leads_users_get) | **GET** /leads/users | Get a list of available users


# **leads_campaigns_get**
> LeadsCampaignsGet200Response leads_campaigns_get()

Get a list of available campaigns

Get a list of available campaigns

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_campaigns_get200_response import LeadsCampaignsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of available campaigns
        api_response = api_instance.leads_campaigns_get()
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_campaigns_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LeadsCampaignsGet200Response**](LeadsCampaignsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available campaigns |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_emails_templates_get**
> LeadsEmailsTemplatesGet200Response leads_emails_templates_get()

Get a list of email templates

Get list of available email templates for a lead email

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_emails_templates_get200_response import LeadsEmailsTemplatesGet200Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of email templates
        api_response = api_instance.leads_emails_templates_get()
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_emails_templates_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LeadsEmailsTemplatesGet200Response**](LeadsEmailsTemplatesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available email templates |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_field_id_get**
> LeadField leads_fields_field_id_get(field_id)

Get a lead field

Get a lead field

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field import LeadField
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    field_id = 1 # int | Field Id

    # example passing only required values which don't have defaults set
    try:
        # Get a lead field
        api_response = api_instance.leads_fields_field_id_get(field_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_field_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **int**| Field Id |

### Return type

[**LeadField**](LeadField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a lead field |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_field_id_order_patch**
> LeadsFieldsFieldIdOrderPatch200Response leads_fields_field_id_order_patch(field_id)

Update a lead field order position

Update a lead field order position for the current Lead. You can send value equal to 0 and type 'increment' or 'decrement' to set the field as first or last in the field list.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_fields_field_id_order_patch200_response import LeadsFieldsFieldIdOrderPatch200Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.lead_field_order import LeadFieldOrder
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    field_id = 1 # int | Field Id
    lead_field_order = LeadFieldOrder(
        value=1,
        type="increment",
    ) # LeadFieldOrder |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a lead field order position
        api_response = api_instance.leads_fields_field_id_order_patch(field_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_field_id_order_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a lead field order position
        api_response = api_instance.leads_fields_field_id_order_patch(field_id, lead_field_order=lead_field_order)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_field_id_order_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **int**| Field Id |
 **lead_field_order** | [**LeadFieldOrder**](LeadFieldOrder.md)|  | [optional]

### Return type

[**LeadsFieldsFieldIdOrderPatch200Response**](LeadsFieldsFieldIdOrderPatch200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Lead field order position |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_field_id_patch**
> LeadField leads_fields_field_id_patch(field_id)

Update a lead field

Update a field for the current lead

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field import LeadField
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_fields_get_request import LeadsFieldsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    field_id = 1 # int | Field Id
    leads_fields_get_request = LeadsFieldsGetRequest(None) # LeadsFieldsGetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a lead field
        api_response = api_instance.leads_fields_field_id_patch(field_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_field_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a lead field
        api_response = api_instance.leads_fields_field_id_patch(field_id, leads_fields_get_request=leads_fields_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_field_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_id** | **int**| Field Id |
 **leads_fields_get_request** | [**LeadsFieldsGetRequest**](LeadsFieldsGetRequest.md)|  | [optional]

### Return type

[**LeadField**](LeadField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated field attributes |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_get**
> LeadsFieldsGet200Response leads_fields_get()

Get a list of available lead fields

Get a list of available lead fields

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_fields_get200_response import LeadsFieldsGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available lead fields
        api_response = api_instance.leads_fields_get(page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsFieldsGet200Response**](LeadsFieldsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available fields |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_post**
> LeadField leads_fields_post()

Create a new lead field

Create a new lead field

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field import LeadField
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_fields_get_request import LeadsFieldsGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    leads_fields_get_request = LeadsFieldsGetRequest(None) # LeadsFieldsGetRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new lead field
        api_response = api_instance.leads_fields_post(leads_fields_get_request=leads_fields_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leads_fields_get_request** | [**LeadsFieldsGetRequest**](LeadsFieldsGetRequest.md)|  | [optional]

### Return type

[**LeadField**](LeadField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created field |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_tabs_get**
> LeadsFieldsTabsGet200Response leads_fields_tabs_get()

Get a list of all lead field tabs

Get a list of all lead field tabs

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_fields_tabs_get200_response import LeadsFieldsTabsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead field tabs
        api_response = api_instance.leads_fields_tabs_get(page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_tabs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsFieldsTabsGet200Response**](LeadsFieldsTabsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all lead field tabs |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_tabs_post**
> LeadFieldTab leads_fields_tabs_post()

Create a lead field tab

Create a lead field tab

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field_tab import LeadFieldTab
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_field_tab = LeadFieldTab(
        active=1,
        position=1,
        _class="documents",
        name="New tab",
        order=1,
    ) # LeadFieldTab |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a lead field tab
        api_response = api_instance.leads_fields_tabs_post(lead_field_tab=lead_field_tab)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_tabs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_field_tab** | [**LeadFieldTab**](LeadFieldTab.md)|  | [optional]

### Return type

[**LeadFieldTab**](LeadFieldTab.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a lead field tab |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_tabs_tab_id_get**
> LeadFieldTab leads_fields_tabs_tab_id_get(tab_id)

Get a lead field tab

Get a lead field tab

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field_tab import LeadFieldTab
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    tab_id = 1 # int | Lead field tab Id

    # example passing only required values which don't have defaults set
    try:
        # Get a lead field tab
        api_response = api_instance.leads_fields_tabs_tab_id_get(tab_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_tabs_tab_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tab_id** | **int**| Lead field tab Id |

### Return type

[**LeadFieldTab**](LeadFieldTab.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead field tab |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_fields_tabs_tab_id_patch**
> LeadFieldTab leads_fields_tabs_tab_id_patch(tab_id)

Update a lead field tab

Update a lead field tab

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.lead_field_tab import LeadFieldTab
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    tab_id = 1 # int | Lead field tab Id
    lead_field_tab = LeadFieldTab(
        active=1,
        position=1,
        _class="documents",
        name="New tab",
        order=1,
    ) # LeadFieldTab |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a lead field tab
        api_response = api_instance.leads_fields_tabs_tab_id_patch(tab_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_tabs_tab_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a lead field tab
        api_response = api_instance.leads_fields_tabs_tab_id_patch(tab_id, lead_field_tab=lead_field_tab)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_fields_tabs_tab_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tab_id** | **int**| Lead field tab Id |
 **lead_field_tab** | [**LeadFieldTab**](LeadFieldTab.md)|  | [optional]

### Return type

[**LeadFieldTab**](LeadFieldTab.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated lead field tab |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_file_labels_get**
> LeadsFileLabelsGet200Response leads_file_labels_get()

Get a list of available document labels

Get a list of all document labels available when uploading and downloading files

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_file_labels_get200_response import LeadsFileLabelsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available document labels
        api_response = api_instance.leads_file_labels_get(page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_file_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsFileLabelsGet200Response**](LeadsFileLabelsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available labels |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_get**
> LeadsGet200Response leads_get()

Get a list of leads

Get a list of leads

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get200_response import LeadsGet200Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)
    sort_by = "id" # str | Sorting of leads by the field value (optional)
    sort_dir = "asc" # str | Direction of sorting (optional) if omitted the server will use the default value of "asc"
    group = 1 # int | Filter leads by a group id (optional)
    mid = 1 # int | Filter leads by a merchant id (optional)
    campaign = 1 # int | Filter leads by a campaign id (optional)
    source = 1 # int | Filter leads by a source id (optional)
    status = 1 # int | Filter leads by a status id (optional)
    category = 1 # int | Filter leads by a status category id (optional)
    user = 1 # int | Filter leads by a user id (optional)
    date_filter = "created" # str | Filtering leads by a date range depends on this filter (optional)
    start_date = dateutil_parser('2019-01-01T12:04:40+05:00') # datetime | Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**) (optional)
    end_date = dateutil_parser('2019-01-01T12:04:40+05:00') # datetime | Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**) (optional)
    email = "email_example" # str | Filter leads by using an email address (optional)
    fields = "?fields[field_id]=field_value&fields[field_id2]=field_value2" # str | Filter leads by searching any lead field values. Search multiple values as an AND operation.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of leads
        api_response = api_instance.leads_get(page=page, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, group=group, mid=mid, campaign=campaign, source=source, status=status, category=category, user=user, date_filter=date_filter, start_date=start_date, end_date=end_date, email=email, fields=fields)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]
 **sort_by** | **str**| Sorting of leads by the field value | [optional]
 **sort_dir** | **str**| Direction of sorting | [optional] if omitted the server will use the default value of "asc"
 **group** | **int**| Filter leads by a group id | [optional]
 **mid** | **int**| Filter leads by a merchant id | [optional]
 **campaign** | **int**| Filter leads by a campaign id | [optional]
 **source** | **int**| Filter leads by a source id | [optional]
 **status** | **int**| Filter leads by a status id | [optional]
 **category** | **int**| Filter leads by a status category id | [optional]
 **user** | **int**| Filter leads by a user id | [optional]
 **date_filter** | **str**| Filtering leads by a date range depends on this filter | [optional]
 **start_date** | **datetime**| Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that &#x60;+&#x60; sign should be encoded to &#x60;%2B&#x60;**) | [optional]
 **end_date** | **datetime**| Filter leads by a date in ISO 8601 format (Y-m-d\\TH:i:sP) (**Please note that &#x60;+&#x60; sign should be encoded to &#x60;%2B&#x60;**) | [optional]
 **email** | **str**| Filter leads by using an email address | [optional]
 **fields** | **str**| Filter leads by searching any lead field values. Search multiple values as an AND operation.  | [optional]

### Return type

[**LeadsGet200Response**](LeadsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of leads |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_groups_get**
> LeadsGroupsGet200Response leads_groups_get()

Get a list of available groups

Get a list of available groups

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_groups_get200_response import LeadsGroupsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    status = 1 # int | Status Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available groups
        api_response = api_instance.leads_groups_get(status=status)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| Status Id | [optional]

### Return type

[**LeadsGroupsGet200Response**](LeadsGroupsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available groups |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_campaign_get**
> LeadsLeadIdActivityCampaignGet200Response leads_lead_id_activity_campaign_get(lead_id)

Get a list of all lead campaign activity

Get a list of all lead campaign activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_activity_campaign_get200_response import LeadsLeadIdActivityCampaignGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead campaign activity
        api_response = api_instance.leads_lead_id_activity_campaign_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_campaign_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead campaign activity
        api_response = api_instance.leads_lead_id_activity_campaign_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_campaign_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivityCampaignGet200Response**](LeadsLeadIdActivityCampaignGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_deletion_get**
> LeadsLeadIdActivityDeletionGet200Response leads_lead_id_activity_deletion_get(lead_id)

Get a list of all lead deletion activity

Get a list of all lead deletion activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_activity_deletion_get200_response import LeadsLeadIdActivityDeletionGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead deletion activity
        api_response = api_instance.leads_lead_id_activity_deletion_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_deletion_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead deletion activity
        api_response = api_instance.leads_lead_id_activity_deletion_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_deletion_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivityDeletionGet200Response**](LeadsLeadIdActivityDeletionGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_duplicates_get**
> LeadsLeadIdActivityDuplicatesGet200Response leads_lead_id_activity_duplicates_get(lead_id)

Get a list of all lead duplicate activity

Get a list of all lead duplicate activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_activity_duplicates_get200_response import LeadsLeadIdActivityDuplicatesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead duplicate activity
        api_response = api_instance.leads_lead_id_activity_duplicates_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_duplicates_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead duplicate activity
        api_response = api_instance.leads_lead_id_activity_duplicates_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_duplicates_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivityDuplicatesGet200Response**](LeadsLeadIdActivityDuplicatesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_links_get**
> LeadsLeadIdActivityLinksGet200Response leads_lead_id_activity_links_get(lead_id)

Get a list of all lead links activity

Get a list of all lead links activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_activity_links_get200_response import LeadsLeadIdActivityLinksGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead links activity
        api_response = api_instance.leads_lead_id_activity_links_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_links_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead links activity
        api_response = api_instance.leads_lead_id_activity_links_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_links_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivityLinksGet200Response**](LeadsLeadIdActivityLinksGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_source_get**
> LeadsLeadIdActivitySourceGet200Response leads_lead_id_activity_source_get(lead_id)

Get a list of all lead source activity

Get a list of all lead source activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_activity_source_get200_response import LeadsLeadIdActivitySourceGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead source activity
        api_response = api_instance.leads_lead_id_activity_source_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_source_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead source activity
        api_response = api_instance.leads_lead_id_activity_source_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_source_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivitySourceGet200Response**](LeadsLeadIdActivitySourceGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_activity_status_get**
> LeadsLeadIdActivityStatusGet200Response leads_lead_id_activity_status_get(lead_id)

Get a list of all lead status activity

Get a list of all lead status activity

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_lead_id_activity_status_get200_response import LeadsLeadIdActivityStatusGet200Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead status activity
        api_response = api_instance.leads_lead_id_activity_status_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_status_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead status activity
        api_response = api_instance.leads_lead_id_activity_status_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_activity_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdActivityStatusGet200Response**](LeadsLeadIdActivityStatusGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of activity |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_applications_application_id_populate_post**
> LeadsLeadIdApplicationsApplicationIdPopulatePost200Response leads_lead_id_applications_application_id_populate_post(lead_id, application_id)

Populate PDF Document

Populate a PDF document from a lead.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_applications_application_id_populate_post200_response import LeadsLeadIdApplicationsApplicationIdPopulatePost200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    application_id = 1 # int | Application Id

    # example passing only required values which don't have defaults set
    try:
        # Populate PDF Document
        api_response = api_instance.leads_lead_id_applications_application_id_populate_post(lead_id, application_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_applications_application_id_populate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **application_id** | **int**| Application Id |

### Return type

[**LeadsLeadIdApplicationsApplicationIdPopulatePost200Response**](LeadsLeadIdApplicationsApplicationIdPopulatePost200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document populated successfully. |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_appointments_get**
> LeadsLeadIdAppointmentsGet200Response leads_lead_id_appointments_get(lead_id)

Get lead appointments

Get lead appointments

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_appointments_get200_response import LeadsLeadIdAppointmentsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    set_for = 1 # int | Filter by the user for who appointment was created (optional)
    set_by = 1 # int | Filter by the user for who have created an appointment (optional)
    modified_by = 1 # int | Filter by the user for who have modified an appointment (optional)
    confirmed_by = 1 # int | Filter by the user for who have confirmed an appointment (optional)
    rescheduled_by = 1 # int | Filter by the user for who have rescheduled an appointment (optional)
    seen_by = 1 # int | Filter by the user for who have mark an appointment as seen (optional)
    rescheduled_count = 1 # int | Filter by the count of rescheduling (optional)
    done = True # bool | Filter by the done flag (optional)
    per_page = 10 # int | Count of records per page (optional)
    sort_by = "id" # str | Sort appointments by columns (optional)
    sort_dir = "asc" # str | Sort direction (optional)
    date_filter = "date" # str | Filtering appointments by a date range depends on this filter (optional)
    start_date = dateutil_parser('Tue Jan 01 00:00:00 UTC 2019').date() # date | Filter appointments by a date in format Y-m-d (optional)
    end_date = dateutil_parser('Wed Jan 02 00:00:00 UTC 2019').date() # date | Filter leads by a date in format Y-m-d (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get lead appointments
        api_response = api_instance.leads_lead_id_appointments_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_appointments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead appointments
        api_response = api_instance.leads_lead_id_appointments_get(lead_id, page=page, set_for=set_for, set_by=set_by, modified_by=modified_by, confirmed_by=confirmed_by, rescheduled_by=rescheduled_by, seen_by=seen_by, rescheduled_count=rescheduled_count, done=done, per_page=per_page, sort_by=sort_by, sort_dir=sort_dir, date_filter=date_filter, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_appointments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **set_for** | **int**| Filter by the user for who appointment was created | [optional]
 **set_by** | **int**| Filter by the user for who have created an appointment | [optional]
 **modified_by** | **int**| Filter by the user for who have modified an appointment | [optional]
 **confirmed_by** | **int**| Filter by the user for who have confirmed an appointment | [optional]
 **rescheduled_by** | **int**| Filter by the user for who have rescheduled an appointment | [optional]
 **seen_by** | **int**| Filter by the user for who have mark an appointment as seen | [optional]
 **rescheduled_count** | **int**| Filter by the count of rescheduling | [optional]
 **done** | **bool**| Filter by the done flag | [optional]
 **per_page** | **int**| Count of records per page | [optional]
 **sort_by** | **str**| Sort appointments by columns | [optional]
 **sort_dir** | **str**| Sort direction | [optional]
 **date_filter** | **str**| Filtering appointments by a date range depends on this filter | [optional]
 **start_date** | **date**| Filter appointments by a date in format Y-m-d | [optional]
 **end_date** | **date**| Filter leads by a date in format Y-m-d | [optional]

### Return type

[**LeadsLeadIdAppointmentsGet200Response**](LeadsLeadIdAppointmentsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of lead appointments |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_appointments_post**
> LeadsLeadIdAppointmentsGet200Response1 leads_lead_id_appointments_post(lead_id, leads_lead_id_appointments_get_request)

Create a lead appointment

Create a lead appointment

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_appointments_get200_response1 import LeadsLeadIdAppointmentsGet200Response1
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_appointments_get_request import LeadsLeadIdAppointmentsGetRequest
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    leads_lead_id_appointments_get_request = LeadsLeadIdAppointmentsGetRequest(
        date=dateutil_parser('2018-05-30T13:16:13Z'),
        date_end=dateutil_parser('2018-05-30T13:26:13Z'),
        text="text_example",
        set_by="1",
        set_for="1",
    ) # LeadsLeadIdAppointmentsGetRequest | Create a lead appointment

    # example passing only required values which don't have defaults set
    try:
        # Create a lead appointment
        api_response = api_instance.leads_lead_id_appointments_post(lead_id, leads_lead_id_appointments_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_appointments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **leads_lead_id_appointments_get_request** | [**LeadsLeadIdAppointmentsGetRequest**](LeadsLeadIdAppointmentsGetRequest.md)| Create a lead appointment |

### Return type

[**LeadsLeadIdAppointmentsGet200Response1**](LeadsLeadIdAppointmentsGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Appointment has been created successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_documents_document_id_get**
> file_type leads_lead_id_documents_document_id_get(lead_id, document_id)

Download a document

Download a document

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    document_id = 1 # int | Document Id

    # example passing only required values which don't have defaults set
    try:
        # Download a document
        api_response = api_instance.leads_lead_id_documents_document_id_get(lead_id, document_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_documents_document_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **document_id** | **int**| Document Id |

### Return type

**file_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_documents_get**
> LeadsLeadIdDocumentsGet200Response leads_lead_id_documents_get(lead_id)

Get a list of available documents

Get a list of available documents

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_documents_get200_response import LeadsLeadIdDocumentsGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of available documents
        api_response = api_instance.leads_lead_id_documents_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_documents_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available documents
        api_response = api_instance.leads_lead_id_documents_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_documents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdDocumentsGet200Response**](LeadsLeadIdDocumentsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available documents |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_documents_post**
> str leads_lead_id_documents_post(lead_id, tab, label, filename)

Upload a document

Upload a document

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    tab = 1 # int | Tab Id
    label = 1 # int | Label Id
    filename = "filename_example" # str | File name
    notify_users = "notify_users_example" # str | Comma separated list of user ids to notify or `all_assigned` to notify all users assigned to the lead (optional)
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a document
        api_response = api_instance.leads_lead_id_documents_post(lead_id, tab, label, filename)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_documents_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a document
        api_response = api_instance.leads_lead_id_documents_post(lead_id, tab, label, filename, notify_users=notify_users, body=body)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_documents_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **tab** | **int**| Tab Id |
 **label** | **int**| Label Id |
 **filename** | **str**| File name |
 **notify_users** | **str**| Comma separated list of user ids to notify or &#x60;all_assigned&#x60; to notify all users assigned to the lead | [optional]
 **body** | **file_type**|  | [optional]

### Return type

**str**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document has been uploaded successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_emails_template_id_post**
> LeadsLeadIdEmailsTemplateIdPost200Response leads_lead_id_emails_template_id_post(lead_id, template_id)

Send an email to lead with template

Send an email to lead with template

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_emails_template_id_post_request import LeadsLeadIdEmailsTemplateIdPostRequest
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_emails_template_id_post200_response import LeadsLeadIdEmailsTemplateIdPost200Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    template_id = 1 # int | Template Id
    leads_lead_id_emails_template_id_post_request = LeadsLeadIdEmailsTemplateIdPostRequest(None) # LeadsLeadIdEmailsTemplateIdPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an email to lead with template
        api_response = api_instance.leads_lead_id_emails_template_id_post(lead_id, template_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_emails_template_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email to lead with template
        api_response = api_instance.leads_lead_id_emails_template_id_post(lead_id, template_id, leads_lead_id_emails_template_id_post_request=leads_lead_id_emails_template_id_post_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_emails_template_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **template_id** | **int**| Template Id |
 **leads_lead_id_emails_template_id_post_request** | [**LeadsLeadIdEmailsTemplateIdPostRequest**](LeadsLeadIdEmailsTemplateIdPostRequest.md)|  | [optional]

### Return type

[**LeadsLeadIdEmailsTemplateIdPost200Response**](LeadsLeadIdEmailsTemplateIdPost200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of proccess |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_get**
> LeadsLeadIdGet200Response leads_lead_id_get(lead_id)

Get detailed lead information

Get detailed lead information. If field has a default value, the `uid` field will be `null`

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_lead_id_get200_response import LeadsLeadIdGet200Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id

    # example passing only required values which don't have defaults set
    try:
        # Get detailed lead information
        api_response = api_instance.leads_lead_id_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |

### Return type

[**LeadsLeadIdGet200Response**](LeadsLeadIdGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed lead information |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_mailbox_email_id_attachment_attachment_id_get**
> file_type leads_lead_id_mailbox_email_id_attachment_attachment_id_get(lead_id, email_id, attachment_id)

Download a mailbox email attachment

Download a mailbox email attachment

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    email_id = 1 # int | Email Id
    attachment_id = 1 # int | Attachment Id

    # example passing only required values which don't have defaults set
    try:
        # Download a mailbox email attachment
        api_response = api_instance.leads_lead_id_mailbox_email_id_attachment_attachment_id_get(lead_id, email_id, attachment_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_mailbox_email_id_attachment_attachment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **email_id** | **int**| Email Id |
 **attachment_id** | **int**| Attachment Id |

### Return type

**file_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_notes_get**
> LeadsLeadIdNotesGet200Response leads_lead_id_notes_get(lead_id)

Get lead notes

Get lead notes

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_notes_get200_response import LeadsLeadIdNotesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get lead notes
        api_response = api_instance.leads_lead_id_notes_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_notes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead notes
        api_response = api_instance.leads_lead_id_notes_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_notes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdNotesGet200Response**](LeadsLeadIdNotesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of lead notes |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_notes_post**
> LeadsLeadIdNotesGet200Response1 leads_lead_id_notes_post(lead_id, leads_lead_id_notes_get_request)

Create a lead note

Create a lead note

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_notes_get200_response1 import LeadsLeadIdNotesGet200Response1
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_notes_get_request import LeadsLeadIdNotesGetRequest
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    leads_lead_id_notes_get_request = LeadsLeadIdNotesGetRequest(
        tab=1,
        note="Test note",
        sticky="true",
        notify_users="1,2,3",
    ) # LeadsLeadIdNotesGetRequest | Create a lead note

    # example passing only required values which don't have defaults set
    try:
        # Create a lead note
        api_response = api_instance.leads_lead_id_notes_post(lead_id, leads_lead_id_notes_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_notes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **leads_lead_id_notes_get_request** | [**LeadsLeadIdNotesGetRequest**](LeadsLeadIdNotesGetRequest.md)| Create a lead note |

### Return type

[**LeadsLeadIdNotesGet200Response1**](LeadsLeadIdNotesGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note has been added successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_patch**
> LeadsLeadIdGet200Response1 leads_lead_id_patch(lead_id, leads_lead_id_get_request)

Update a lead

Update a lead

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_get200_response1 import LeadsLeadIdGet200Response1
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_get_request import LeadsLeadIdGetRequest
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    leads_lead_id_get_request = LeadsLeadIdGetRequest(
        campaign=1,
        status=1,
        source=1,
        group=1,
        fields=[
            LeadsGetRequestFieldsInner(
                id="1",
                record="1",
                value="Test",
            ),
        ],
    ) # LeadsLeadIdGetRequest | Lead changes (send only fields you want to change)

    # example passing only required values which don't have defaults set
    try:
        # Update a lead
        api_response = api_instance.leads_lead_id_patch(lead_id, leads_lead_id_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **leads_lead_id_get_request** | [**LeadsLeadIdGetRequest**](LeadsLeadIdGetRequest.md)| Lead changes (send only fields you want to change) |

### Return type

[**LeadsLeadIdGet200Response1**](LeadsLeadIdGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead has been updated successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_records_cat_id_record_id_delete**
> LeadsLeadIdRecordsCatIdRecordIdDelete200Response leads_lead_id_records_cat_id_record_id_delete(lead_id, cat_id, record_id)

Delete record from a lead record set

The method allows deleting records from lead tabs with the type \"set\". Values of `catId` and `recordId` can be obtained by request [Get detailed lead information](#/paths/~1leads~1{leadId}/get) (`details.id` = `catId`, `details.record` = `recordId`).

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_records_cat_id_record_id_delete200_response import LeadsLeadIdRecordsCatIdRecordIdDelete200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    cat_id = 1 # int | Record category ID
    record_id = 1 # int | Record ID

    # example passing only required values which don't have defaults set
    try:
        # Delete record from a lead record set
        api_response = api_instance.leads_lead_id_records_cat_id_record_id_delete(lead_id, cat_id, record_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_records_cat_id_record_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **cat_id** | **int**| Record category ID |
 **record_id** | **int**| Record ID |

### Return type

[**LeadsLeadIdRecordsCatIdRecordIdDelete200Response**](LeadsLeadIdRecordsCatIdRecordIdDelete200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The record has been deleted successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_sms_template_id_post**
> LeadsLeadIdSmsTemplateIdPost200Response leads_lead_id_sms_template_id_post(lead_id, template_id)

Send an SMS to lead with selected SMS template

Send an SMS to lead with selected SMS template.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_lead_id_sms_template_id_post_request import LeadsLeadIdSmsTemplateIdPostRequest
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_sms_template_id_post200_response import LeadsLeadIdSmsTemplateIdPost200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    template_id = 1 # int | Template Id
    leads_lead_id_sms_template_id_post_request = LeadsLeadIdSmsTemplateIdPostRequest(None) # LeadsLeadIdSmsTemplateIdPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an SMS to lead with selected SMS template
        api_response = api_instance.leads_lead_id_sms_template_id_post(lead_id, template_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_sms_template_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an SMS to lead with selected SMS template
        api_response = api_instance.leads_lead_id_sms_template_id_post(lead_id, template_id, leads_lead_id_sms_template_id_post_request=leads_lead_id_sms_template_id_post_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_sms_template_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **template_id** | **int**| Template Id |
 **leads_lead_id_sms_template_id_post_request** | [**LeadsLeadIdSmsTemplateIdPostRequest**](LeadsLeadIdSmsTemplateIdPostRequest.md)|  | [optional]

### Return type

[**LeadsLeadIdSmsTemplateIdPost200Response**](LeadsLeadIdSmsTemplateIdPost200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of proccess |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_tabs_tab_id_fields_get**
> LeadsLeadIdTabsTabIdFieldsGet200Response leads_lead_id_tabs_tab_id_fields_get(lead_id, tab_id)

Get lead information from a specific tab

Get lead information from a specific tab. If field has a default value, the `uid` field will be `null`

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_tabs_tab_id_fields_get200_response import LeadsLeadIdTabsTabIdFieldsGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    tab_id = 1 # int | Lead field tab Id

    # example passing only required values which don't have defaults set
    try:
        # Get lead information from a specific tab
        api_response = api_instance.leads_lead_id_tabs_tab_id_fields_get(lead_id, tab_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_tabs_tab_id_fields_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **tab_id** | **int**| Lead field tab Id |

### Return type

[**LeadsLeadIdTabsTabIdFieldsGet200Response**](LeadsLeadIdTabsTabIdFieldsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead information from a specific tab |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_tasks_get**
> LeadsLeadIdTasksGet200Response leads_lead_id_tasks_get(lead_id)

Get lead tasks

Get lead tasks

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_tasks_get200_response import LeadsLeadIdTasksGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get lead tasks
        api_response = api_instance.leads_lead_id_tasks_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_tasks_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get lead tasks
        api_response = api_instance.leads_lead_id_tasks_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_tasks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdTasksGet200Response**](LeadsLeadIdTasksGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of lead tasks |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_tasks_post**
> LeadsLeadIdTasksGet200Response1 leads_lead_id_tasks_post(lead_id, leads_lead_id_tasks_get_request)

Create a lead task

Create a lead task

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_tasks_get200_response1 import LeadsLeadIdTasksGet200Response1
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_tasks_get_request import LeadsLeadIdTasksGetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    leads_lead_id_tasks_get_request = LeadsLeadIdTasksGetRequest(
        priority="Normal",
        date="2018-05-30T13:16:13+00:00",
        date_end="2018-05-30T13:26:13+00:00",
        text="text_example",
        set_by="1",
        set_for="1",
    ) # LeadsLeadIdTasksGetRequest | Create a lead task

    # example passing only required values which don't have defaults set
    try:
        # Create a lead task
        api_response = api_instance.leads_lead_id_tasks_post(lead_id, leads_lead_id_tasks_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_tasks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **leads_lead_id_tasks_get_request** | [**LeadsLeadIdTasksGetRequest**](LeadsLeadIdTasksGetRequest.md)| Create a lead task |

### Return type

[**LeadsLeadIdTasksGet200Response1**](LeadsLeadIdTasksGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task has been created successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_users_get**
> LeadsLeadIdUsersGet200Response leads_lead_id_users_get(lead_id)

Get a list of assigned users

Get a list of assigned users

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_users_get200_response import LeadsLeadIdUsersGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of assigned users
        api_response = api_instance.leads_lead_id_users_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of assigned users
        api_response = api_instance.leads_lead_id_users_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdUsersGet200Response**](LeadsLeadIdUsersGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of assigned users |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_users_post**
> LeadsLeadIdUsersGet200Response1 leads_lead_id_users_post(lead_id, leads_lead_id_users_get_request)

Assign a user

Assign a user

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_users_get_request import LeadsLeadIdUsersGetRequest
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_users_get200_response1 import LeadsLeadIdUsersGet200Response1
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    leads_lead_id_users_get_request = LeadsLeadIdUsersGetRequest(None) # LeadsLeadIdUsersGetRequest | Create a lead task

    # example passing only required values which don't have defaults set
    try:
        # Assign a user
        api_response = api_instance.leads_lead_id_users_post(lead_id, leads_lead_id_users_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **leads_lead_id_users_get_request** | [**LeadsLeadIdUsersGetRequest**](LeadsLeadIdUsersGetRequest.md)| Create a lead task |

### Return type

[**LeadsLeadIdUsersGet200Response1**](LeadsLeadIdUsersGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User has been assigned successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_users_user_id_delete**
> LeadsLeadIdUsersUserIdDelete200Response leads_lead_id_users_user_id_delete(lead_id, user_id)

Unassign a user from a lead

Unassign a user from a lead

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_users_user_id_delete200_response import LeadsLeadIdUsersUserIdDelete200Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    lead_id = 1 # int | Lead Id
    user_id = 1 # int | User Id

    # example passing only required values which don't have defaults set
    try:
        # Unassign a user from a lead
        api_response = api_instance.leads_lead_id_users_user_id_delete(lead_id, user_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_lead_id_users_user_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **user_id** | **int**| User Id |

### Return type

[**LeadsLeadIdUsersUserIdDelete200Response**](LeadsLeadIdUsersUserIdDelete200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User has been unassigned successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_post**
> LeadsGet200Response1 leads_post(leads_get_request)

Create a lead

Create a lead

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get_request import LeadsGetRequest
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_get200_response1 import LeadsGet200Response1
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    leads_get_request = LeadsGetRequest(
        campaign=1,
        status=1,
        source=1,
        group=1,
        users=[1,2],
        users_emails=["aaa@example.com","bbb@example.com"],
        fields=[
            LeadsGetRequestFieldsInner(
                id="1",
                record="1",
                value="Test",
            ),
        ],
    ) # LeadsGetRequest | Lead details

    # example passing only required values which don't have defaults set
    try:
        # Create a lead
        api_response = api_instance.leads_post(leads_get_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leads_get_request** | [**LeadsGetRequest**](LeadsGetRequest.md)| Lead details |

### Return type

[**LeadsGet200Response1**](LeadsGet200Response1.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead has been created successfully |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_pricing_templates_get**
> LeadsPricingTemplatesGet200Response leads_pricing_templates_get()

Get pricing templates

Get pricing templates

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_pricing_templates_get200_response import LeadsPricingTemplatesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get pricing templates
        api_response = api_instance.leads_pricing_templates_get(page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_pricing_templates_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsPricingTemplatesGet200Response**](LeadsPricingTemplatesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of pricing templates |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_sms_templates_get**
> LeadsSmsTemplatesGet200Response leads_sms_templates_get()

Get list of SMS templates

Get list of available SMS templates for sending SMS to a lead

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_sms_templates_get200_response import LeadsSmsTemplatesGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of SMS templates
        api_response = api_instance.leads_sms_templates_get()
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_sms_templates_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LeadsSmsTemplatesGet200Response**](LeadsSmsTemplatesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available SMS templates |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_sources_get**
> LeadsSourcesGet200Response leads_sources_get()

Get a list of available sources

Get a list of available sources

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_sources_get200_response import LeadsSourcesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of available sources
        api_response = api_instance.leads_sources_get()
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_sources_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LeadsSourcesGet200Response**](LeadsSourcesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available sources |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_statuses_get**
> LeadsStatusesGet200Response leads_statuses_get()

Get a list of available statuses

Get a list of available statuses

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_statuses_get200_response import LeadsStatusesGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    group = 1 # int | Group Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available statuses
        api_response = api_instance.leads_statuses_get(group=group)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_statuses_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **int**| Group Id | [optional]

### Return type

[**LeadsStatusesGet200Response**](LeadsStatusesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available statuses |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_users_get**
> LeadsLeadIdUsersGet200Response leads_users_get()

Get a list of available users

Get a list of available users for assigning

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import leads_api
from iriscrm.model.leads_lead_id_users_get200_response import LeadsLeadIdUsersGet200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.mycoastalpay.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = iriscrm.Configuration(
    host = "https://www.mycoastalpay.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with iriscrm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available users
        api_response = api_instance.leads_users_get(page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling LeadsApi->leads_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdUsersGet200Response**](LeadsLeadIdUsersGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available users |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


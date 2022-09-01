# iriscrm
# Introduction
Welcome to Coastal Pay’s API!

The API is organized around `REST`. All requests should be made over `SSL`.

All request and response bodies, including errors, are encoded in `JSON`.
# Open API
The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls.
### You can use the E-Signature API to:
- [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post)
- [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)
- [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get)
- [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get)
- [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get)
- [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post)
- [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get)
- [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get)
- [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch)
- [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete)

### You can use the Lead API to:
- [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post)
- [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get)
- [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get)
- [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch)
- [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get)
- [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post)
- [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get)
- [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get)
- [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch)
- [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch)
- [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post)
- [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get)
- [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get)
- [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch)
- [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post)
- [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get)
- [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post)
- [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get)
- [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post)
- [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post)
- [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get)
- [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post)
- [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get)
- [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete)
- [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post)
- [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get)
- [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get)
- [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get)
- [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post)
- [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get)
- [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get)
- [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post)
- [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get)
- [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get)
- [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get)
- [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get)
- [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get)
- [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get)
- [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get)
- [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get)
- [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get)
- [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get)
- [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get)
- [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)

# Generate an API token
When you send an API request, you will need to include an API token in your request in order to authenticate your account.

The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.

To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.


# Using the API
Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.

`curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`

Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.

The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.

By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.

Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests.
# Using the Subscription API
API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.

To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.

All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.

To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:

<img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/>
# Authentication
Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.
# Errors
Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`.
# Limiting
You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status.
Headers description:
* `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period
* `X-RateLimit-Remaining` tells you how many requests you have left within this current time period
* `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/gossterrible/iris_python_sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gossterrible/iris_python_sdk.git`)

Then import the package:
```python
import iriscrm
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import iriscrm
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import iriscrm
from pprint import pprint
from iriscrm.api import e_signature_api
from iriscrm.model.application_field import ApplicationField
from iriscrm.model.brief_application_info import BriefApplicationInfo
from iriscrm.model.leads_applications_app_id_mappings_get200_response import LeadsApplicationsAppIdMappingsGet200Response
from iriscrm.model.leads_applications_app_id_mappings_map_id_delete200_response import LeadsApplicationsAppIdMappingsMapIdDelete200Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_get405_response import LeadsGet405Response
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_signatures_application_id_generate_post200_response import LeadsLeadIdSignaturesApplicationIdGeneratePost200Response
from iriscrm.model.leads_lead_id_signatures_application_id_generate_post_request import LeadsLeadIdSignaturesApplicationIdGeneratePostRequest
from iriscrm.model.leads_lead_id_signatures_application_id_send_post200_response import LeadsLeadIdSignaturesApplicationIdSendPost200Response
from iriscrm.model.leads_lead_id_signatures_application_id_send_post_request import LeadsLeadIdSignaturesApplicationIdSendPostRequest
from iriscrm.model.leads_lead_id_signatures_get200_response import LeadsLeadIdSignaturesGet200Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    try:
        # Get a list of available application field mappings
        api_response = api_instance.leads_applications_app_id_mappings_get(app_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://www.mycoastalpay.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ESignatureApi* | [**leads_applications_app_id_mappings_get**](docs/ESignatureApi.md#leads_applications_app_id_mappings_get) | **GET** /leads/applications/{appId}/mappings | Get a list of available application field mappings
*ESignatureApi* | [**leads_applications_app_id_mappings_map_id_delete**](docs/ESignatureApi.md#leads_applications_app_id_mappings_map_id_delete) | **DELETE** /leads/applications/{appId}/mappings/{mapId} | Delete an application field mapping
*ESignatureApi* | [**leads_applications_app_id_mappings_map_id_get**](docs/ESignatureApi.md#leads_applications_app_id_mappings_map_id_get) | **GET** /leads/applications/{appId}/mappings/{mapId} | Get an application field mapping list
*ESignatureApi* | [**leads_applications_app_id_mappings_map_id_patch**](docs/ESignatureApi.md#leads_applications_app_id_mappings_map_id_patch) | **PATCH** /leads/applications/{appId}/mappings/{mapId} | Update an application field mapping
*ESignatureApi* | [**leads_applications_app_id_mappings_post**](docs/ESignatureApi.md#leads_applications_app_id_mappings_post) | **POST** /leads/applications/{appId}/mappings | Create a new application field mapping
*ESignatureApi* | [**leads_applications_get**](docs/ESignatureApi.md#leads_applications_get) | **GET** /leads/applications | Get a list of available applications
*ESignatureApi* | [**leads_lead_id_signatures_application_id_generate_post**](docs/ESignatureApi.md#leads_lead_id_signatures_application_id_generate_post) | **POST** /leads/{leadId}/signatures/{applicationId}/generate | Generate an e-signature document
*ESignatureApi* | [**leads_lead_id_signatures_application_id_send_post**](docs/ESignatureApi.md#leads_lead_id_signatures_application_id_send_post) | **POST** /leads/{leadId}/signatures/{applicationId}/send | Send an e-signature document
*ESignatureApi* | [**leads_lead_id_signatures_get**](docs/ESignatureApi.md#leads_lead_id_signatures_get) | **GET** /leads/{leadId}/signatures | Get a list of all lead e-signatures documents
*ESignatureApi* | [**leads_signatures_application_id_download_get**](docs/ESignatureApi.md#leads_signatures_application_id_download_get) | **GET** /leads/signatures/{applicationId}/download | Download an e-signature document
*LeadsApi* | [**leads_campaigns_get**](docs/LeadsApi.md#leads_campaigns_get) | **GET** /leads/campaigns | Get a list of available campaigns
*LeadsApi* | [**leads_emails_templates_get**](docs/LeadsApi.md#leads_emails_templates_get) | **GET** /leads/emails/templates | Get a list of email templates
*LeadsApi* | [**leads_fields_field_id_get**](docs/LeadsApi.md#leads_fields_field_id_get) | **GET** /leads/fields/{fieldId} | Get a lead field
*LeadsApi* | [**leads_fields_field_id_order_patch**](docs/LeadsApi.md#leads_fields_field_id_order_patch) | **PATCH** /leads/fields/{fieldId}/order | Update a lead field order position
*LeadsApi* | [**leads_fields_field_id_patch**](docs/LeadsApi.md#leads_fields_field_id_patch) | **PATCH** /leads/fields/{fieldId} | Update a lead field
*LeadsApi* | [**leads_fields_get**](docs/LeadsApi.md#leads_fields_get) | **GET** /leads/fields | Get a list of available lead fields
*LeadsApi* | [**leads_fields_post**](docs/LeadsApi.md#leads_fields_post) | **POST** /leads/fields | Create a new lead field
*LeadsApi* | [**leads_fields_tabs_get**](docs/LeadsApi.md#leads_fields_tabs_get) | **GET** /leads/fields/tabs | Get a list of all lead field tabs
*LeadsApi* | [**leads_fields_tabs_post**](docs/LeadsApi.md#leads_fields_tabs_post) | **POST** /leads/fields/tabs | Create a lead field tab
*LeadsApi* | [**leads_fields_tabs_tab_id_get**](docs/LeadsApi.md#leads_fields_tabs_tab_id_get) | **GET** /leads/fields/tabs/{tabId} | Get a lead field tab
*LeadsApi* | [**leads_fields_tabs_tab_id_patch**](docs/LeadsApi.md#leads_fields_tabs_tab_id_patch) | **PATCH** /leads/fields/tabs/{tabId} | Update a lead field tab
*LeadsApi* | [**leads_file_labels_get**](docs/LeadsApi.md#leads_file_labels_get) | **GET** /leads/file_labels | Get a list of available document labels
*LeadsApi* | [**leads_get**](docs/LeadsApi.md#leads_get) | **GET** /leads | Get a list of leads
*LeadsApi* | [**leads_groups_get**](docs/LeadsApi.md#leads_groups_get) | **GET** /leads/groups | Get a list of available groups
*LeadsApi* | [**leads_lead_id_activity_campaign_get**](docs/LeadsApi.md#leads_lead_id_activity_campaign_get) | **GET** /leads/{leadId}/activity/campaign | Get a list of all lead campaign activity
*LeadsApi* | [**leads_lead_id_activity_deletion_get**](docs/LeadsApi.md#leads_lead_id_activity_deletion_get) | **GET** /leads/{leadId}/activity/deletion | Get a list of all lead deletion activity
*LeadsApi* | [**leads_lead_id_activity_duplicates_get**](docs/LeadsApi.md#leads_lead_id_activity_duplicates_get) | **GET** /leads/{leadId}/activity/duplicates | Get a list of all lead duplicate activity
*LeadsApi* | [**leads_lead_id_activity_links_get**](docs/LeadsApi.md#leads_lead_id_activity_links_get) | **GET** /leads/{leadId}/activity/links | Get a list of all lead links activity
*LeadsApi* | [**leads_lead_id_activity_source_get**](docs/LeadsApi.md#leads_lead_id_activity_source_get) | **GET** /leads/{leadId}/activity/source | Get a list of all lead source activity
*LeadsApi* | [**leads_lead_id_activity_status_get**](docs/LeadsApi.md#leads_lead_id_activity_status_get) | **GET** /leads/{leadId}/activity/status | Get a list of all lead status activity
*LeadsApi* | [**leads_lead_id_applications_application_id_populate_post**](docs/LeadsApi.md#leads_lead_id_applications_application_id_populate_post) | **POST** /leads/{leadId}/applications/{applicationId}/populate | Populate PDF Document
*LeadsApi* | [**leads_lead_id_appointments_get**](docs/LeadsApi.md#leads_lead_id_appointments_get) | **GET** /leads/{leadId}/appointments | Get lead appointments
*LeadsApi* | [**leads_lead_id_appointments_post**](docs/LeadsApi.md#leads_lead_id_appointments_post) | **POST** /leads/{leadId}/appointments | Create a lead appointment
*LeadsApi* | [**leads_lead_id_documents_document_id_get**](docs/LeadsApi.md#leads_lead_id_documents_document_id_get) | **GET** /leads/{leadId}/documents/{documentId} | Download a document
*LeadsApi* | [**leads_lead_id_documents_get**](docs/LeadsApi.md#leads_lead_id_documents_get) | **GET** /leads/{leadId}/documents | Get a list of available documents
*LeadsApi* | [**leads_lead_id_documents_post**](docs/LeadsApi.md#leads_lead_id_documents_post) | **POST** /leads/{leadId}/documents | Upload a document
*LeadsApi* | [**leads_lead_id_emails_template_id_post**](docs/LeadsApi.md#leads_lead_id_emails_template_id_post) | **POST** /leads/{leadId}/emails/{templateId} | Send an email to lead with template
*LeadsApi* | [**leads_lead_id_get**](docs/LeadsApi.md#leads_lead_id_get) | **GET** /leads/{leadId} | Get detailed lead information
*LeadsApi* | [**leads_lead_id_mailbox_email_id_attachment_attachment_id_get**](docs/LeadsApi.md#leads_lead_id_mailbox_email_id_attachment_attachment_id_get) | **GET** /leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId} | Download a mailbox email attachment
*LeadsApi* | [**leads_lead_id_notes_get**](docs/LeadsApi.md#leads_lead_id_notes_get) | **GET** /leads/{leadId}/notes | Get lead notes
*LeadsApi* | [**leads_lead_id_notes_post**](docs/LeadsApi.md#leads_lead_id_notes_post) | **POST** /leads/{leadId}/notes | Create a lead note
*LeadsApi* | [**leads_lead_id_patch**](docs/LeadsApi.md#leads_lead_id_patch) | **PATCH** /leads/{leadId} | Update a lead
*LeadsApi* | [**leads_lead_id_records_cat_id_record_id_delete**](docs/LeadsApi.md#leads_lead_id_records_cat_id_record_id_delete) | **DELETE** /leads/{leadId}/records/{catId}/{recordId} | Delete record from a lead record set
*LeadsApi* | [**leads_lead_id_sms_template_id_post**](docs/LeadsApi.md#leads_lead_id_sms_template_id_post) | **POST** /leads/{leadId}/sms/{templateId} | Send an SMS to lead with selected SMS template
*LeadsApi* | [**leads_lead_id_tabs_tab_id_fields_get**](docs/LeadsApi.md#leads_lead_id_tabs_tab_id_fields_get) | **GET** /leads/{leadId}/tabs/{tabId}/fields | Get lead information from a specific tab
*LeadsApi* | [**leads_lead_id_tasks_get**](docs/LeadsApi.md#leads_lead_id_tasks_get) | **GET** /leads/{leadId}/tasks | Get lead tasks
*LeadsApi* | [**leads_lead_id_tasks_post**](docs/LeadsApi.md#leads_lead_id_tasks_post) | **POST** /leads/{leadId}/tasks | Create a lead task
*LeadsApi* | [**leads_lead_id_users_get**](docs/LeadsApi.md#leads_lead_id_users_get) | **GET** /leads/{leadId}/users | Get a list of assigned users
*LeadsApi* | [**leads_lead_id_users_post**](docs/LeadsApi.md#leads_lead_id_users_post) | **POST** /leads/{leadId}/users | Assign a user
*LeadsApi* | [**leads_lead_id_users_user_id_delete**](docs/LeadsApi.md#leads_lead_id_users_user_id_delete) | **DELETE** /leads/{leadId}/users/{userId} | Unassign a user from a lead
*LeadsApi* | [**leads_post**](docs/LeadsApi.md#leads_post) | **POST** /leads | Create a lead
*LeadsApi* | [**leads_pricing_templates_get**](docs/LeadsApi.md#leads_pricing_templates_get) | **GET** /leads/pricing_templates | Get pricing templates
*LeadsApi* | [**leads_sms_templates_get**](docs/LeadsApi.md#leads_sms_templates_get) | **GET** /leads/sms/templates | Get list of SMS templates
*LeadsApi* | [**leads_sources_get**](docs/LeadsApi.md#leads_sources_get) | **GET** /leads/sources | Get a list of available sources
*LeadsApi* | [**leads_statuses_get**](docs/LeadsApi.md#leads_statuses_get) | **GET** /leads/statuses | Get a list of available statuses
*LeadsApi* | [**leads_users_get**](docs/LeadsApi.md#leads_users_get) | **GET** /leads/users | Get a list of available users


## Documentation For Models

 - [ApplicationField](docs/ApplicationField.md)
 - [ApplicationFieldInfoInner](docs/ApplicationFieldInfoInner.md)
 - [ApplicationFieldInfoInnerDuplicatesInner](docs/ApplicationFieldInfoInnerDuplicatesInner.md)
 - [BriefApplicationInfo](docs/BriefApplicationInfo.md)
 - [BriefCampaignInfo](docs/BriefCampaignInfo.md)
 - [BriefCategoryInfo](docs/BriefCategoryInfo.md)
 - [BriefEmailTemplate](docs/BriefEmailTemplate.md)
 - [BriefGroupInfo](docs/BriefGroupInfo.md)
 - [BriefLeadInfo](docs/BriefLeadInfo.md)
 - [BriefSmsTemplate](docs/BriefSmsTemplate.md)
 - [BriefSourceInfo](docs/BriefSourceInfo.md)
 - [BriefStatusInfo](docs/BriefStatusInfo.md)
 - [BriefTabInfo](docs/BriefTabInfo.md)
 - [BriefUserInfo](docs/BriefUserInfo.md)
 - [BriefUserInfoWithClass](docs/BriefUserInfoWithClass.md)
 - [CampaignActivity](docs/CampaignActivity.md)
 - [CategoryWithStatuses](docs/CategoryWithStatuses.md)
 - [DeletionActivity](docs/DeletionActivity.md)
 - [DuplicateActivity](docs/DuplicateActivity.md)
 - [FileLabel](docs/FileLabel.md)
 - [LeadAppointment](docs/LeadAppointment.md)
 - [LeadField](docs/LeadField.md)
 - [LeadFieldOptions](docs/LeadFieldOptions.md)
 - [LeadFieldOptionsCopy](docs/LeadFieldOptionsCopy.md)
 - [LeadFieldOptionsDropdown](docs/LeadFieldOptionsDropdown.md)
 - [LeadFieldOptionsZipcodeAutocomplete](docs/LeadFieldOptionsZipcodeAutocomplete.md)
 - [LeadFieldOrder](docs/LeadFieldOrder.md)
 - [LeadFieldTab](docs/LeadFieldTab.md)
 - [LeadFieldValue](docs/LeadFieldValue.md)
 - [LeadsApplicationsAppIdMappingsGet200Response](docs/LeadsApplicationsAppIdMappingsGet200Response.md)
 - [LeadsApplicationsAppIdMappingsMapIdDelete200Response](docs/LeadsApplicationsAppIdMappingsMapIdDelete200Response.md)
 - [LeadsCampaignsGet200Response](docs/LeadsCampaignsGet200Response.md)
 - [LeadsEmailsTemplatesGet200Response](docs/LeadsEmailsTemplatesGet200Response.md)
 - [LeadsFieldsFieldIdOrderPatch200Response](docs/LeadsFieldsFieldIdOrderPatch200Response.md)
 - [LeadsFieldsGet200Response](docs/LeadsFieldsGet200Response.md)
 - [LeadsFieldsGetRequest](docs/LeadsFieldsGetRequest.md)
 - [LeadsFieldsGetRequestAllOf](docs/LeadsFieldsGetRequestAllOf.md)
 - [LeadsFieldsTabsGet200Response](docs/LeadsFieldsTabsGet200Response.md)
 - [LeadsFileLabelsGet200Response](docs/LeadsFileLabelsGet200Response.md)
 - [LeadsGet200Response](docs/LeadsGet200Response.md)
 - [LeadsGet200Response1](docs/LeadsGet200Response1.md)
 - [LeadsGet401Response](docs/LeadsGet401Response.md)
 - [LeadsGet403Response](docs/LeadsGet403Response.md)
 - [LeadsGet405Response](docs/LeadsGet405Response.md)
 - [LeadsGetRequest](docs/LeadsGetRequest.md)
 - [LeadsGetRequestFieldsInner](docs/LeadsGetRequestFieldsInner.md)
 - [LeadsGroupsGet200Response](docs/LeadsGroupsGet200Response.md)
 - [LeadsLeadIdActivityCampaignGet200Response](docs/LeadsLeadIdActivityCampaignGet200Response.md)
 - [LeadsLeadIdActivityDeletionGet200Response](docs/LeadsLeadIdActivityDeletionGet200Response.md)
 - [LeadsLeadIdActivityDuplicatesGet200Response](docs/LeadsLeadIdActivityDuplicatesGet200Response.md)
 - [LeadsLeadIdActivityLinksGet200Response](docs/LeadsLeadIdActivityLinksGet200Response.md)
 - [LeadsLeadIdActivitySourceGet200Response](docs/LeadsLeadIdActivitySourceGet200Response.md)
 - [LeadsLeadIdActivityStatusGet200Response](docs/LeadsLeadIdActivityStatusGet200Response.md)
 - [LeadsLeadIdApplicationsApplicationIdPopulatePost200Response](docs/LeadsLeadIdApplicationsApplicationIdPopulatePost200Response.md)
 - [LeadsLeadIdApplicationsApplicationIdPopulatePost500Response](docs/LeadsLeadIdApplicationsApplicationIdPopulatePost500Response.md)
 - [LeadsLeadIdAppointmentsGet200Response](docs/LeadsLeadIdAppointmentsGet200Response.md)
 - [LeadsLeadIdAppointmentsGet200Response1](docs/LeadsLeadIdAppointmentsGet200Response1.md)
 - [LeadsLeadIdAppointmentsGetRequest](docs/LeadsLeadIdAppointmentsGetRequest.md)
 - [LeadsLeadIdDocumentsGet200Response](docs/LeadsLeadIdDocumentsGet200Response.md)
 - [LeadsLeadIdDocumentsGet200ResponseDataInner](docs/LeadsLeadIdDocumentsGet200ResponseDataInner.md)
 - [LeadsLeadIdDocumentsGet200ResponseDataInnerLabel](docs/LeadsLeadIdDocumentsGet200ResponseDataInnerLabel.md)
 - [LeadsLeadIdDocumentsGet200ResponseDataInnerTab](docs/LeadsLeadIdDocumentsGet200ResponseDataInnerTab.md)
 - [LeadsLeadIdEmailsTemplateIdPost200Response](docs/LeadsLeadIdEmailsTemplateIdPost200Response.md)
 - [LeadsLeadIdEmailsTemplateIdPostRequest](docs/LeadsLeadIdEmailsTemplateIdPostRequest.md)
 - [LeadsLeadIdEmailsTemplateIdPostRequestOneOf](docs/LeadsLeadIdEmailsTemplateIdPostRequestOneOf.md)
 - [LeadsLeadIdEmailsTemplateIdPostRequestOneOf1](docs/LeadsLeadIdEmailsTemplateIdPostRequestOneOf1.md)
 - [LeadsLeadIdGet200Response](docs/LeadsLeadIdGet200Response.md)
 - [LeadsLeadIdGet200Response1](docs/LeadsLeadIdGet200Response1.md)
 - [LeadsLeadIdGet200ResponseDetailsInner](docs/LeadsLeadIdGet200ResponseDetailsInner.md)
 - [LeadsLeadIdGet404Response](docs/LeadsLeadIdGet404Response.md)
 - [LeadsLeadIdGetRequest](docs/LeadsLeadIdGetRequest.md)
 - [LeadsLeadIdNotesGet200Response](docs/LeadsLeadIdNotesGet200Response.md)
 - [LeadsLeadIdNotesGet200Response1](docs/LeadsLeadIdNotesGet200Response1.md)
 - [LeadsLeadIdNotesGet200ResponseDataInner](docs/LeadsLeadIdNotesGet200ResponseDataInner.md)
 - [LeadsLeadIdNotesGetRequest](docs/LeadsLeadIdNotesGetRequest.md)
 - [LeadsLeadIdRecordsCatIdRecordIdDelete200Response](docs/LeadsLeadIdRecordsCatIdRecordIdDelete200Response.md)
 - [LeadsLeadIdSignaturesApplicationIdGeneratePost200Response](docs/LeadsLeadIdSignaturesApplicationIdGeneratePost200Response.md)
 - [LeadsLeadIdSignaturesApplicationIdGeneratePostRequest](docs/LeadsLeadIdSignaturesApplicationIdGeneratePostRequest.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPost200Response](docs/LeadsLeadIdSignaturesApplicationIdSendPost200Response.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequest](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequest.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInner](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInner.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf1](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf1.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf2](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf2.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf3](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf3.md)
 - [LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf4](docs/LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInnerAnyOf4.md)
 - [LeadsLeadIdSignaturesGet200Response](docs/LeadsLeadIdSignaturesGet200Response.md)
 - [LeadsLeadIdSignaturesGet200ResponseDataInner](docs/LeadsLeadIdSignaturesGet200ResponseDataInner.md)
 - [LeadsLeadIdSmsTemplateIdPost200Response](docs/LeadsLeadIdSmsTemplateIdPost200Response.md)
 - [LeadsLeadIdSmsTemplateIdPostRequest](docs/LeadsLeadIdSmsTemplateIdPostRequest.md)
 - [LeadsLeadIdSmsTemplateIdPostRequestOneOf](docs/LeadsLeadIdSmsTemplateIdPostRequestOneOf.md)
 - [LeadsLeadIdSmsTemplateIdPostRequestOneOf1](docs/LeadsLeadIdSmsTemplateIdPostRequestOneOf1.md)
 - [LeadsLeadIdTabsTabIdFieldsGet200Response](docs/LeadsLeadIdTabsTabIdFieldsGet200Response.md)
 - [LeadsLeadIdTasksGet200Response](docs/LeadsLeadIdTasksGet200Response.md)
 - [LeadsLeadIdTasksGet200Response1](docs/LeadsLeadIdTasksGet200Response1.md)
 - [LeadsLeadIdTasksGet200ResponseDataInner](docs/LeadsLeadIdTasksGet200ResponseDataInner.md)
 - [LeadsLeadIdTasksGetRequest](docs/LeadsLeadIdTasksGetRequest.md)
 - [LeadsLeadIdUsersGet200Response](docs/LeadsLeadIdUsersGet200Response.md)
 - [LeadsLeadIdUsersGet200Response1](docs/LeadsLeadIdUsersGet200Response1.md)
 - [LeadsLeadIdUsersGetRequest](docs/LeadsLeadIdUsersGetRequest.md)
 - [LeadsLeadIdUsersGetRequestOneOf](docs/LeadsLeadIdUsersGetRequestOneOf.md)
 - [LeadsLeadIdUsersGetRequestOneOf1](docs/LeadsLeadIdUsersGetRequestOneOf1.md)
 - [LeadsLeadIdUsersUserIdDelete200Response](docs/LeadsLeadIdUsersUserIdDelete200Response.md)
 - [LeadsPricingTemplatesGet200Response](docs/LeadsPricingTemplatesGet200Response.md)
 - [LeadsPricingTemplatesGet200ResponseDataInner](docs/LeadsPricingTemplatesGet200ResponseDataInner.md)
 - [LeadsPricingTemplatesGet200ResponseDataInnerValuesInner](docs/LeadsPricingTemplatesGet200ResponseDataInnerValuesInner.md)
 - [LeadsSmsTemplatesGet200Response](docs/LeadsSmsTemplatesGet200Response.md)
 - [LeadsSourcesGet200Response](docs/LeadsSourcesGet200Response.md)
 - [LeadsStatusesGet200Response](docs/LeadsStatusesGet200Response.md)
 - [Links](docs/Links.md)
 - [LinksActivity](docs/LinksActivity.md)
 - [Meta](docs/Meta.md)
 - [SourceActivity](docs/SourceActivity.md)
 - [StatusActivity](docs/StatusActivity.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

helpdesk@coastalpay.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in iriscrm.apis and iriscrm.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from iriscrm.api.default_api import DefaultApi`
- `from iriscrm.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import iriscrm
from iriscrm.apis import *
from iriscrm.models import *
```


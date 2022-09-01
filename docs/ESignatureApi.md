# iriscrm.ESignatureApi

All URIs are relative to *https://www.mycoastalpay.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_applications_app_id_mappings_get**](ESignatureApi.md#leads_applications_app_id_mappings_get) | **GET** /leads/applications/{appId}/mappings | Get a list of available application field mappings
[**leads_applications_app_id_mappings_map_id_delete**](ESignatureApi.md#leads_applications_app_id_mappings_map_id_delete) | **DELETE** /leads/applications/{appId}/mappings/{mapId} | Delete an application field mapping
[**leads_applications_app_id_mappings_map_id_get**](ESignatureApi.md#leads_applications_app_id_mappings_map_id_get) | **GET** /leads/applications/{appId}/mappings/{mapId} | Get an application field mapping list
[**leads_applications_app_id_mappings_map_id_patch**](ESignatureApi.md#leads_applications_app_id_mappings_map_id_patch) | **PATCH** /leads/applications/{appId}/mappings/{mapId} | Update an application field mapping
[**leads_applications_app_id_mappings_post**](ESignatureApi.md#leads_applications_app_id_mappings_post) | **POST** /leads/applications/{appId}/mappings | Create a new application field mapping
[**leads_applications_get**](ESignatureApi.md#leads_applications_get) | **GET** /leads/applications | Get a list of available applications
[**leads_lead_id_signatures_application_id_generate_post**](ESignatureApi.md#leads_lead_id_signatures_application_id_generate_post) | **POST** /leads/{leadId}/signatures/{applicationId}/generate | Generate an e-signature document
[**leads_lead_id_signatures_application_id_send_post**](ESignatureApi.md#leads_lead_id_signatures_application_id_send_post) | **POST** /leads/{leadId}/signatures/{applicationId}/send | Send an e-signature document
[**leads_lead_id_signatures_get**](ESignatureApi.md#leads_lead_id_signatures_get) | **GET** /leads/{leadId}/signatures | Get a list of all lead e-signatures documents
[**leads_signatures_application_id_download_get**](ESignatureApi.md#leads_signatures_application_id_download_get) | **GET** /leads/signatures/{applicationId}/download | Download an e-signature document


# **leads_applications_app_id_mappings_get**
> LeadsApplicationsAppIdMappingsGet200Response leads_applications_app_id_mappings_get(app_id)

Get a list of available application field mappings

Get a list of available application field mappings

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_applications_app_id_mappings_get200_response import LeadsApplicationsAppIdMappingsGet200Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of available application field mappings
        api_response = api_instance.leads_applications_app_id_mappings_get(app_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of available application field mappings
        api_response = api_instance.leads_applications_app_id_mappings_get(app_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsApplicationsAppIdMappingsGet200Response**](LeadsApplicationsAppIdMappingsGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available application field mappings |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_applications_app_id_mappings_map_id_delete**
> LeadsApplicationsAppIdMappingsMapIdDelete200Response leads_applications_app_id_mappings_map_id_delete(app_id, map_id)

Delete an application field mapping

Deletion of application field mapping

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_applications_app_id_mappings_map_id_delete200_response import LeadsApplicationsAppIdMappingsMapIdDelete200Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    map_id = 1 # int | Mapping Id

    # example passing only required values which don't have defaults set
    try:
        # Delete an application field mapping
        api_response = api_instance.leads_applications_app_id_mappings_map_id_delete(app_id, map_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_map_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application Id |
 **map_id** | **int**| Mapping Id |

### Return type

[**LeadsApplicationsAppIdMappingsMapIdDelete200Response**](LeadsApplicationsAppIdMappingsMapIdDelete200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated application field mapping |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_applications_app_id_mappings_map_id_get**
> ApplicationField leads_applications_app_id_mappings_map_id_get(app_id, map_id)

Get an application field mapping list

Get an application field mapping list

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.application_field import ApplicationField
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    map_id = 1 # int | Mapping Id

    # example passing only required values which don't have defaults set
    try:
        # Get an application field mapping list
        api_response = api_instance.leads_applications_app_id_mappings_map_id_get(app_id, map_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_map_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application Id |
 **map_id** | **int**| Mapping Id |

### Return type

[**ApplicationField**](ApplicationField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application field mapping |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_applications_app_id_mappings_map_id_patch**
> ApplicationField leads_applications_app_id_mappings_map_id_patch(app_id, map_id)

Update an application field mapping

Update an application field mapping

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.application_field import ApplicationField
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    map_id = 1 # int | Mapping Id
    application_field = ApplicationField(
        _from=1,
        record=1,
        to="Test",
        to_alt="Alt test",
        to_type="Text",
        special="chk",
    ) # ApplicationField |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an application field mapping
        api_response = api_instance.leads_applications_app_id_mappings_map_id_patch(app_id, map_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_map_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an application field mapping
        api_response = api_instance.leads_applications_app_id_mappings_map_id_patch(app_id, map_id, application_field=application_field)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_map_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application Id |
 **map_id** | **int**| Mapping Id |
 **application_field** | [**ApplicationField**](ApplicationField.md)|  | [optional]

### Return type

[**ApplicationField**](ApplicationField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated application field mapping |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_applications_app_id_mappings_post**
> ApplicationField leads_applications_app_id_mappings_post(app_id)

Create a new application field mapping

Creation of new application field mapping

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.application_field import ApplicationField
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    app_id = 1 # int | Application Id
    application_field = ApplicationField(
        _from=1,
        record=1,
        to="Test",
        to_alt="Alt test",
        to_type="Text",
        special="chk",
    ) # ApplicationField |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new application field mapping
        api_response = api_instance.leads_applications_app_id_mappings_post(app_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new application field mapping
        api_response = api_instance.leads_applications_app_id_mappings_post(app_id, application_field=application_field)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_app_id_mappings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Application Id |
 **application_field** | [**ApplicationField**](ApplicationField.md)|  | [optional]

### Return type

[**ApplicationField**](ApplicationField.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created new application field mapping |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_applications_get**
> [BriefApplicationInfo] leads_applications_get()

Get a list of available applications

Get a list of available applications

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.brief_application_info import BriefApplicationInfo
from iriscrm.model.leads_get401_response import LeadsGet401Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of available applications
        api_response = api_instance.leads_applications_get()
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_applications_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[BriefApplicationInfo]**](BriefApplicationInfo.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available applications |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_signatures_application_id_generate_post**
> LeadsLeadIdSignaturesApplicationIdGeneratePost200Response leads_lead_id_signatures_application_id_generate_post(lead_id, application_id)

Generate an e-signature document

Generate a new electronic signature document and receive a signature-ready application URL.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_lead_id_signatures_application_id_generate_post200_response import LeadsLeadIdSignaturesApplicationIdGeneratePost200Response
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_signatures_application_id_generate_post_request import LeadsLeadIdSignaturesApplicationIdGeneratePostRequest
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    lead_id = 1 # int | Lead Id
    application_id = 1 # int | Application Id
    leads_lead_id_signatures_application_id_generate_post_request = LeadsLeadIdSignaturesApplicationIdGeneratePostRequest(
        expire=True,
    ) # LeadsLeadIdSignaturesApplicationIdGeneratePostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate an e-signature document
        api_response = api_instance.leads_lead_id_signatures_application_id_generate_post(lead_id, application_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_application_id_generate_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate an e-signature document
        api_response = api_instance.leads_lead_id_signatures_application_id_generate_post(lead_id, application_id, leads_lead_id_signatures_application_id_generate_post_request=leads_lead_id_signatures_application_id_generate_post_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_application_id_generate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **application_id** | **int**| Application Id |
 **leads_lead_id_signatures_application_id_generate_post_request** | [**LeadsLeadIdSignaturesApplicationIdGeneratePostRequest**](LeadsLeadIdSignaturesApplicationIdGeneratePostRequest.md)|  | [optional]

### Return type

[**LeadsLeadIdSignaturesApplicationIdGeneratePost200Response**](LeadsLeadIdSignaturesApplicationIdGeneratePost200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New E-Sign application hash and link to signature |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_signatures_application_id_send_post**
> LeadsLeadIdSignaturesApplicationIdSendPost200Response leads_lead_id_signatures_application_id_send_post(lead_id, application_id)

Send an e-signature document

Send an e-signature document using an email template for signature.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_lead_id_signatures_application_id_send_post_request import LeadsLeadIdSignaturesApplicationIdSendPostRequest
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
from iriscrm.model.leads_get401_response import LeadsGet401Response
from iriscrm.model.leads_get403_response import LeadsGet403Response
from iriscrm.model.leads_lead_id_get404_response import LeadsLeadIdGet404Response
from iriscrm.model.leads_lead_id_signatures_application_id_send_post200_response import LeadsLeadIdSignaturesApplicationIdSendPost200Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    lead_id = 1 # int | Lead Id
    application_id = 1 # int | Application Id
    leads_lead_id_signatures_application_id_send_post_request = LeadsLeadIdSignaturesApplicationIdSendPostRequest(
        recipients=[
            LeadsLeadIdSignaturesApplicationIdSendPostRequestRecipientsInner(None),
        ],
        expire=True,
    ) # LeadsLeadIdSignaturesApplicationIdSendPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an e-signature document
        api_response = api_instance.leads_lead_id_signatures_application_id_send_post(lead_id, application_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_application_id_send_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an e-signature document
        api_response = api_instance.leads_lead_id_signatures_application_id_send_post(lead_id, application_id, leads_lead_id_signatures_application_id_send_post_request=leads_lead_id_signatures_application_id_send_post_request)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_application_id_send_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **application_id** | **int**| Application Id |
 **leads_lead_id_signatures_application_id_send_post_request** | [**LeadsLeadIdSignaturesApplicationIdSendPostRequest**](LeadsLeadIdSignaturesApplicationIdSendPostRequest.md)|  | [optional]

### Return type

[**LeadsLeadIdSignaturesApplicationIdSendPost200Response**](LeadsLeadIdSignaturesApplicationIdSendPost200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New E-Sign application hash and link to signature |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_lead_id_signatures_get**
> LeadsLeadIdSignaturesGet200Response leads_lead_id_signatures_get(lead_id)

Get a list of all lead e-signatures documents

Get a list of all lead e-signatures documents

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_lead_id_signatures_get200_response import LeadsLeadIdSignaturesGet200Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    lead_id = 1 # int | Lead Id
    page = 1 # int | Page number (optional)
    per_page = 10 # int | Count of records per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all lead e-signatures documents
        api_response = api_instance.leads_lead_id_signatures_get(lead_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all lead e-signatures documents
        api_response = api_instance.leads_lead_id_signatures_get(lead_id, page=page, per_page=per_page)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_lead_id_signatures_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_id** | **int**| Lead Id |
 **page** | **int**| Page number | [optional]
 **per_page** | **int**| Count of records per page | [optional]

### Return type

[**LeadsLeadIdSignaturesGet200Response**](LeadsLeadIdSignaturesGet200Response.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list with all lead e-signatures |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leads_signatures_application_id_download_get**
> file_type leads_signatures_application_id_download_get(application_id)

Download an e-signature document

Download an e-signature document.

### Example

* Api Key Authentication (Token):

```python
import time
import iriscrm
from iriscrm.api import e_signature_api
from iriscrm.model.leads_lead_id_applications_application_id_populate_post500_response import LeadsLeadIdApplicationsApplicationIdPopulatePost500Response
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
    api_instance = e_signature_api.ESignatureApi(api_client)
    application_id = 1 # int | Application Id

    # example passing only required values which don't have defaults set
    try:
        # Download an e-signature document
        api_response = api_instance.leads_signatures_application_id_download_get(application_id)
        pprint(api_response)
    except iriscrm.ApiException as e:
        print("Exception when calling ESignatureApi->leads_signatures_application_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **int**| Application Id |

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
**200** | E-Sign document |  -  |
**401** | API key is missing or invalid |  -  |
**403** | Not enough permissions |  -  |
**404** | Resource not found |  -  |
**405** | Validation exception |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


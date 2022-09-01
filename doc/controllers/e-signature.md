# E-Signature

Connect with the E-Signature API to create workflows that send specific documents for e-signature documents.<br/><br/>Create field mappings between Lead fields to populate their respective PDF documents.<br/><br/>Receive notifications when documents are generated, opened, and signed by recipients.

```python
e_signature_controller = client.e_signature
```

## Class Name

`ESignatureController`

## Methods

* [Generate an E-Signature Document](../../doc/controllers/e-signature.md#generate-an-e-signature-document)
* [Send an E-Signature Document](../../doc/controllers/e-signature.md#send-an-e-signature-document)
* [Download an E-Signature Document](../../doc/controllers/e-signature.md#download-an-e-signature-document)
* [Get a List of All Lead E-Signatures Documents](../../doc/controllers/e-signature.md#get-a-list-of-all-lead-e-signatures-documents)
* [Get a List of Available Applications](../../doc/controllers/e-signature.md#get-a-list-of-available-applications)
* [Create a New Application Field Mapping](../../doc/controllers/e-signature.md#create-a-new-application-field-mapping)
* [Get a List of Available Application Field Mappings](../../doc/controllers/e-signature.md#get-a-list-of-available-application-field-mappings)
* [Get an Application Field Mapping List](../../doc/controllers/e-signature.md#get-an-application-field-mapping-list)
* [Update an Application Field Mapping](../../doc/controllers/e-signature.md#update-an-application-field-mapping)
* [Delete an Application Field Mapping](../../doc/controllers/e-signature.md#delete-an-application-field-mapping)


# Generate an E-Signature Document

Generate a new electronic signature document and receive a signature-ready application URL.

```python
def generate_an_e_signature_document(self,
                                    lead_id,
                                    application_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `application_id` | `int` | Template, Required | Application Id |
| `body` | [`LeadsSignaturesGenerateRequest`](../../doc/models/leads-signatures-generate-request.md) | Body, Optional | - |

## Response Type

[`LeadsSignaturesGenerateResponse`](../../doc/models/leads-signatures-generate-response.md)

## Example Usage

```python
lead_id = 218
application_id = 164

result = e_signature_controller.generate_an_e_signature_document(lead_id, application_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |
| 500 | Unexpected server error | [`ServerErrorException`](../../doc/models/server-error-exception.md) |


# Send an E-Signature Document

Send an e-signature document using an email template for signature.

```python
def send_an_e_signature_document(self,
                                lead_id,
                                application_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `application_id` | `int` | Template, Required | Application Id |
| `body` | [`LeadsSignaturesSendRequest`](../../doc/models/leads-signatures-send-request.md) | Body, Optional | - |

## Response Type

[`LeadsSignaturesSendResponse`](../../doc/models/leads-signatures-send-response.md)

## Example Usage

```python
lead_id = 218
application_id = 164

result = e_signature_controller.send_an_e_signature_document(lead_id, application_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |
| 500 | Unexpected server error | [`ServerErrorException`](../../doc/models/server-error-exception.md) |


# Download an E-Signature Document

Download an e-signature document.

```python
def download_an_e_signature_document(self,
                                    application_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_id` | `int` | Template, Required | Application Id |

## Response Type

`binary`

## Example Usage

```python
application_id = 164

result = e_signature_controller.download_an_e_signature_document(application_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |
| 500 | Unexpected server error | [`ServerErrorException`](../../doc/models/server-error-exception.md) |


# Get a List of All Lead E-Signatures Documents

Get a list of all lead e-signatures documents

```python
def get_a_list_of_all_lead_e_signatures_documents(self,
                                                 lead_id,
                                                 page=None,
                                                 per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPageEnum`](../../doc/models/per-page-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsSignaturesResponse`](../../doc/models/leads-signatures-response.md)

## Example Usage

```python
lead_id = 218

result = e_signature_controller.get_a_list_of_all_lead_e_signatures_documents(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Get a List of Available Applications

Get a list of available applications

```python
def get_a_list_of_available_applications(self)
```

## Response Type

[`List of BriefApplicationInfo`](../../doc/models/brief-application-info.md)

## Example Usage

```python
result = e_signature_controller.get_a_list_of_available_applications()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Create a New Application Field Mapping

Creation of new application field mapping

```python
def create_a_new_application_field_mapping(self,
                                          app_id,
                                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `int` | Template, Required | Application Id |
| `body` | [`ApplicationField`](../../doc/models/application-field.md) | Body, Optional | - |

## Response Type

[`ApplicationField`](../../doc/models/application-field.md)

## Example Usage

```python
app_id = 26
body = ApplicationField()
body.mfrom = 1

result = e_signature_controller.create_a_new_application_field_mapping(app_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Available Application Field Mappings

Get a list of available application field mappings

```python
def get_a_list_of_available_application_field_mappings(self,
                                                      app_id,
                                                      page=None,
                                                      per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `int` | Template, Required | Application Id |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPageEnum`](../../doc/models/per-page-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsApplicationsMappingsResponse`](../../doc/models/leads-applications-mappings-response.md)

## Example Usage

```python
app_id = 26

result = e_signature_controller.get_a_list_of_available_application_field_mappings(app_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get an Application Field Mapping List

Get an application field mapping list

```python
def get_an_application_field_mapping_list(self,
                                         app_id,
                                         map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `int` | Template, Required | Application Id |
| `map_id` | `int` | Template, Required | Mapping Id |

## Response Type

[`ApplicationField`](../../doc/models/application-field.md)

## Example Usage

```python
app_id = 26
map_id = 18

result = e_signature_controller.get_an_application_field_mapping_list(app_id, map_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Update an Application Field Mapping

Update an application field mapping

```python
def update_an_application_field_mapping(self,
                                       app_id,
                                       map_id,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `int` | Template, Required | Application Id |
| `map_id` | `int` | Template, Required | Mapping Id |
| `body` | [`ApplicationField`](../../doc/models/application-field.md) | Body, Optional | - |

## Response Type

[`ApplicationField`](../../doc/models/application-field.md)

## Example Usage

```python
app_id = 26
map_id = 18
body = ApplicationField()
body.mfrom = 1

result = e_signature_controller.update_an_application_field_mapping(app_id, map_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Delete an Application Field Mapping

Deletion of application field mapping

```python
def delete_an_application_field_mapping(self,
                                       app_id,
                                       map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `int` | Template, Required | Application Id |
| `map_id` | `int` | Template, Required | Mapping Id |

## Response Type

[`LeadsApplicationsMappingsResponse1`](../../doc/models/leads-applications-mappings-response-1.md)

## Example Usage

```python
app_id = 26
map_id = 18

result = e_signature_controller.delete_an_application_field_mapping(app_id, map_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


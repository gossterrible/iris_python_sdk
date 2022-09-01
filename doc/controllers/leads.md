# Leads

Connect with the Leads API to interact with your lead data.  Includes management of fields, user assignments, status changes, tasks, appointments, email, text messaging, and document attachments.<br/><br/>Create custom reports without limits using the data already housed within your CRM.

```python
leads_controller = client.leads
```

## Class Name

`LeadsController`

## Methods

* [Create a Lead](../../doc/controllers/leads.md#create-a-lead)
* [Get a List of Leads](../../doc/controllers/leads.md#get-a-list-of-leads)
* [Get Detailed Lead Information](../../doc/controllers/leads.md#get-detailed-lead-information)
* [Update a Lead](../../doc/controllers/leads.md#update-a-lead)
* [Get Lead Information From a Specific Tab](../../doc/controllers/leads.md#get-lead-information-from-a-specific-tab)
* [Delete Record From a Lead Record Set](../../doc/controllers/leads.md#delete-record-from-a-lead-record-set)
* [Create a New Lead Field](../../doc/controllers/leads.md#create-a-new-lead-field)
* [Get a List of Available Lead Fields](../../doc/controllers/leads.md#get-a-list-of-available-lead-fields)
* [Get a Lead Field](../../doc/controllers/leads.md#get-a-lead-field)
* [Update a Lead Field](../../doc/controllers/leads.md#update-a-lead-field)
* [Update a Lead Field Order Position](../../doc/controllers/leads.md#update-a-lead-field-order-position)
* [Create a Lead Field Tab](../../doc/controllers/leads.md#create-a-lead-field-tab)
* [Get a List of All Lead Field Tabs](../../doc/controllers/leads.md#get-a-list-of-all-lead-field-tabs)
* [Get a Lead Field Tab](../../doc/controllers/leads.md#get-a-lead-field-tab)
* [Update a Lead Field Tab](../../doc/controllers/leads.md#update-a-lead-field-tab)
* [Get Pricing Templates](../../doc/controllers/leads.md#get-pricing-templates)
* [Create a Lead Note](../../doc/controllers/leads.md#create-a-lead-note)
* [Get Lead Notes](../../doc/controllers/leads.md#get-lead-notes)
* [Create a Lead Appointment](../../doc/controllers/leads.md#create-a-lead-appointment)
* [Get Lead Appointments](../../doc/controllers/leads.md#get-lead-appointments)
* [Populate PDF Document](../../doc/controllers/leads.md#populate-pdf-document)
* [Create a Lead Task](../../doc/controllers/leads.md#create-a-lead-task)
* [Get Lead Tasks](../../doc/controllers/leads.md#get-lead-tasks)
* [Assign a User](../../doc/controllers/leads.md#assign-a-user)
* [Get a List of Assigned Users](../../doc/controllers/leads.md#get-a-list-of-assigned-users)
* [Unassign a User From a Lead](../../doc/controllers/leads.md#unassign-a-user-from-a-lead)
* [Upload a Document](../../doc/controllers/leads.md#upload-a-document)
* [Get a List of Available Documents](../../doc/controllers/leads.md#get-a-list-of-available-documents)
* [Get a List of Available Document Labels](../../doc/controllers/leads.md#get-a-list-of-available-document-labels)
* [Download a Document](../../doc/controllers/leads.md#download-a-document)
* [Send an Email to Lead With Template](../../doc/controllers/leads.md#send-an-email-to-lead-with-template)
* [Get a List of Email Templates](../../doc/controllers/leads.md#get-a-list-of-email-templates)
* [Download a Mailbox Email Attachment](../../doc/controllers/leads.md#download-a-mailbox-email-attachment)
* [Send an SMS to Lead With Selected SMS Template](../../doc/controllers/leads.md#send-an-sms-to-lead-with-selected-sms-template)
* [Get List of SMS Templates](../../doc/controllers/leads.md#get-list-of-sms-templates)
* [Get a List of All Lead Campaign Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-campaign-activity)
* [Get a List of All Lead Deletion Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-deletion-activity)
* [Get a List of All Lead Duplicate Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-duplicate-activity)
* [Get a List of All Lead Links Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-links-activity)
* [Get a List of All Lead Source Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-source-activity)
* [Get a List of All Lead Status Activity](../../doc/controllers/leads.md#get-a-list-of-all-lead-status-activity)
* [Get a List of Available Campaigns](../../doc/controllers/leads.md#get-a-list-of-available-campaigns)
* [Get a List of Available Groups](../../doc/controllers/leads.md#get-a-list-of-available-groups)
* [Get a List of Available Sources](../../doc/controllers/leads.md#get-a-list-of-available-sources)
* [Get a List of Available Statuses](../../doc/controllers/leads.md#get-a-list-of-available-statuses)
* [Get a List of Available Users](../../doc/controllers/leads.md#get-a-list-of-available-users)


# Create a Lead

Create a lead

```python
def create_a_lead(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsRequest`](../../doc/models/leads-request.md) | Body, Required | Lead details |

## Response Type

[`LeadsResponse`](../../doc/models/leads-response.md)

## Example Usage

```python
body = LeadsRequest()
body.status = 1
body.fields = []

body.fields.append(Field())
body.fields[0].id = '1'
body.fields[0].value = 'Test'

body.fields.append(Field())
body.fields[1].id = '1'
body.fields[1].value = 'Test'

body.fields.append(Field())
body.fields[2].id = '1'
body.fields[2].value = 'Test'


result = leads_controller.create_a_lead(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Leads

Get a list of leads

```python
def get_a_list_of_leads(self,
                       page=None,
                       per_page=None,
                       sort_by=None,
                       sort_dir='asc',
                       group=None,
                       mid=None,
                       campaign=None,
                       source=None,
                       status=None,
                       category=None,
                       user=None,
                       date_filter=None,
                       start_date=None,
                       end_date=None,
                       email=None,
                       fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPageEnum`](../../doc/models/per-page-enum.md) | Query, Optional | Count of records per page |
| `sort_by` | [`SortByEnum`](../../doc/models/sort-by-enum.md) | Query, Optional | Sorting of leads by the field value |
| `sort_dir` | [`SortDirEnum`](../../doc/models/sort-dir-enum.md) | Query, Optional | Direction of sorting<br>**Default**: `'asc'` |
| `group` | `int` | Query, Optional | Filter leads by a group id |
| `mid` | `int` | Query, Optional | Filter leads by a merchant id |
| `campaign` | `int` | Query, Optional | Filter leads by a campaign id |
| `source` | `int` | Query, Optional | Filter leads by a source id |
| `status` | `int` | Query, Optional | Filter leads by a status id |
| `category` | `int` | Query, Optional | Filter leads by a status category id |
| `user` | `int` | Query, Optional | Filter leads by a user id |
| `date_filter` | [`DateFilterEnum`](../../doc/models/date-filter-enum.md) | Query, Optional | Filtering leads by a date range depends on this filter |
| `start_date` | `datetime` | Query, Optional | Filter leads by a date in ISO 8601 format (Y-m-d\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**) |
| `end_date` | `datetime` | Query, Optional | Filter leads by a date in ISO 8601 format (Y-m-d\TH:i:sP) (**Please note that `+` sign should be encoded to `%2B`**) |
| `email` | `string` | Query, Optional | Filter leads by using an email address |
| `fields` | `string` | Query, Optional | Filter leads by searching any lead field values. Search multiple values as an AND operation. |

## Response Type

[`LeadsResponse1`](../../doc/models/leads-response-1.md)

## Example Usage

```python
sort_dir = SortDirEnum.ASC
start_date = dateutil.parser.parse('01/01/2019 07:04:40')
end_date = dateutil.parser.parse('01/01/2019 07:04:40')
fields = '?fields[field_id]=field_value&fields[field_id2]=field_value2'

result = leads_controller.get_a_list_of_leads(None, None, None, sort_dir, None, None, None, None, None, None, None, None, start_date, end_date, None, fields)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Detailed Lead Information

Get detailed lead information. If field has a default value, the `uid` field will be `null`

```python
def get_detailed_lead_information(self,
                                 lead_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |

## Response Type

[`LeadsResponse2`](../../doc/models/leads-response-2.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_detailed_lead_information(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Update a Lead

Update a lead

```python
def update_a_lead(self,
                 lead_id,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `body` | [`LeadsRequest1`](../../doc/models/leads-request-1.md) | Body, Required | Lead changes (send only fields you want to change) |

## Response Type

[`LeadsResponse3`](../../doc/models/leads-response-3.md)

## Example Usage

```python
lead_id = 218
body = LeadsRequest1()

result = leads_controller.update_a_lead(lead_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Lead Information From a Specific Tab

Get lead information from a specific tab. If field has a default value, the `uid` field will be `null`

```python
def get_lead_information_from_a_specific_tab(self,
                                            lead_id,
                                            tab_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `tab_id` | `int` | Template, Required | Lead field tab Id |

## Response Type

[`LeadsTabsFieldsResponse`](../../doc/models/leads-tabs-fields-response.md)

## Example Usage

```python
lead_id = 218
tab_id = 64

result = leads_controller.get_lead_information_from_a_specific_tab(lead_id, tab_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Delete Record From a Lead Record Set

The method allows deleting records from lead tabs with the type "set". Values of `catId` and `recordId` can be obtained by request [Get detailed lead information](#/paths/~1leads~1{leadId}/get) (`details.id` = `catId`, `details.record` = `recordId`).

```python
def delete_record_from_a_lead_record_set(self,
                                        lead_id,
                                        cat_id,
                                        record_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `cat_id` | `int` | Template, Required | Record category ID |
| `record_id` | `int` | Template, Required | Record ID |

## Response Type

[`LeadsRecordsRecordIdResponse`](../../doc/models/leads-records-record-id-response.md)

## Example Usage

```python
lead_id = 218
cat_id = 78
record_id = 180

result = leads_controller.delete_record_from_a_lead_record_set(lead_id, cat_id, record_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Create a New Lead Field

Create a new lead field

```python
def create_a_new_lead_field(self,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadsFieldsRequest`](../../doc/models/leads-fields-request.md) | Body, Optional | - |

## Response Type

[`LeadField`](../../doc/models/lead-field.md)

## Example Usage

```python
body = LeadsFieldsRequest()
body.tab = 1
body.label = 'New Field'
body.mtype = TypeEnum.SELECT

result = leads_controller.create_a_new_lead_field(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Available Lead Fields

Get a list of available lead fields

```python
def get_a_list_of_available_lead_fields(self,
                                       page=None,
                                       per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPageEnum`](../../doc/models/per-page-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsFieldsResponse`](../../doc/models/leads-fields-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_lead_fields()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a Lead Field

Get a lead field

```python
def get_a_lead_field(self,
                    field_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_id` | `int` | Template, Required | Field Id |

## Response Type

[`LeadField`](../../doc/models/lead-field.md)

## Example Usage

```python
field_id = 40

result = leads_controller.get_a_lead_field(field_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Update a Lead Field

Update a field for the current lead

```python
def update_a_lead_field(self,
                       field_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_id` | `int` | Template, Required | Field Id |
| `body` | [`LeadsFieldsRequest`](../../doc/models/leads-fields-request.md) | Body, Optional | - |

## Response Type

[`LeadField`](../../doc/models/lead-field.md)

## Example Usage

```python
field_id = 40
body = LeadsFieldsRequest()
body.tab = 1
body.label = 'New Field'
body.mtype = TypeEnum.SELECT

result = leads_controller.update_a_lead_field(field_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Update a Lead Field Order Position

Update a lead field order position for the current Lead. You can send value equal to 0 and type 'increment' or 'decrement' to set the field as first or last in the field list.

```python
def update_a_lead_field_order_position(self,
                                      field_id,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_id` | `int` | Template, Required | Field Id |
| `body` | [`LeadFieldOrder`](../../doc/models/lead-field-order.md) | Body, Optional | - |

## Response Type

[`LeadsFieldsOrderResponse`](../../doc/models/leads-fields-order-response.md)

## Example Usage

```python
field_id = 40
body = LeadFieldOrder()
body.value = 1

result = leads_controller.update_a_lead_field_order_position(field_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Create a Lead Field Tab

Create a lead field tab

```python
def create_a_lead_field_tab(self,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LeadFieldTab`](../../doc/models/lead-field-tab.md) | Body, Optional | - |

## Response Type

[`LeadFieldTab`](../../doc/models/lead-field-tab.md)

## Example Usage

```python
body = LeadFieldTab()
body.position = PositionEnum.ENUM_1
body.mclass = ClassEnum.DOCUMENTS
body.name = 'New tab'
body.order = 1

result = leads_controller.create_a_lead_field_tab(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of All Lead Field Tabs

Get a list of all lead field tabs

```python
def get_a_list_of_all_lead_field_tabs(self,
                                     page=None,
                                     per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPageEnum`](../../doc/models/per-page-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsFieldsTabsResponse`](../../doc/models/leads-fields-tabs-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_all_lead_field_tabs()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a Lead Field Tab

Get a lead field tab

```python
def get_a_lead_field_tab(self,
                        tab_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tab_id` | `int` | Template, Required | Lead field tab Id |

## Response Type

[`LeadFieldTab`](../../doc/models/lead-field-tab.md)

## Example Usage

```python
tab_id = 64

result = leads_controller.get_a_lead_field_tab(tab_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Update a Lead Field Tab

Update a lead field tab

```python
def update_a_lead_field_tab(self,
                           tab_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tab_id` | `int` | Template, Required | Lead field tab Id |
| `body` | [`LeadFieldTab`](../../doc/models/lead-field-tab.md) | Body, Optional | - |

## Response Type

[`LeadFieldTab`](../../doc/models/lead-field-tab.md)

## Example Usage

```python
tab_id = 64
body = LeadFieldTab()
body.position = PositionEnum.ENUM_1
body.mclass = ClassEnum.DOCUMENTS
body.name = 'New tab'
body.order = 1

result = leads_controller.update_a_lead_field_tab(tab_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Pricing Templates

Get pricing templates

```python
def get_pricing_templates(self,
                         page=None,
                         per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsPricingTemplatesResponse`](../../doc/models/leads-pricing-templates-response.md)

## Example Usage

```python
result = leads_controller.get_pricing_templates()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Create a Lead Note

Create a lead note

```python
def create_a_lead_note(self,
                      lead_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `body` | [`LeadsNotesRequest`](../../doc/models/leads-notes-request.md) | Body, Required | Create a lead note |

## Response Type

[`LeadsNotesResponse`](../../doc/models/leads-notes-response.md)

## Example Usage

```python
lead_id = 218
body = LeadsNotesRequest()
body.tab = 1
body.note = 'Test note'
body.sticky = StickyEnum.YES

result = leads_controller.create_a_lead_note(lead_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Lead Notes

Get lead notes

```python
def get_lead_notes(self,
                  lead_id,
                  page=None,
                  per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsNotesResponse1`](../../doc/models/leads-notes-response-1.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_lead_notes(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Create a Lead Appointment

Create a lead appointment

```python
def create_a_lead_appointment(self,
                             lead_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `body` | [`LeadsAppointmentsRequest`](../../doc/models/leads-appointments-request.md) | Body, Required | Create a lead appointment |

## Response Type

[`LeadsAppointmentsResponse`](../../doc/models/leads-appointments-response.md)

## Example Usage

```python
lead_id = 218
body = LeadsAppointmentsRequest()
body.date = dateutil.parser.parse('05/30/2018 13:16:13')
body.date_end = dateutil.parser.parse('05/30/2018 13:26:13')
body.text = 'text4'
body.set_by = '1'
body.set_for = '1'

result = leads_controller.create_a_lead_appointment(lead_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Lead Appointments

Get lead appointments

```python
def get_lead_appointments(self,
                         lead_id,
                         page=None,
                         set_for=None,
                         set_by=None,
                         modified_by=None,
                         confirmed_by=None,
                         rescheduled_by=None,
                         seen_by=None,
                         rescheduled_count=None,
                         done=None,
                         per_page=None,
                         sort_by=None,
                         sort_dir=None,
                         date_filter=None,
                         start_date=None,
                         end_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `page` | `int` | Query, Optional | Page number |
| `set_for` | `int` | Query, Optional | Filter by the user for who appointment was created |
| `set_by` | `int` | Query, Optional | Filter by the user for who have created an appointment |
| `modified_by` | `int` | Query, Optional | Filter by the user for who have modified an appointment |
| `confirmed_by` | `int` | Query, Optional | Filter by the user for who have confirmed an appointment |
| `rescheduled_by` | `int` | Query, Optional | Filter by the user for who have rescheduled an appointment |
| `seen_by` | `int` | Query, Optional | Filter by the user for who have mark an appointment as seen |
| `rescheduled_count` | `int` | Query, Optional | Filter by the count of rescheduling |
| `done` | `bool` | Query, Optional | Filter by the done flag |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |
| `sort_by` | [`SortBy1Enum`](../../doc/models/sort-by-1-enum.md) | Query, Optional | Sort appointments by columns |
| `sort_dir` | [`SortDirEnum`](../../doc/models/sort-dir-enum.md) | Query, Optional | Sort direction |
| `date_filter` | [`DateFilter1Enum`](../../doc/models/date-filter-1-enum.md) | Query, Optional | Filtering appointments by a date range depends on this filter |
| `start_date` | `date` | Query, Optional | Filter appointments by a date in format Y-m-d |
| `end_date` | `date` | Query, Optional | Filter leads by a date in format Y-m-d |

## Response Type

[`LeadsAppointmentsResponse1`](../../doc/models/leads-appointments-response-1.md)

## Example Usage

```python
lead_id = 218
start_date = dateutil.parser.parse('2019-01-01').date()
end_date = dateutil.parser.parse('2019-01-02').date()

result = leads_controller.get_lead_appointments(lead_id, None, None, None, None, None, None, None, None, None, None, None, None, None, start_date, end_date)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Populate PDF Document

Populate a PDF document from a lead.

```python
def populate_pdf_document(self,
                         lead_id,
                         application_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `application_id` | `int` | Template, Required | Application Id |

## Response Type

[`LeadsApplicationsPopulateResponse`](../../doc/models/leads-applications-populate-response.md)

## Example Usage

```python
lead_id = 218
application_id = 164

result = leads_controller.populate_pdf_document(lead_id, application_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |
| 500 | Unexpected server error | [`ServerErrorException`](../../doc/models/server-error-exception.md) |


# Create a Lead Task

Create a lead task

```python
def create_a_lead_task(self,
                      lead_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `body` | [`LeadsTasksRequest`](../../doc/models/leads-tasks-request.md) | Body, Required | Create a lead task |

## Response Type

[`LeadsTasksResponse`](../../doc/models/leads-tasks-response.md)

## Example Usage

```python
lead_id = 218
body = LeadsTasksRequest()
body.priority = PriorityEnum.NORMAL
body.date = '05/30/2018 13:16:13'
body.date_end = '05/30/2018 13:26:13'
body.text = 'text4'
body.set_by = '1'
body.set_for = '1'

result = leads_controller.create_a_lead_task(lead_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get Lead Tasks

Get lead tasks

```python
def get_lead_tasks(self,
                  lead_id,
                  page=None,
                  per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsTasksResponse1`](../../doc/models/leads-tasks-response-1.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_lead_tasks(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Assign a User

Assign a user

```python
def assign_a_user(self,
                 lead_id,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `body` | `` | Body, Required | Create a lead task |

## Response Type

[`LeadsUsersResponse`](../../doc/models/leads-users-response.md)

## Example Usage

```python
lead_id = 218
body = jsonpickle.decode('{"$$__case":0,"$$__case_of":"oneOf","value":{"user":107,"assign_manager":null}}')

result = leads_controller.assign_a_user(lead_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Assigned Users

Get a list of assigned users

```python
def get_a_list_of_assigned_users(self,
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

[`LeadsUsersResponse1`](../../doc/models/leads-users-response-1.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_assigned_users(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Unassign a User From a Lead

Unassign a user from a lead

```python
def unassign_a_user_from_a_lead(self,
                               lead_id,
                               user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `user_id` | `int` | Template, Required | User Id |

## Response Type

[`LeadsUsersResponse`](../../doc/models/leads-users-response.md)

## Example Usage

```python
lead_id = 218
user_id = 28

result = leads_controller.unassign_a_user_from_a_lead(lead_id, user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Upload a Document

Upload a document

```python
def upload_a_document(self,
                     lead_id,
                     tab,
                     label,
                     filename,
                     notify_users=None,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `tab` | `int` | Query, Required | Tab Id |
| `label` | `int` | Query, Required | Label Id |
| `filename` | `string` | Query, Required | File name |
| `notify_users` | `string` | Query, Optional | Comma separated list of user ids to notify or `all_assigned` to notify all users assigned to the lead |
| `body` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

`string`

## Example Usage

```python
lead_id = 218
tab = 50
label = 166
filename = 'filename2'

result = leads_controller.upload_a_document(lead_id, tab, label, filename)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Available Documents

Get a list of available documents

```python
def get_a_list_of_available_documents(self,
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

[`LeadsDocumentsResponse`](../../doc/models/leads-documents-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_available_documents(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of Available Document Labels

Get a list of all document labels available when uploading and downloading files

```python
def get_a_list_of_available_document_labels(self,
                                           page=None,
                                           per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsFileLabelsResponse`](../../doc/models/leads-file-labels-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_document_labels()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Download a Document

Download a document

```python
def download_a_document(self,
                       lead_id,
                       document_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `document_id` | `int` | Template, Required | Document Id |

## Response Type

`binary`

## Example Usage

```python
lead_id = 218
document_id = 92

result = leads_controller.download_a_document(lead_id, document_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Send an Email to Lead With Template

Send an email to lead with template

```python
def send_an_email_to_lead_with_template(self,
                                       lead_id,
                                       template_id,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `template_id` | `int` | Template, Required | Template Id |
| `body` | `` | Body, Optional | - |

## Response Type

[`LeadsEmailsResponse`](../../doc/models/leads-emails-response.md)

## Example Usage

```python
lead_id = 218
template_id = 100

result = leads_controller.send_an_email_to_lead_with_template(lead_id, template_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of Email Templates

Get list of available email templates for a lead email

```python
def get_a_list_of_email_templates(self)
```

## Response Type

[`LeadsEmailsTemplatesResponse`](../../doc/models/leads-emails-templates-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_email_templates()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Download a Mailbox Email Attachment

Download a mailbox email attachment

```python
def download_a_mailbox_email_attachment(self,
                                       lead_id,
                                       email_id,
                                       attachment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `email_id` | `int` | Template, Required | Email Id |
| `attachment_id` | `int` | Template, Required | Attachment Id |

## Response Type

`binary`

## Example Usage

```python
lead_id = 218
email_id = 8
attachment_id = 118

result = leads_controller.download_a_mailbox_email_attachment(lead_id, email_id, attachment_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Send an SMS to Lead With Selected SMS Template

Send an SMS to lead with selected SMS template.

```python
def send_an_sms_to_lead_with_selected_sms_template(self,
                                                  lead_id,
                                                  template_id,
                                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lead_id` | `int` | Template, Required | Lead Id |
| `template_id` | `int` | Template, Required | Template Id |
| `body` | `` | Body, Optional | - |

## Response Type

[`LeadsSmsResponse`](../../doc/models/leads-sms-response.md)

## Example Usage

```python
lead_id = 218
template_id = 100

result = leads_controller.send_an_sms_to_lead_with_selected_sms_template(lead_id, template_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get List of SMS Templates

Get list of available SMS templates for sending SMS to a lead

```python
def get_list_of_sms_templates(self)
```

## Response Type

[`LeadsSmsTemplatesResponse`](../../doc/models/leads-sms-templates-response.md)

## Example Usage

```python
result = leads_controller.get_list_of_sms_templates()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |
| 405 | Validation exception | [`ValidationErrorException`](../../doc/models/validation-error-exception.md) |


# Get a List of All Lead Campaign Activity

Get a list of all lead campaign activity

```python
def get_a_list_of_all_lead_campaign_activity(self,
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

[`LeadsActivityCampaignResponse`](../../doc/models/leads-activity-campaign-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_campaign_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of All Lead Deletion Activity

Get a list of all lead deletion activity

```python
def get_a_list_of_all_lead_deletion_activity(self,
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

[`LeadsActivityDeletionResponse`](../../doc/models/leads-activity-deletion-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_deletion_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of All Lead Duplicate Activity

Get a list of all lead duplicate activity

```python
def get_a_list_of_all_lead_duplicate_activity(self,
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

[`LeadsActivityDuplicatesResponse`](../../doc/models/leads-activity-duplicates-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_duplicate_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of All Lead Links Activity

Get a list of all lead links activity

```python
def get_a_list_of_all_lead_links_activity(self,
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

[`LeadsActivityLinksResponse`](../../doc/models/leads-activity-links-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_links_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of All Lead Source Activity

Get a list of all lead source activity

```python
def get_a_list_of_all_lead_source_activity(self,
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

[`LeadsActivitySourceResponse`](../../doc/models/leads-activity-source-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_source_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of All Lead Status Activity

Get a list of all lead status activity

```python
def get_a_list_of_all_lead_status_activity(self,
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

[`LeadsActivityStatusResponse`](../../doc/models/leads-activity-status-response.md)

## Example Usage

```python
lead_id = 218

result = leads_controller.get_a_list_of_all_lead_status_activity(lead_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |
| 404 | Resource not found | [`NotFoundErrorException`](../../doc/models/not-found-error-exception.md) |


# Get a List of Available Campaigns

Get a list of available campaigns

```python
def get_a_list_of_available_campaigns(self)
```

## Response Type

[`LeadsCampaignsResponse`](../../doc/models/leads-campaigns-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_campaigns()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Get a List of Available Groups

Get a list of available groups

```python
def get_a_list_of_available_groups(self,
                                  status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Query, Optional | Status Id |

## Response Type

[`LeadsGroupsResponse`](../../doc/models/leads-groups-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_groups()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Get a List of Available Sources

Get a list of available sources

```python
def get_a_list_of_available_sources(self)
```

## Response Type

[`LeadsSourcesResponse`](../../doc/models/leads-sources-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_sources()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Get a List of Available Statuses

Get a list of available statuses

```python
def get_a_list_of_available_statuses(self,
                                    group=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | `int` | Query, Optional | Group Id |

## Response Type

[`LeadsStatusesResponse`](../../doc/models/leads-statuses-response.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_statuses()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


# Get a List of Available Users

Get a list of available users for assigning

```python
def get_a_list_of_available_users(self,
                                 page=None,
                                 per_page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `per_page` | [`PerPage3Enum`](../../doc/models/per-page-3-enum.md) | Query, Optional | Count of records per page |

## Response Type

[`LeadsUsersResponse1`](../../doc/models/leads-users-response-1.md)

## Example Usage

```python
result = leads_controller.get_a_list_of_available_users()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | API key is missing or invalid | [`UnauthorizedErrorException`](../../doc/models/unauthorized-error-exception.md) |
| 403 | Not enough permissions | [`ForbiddenErrorException`](../../doc/models/forbidden-error-exception.md) |


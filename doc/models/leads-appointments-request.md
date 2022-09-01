
# Leads Appointments Request

## Structure

`LeadsAppointmentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `datetime` | Required | Date in format ISO 8601 (Y-m-d\TH:i:sP) |
| `date_end` | `datetime` | Required | End date in format ISO 8601 (Y-m-d\TH:i:sP) |
| `text` | `string` | Required | Task description |
| `set_by` | `string` | Required | Task set by user (User Id) |
| `set_for` | `string` | Required | Task set for user (User Id) |

## Example (as JSON)

```json
{
  "date": "05/30/2018 13:16:13",
  "date_end": "05/30/2018 13:26:13",
  "text": null,
  "set_by": "1",
  "set_for": "1"
}
```


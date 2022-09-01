
# Leads Tasks Request

## Structure

`LeadsTasksRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `priority` | [`PriorityEnum`](../../doc/models/priority-enum.md) | Required | Priority |
| `date` | `string` | Required | Date in ISO 8601 format (Y-m-d\TH:i:sP) |
| `date_end` | `string` | Required | End date in ISO 8601 format (Y-m-d\TH:i:sP) |
| `text` | `string` | Required | Task description |
| `set_by` | `string` | Required | Task set by user (user Id) |
| `set_for` | `string` | Required | Task set for user (user Id) |

## Example (as JSON)

```json
{
  "priority": "Normal",
  "date": "05/30/2018 13:16:13",
  "date_end": "05/30/2018 13:26:13",
  "text": null,
  "set_by": "1",
  "set_for": "1"
}
```


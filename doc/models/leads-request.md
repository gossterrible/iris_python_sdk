
# Leads Request

## Structure

`LeadsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign` | `int` | Optional | Campaign Id |
| `status` | `int` | Required | Status Id |
| `source` | `int` | Optional | Source Id |
| `group` | `int` | Optional | Group Id |
| `users` | `List of int` | Optional | Ids of users to assign to a new lead |
| `users_emails` | `List of string` | Optional | Emails of users to assign to a new lead |
| `fields` | [`List of Field`](../../doc/models/field.md) | Required | Lead fields |

## Example (as JSON)

```json
{
  "status": 1,
  "fields": {
    "id": "1",
    "value": "Test"
  }
}
```


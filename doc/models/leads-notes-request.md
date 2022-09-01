
# Leads Notes Request

## Structure

`LeadsNotesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tab` | `int` | Required | Tab Id |
| `note` | `string` | Required | Note text |
| `sticky` | [`StickyEnum`](../../doc/models/sticky-enum.md) | Required | Pin to top? |
| `notify_users` | `string` | Optional | Comma separated list of user ids to notify or `all_assigned` to notify all users assigned to the lead |

## Example (as JSON)

```json
{
  "tab": 1,
  "note": "Test note",
  "sticky": "Yes"
}
```


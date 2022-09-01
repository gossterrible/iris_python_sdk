
# Datum

## Structure

`Datum`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Template Id |
| `name` | `string` | Optional | Template name |
| `created_by` | `int` | Optional | Template creator |
| `created_at` | `datetime` | Optional | Template modification date and time (ISO-8601) |
| `modified_by` | `int` | Optional | Template modification date and time (ISO-8601) |
| `modified_at` | `datetime` | Optional | Last template editor |
| `fields_changed_by` | `int` | Optional | Last fields editor |
| `fields_changed_at` | `datetime` | Optional | Last fileds modification date and time (ISO-8601) |
| `values` | [`List of Value`](../../doc/models/value.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "created_by": null,
  "created_at": null,
  "modified_by": null,
  "modified_at": null,
  "fields_changed_by": null,
  "fields_changed_at": null,
  "values": null
}
```


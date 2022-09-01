
# Lead Field Tab

## Structure

`LeadFieldTab`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Tab Id |
| `active` | [`ActiveEnum`](../../doc/models/active-enum.md) | Optional | Active tab |
| `position` | [`PositionEnum`](../../doc/models/position-enum.md) | Required | Tab position<br>**Default**: `1` |
| `mclass` | [`ClassEnum`](../../doc/models/class-enum.md) | Required | Tab class |
| `name` | `string` | Required | Tab class |
| `order` | `int` | Required | Tab order |

## Example (as JSON)

```json
{
  "position": 1,
  "class": "documents",
  "name": "New tab",
  "order": 1
}
```


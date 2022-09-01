
# Application Field

## Structure

`ApplicationField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Application field Id |
| `mfrom` | `int` | Required | Application field from field Id |
| `record` | `int` | Optional | Application field record |
| `to` | `string` | Optional | Name of mapped field |
| `to_alt` | `string` | Optional | Alt of mapped field |
| `to_type` | `string` | Optional | Type of mapped field |
| `special` | [`Special1Enum`](../../doc/models/special-1-enum.md) | Optional | Special type of mapped field<br>**Default**: `'null'` |
| `info` | [`List of Info`](../../doc/models/info.md) | Optional | - |

## Example (as JSON)

```json
{
  "from": 1
}
```


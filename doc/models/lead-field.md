
# Lead Field

## Structure

`LeadField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Field Id |
| `tab` | `int` | Required | Field tab Id |
| `label` | `string` | Required | Field label |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Required | Field type |
| `length` | `int` | Optional | Field size |
| `default` | `string` | Optional | Field default value |
| `alignment` | [`AlignmentEnum`](../../doc/models/alignment-enum.md) | Optional | Field alignment |
| `searchable` | [`SearchableEnum`](../../doc/models/searchable-enum.md) | Optional | Searchable field |
| `special` | [`SpecialEnum`](../../doc/models/special-enum.md) | Optional | Field special value |
| `options` | [`Options`](../../doc/models/options.md) | Optional | - |
| `order` | `int` | Optional | - |
| `read_only` | `bool` | Optional | Whether the field is read only |
| `required` | `bool` | Optional | Whether the field is required |

## Example (as JSON)

```json
{
  "tab": 1,
  "label": "New Field",
  "type": "Select"
}
```


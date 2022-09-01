
# Brief Lead Info

## Structure

`BriefLeadInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Lead Id |
| `mid` | `int` | Optional | Lead merchant Id |
| `name` | `string` | Optional | Lead name |
| `group` | [`BriefGroupInfo`](../../doc/models/brief-group-info.md) | Optional | - |
| `category` | [`BriefCategoryInfo`](../../doc/models/brief-category-info.md) | Optional | - |
| `status` | [`BriefStatusInfo`](../../doc/models/brief-status-info.md) | Optional | - |
| `campaign` | [`BriefCampaignInfo`](../../doc/models/brief-campaign-info.md) | Optional | - |
| `source` | [`BriefSourceInfo`](../../doc/models/brief-source-info.md) | Optional | - |
| `created` | `datetime` | Optional | Lead creation date (Y-m-d\TH:i:sP) |
| `modified` | `datetime` | Optional | Lead modification date (Y-m-d\TH:i:sP) |

## Example (as JSON)

```json
{
  "id": null,
  "mid": null,
  "name": null,
  "group": null,
  "category": null,
  "status": null,
  "campaign": null,
  "source": null,
  "created": null,
  "modified": null
}
```


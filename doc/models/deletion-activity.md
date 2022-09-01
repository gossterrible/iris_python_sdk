
# Deletion Activity

## Structure

`DeletionActivity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Activity Id |
| `deleted_id` | `int` | Optional | User Id |
| `deleted_at` | `datetime` | Optional | Date of deletion (Y-m-d\TH:i:sP) |
| `undeleted_id` | `int` | Optional | User Id |
| `undeleted_at` | `datetime` | Optional | Date of undeletion (Y-m-d\TH:i:sP) |

## Example (as JSON)

```json
{
  "id": null,
  "deletedId": null,
  "deletedAt": null,
  "undeletedId": null,
  "undeletedAt": null
}
```


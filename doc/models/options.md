
# Options

## Structure

`Options`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dropdown` | [`Dropdown`](../../doc/models/dropdown.md) | Optional | Add new list item |
| `dupecheck` | `bool` | Optional | Enable dupecheck |
| `contactid` | `string` | Optional | Id of contact field |
| `mask` | [`MaskEnum`](../../doc/models/mask-enum.md) | Optional | Field mask |
| `copy` | [`Copy`](../../doc/models/copy.md) | Optional | Copy button properties |
| `hyperlink` | `bool` | Optional | Enable hyperlink |
| `sms` | `bool` | Optional | Enable SMS |
| `dialer` | `bool` | Optional | Enable dialer |
| `googlemaps` | `object` | Optional | Google Maps search properties |
| `zip_code_field` | `int` | Optional | Zip code field ID for TimeZone field only |
| `zipcode_autocomplete` | [`ZipcodeAutocomplete`](../../doc/models/zipcode-autocomplete.md) | Optional | ZIP Code autofill properties |

## Example (as JSON)

```json
{
  "dropdown": null,
  "dupecheck": null,
  "contactid": null,
  "mask": null,
  "copy": null,
  "hyperlink": null,
  "sms": null,
  "dialer": null,
  "googlemaps": null,
  "zip_code_field": null,
  "zipcode_autocomplete": null
}
```


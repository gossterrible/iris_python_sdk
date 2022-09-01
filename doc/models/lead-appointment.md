
# Lead Appointment

## Structure

`LeadAppointment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Appointment Id |
| `user` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `set_for` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `set_at` | `datetime` | Optional | Appointment creation date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `set_by` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `modified` | `datetime` | Optional | Appointment modification date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `modified_by` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `text` | `string` | Optional | Appointment description |
| `date` | `datetime` | Optional | Appointment date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `date_end` | `datetime` | Optional | Appointment end date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `done` | [`DoneEnum`](../../doc/models/done-enum.md) | Optional | Is appointment done? |
| `confirmed` | `datetime` | Optional | Appointment confirmed date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `confirmed_by` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `seen` | `datetime` | Optional | Appointment seen date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `seen_by` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `rescheduled` | `datetime` | Optional | Appointment rescheduled date and time in format ISO 8601 (Y-m-d\TH:i:sP) |
| `rescheduled_by` | [`BriefUserInfo`](../../doc/models/brief-user-info.md) | Optional | - |
| `rescheduled_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "user": null,
  "set_for": null,
  "set_at": null,
  "set_by": null,
  "modified": null,
  "modified_by": null,
  "text": null,
  "date": null,
  "date_end": null,
  "done": null,
  "confirmed": null,
  "confirmed_by": null,
  "seen": null,
  "seen_by": null,
  "rescheduled": null,
  "rescheduled_by": null,
  "rescheduled_count": null
}
```


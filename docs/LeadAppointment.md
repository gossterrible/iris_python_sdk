# LeadAppointment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Appointment Id | [optional] 
**user** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**set_for** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**set_at** | **datetime** | Appointment creation date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**set_by** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**modified** | **datetime** | Appointment modification date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**modified_by** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**text** | **str** | Appointment description | [optional] 
**date** | **datetime** | Appointment date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**date_end** | **datetime** | Appointment end date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**done** | **str** | Is appointment done? | [optional] 
**confirmed** | **datetime** | Appointment confirmed date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**confirmed_by** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**seen** | **datetime** | Appointment seen date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**seen_by** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**rescheduled** | **datetime** | Appointment rescheduled date and time in format ISO 8601 (Y-m-d\\TH:i:sP) | [optional] 
**rescheduled_by** | [**BriefUserInfo**](BriefUserInfo.md) |  | [optional] 
**rescheduled_count** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



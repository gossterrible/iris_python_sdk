# ApplicationField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **int** | Application field from field Id | 
**id** | **int** | Application field Id | [optional] [readonly] 
**record** | **int** | Application field record | [optional] 
**to** | **str** | Name of mapped field | [optional] 
**to_alt** | **str** | Alt of mapped field | [optional] 
**to_type** | **str** | Type of mapped field | [optional] 
**special** | **str** | Special type of mapped field | [optional]  if omitted the server will use the default value of "null"
**info** | [**[ApplicationFieldInfoInner]**](ApplicationFieldInfoInner.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



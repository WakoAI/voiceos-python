# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) |  | 
**url** | **str** | The url to call when the event is triggered | 
**method** | [**MethodEnum**](MethodEnum.md) | The method to use when calling the url | 
**headers** | **Dict[str, str]** | The headers to use when calling the url | [optional] 
**filter** | **Dict[str, int]** | The filter to use when triggering the webhook | [optional] 

## Example

```python
from voiceos.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_form_dict = webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



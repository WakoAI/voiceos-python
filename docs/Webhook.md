# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventName]**](EventName.md) | The events that will trigger the webhook to send a request. | 
**url** | **str** | The url of the webhook. Where the requests will be sent. | 
**method** | [**MethodEnum**](MethodEnum.md) | The method of the webhook. | 
**headers** | **Dict[str, str]** | The headers of the webhook. Use the headers to authenticate requests to your backend. | [optional] 
**filter** | **str** | The filter for the webhook events. Use to filter events with conditional statements. | [optional] 

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



# ConversationRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_url** | **str** | The recording url of the conversation. | 

## Example

```python
from voiceos.models.conversation_recording import ConversationRecording

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationRecording from a JSON string
conversation_recording_instance = ConversationRecording.from_json(json)
# print the JSON string representation of the object
print(ConversationRecording.to_json())

# convert the object into a dict
conversation_recording_dict = conversation_recording_instance.to_dict()
# create an instance of ConversationRecording from a dict
conversation_recording_form_dict = conversation_recording.from_dict(conversation_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



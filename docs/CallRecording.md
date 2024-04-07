# CallRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_url** | **str** | The recording url of the conversation. | 

## Example

```python
from voiceos.models.call_recording import CallRecording

# TODO update the JSON string below
json = "{}"
# create an instance of CallRecording from a JSON string
call_recording_instance = CallRecording.from_json(json)
# print the JSON string representation of the object
print(CallRecording.to_json())

# convert the object into a dict
call_recording_dict = call_recording_instance.to_dict()
# create an instance of CallRecording from a dict
call_recording_form_dict = call_recording.from_dict(call_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



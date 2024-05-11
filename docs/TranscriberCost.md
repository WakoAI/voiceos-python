# TranscriberCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**WakoApiModelsTranscriberProvider**](WakoApiModelsTranscriberProvider.md) | The provider of the transcriber. | 
**cost** | **float** | The cost for the transcriber usage (USD). | 
**seconds** | **float** | The number of seconds used for the transcriber. | 

## Example

```python
from voiceos.models.transcriber_cost import TranscriberCost

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriberCost from a JSON string
transcriber_cost_instance = TranscriberCost.from_json(json)
# print the JSON string representation of the object
print(TranscriberCost.to_json())

# convert the object into a dict
transcriber_cost_dict = transcriber_cost_instance.to_dict()
# create an instance of TranscriberCost from a dict
transcriber_cost_form_dict = transcriber_cost.from_dict(transcriber_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# voiceos.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_get**](DefaultApi.md#health_check_get) | **GET** / | Health Check


# **health_check_get**
> object health_check_get()

Health Check

### Example


```python
import voiceos
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_get()
        print("The response of DefaultApi->health_check_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# voiceos.CallsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_call**](CallsApi.md#create_call) | **POST** /calls/create | Create Call
[**get_call**](CallsApi.md#get_call) | **GET** /calls/{call_id} | Get Call
[**get_recording**](CallsApi.md#get_recording) | **GET** /calls/{call_id}/recording | Get Call Recording
[**list_calls**](CallsApi.md#list_calls) | **GET** /calls | List Calls


# **create_call**
> object create_call(create_call)

Create Call

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.create_call import CreateCall
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.CallsApi(api_client)
    create_call = voiceos.CreateCall() # CreateCall | 

    try:
        # Create Call
        api_response = api_instance.create_call(create_call)
        print("The response of CallsApi->create_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_call** | [**CreateCall**](CreateCall.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call**
> CallResponse get_call(call_id)

Get Call

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.call_response import CallResponse
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.CallsApi(api_client)
    call_id = 'call_id_example' # str | 

    try:
        # Get Call
        api_response = api_instance.get_call(call_id)
        print("The response of CallsApi->get_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->get_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**CallResponse**](CallResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording**
> CallRecording get_recording(call_id)

Get Call Recording

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.call_recording import CallRecording
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.CallsApi(api_client)
    call_id = 'call_id_example' # str | 

    try:
        # Get Call Recording
        api_response = api_instance.get_recording(call_id)
        print("The response of CallsApi->get_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->get_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_id** | **str**|  | 

### Return type

[**CallRecording**](CallRecording.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calls**
> CallsPagination list_calls(status=status, created_before=created_before, created_after=created_after, index=index, size=size)

List Calls

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.call_status import CallStatus
from voiceos.models.calls_pagination import CallsPagination
from voiceos.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = voiceos.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with voiceos.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voiceos.CallsApi(api_client)
    status = voiceos.CallStatus() # CallStatus |  (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    index = 1 # int |  (optional) (default to 1)
    size = 100 # int |  (optional) (default to 100)

    try:
        # List Calls
        api_response = api_instance.list_calls(status=status, created_before=created_before, created_after=created_after, index=index, size=size)
        print("The response of CallsApi->list_calls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->list_calls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**CallStatus**](.md)|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
 **index** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 100]

### Return type

[**CallsPagination**](CallsPagination.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# voiceos.PhoneNumbersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_phone_number_phone_numbers_buy_post**](PhoneNumbersApi.md#buy_phone_number_phone_numbers_buy_post) | **POST** /phone_numbers/buy | Buy Phone Number
[**delete_phone_number_phone_numbers_phone_number_delete**](PhoneNumbersApi.md#delete_phone_number_phone_numbers_phone_number_delete) | **DELETE** /phone_numbers/{phone_number} | Delete Phone Number
[**get_phone_number**](PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phone_number} | Get Phone Number
[**list_available_phone_numbers**](PhoneNumbersApi.md#list_available_phone_numbers) | **GET** /phone_numbers/buy | List Available Phone Numbers
[**list_phone_numbers**](PhoneNumbersApi.md#list_phone_numbers) | **GET** /phone_numbers | List Phone Numbers
[**update_phone_number_phone_numbers_phone_number_patch**](PhoneNumbersApi.md#update_phone_number_phone_numbers_phone_number_patch) | **PATCH** /phone_numbers/{phone_number} | Update Phone Number


# **buy_phone_number_phone_numbers_buy_post**
> PhoneNumberResponse buy_phone_number_phone_numbers_buy_post(buy_phone_number)

Buy Phone Number

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.buy_phone_number import BuyPhoneNumber
from voiceos.models.phone_number_response import PhoneNumberResponse
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    buy_phone_number = voiceos.BuyPhoneNumber() # BuyPhoneNumber | 

    try:
        # Buy Phone Number
        api_response = api_instance.buy_phone_number_phone_numbers_buy_post(buy_phone_number)
        print("The response of PhoneNumbersApi->buy_phone_number_phone_numbers_buy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->buy_phone_number_phone_numbers_buy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_phone_number** | [**BuyPhoneNumber**](BuyPhoneNumber.md)|  | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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

# **delete_phone_number_phone_numbers_phone_number_delete**
> PhoneNumber delete_phone_number_phone_numbers_phone_number_delete(phone_number, release_phone_number=release_phone_number)

Delete Phone Number

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.phone_number import PhoneNumber
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | 
    release_phone_number = False # bool |  (optional) (default to False)

    try:
        # Delete Phone Number
        api_response = api_instance.delete_phone_number_phone_numbers_phone_number_delete(phone_number, release_phone_number=release_phone_number)
        print("The response of PhoneNumbersApi->delete_phone_number_phone_numbers_phone_number_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->delete_phone_number_phone_numbers_phone_number_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **release_phone_number** | **bool**|  | [optional] [default to False]

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **get_phone_number**
> PhoneNumberResponse get_phone_number(phone_number)

Get Phone Number

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.phone_number_response import PhoneNumberResponse
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | 

    try:
        # Get Phone Number
        api_response = api_instance.get_phone_number(phone_number)
        print("The response of PhoneNumbersApi->get_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->get_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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

# **list_available_phone_numbers**
> List[PhoneNumberToBuy] list_available_phone_numbers(area_code=area_code, contains=contains, limit=limit)

List Available Phone Numbers

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.phone_number_to_buy import PhoneNumberToBuy
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    area_code = 'area_code_example' # str |  (optional)
    contains = 'contains_example' # str |  (optional)
    limit = 10 # int |  (optional) (default to 10)

    try:
        # List Available Phone Numbers
        api_response = api_instance.list_available_phone_numbers(area_code=area_code, contains=contains, limit=limit)
        print("The response of PhoneNumbersApi->list_available_phone_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->list_available_phone_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_code** | **str**|  | [optional] 
 **contains** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[PhoneNumberToBuy]**](PhoneNumberToBuy.md)

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

# **list_phone_numbers**
> PhoneNumberPagination list_phone_numbers(created_after=created_after, created_before=created_before, index=index, size=size)

List Phone Numbers

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.phone_number_pagination import PhoneNumberPagination
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    index = 1 # int |  (optional) (default to 1)
    size = 100 # int |  (optional) (default to 100)

    try:
        # List Phone Numbers
        api_response = api_instance.list_phone_numbers(created_after=created_after, created_before=created_before, index=index, size=size)
        print("The response of PhoneNumbersApi->list_phone_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->list_phone_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **index** | **int**|  | [optional] [default to 1]
 **size** | **int**|  | [optional] [default to 100]

### Return type

[**PhoneNumberPagination**](PhoneNumberPagination.md)

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

# **update_phone_number_phone_numbers_phone_number_patch**
> PhoneNumberResponse update_phone_number_phone_numbers_phone_number_patch(phone_number, update_phone_number)

Update Phone Number

### Example

* Api Key Authentication (APIKeyHeader):

```python
import voiceos
from voiceos.models.phone_number_response import PhoneNumberResponse
from voiceos.models.update_phone_number import UpdatePhoneNumber
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
    api_instance = voiceos.PhoneNumbersApi(api_client)
    phone_number = 'phone_number_example' # str | 
    update_phone_number = voiceos.UpdatePhoneNumber() # UpdatePhoneNumber | 

    try:
        # Update Phone Number
        api_response = api_instance.update_phone_number_phone_numbers_phone_number_patch(phone_number, update_phone_number)
        print("The response of PhoneNumbersApi->update_phone_number_phone_numbers_phone_number_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->update_phone_number_phone_numbers_phone_number_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  | 
 **update_phone_number** | [**UpdatePhoneNumber**](UpdatePhoneNumber.md)|  | 

### Return type

[**PhoneNumberResponse**](PhoneNumberResponse.md)

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


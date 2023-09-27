# SubaccountEmail
(*subaccount_email*)

### Available Operations

* [email_router_send_email](#email_router_send_email) - Send Email To Contacts
* [email_router_send_email_with_template](#email_router_send_email_with_template) - Send Email To Contacts With Template

## email_router_send_email

Send Email To Contacts

### Example Usage

```python
import sendpost
from sendpost.models import operations, shared

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body='corrupti'.encode(),
    x_send_post_mock_email=False,
    x_send_post_mock_time_shift='illum',
    x_sub_account_api_key='vel',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.EmailRouterSendEmailRequest](../../models/operations/emailroutersendemailrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.EmailRouterSendEmailResponse](../../models/operations/emailroutersendemailresponse.md)**


## email_router_send_email_with_template

Send Email To Contacts With Template

### Example Usage

```python
import sendpost
from sendpost.models import operations, shared

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailWithTemplateRequest(
    request_body='error'.encode(),
    x_sub_account_api_key='deserunt',
)

res = s.subaccount_email.email_router_send_email_with_template(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.EmailRouterSendEmailWithTemplateRequest](../../models/operations/emailroutersendemailwithtemplaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.EmailRouterSendEmailWithTemplateResponse](../../models/operations/emailroutersendemailwithtemplateresponse.md)**


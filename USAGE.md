<!-- Start SDK Example Usage [usage] -->
```python
import sendpost
from sendpost.models import operations

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body='0x6B34FffDd5'.encode(),
    x_sub_account_api_key='<value>',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->
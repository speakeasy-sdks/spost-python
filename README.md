# sendpost

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install sendpost
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import sendpost
from sendpost.models import operations, shared

s = sendpost.Sendpost()

req = operations.EmailRouterSendEmailRequest(
    request_body='corrupti'.encode(),
    x_send_post_mock_email=False,
    x_send_post_mock_time_shift='provident',
    x_sub_account_api_key='distinctio',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [SubaccountEmail](docs/sdks/subaccountemail/README.md)

* [email_router_send_email](docs/sdks/subaccountemail/README.md#email_router_send_email) - Send Email To Contacts
* [email_router_send_email_with_template](docs/sdks/subaccountemail/README.md#email_router_send_email_with_template) - Send Email To Contacts With Template
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

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
    request_body=':k13|`asY9'.encode(),
    x_send_post_mock_email=False,
    x_send_post_mock_time_shift='Recycled',
    x_sub_account_api_key='Supervisor',
)

res = s.subaccount_email.email_router_send_email(req)

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [subaccount_email](docs/sdks/subaccountemail/README.md)

* [email_router_send_email](docs/sdks/subaccountemail/README.md#email_router_send_email) - Send Email To Contacts
* [email_router_send_email_with_template](docs/sdks/subaccountemail/README.md#email_router_send_email_with_template) - Send Email To Contacts With Template
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

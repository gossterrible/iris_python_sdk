"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete)  ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.   # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import iriscrm
from iriscrm.model.leads_lead_id_tasks_get200_response_data_inner import LeadsLeadIdTasksGet200ResponseDataInner
from iriscrm.model.links import Links
from iriscrm.model.meta import Meta
globals()['LeadsLeadIdTasksGet200ResponseDataInner'] = LeadsLeadIdTasksGet200ResponseDataInner
globals()['Links'] = Links
globals()['Meta'] = Meta
from iriscrm.model.leads_lead_id_tasks_get200_response import LeadsLeadIdTasksGet200Response


class TestLeadsLeadIdTasksGet200Response(unittest.TestCase):
    """LeadsLeadIdTasksGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLeadsLeadIdTasksGet200Response(self):
        """Test LeadsLeadIdTasksGet200Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LeadsLeadIdTasksGet200Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

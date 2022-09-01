"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete)  ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.   # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import iriscrm
from iriscrm.api.leads_api import LeadsApi  # noqa: E501


class TestLeadsApi(unittest.TestCase):
    """LeadsApi unit test stubs"""

    def setUp(self):
        self.api = LeadsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_leads_campaigns_get(self):
        """Test case for leads_campaigns_get

        Get a list of available campaigns  # noqa: E501
        """
        pass

    def test_leads_emails_templates_get(self):
        """Test case for leads_emails_templates_get

        Get a list of email templates  # noqa: E501
        """
        pass

    def test_leads_fields_field_id_get(self):
        """Test case for leads_fields_field_id_get

        Get a lead field  # noqa: E501
        """
        pass

    def test_leads_fields_field_id_order_patch(self):
        """Test case for leads_fields_field_id_order_patch

        Update a lead field order position  # noqa: E501
        """
        pass

    def test_leads_fields_field_id_patch(self):
        """Test case for leads_fields_field_id_patch

        Update a lead field  # noqa: E501
        """
        pass

    def test_leads_fields_get(self):
        """Test case for leads_fields_get

        Get a list of available lead fields  # noqa: E501
        """
        pass

    def test_leads_fields_post(self):
        """Test case for leads_fields_post

        Create a new lead field  # noqa: E501
        """
        pass

    def test_leads_fields_tabs_get(self):
        """Test case for leads_fields_tabs_get

        Get a list of all lead field tabs  # noqa: E501
        """
        pass

    def test_leads_fields_tabs_post(self):
        """Test case for leads_fields_tabs_post

        Create a lead field tab  # noqa: E501
        """
        pass

    def test_leads_fields_tabs_tab_id_get(self):
        """Test case for leads_fields_tabs_tab_id_get

        Get a lead field tab  # noqa: E501
        """
        pass

    def test_leads_fields_tabs_tab_id_patch(self):
        """Test case for leads_fields_tabs_tab_id_patch

        Update a lead field tab  # noqa: E501
        """
        pass

    def test_leads_file_labels_get(self):
        """Test case for leads_file_labels_get

        Get a list of available document labels  # noqa: E501
        """
        pass

    def test_leads_get(self):
        """Test case for leads_get

        Get a list of leads  # noqa: E501
        """
        pass

    def test_leads_groups_get(self):
        """Test case for leads_groups_get

        Get a list of available groups  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_campaign_get(self):
        """Test case for leads_lead_id_activity_campaign_get

        Get a list of all lead campaign activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_deletion_get(self):
        """Test case for leads_lead_id_activity_deletion_get

        Get a list of all lead deletion activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_duplicates_get(self):
        """Test case for leads_lead_id_activity_duplicates_get

        Get a list of all lead duplicate activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_links_get(self):
        """Test case for leads_lead_id_activity_links_get

        Get a list of all lead links activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_source_get(self):
        """Test case for leads_lead_id_activity_source_get

        Get a list of all lead source activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_activity_status_get(self):
        """Test case for leads_lead_id_activity_status_get

        Get a list of all lead status activity  # noqa: E501
        """
        pass

    def test_leads_lead_id_applications_application_id_populate_post(self):
        """Test case for leads_lead_id_applications_application_id_populate_post

        Populate PDF Document  # noqa: E501
        """
        pass

    def test_leads_lead_id_appointments_get(self):
        """Test case for leads_lead_id_appointments_get

        Get lead appointments  # noqa: E501
        """
        pass

    def test_leads_lead_id_appointments_post(self):
        """Test case for leads_lead_id_appointments_post

        Create a lead appointment  # noqa: E501
        """
        pass

    def test_leads_lead_id_documents_document_id_get(self):
        """Test case for leads_lead_id_documents_document_id_get

        Download a document  # noqa: E501
        """
        pass

    def test_leads_lead_id_documents_get(self):
        """Test case for leads_lead_id_documents_get

        Get a list of available documents  # noqa: E501
        """
        pass

    def test_leads_lead_id_documents_post(self):
        """Test case for leads_lead_id_documents_post

        Upload a document  # noqa: E501
        """
        pass

    def test_leads_lead_id_emails_template_id_post(self):
        """Test case for leads_lead_id_emails_template_id_post

        Send an email to lead with template  # noqa: E501
        """
        pass

    def test_leads_lead_id_get(self):
        """Test case for leads_lead_id_get

        Get detailed lead information  # noqa: E501
        """
        pass

    def test_leads_lead_id_mailbox_email_id_attachment_attachment_id_get(self):
        """Test case for leads_lead_id_mailbox_email_id_attachment_attachment_id_get

        Download a mailbox email attachment  # noqa: E501
        """
        pass

    def test_leads_lead_id_notes_get(self):
        """Test case for leads_lead_id_notes_get

        Get lead notes  # noqa: E501
        """
        pass

    def test_leads_lead_id_notes_post(self):
        """Test case for leads_lead_id_notes_post

        Create a lead note  # noqa: E501
        """
        pass

    def test_leads_lead_id_patch(self):
        """Test case for leads_lead_id_patch

        Update a lead  # noqa: E501
        """
        pass

    def test_leads_lead_id_records_cat_id_record_id_delete(self):
        """Test case for leads_lead_id_records_cat_id_record_id_delete

        Delete record from a lead record set  # noqa: E501
        """
        pass

    def test_leads_lead_id_sms_template_id_post(self):
        """Test case for leads_lead_id_sms_template_id_post

        Send an SMS to lead with selected SMS template  # noqa: E501
        """
        pass

    def test_leads_lead_id_tabs_tab_id_fields_get(self):
        """Test case for leads_lead_id_tabs_tab_id_fields_get

        Get lead information from a specific tab  # noqa: E501
        """
        pass

    def test_leads_lead_id_tasks_get(self):
        """Test case for leads_lead_id_tasks_get

        Get lead tasks  # noqa: E501
        """
        pass

    def test_leads_lead_id_tasks_post(self):
        """Test case for leads_lead_id_tasks_post

        Create a lead task  # noqa: E501
        """
        pass

    def test_leads_lead_id_users_get(self):
        """Test case for leads_lead_id_users_get

        Get a list of assigned users  # noqa: E501
        """
        pass

    def test_leads_lead_id_users_post(self):
        """Test case for leads_lead_id_users_post

        Assign a user  # noqa: E501
        """
        pass

    def test_leads_lead_id_users_user_id_delete(self):
        """Test case for leads_lead_id_users_user_id_delete

        Unassign a user from a lead  # noqa: E501
        """
        pass

    def test_leads_post(self):
        """Test case for leads_post

        Create a lead  # noqa: E501
        """
        pass

    def test_leads_pricing_templates_get(self):
        """Test case for leads_pricing_templates_get

        Get pricing templates  # noqa: E501
        """
        pass

    def test_leads_sms_templates_get(self):
        """Test case for leads_sms_templates_get

        Get list of SMS templates  # noqa: E501
        """
        pass

    def test_leads_sources_get(self):
        """Test case for leads_sources_get

        Get a list of available sources  # noqa: E501
        """
        pass

    def test_leads_statuses_get(self):
        """Test case for leads_statuses_get

        Get a list of available statuses  # noqa: E501
        """
        pass

    def test_leads_users_get(self):
        """Test case for leads_users_get

        Get a list of available users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

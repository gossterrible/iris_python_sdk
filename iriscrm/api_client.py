"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete) ### You can use the Helpdesk API to: - [Create a new ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk/post) - [Get a list of helpdesk tickets](https://www.mycoastalpay.com/api#/paths/~1helpdesk/get) - [Add a ticket comment](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1comment/post) - [Get detailed ticked information](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/get) - [Update a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/patch) - [Delete a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/delete) - [Upload an attachment to a ticket, comment, checklist, or ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1file/post) - [Download an attachment from a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1download~1{attachmentId}/get) - [Create a new helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/post) - [Get a list of helpdesk ticket types](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/get) - [Get details for a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/get) - [Update a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/patch) - [Delete a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/delete) - [Download an attachment from a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get) - [Get a list of available users to notify and assign](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1users/get) ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  ### You can use the Merchant API to: - [Get a list of merchants](https://www.mycoastalpay.com/api#/paths/~1merchants/get) - [Get detailed merchant information](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/get) - [Update an existing merchant](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/patch) - [Get a list of batches and transactions](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1transactions/get) - [Get a list of chargebacks](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1chargebacks/get) - [Get a list of retrievals](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1retrievals/get) - [Get a list of statements](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements/get) - [Download a statement](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements~1{statementId}/get) ### You can use the Residuals API to: - [Get residuals summary data](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1{year}~1{month}/get) - [Get residuals summary with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1rows~1{processor_id}~1{year}~1{month}/get) - [Get residuals details with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1details~1{processor_id}~1{year}~1{month}/get) - [Get residuals line items](https://www.mycoastalpay.com/api#/paths/~1residuals~1lineitems~1{year}~1{month}/get) - [Get residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1/get) - [Get a list of users with assigned residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1assigned~1{year}~1{month}/get)   # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.  Then open the ** API Settings ** tab, click ** Create New API Token **, configure your token’s settings as needed, and click ** Add New Token **:  <img src='https://www.mycoastalpay.com/images/docs/mapi001.png'/>  Your new token will now be created and displayed in a popup window:  <img src='https://www.mycoastalpay.com/images/docs/mapi002.png'/>  Once the token is created, it will be shown in the list of available API Tokens where you can copy the token, update its settings, or delete it once it’s no longer needed:  <img src='https://www.mycoastalpay.com/images/docs/mapi003.png'/>  ** Note: ** The created tokens will inherit the user’s permissions to assigned merchants, leads, groups and processors. # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # PHP SDK  ### Installation and Usage  #### Availability  The IRIS CRM PHP SDK requires PHP version 5.5 or higher and the PHP cURL extension.  #### Composer  To install the bindings via [Composer](http://getcomposer.org/), please run:  ```bash  composer require iris-crm/php-sdk      ```   In your code, configure the environment and API credentials:  ```php require_once(__DIR__ . '/vendor/autoload.php');  use Swagger\\Client\\Configuration; use Swagger\\Client\\Api\\LeadsApi;  // Configure API key authorization $config = Configuration::getDefaultConfiguration() ->setApiKey('X-API-KEY', 'YOUR_API_KEY') ->setHost('https://www.mycoastalpay.com/api/v1/'); ``` Here’s an example of how to get a list of leads using an SDK. Swagger\\Client\\Api\\LeadsApi it's a SDK Class for Lead endpoints. ```php $apiInstance = new LeadsApi(null, $config);  $page        = 1; // int | Page number $sort_by     = \"created\"; // string | Sorting of leads by the field value $sort_dir    = \"asc\"; // string | Direction of sorting $group       = 2; // int | Filter leads by a group id $campaign    = 3; // int | Filter leads by a campaign id $source      = 4; // int | Filter leads by a source id $status      = 1; // int | Filter leads by a status id $category    = 1; // int | Filter leads by a status category id $user        = 12; // int | Filter leads by a user id $date_filter = \"created\"; // string | Filtering leads by a date range depends on this filter $start_date  = new \\DateTime(\"2018-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $end_date    = new \\DateTime(\"2019-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $email       = \"test@mail.com\"; // string | Filter leads by a email try {     $result = $apiInstance->leadsGet($page, $sort_by, $sort_dir, $group, $campaign, $source, $status, $category, $user, $date_filter, $start_date, $end_date, $email);     print_r($result); } catch (Exception $e) {     echo 'Exception when calling LeadsApi->leadsGet: ' . $e->getMessage() . PHP_EOL; } ``` All parameters for leadsGet method is optional and can be skipped.  If you want skip some parameters - you need to set parameter to `null`  All available classes and methods you can get in \"API Endpoints\" section below. ### API Endpoints All URIs are relative to *https://www.mycoastalpay.com/api/v1*  Class | Method | HTTP Request | Description ------------ | ------------- | ------------- | ------------- *LeadsApi* | **leadsApplicationsAppIdMappingsGet** | **GET** /leads/applications/{appId}/mappings | Get a list of available application field mappings *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdDelete** | **DELETE** /leads/applications/{appId}/mappings/{mapId} | Delete an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdGet** | **GET** /leads/applications/{appId}/mappings/{mapId} | Get an application field mapping list *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdPatch** | **PATCH** /leads/applications/{appId}/mappings/{mapId} | Update an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsPost** | **POST** /leads/applications/{appId}/mappings | Create a new application field mapping *LeadsApi* | **leadsApplicationsGet** | **GET** /leads/applications | Get a list of available applications *LeadsApi* | **leadsCampaignsGet** | **GET** /leads/campaigns | Get a list of available campaigns *LeadsApi* | **leadsDynamicFieldsSchemaGet** | **GET** /leads/dynamic-fields-schema | Get a schema of lead fields *LeadsApi* | **leadsEmailsTemplatesGet** | **GET** /leads/emails/templates | Get a list of email templates *LeadsApi* | **leadsFieldsFieldIdGet** | **GET** /leads/fields/{fieldId} | Get a lead field *LeadsApi* | **leadsFieldsFieldIdOrderPatch** | **PATCH** /leads/fields/{fieldId}/order | Update a lead field order position *LeadsApi* | **leadsFieldsFieldIdPatch** | **PATCH** /leads/fields/{fieldId} | Update a lead field *LeadsApi* | **leadsFieldsGet** | **GET** /leads/fields | Get a list of available lead fields *LeadsApi* | **leadsFieldsPost** | **POST** /leads/fields | Create a new lead field *LeadsApi* | **leadsFieldsTabsGet** | **GET** /leads/fields/tabs | Get a list of all lead field tabs *LeadsApi* | **leadsFieldsTabsPost** | **POST** /leads/fields/tabs | Create a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdGet** | **GET** /leads/fields/tabs/{tabId} | Get a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdPatch** | **PATCH** /leads/fields/tabs/{tabId} | Update a lead field tab *LeadsApi* | **leadsGet** | **GET** /leads | Get a list of leads *LeadsApi* | **leadsGroupsGet** | **GET** /leads/groups | Get a list of available groups *LeadsApi* | **leadsLeadIdActivityCampaignGet** | **GET** /leads/{leadId}/activity/campaign | Get a list of all lead campaign activity *LeadsApi* | **leadsLeadIdActivityDeletionGet** | **GET** /leads/{leadId}/activity/deletion | Get a list of all lead deletion activity *LeadsApi* | **leadsLeadIdActivityDuplicatesGet** | **GET** /leads/{leadId}/activity/duplicates | Get a list of all lead duplicate activity *LeadsApi* | **leadsLeadIdActivityLinksGet** | **GET** /leads/{leadId}/activity/links | Get a list of all lead links activity *LeadsApi* | **leadsLeadIdActivitySourceGet** | **GET** /leads/{leadId}/activity/source | Get a list of all lead source activity *LeadsApi* | **leadsLeadIdActivityStatusGet** | **GET** /leads/{leadId}/activity/status | Get a list of all lead status activity *LeadsApi* | **leadsLeadIdApplicationsApplicationIdPopulatePost** | **POST** /leads/{leadId}/applications/{applicationId}/populate | Populate PDF Document *LeadsApi* | **leadsLeadIdAppointmentsGet** | **GET** /leads/{leadId}/appointments | Get lead appointments *LeadsApi* | **leadsLeadIdAppointmentsPost** | **POST** /leads/{leadId}/appointments | Create a lead appointment *LeadsApi* | **leadsLeadIdDocumentsDocumentIdGet** | **GET** /leads/{leadId}/documents/{documentId} | Download a document *LeadsApi* | **leadsLeadIdDocumentsGet** | **GET** /leads/{leadId}/documents | Get a list of available documents *LeadsApi* | **leadsLeadIdDocumentsPost** | **POST** /leads/{leadId}/documents | Upload a document *LeadsApi* | **leadsLeadIdEmailsTemplateIdPost** | **POST** /leads/{leadId}/emails/{templateId} | Send an email to lead with template *LeadsApi* | **leadsLeadIdGet** | **GET** /leads/{leadId} | Get detailed lead information *LeadsApi* | **leadsLeadIdMailboxEmailIdAttachmentAttachmentIdGet** | **GET** /leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId} | Download a mailbox email attachment *LeadsApi* | **leadsLeadIdNotesGet** | **GET** /leads/{leadId}/notes | Get lead notes *LeadsApi* | **leadsLeadIdNotesPost** | **POST** /leads/{leadId}/notes | Create a lead note *LeadsApi* | **leadsLeadIdPatch** | **PATCH** /leads/{leadId} | Update a lead *LeadsApi* | **leadsLeadIdSignaturesApplicationIdGeneratePost** | **POST** /leads/{leadId}/signatures/{applicationId}/generate | Generate an e-signature document *LeadsApi* | **leadsLeadIdSignaturesApplicationIdSendPost** | **POST** /leads/{leadId}/signatures/{applicationId}/send | Send an e-signature document *LeadsApi* | **leadsLeadIdSignaturesGet** | **GET** /leads/{leadId}/signatures | Get a list of all lead e-signatures documents *LeadsApi* | **leadsLeadIdSmsTemplateIdPost** | **POST** /leads/{leadId}/sms/{templateId} | Send an SMS to lead with selected SMS template *LeadsApi* | **leadsLeadIdTasksGet** | **POST** /leads/{leadId}/tasks | Create a lead task *LeadsApi* | **leadsLeadIdUsersGet** | **GET** /leads/{leadId}/users | Get a list of assigned users *LeadsApi* | **leadsLeadIdUsersPost** | **POST** /leads/{leadId}/users | Assign a user *LeadsApi* | **leadsLeadIdUsersUserIdDelete** | **DELETE** /leads/{leadId}/users/{userId} | Unassign a user from a lead *LeadsApi* | **leadsPost** | **POST** /leads | Create a lead *LeadsApi* | **leadsSignaturesApplicationIdDownloadGet** | **GET** /leads/signatures/{applicationId}/download | Download an e-signature document *LeadsApi* | **leadsSmsTemplatesGet** | **GET** /leads/sms/templates | Get list of SMS templates *LeadsApi* | **leadsSourcesGet** | **GET** /leads/sources | Get a list of available sources *LeadsApi* | **leadsStatusesGet** | **GET** /leads/statuses | Get a list of available statuses *LeadsApi* | **leadsUsersGet** | **GET** /leads/users | Get a list of available users *MerchantsApi* | **merchantsGet** | **GET** /merchants | Get a list of merchants *MerchantsApi* | **merchantsMerchantNumberChargebacksGet** | **GET** /merchants/{merchantNumber}/chargebacks | Get a list of chargebacks *MerchantsApi* | **merchantsMerchantNumberGet** | **GET** /merchants/{merchantNumber} | Get detailed merchant information *MerchantsApi* | **merchantsMerchantNumberPatch** | **PATCH** /merchants/{merchantNumber} | Update an existing merchant *MerchantsApi* | **merchantsMerchantNumberRetrievalsGet** | **GET** /merchants/{merchantNumber}/retrievals | Get a list of retrievals *MerchantsApi* | **merchantsMerchantNumberStatementsGet** | **GET** /merchants/{merchantNumber}/statements | Get a list of statements *MerchantsApi* | **merchantsMerchantNumberStatementsStatementIdGet** | **GET** /merchants/{merchantNumber}/statements/{statementId} | Download a statement *MerchantsApi* | **merchantsMerchantNumberTransactionsGet** | **GET** /merchants/{merchantNumber}/transactions | Get a list of batches and transactions *SubscriptionsApi* | **subscriptionsGet** | **GET** /subscriptions | Return a list of subscriptions *SubscriptionsApi* | **subscriptionsPost** | **POST** /subscriptions | Create a subscription *SubscriptionsApi* | **subscriptionsSampleApiUpdatedGet** | **GET** /subscriptions/sample/api.updated | Data sample for the \\&quot;api.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationCreatedGet** | **GET** /subscriptions/sample/turboapp.submitted | Data sample for the \\&quot;turboapp.submitted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationUpdatedGet** | **GET** /subscriptions/sample/turboapp.updated | Data sample for the \\&quot;turboapp.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadCreatedGet** | **GET** /subscriptions/sample/lead.created | Data sample for the \\&quot;lead.created\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDeletedGet** | **GET** /subscriptions/sample/lead.deleted | Data sample for the \\&quot;lead.deleted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDocumentUploadedGet** | **GET** /subscriptions/sample/lead.document.uploaded | Data sample for the \\&quot;lead.document.uploaded\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadEmailReceivedGet** | **GET** /subscriptions/sample/lead.email.received | Data sample for the \\&quot;lead.email.received\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadNoteAddedGet** | **GET** /subscriptions/sample/lead.note.added | Data sample for the \\&quot;lead.note.added\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadRestoredGet** | **GET** /subscriptions/sample/lead.restored | Data sample for the \\&quot;lead.restored\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadStatusUpdatedGet** | **GET** /subscriptions/sample/lead.status.updated | Data sample for the \\&quot;lead.status.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadUpdatedGet** | **GET** /subscriptions/sample/lead.updated | Data sample for the \\&quot;lead.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSubscriptionIdDelete** | **DELETE** /subscriptions/{subscriptionId} | Delete a subscription *SubscriptionsApi* | **subscriptionsSubscriptionIdGet** | **GET** /subscriptions/{subscriptionId} | Return a subscription by its id *SubscriptionsApi* | **subscriptionsSubscriptionIdPatch** | **PATCH** /subscriptions/{subscriptionId} | Update a subscription # Change Log   ### 1.14.0 (2022-08-23)   #### Updated:   * Added `details.fields.uid` field to the `Get detailed lead information` endpoint **Link:** [#/paths/~1leads~1{leadId}/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}/get)       ### 1.10.4 (2022-05-02)   #### Updated:   * Added a fields filter to a leads list endpoint **Link:** [#/paths/~1leads/get](https://www.mycoastalpay.com/api/#/paths/~1leads/get)       ### 1.10.3 (2022-04-29)   #### Updated:   * Added user activity indicator to the `get residuals line items` endpoint **Link:** [#/paths/~1residuals~1lineitems~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1residuals~1lineitems~1{year}~1{month}/get)       ### 1.10.2 (2022-04-29)   #### Updated:   * Updated endpoint Create Lead, added an users_emails field. **Link:** [#/paths/~1leads/post](https://www.mycoastalpay.com/api/#/paths/~1leads/post)       ### 1.10.1 (2022-04-29)   #### Updated:   * Updated endpoint Assign a user to a lead by email **Link:** [#/paths/~1leads~1{leadId}~1users/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1users/post)       ### 1.10.0 (2022-04-06)   #### Created:   * Added an endpoint for merchant creation and assigning users. **Link:** [#/paths/~1merchants/post](https://www.mycoastalpay.com/api/#/paths/~1merchants/post)   * Added an endpoint for getting assigned users to merchant **Link:** [#/paths/~1merchants~1{merchantNumber}~1users/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1users/get)   * Added an endpoint for updating merchant details **Link:** [#/paths/~1merchants~1{merchantNumber}~1details/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1details/post)   * Added an endpoint for transactions import **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/post)   * Added an endpoint for adjustments import **Link:** [#/paths/~1merchants~1{merchantNumber}~1adjustments/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1adjustments/post)   * Added an endpoint for getting a list of batches **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/get)   * Added an endpoint for getting a list of authorizations **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get)   * Added an endpoint for batches and authorizations import **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/post)   * Added an endpoint for chargebacks import **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/post)   * Added an endpoint for retrievals import **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/post)   * Added an endpoint for merchant statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/post)   * Added an endpoint for 1099k statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post)   * Added an endpoint for memos import **Link:** [#/paths/~1merchants~1{merchantNumber}~1memos/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1memos/post)   * Added an endpoint for getting Processor and DataSource available for assigning to merchants **Link:** [#/paths/~1processors/get](https://www.mycoastalpay.com/api/#/paths/~1processors/get)       ### 1.9.0 (2022-04-06)   #### Created:   * Added endpoint to get lead details from a specific tab **Link:** [#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get)       ### 1.7.0 (2021-12-08)   #### Updated:   * Added TurboApp Equipment Created event **Link:** [#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get)       ### 1.6.10 (2021-11-24)   #### Updated:   * Updated pagination on get list of statements endpoint. **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/get)       ### 1.6.9 (2021-08-02)   #### Updated:   * Added `void_reject_chargeback` property to the batches and transactions list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.8 (2021-08-04)   #### Created:   * Added `Delete record from a lead record set` endpoint **Link:** [#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete)       ### 1.6.7 (2021-07-20)   #### Updated:   * Added `unassigned` property to the chargebacks list response. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.6.6 (2021-07-14)   #### Updated:   * Added `adjustments` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.5 (2021-07-02)   #### Updated:   * Added `type` property to the chargebacks list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.6.4 (2021-05-06)   #### Updated:   * Added `terminal_number` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.3 (2021-04-26)   #### Updated:   * Added `created_username`,`modified_username`, and `resolved_username` properties to the ticket creation endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `created_username`,`modified_username`, and `resolved_username` to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.6.2 (2021-05-31)   #### Created:   * Added `end_date` filter to deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)       ### 1.6.1 (2021-04-02)   #### Updated:   * Increased API Rate limit to 500 request per minute **Link:** [#section/Limiting](https://www.mycoastalpay.com/api/#section/Limiting)       ### 1.6.0 (2021-03-02)   #### Created:   * Added `Get pricing templates` endpoint **Link:** [#/paths/~1leads~1pricing_templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1pricing_templates/get)       ### 1.5.21 (2021-03-19)   #### Updated:   * Added new properties to the chargebacks list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added new properties to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)       ### 1.5.20 (2021-02-12)   #### Updated:   * Added `filename` property to the `lead.document.uploaded` subscription response **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)       ### 1.5.19 (2021-02-17)   #### Updated:   * Added deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)   * Added `authorization_code` property to the chargeback response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.5.18 (2021-01-14)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.5.17 (2021-03-17)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)   * Added `id` and `reply_form` properties to the chargebacks response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added the `id` property to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)     #### Created:   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get)   * Added an endpoint for Reply To Chargeback Case - Dispute Chargeback Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post)   * Added an endpoint for Reply To Chargeback Case - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Chargeback Case - Accept Chargeback **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post)   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response with Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Fulfill Retrieval Case Request **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Locate Retrieval Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post)   * Added an endpoint for Reply To Retrieval - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Retrieval Case - Imprint and Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post)   * Added an endpoint for Reply To Retrieval Case - Responding by Other Means **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post)   * Added an endpoint for Reply To Retrieval Case - Add User Notes/Images **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post)   * Added an endpoint for the file upload **Link:** [#/paths/~1merchants~1files/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1files/post)   * Added an endpoint for Download chargeback case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get)   * Added an endpoint for Download retrieval case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get)   * Added new subscription for receiving a notification when a new chargeback case created **Link:** [#/paths/~1subscriptions~1sample~1chargeback.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.added/get)   * Added new subscription for receiving a notification when chargeback case status changed **Link:** [#/paths/~1subscriptions~1sample~1chargeback.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the chargeback case due date **Link:** [#/paths/~1subscriptions~1sample~1chargeback.reminder/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.reminder/get)   * Added new subscription for receiving a notification when a new retrieval case created **Link:** [#/paths/~1subscriptions~1sample~1retrieval.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.added/get)   * Added new subscription for receiving a notification when retrieval case status changed **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the retrieval case due date **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)       ### 1.5.16 (2020-12-11)   #### Updated:   * Renamed task priority from \"Low\" to \"Normal\" **Link:** [#/paths/~1leads~1{leadId}~1tasks/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tasks/post)       ### 1.5.15 (2021-01-18)   #### Updated:   * Added `due` value for `sort_by` and `date_filter` parameters on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `only_business_days` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `only_business_days` property to the Ticket on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `only_business_days` property to the Ticket Type on the get a list of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/get)   * Added `only_business_days` parameter on the get detailed information of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `only_business_days` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `only_business_days` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `attached_files` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `attached_files` property to the Ticket Comment on the Comment create endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)       ### 1.5.14 (2020-11-26)   #### Updated:   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of the ticket create response **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket details response **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket update response **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket's checklist updated subscription response **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.13 (2020-11-20)   #### Updated:   * Added `priority` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `priority` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.12 (2020-11-02)   #### Updated:   * Changed `due_date` property to the datetime format on the ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Changed `due_date` property to the datetime format on the ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.11 (2020-10-20)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.10 (2020-10-19)   #### Updated:   * Added `group_id` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `group_id` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.9 (2020-11-02)   #### Updated:   * Added `new_files` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `new_files` property for ticket type update payload. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.8 (2020-10-20)   #### Updated:   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `preview_images` property for ticket comment request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket and ticket comment properties. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.7 (2020-10-05)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.5 (2020-07-23)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1leads~1file_labels/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1file_labels/get)       ### 1.5.5 (2020-10-20)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1helpdesk~1{ticketId}~1assignments/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1assignments/get)       ### 1.5.4 (2020-07-13)   #### Updated:   * Added `files_count` property to the ticket create endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files_count` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `files_count` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files_count` property to the ticket update endpoint response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files_count` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files_count` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files_count` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files_count` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.3 (2020-07-06)   #### Updated:   * Added `search` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.5.2 (2020-07-10)   #### Updated:   * Added `due_date` property to the ticket create endpoint request and response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `due_date` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due_date` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `due_date` property to the ticket update endpoint request and response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `due_date` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `due_date` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `due_date` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `due_date` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.1 (2020-08-10)   #### Created:   * Added a Residuals API to work with your residuals reports. **Link:** [#tag/Residuals](https://www.mycoastalpay.com/api/#tag/Residuals)       ### 1.4.9 (2020-06-26)   #### Updated:   * Added `hide_resolved` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.8 (2020-06-12)   #### Updated:   * Added `set_for`, `set_at`, `set_by`, `modified`, `modified_by`, `date_end`, `confirmed_by`, `seen_by`, `rescheduled`, `rescheduled_by`, and `rescheduled_count` properties to the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added `set_for`, `set_by`, `modified_by`, `confirmed_by`, `seen_by`, `rescheduled_by`, `rescheduled_count`,  `date_filter`, `start_date`, `end_date`, and `done` filters to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added sorting to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Marked `user` property as deprecated on the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)       ### 1.4.7 (2020-05-13)   #### Updated:   * Added `old_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)   * Added `new_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)       ### 1.4.6 (2020-05-01)   #### Created:   * Added `lead.signature.generated` subscription endpoint. **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.generated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.generated/get)   * Added `lead.signature.opened` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.opened/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.opened/get)   * Added `lead.signature.signed` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.signed/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.signed/get)     #### Updated:   * Added `createdAt` and `createdBy` properties to the `lead.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.deleted` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.restored` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `createdAt` and `createdBy` properties to the `lead.status.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.4.5 (2020-04-21)   #### Updated:   * Added `files` property to the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `file` property for each checklist item in the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files` property to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property for each comment in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `file` property for each checklist item in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files` property for each comment in the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the Helpdesk ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the ticket type creation details endpoint response. **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `file` property for each checklist item on the ticket type endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `file` property for each checklist item on the ticket type update endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `files` property for ticket created subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files` property for ticket updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files` property for ticket resolved subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files` property for ticket commented subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `files` property for ticket checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `file` property for each checklist item on checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)     #### Created:   * Added endpoint for download attachments from Ticket Type **Link:** [#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get)       ### 1.4.4 (2020-04-02)   #### Updated:   * Added `resolver` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.3 (2020-04-01)   #### Updated:   * Added `status_updated` option for `date_filter` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.2 (2020-03-27)   #### Updated:   * Added `lid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `mid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.1 (2020-03-20)   #### Updated:   * Added `hash` and `url` properties to the 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.4.0 (2020-03-05)   #### Updated:   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.created/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.deleted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.restored` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.status.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.note.added` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.note.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.note.added/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.document.uploaded` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.email.received` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.email.received/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.email.received/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.resolved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.commented` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.checklist.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.submitted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.approved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.declined` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)   * Changed all subscriptions dates properties to the snake case **Link:** [#tag/Subscriptions](https://www.mycoastalpay.com/api/#tag/Subscriptions)       ### 1.3.5 (2020-02-26)   #### Created:   * Added a Helpdesk API to work with your helpdesk data. **Link:** [#tag/Helpdesk](https://www.mycoastalpay.com/api/#tag/Helpdesk)       ### 1.3.4 (2020-02-25)   #### Updated:   * Added a `lid` property to the \"turboapp.submitted\" subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)       ### 1.3.3 (2020-02-24)   #### Updated:   * Added a `salesRep` parameter to 'lead.status.updated' subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.3.2 (2019-11-21)   #### Updated:   * Added a `expire` parameter to 'Generate an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post)   * Added the ability to add multiple signers to the document and added an `expire` parameter to 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.3.1 (2019-11-18)   #### Updated:   * Rename subscriptions from \"application.created\" to \"turboapp.submitted\" and \"application.updated\" to \"turboapp.updated\". **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)     #### Created:   * Added new subscriptions for \"turboapp.approved\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added new subscriptions for \"turboapp.declined\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)       ### 1.2.2 (2019-09-03)   #### Updated:   * Added a `per_page` property to all list endpoints.       ### 1.2.1 (2019-08-26)   #### Updated:   * Added a `leads` property to merchants endpoint. **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.2.0 (2019-07-26)   #### Updated:   * The endpoint for creating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions/post](https://www.mycoastalpay.com/api/#/paths/~1subscriptions/post)   * The endpoint for updating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions~1{subscriptionId}/patch](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1{subscriptionId}/patch)       ### 1.1.0 (2019-07-24)   #### Created:   * Added an endpoint for getting SMS templates. **Link:** [#/paths/~1leads~1sms~1templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1sms~1templates/get)   * Added new subscriptions for `application.created` event **Link:** [#/paths/~1subscriptions~1sample~1application.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.created/get)   * Added new subscriptions for `application.updated` event **Link:** [#/paths/~1subscriptions~1sample~1application.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.updated/get)     #### Updated:   * Added a `sic_code` property to merchants endpoint **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.0.0 (2019-06-20)   #### Created:   * Added change log.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


import json
import atexit
import mimetypes
from multiprocessing.pool import ThreadPool
import io
import os
import re
import typing
from urllib.parse import quote
from urllib3.fields import RequestField


from iriscrm import rest
from iriscrm.configuration import Configuration
from iriscrm.exceptions import ApiTypeError, ApiValueError, ApiException
from iriscrm.model_utils import (
    ModelNormal,
    ModelSimple,
    ModelComposed,
    check_allowed_values,
    check_validations,
    date,
    datetime,
    deserialize_file,
    file_type,
    model_to_dict,
    none_type,
    validate_and_convert_types
)


class ApiClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    _pool = None

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1):
        if configuration is None:
            configuration = Configuration.get_default_copy()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _content_type: typing.Optional[str] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            post_params.extend(self.files_parameters(files))
            if header_params['Content-Type'].startswith("multipart"):
                post_params = self.parameters_to_multipart(post_params,
                                                           (dict))

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # auth setting
        self.update_params_for_auth(header_params, query_params,
                                    auth_settings, resource_path, method, body,
                                    request_auths=_request_auths)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        try:
            # perform request and return response
            response_data = self.request(
                method, url, query_params=query_params, headers=header_params,
                post_params=post_params, body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout)
        except ApiException as e:
            e.body = e.body.decode('utf-8')
            raise e

        self.last_response = response_data

        return_data = response_data

        if not _preload_content:
            return (return_data)
            return return_data

        # deserialize response data
        if response_type:
            if response_type != (file_type,):
                encoding = "utf-8"
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
                    if match:
                        encoding = match.group(1)
                response_data.data = response_data.data.decode(encoding)

            return_data = self.deserialize(
                response_data,
                response_type,
                _check_type
            )
        else:
            return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def parameters_to_multipart(self, params, collection_types):
        """Get parameters as list of tuples, formatting as json if value is collection_types

        :param params: Parameters as list of two-tuples
        :param dict collection_types: Parameter collection types
        :return: Parameters as list of tuple or urllib3.fields.RequestField
        """
        new_params = []
        if collection_types is None:
            collection_types = (dict)
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if isinstance(
                     v, collection_types): # v is instance of collection_type, formatting as application/json
                v = json.dumps(v, ensure_ascii=False).encode("utf-8")
                field = RequestField(k, v)
                field.make_multipart(content_type="application/json; charset=utf-8")
                new_params.append(field)
            else:
                new_params.append((k, v))
        return new_params

    @classmethod
    def sanitize_for_serialization(cls, obj):
        """Prepares data for transmission before it is sent with the rest client
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.
        If obj is io.IOBase, return the bytes
        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if isinstance(obj, (ModelNormal, ModelComposed)):
            return {
                key: cls.sanitize_for_serialization(val) for key,
                val in model_to_dict(
                    obj,
                    serialize=True).items()}
        elif isinstance(obj, io.IOBase):
            return cls.get_file_data_and_close_file(obj)
        elif isinstance(obj, (str, int, float, none_type, bool)):
            return obj
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, ModelSimple):
            return cls.sanitize_for_serialization(obj.value)
        elif isinstance(obj, (list, tuple)):
            return [cls.sanitize_for_serialization(item) for item in obj]
        if isinstance(obj, dict):
            return {key: cls.sanitize_for_serialization(val) for key, val in obj.items()}
        raise ApiValueError(
            'Unable to prepare type {} for serialization'.format(
                obj.__class__.__name__))

    def deserialize(self, response, response_type, _check_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param _check_type: boolean, whether to check the types of the data
            received from the server
        :type _check_type: bool

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == (file_type,):
            content_disposition = response.getheader("Content-Disposition")
            return deserialize_file(response.data, self.configuration,
                                    content_disposition=content_disposition)

        # fetch data from response object
        try:
            received_data = json.loads(response.data)
        except ValueError:
            received_data = response.data

        # store our data under the key of 'received_data' so users have some
        # context if they are deserializing a string and the data type is wrong
        deserialized_data = validate_and_convert_types(
            received_data,
            response_type,
            ['received_data'],
            True,
            _check_type,
            configuration=self.configuration
        )
        return deserialized_data

    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        async_req: typing.Optional[bool] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param files: key -> field name, value -> a list of open file
            objects for `multipart/form-data`.
        :type files: dict
        :param async_req bool: execute request asynchronously
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :type collection_formats: dict, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _check_type: boolean describing if the data back from the server
            should have its type checked.
        :type _check_type: bool, optional
        :param _request_auths: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auths: list, optional
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout, _host,
                                   _check_type, _request_auths=_request_auths)

        return self.pool.apply_async(self.__call_api, (resource_path,
                                                       method, path_params,
                                                       query_params,
                                                       header_params, body,
                                                       post_params, files,
                                                       response_type,
                                                       auth_settings,
                                                       _return_http_data_only,
                                                       collection_formats,
                                                       _preload_content,
                                                       _request_timeout,
                                                       _host, _check_type, None, _request_auths))

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    @staticmethod
    def get_file_data_and_close_file(file_instance: io.IOBase) -> bytes:
        file_data = file_instance.read()
        file_instance.close()
        return file_data

    def files_parameters(self,
                         files: typing.Optional[typing.Dict[str,
                                                            typing.List[io.IOBase]]] = None):
        """Builds form parameters.

        :param files: None or a dict with key=param_name and
            value is a list of open file objects
        :return: List of tuples of form parameters with file data
        """
        if files is None:
            return []

        params = []
        for param_name, file_instances in files.items():
            if file_instances is None:
                # if the file field is nullable, skip None values
                continue
            for file_instance in file_instances:
                if file_instance is None:
                    # if the file field is nullable, skip None values
                    continue
                if file_instance.closed is True:
                    raise ApiValueError(
                        "Cannot read a closed file. The passed in file_type "
                        "for %s must be open." % param_name
                    )
                filename = os.path.basename(file_instance.name)
                filedata = self.get_file_data_and_close_file(file_instance)
                mimetype = (mimetypes.guess_type(filename)[0] or
                            'application/octet-stream')
                params.append(
                    tuple([param_name, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types, method=None, body=None):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :param method: http method (e.g. POST, PATCH).
        :param body: http body to send.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        content_types = [x.lower() for x in content_types]

        if (method == 'PATCH' and
                'application/json-patch+json' in content_types and
                isinstance(body, list)):
            return 'application/json-patch+json'

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, queries, auth_settings,
                               resource_path, method, body, request_auths=None):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :param resource_path: A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method.
        :param body: A object representing the body of the HTTP request.
            The object type is the return value of _encoder.default().
        :param request_auths: if set, the provided settings will
            override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auths:
            for auth_setting in request_auths:
                self._apply_auth_params(
                    headers, queries, resource_path, method, body, auth_setting)
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                self._apply_auth_params(
                    headers, queries, resource_path, method, body, auth_setting)

    def _apply_auth_params(self, headers, queries, resource_path, method, body, auth_setting):
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['key'] + "=" + auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (tuple/None): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only',
            '_check_input_type',
            '_check_return_type',
            '_content_type',
            '_spec_property_naming',
            '_request_auths'
        ])
        self.params_map['nullable'].extend(['_request_timeout'])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        extra_types = {
            'async_req': (bool,),
            '_host_index': (none_type, int),
            '_preload_content': (bool,),
            '_request_timeout': (none_type, float, (float,), [float], int, (int,), [int]),
            '_return_http_data_only': (bool,),
            '_check_input_type': (bool,),
            '_check_return_type': (bool,),
            '_spec_property_naming': (bool,),
            '_content_type': (none_type, str),
            '_request_auths': (none_type, list)
        }
        self.openapi_types.update(extra_types)
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param],
                    configuration=self.api_client.configuration
                )

        if kwargs['_check_input_type'] is False:
            return

        for key, value in kwargs.items():
            fixed_val = validate_and_convert_types(
                value,
                self.openapi_types[key],
                [key],
                kwargs['_spec_property_naming'],
                kwargs['_check_input_type'],
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in kwargs.items():
            param_location = self.location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == (file_type,)):
                    params['file'][base_name] = [param_value]
                elif (param_location == 'form' and
                        self.openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][base_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:

        api_instance = ESignatureApi()
        api_instance.leads_applications_app_id_mappings_get  # this is an instance of the class Endpoint
        api_instance.leads_applications_app_id_mappings_get()  # this invokes api_instance.leads_applications_app_id_mappings_get.__call__()
        which then invokes the callable functions stored in that endpoint at
        api_instance.leads_applications_app_id_mappings_get.callable or self.callable in this class

        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        try:
            index = self.api_client.configuration.server_operation_index.get(
                self.settings['operation_id'], self.api_client.configuration.server_index
            ) if kwargs['_host_index'] is None else kwargs['_host_index']
            server_variables = self.api_client.configuration.server_operation_variables.get(
                self.settings['operation_id'], self.api_client.configuration.server_variables
            )
            _host = self.api_client.configuration.get_host_from_settings(
                index, variables=server_variables, servers=self.settings['servers']
            )
        except IndexError:
            if self.settings['servers']:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(self.settings['servers'])
                )
            _host = None

        for key, value in kwargs.items():
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    " to method `%s`" %
                    (key, self.settings['operation_id'])
                )
            # only throw this nullable ApiValueError if _check_input_type
            # is False, if _check_input_type==True we catch this case
            # in self.__validate_inputs
            if (key not in self.params_map['nullable'] and value is None
                    and kwargs['_check_input_type'] is False):
                raise ApiValueError(
                    "Value may not be None for non-nullable parameter `%s`"
                    " when calling `%s`" %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    "Missing the required parameter `%s` when calling "
                    "`%s`" % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        if kwargs.get('_content_type'):
            params['header']['Content-Type'] = kwargs['_content_type']
        else:
            content_type_headers_list = self.headers_map['content_type']
            if content_type_headers_list:
                if params['body'] != "":
                    content_types_list = self.api_client.select_header_content_type(
                        content_type_headers_list, self.settings['http_method'],
                        params['body'])
                    if content_types_list:
                        params['header']['Content-Type'] = content_types_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs['async_req'],
            _check_type=kwargs['_check_return_type'],
            _return_http_data_only=kwargs['_return_http_data_only'],
            _preload_content=kwargs['_preload_content'],
            _request_timeout=kwargs['_request_timeout'],
            _host=_host,
            _request_auths=kwargs['_request_auths'],
            collection_formats=params['collection_format'])

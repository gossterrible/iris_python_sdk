"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete) ### You can use the Helpdesk API to: - [Create a new ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk/post) - [Get a list of helpdesk tickets](https://www.mycoastalpay.com/api#/paths/~1helpdesk/get) - [Add a ticket comment](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1comment/post) - [Get detailed ticked information](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/get) - [Update a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/patch) - [Delete a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/delete) - [Upload an attachment to a ticket, comment, checklist, or ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1file/post) - [Download an attachment from a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1download~1{attachmentId}/get) - [Create a new helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/post) - [Get a list of helpdesk ticket types](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/get) - [Get details for a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/get) - [Update a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/patch) - [Delete a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/delete) - [Download an attachment from a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get) - [Get a list of available users to notify and assign](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1users/get) ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  ### You can use the Merchant API to: - [Get a list of merchants](https://www.mycoastalpay.com/api#/paths/~1merchants/get) - [Get detailed merchant information](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/get) - [Update an existing merchant](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/patch) - [Get a list of batches and transactions](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1transactions/get) - [Get a list of chargebacks](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1chargebacks/get) - [Get a list of retrievals](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1retrievals/get) - [Get a list of statements](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements/get) - [Download a statement](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements~1{statementId}/get) ### You can use the Residuals API to: - [Get residuals summary data](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1{year}~1{month}/get) - [Get residuals summary with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1rows~1{processor_id}~1{year}~1{month}/get) - [Get residuals details with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1details~1{processor_id}~1{year}~1{month}/get) - [Get residuals line items](https://www.mycoastalpay.com/api#/paths/~1residuals~1lineitems~1{year}~1{month}/get) - [Get residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1/get) - [Get a list of users with assigned residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1assigned~1{year}~1{month}/get)   # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.  Then open the ** API Settings ** tab, click ** Create New API Token **, configure your token’s settings as needed, and click ** Add New Token **:  <img src='https://www.mycoastalpay.com/images/docs/mapi001.png'/>  Your new token will now be created and displayed in a popup window:  <img src='https://www.mycoastalpay.com/images/docs/mapi002.png'/>  Once the token is created, it will be shown in the list of available API Tokens where you can copy the token, update its settings, or delete it once it’s no longer needed:  <img src='https://www.mycoastalpay.com/images/docs/mapi003.png'/>  ** Note: ** The created tokens will inherit the user’s permissions to assigned merchants, leads, groups and processors. # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # PHP SDK  ### Installation and Usage  #### Availability  The IRIS CRM PHP SDK requires PHP version 5.5 or higher and the PHP cURL extension.  #### Composer  To install the bindings via [Composer](http://getcomposer.org/), please run:  ```bash  composer require iris-crm/php-sdk      ```   In your code, configure the environment and API credentials:  ```php require_once(__DIR__ . '/vendor/autoload.php');  use Swagger\\Client\\Configuration; use Swagger\\Client\\Api\\LeadsApi;  // Configure API key authorization $config = Configuration::getDefaultConfiguration() ->setApiKey('X-API-KEY', 'YOUR_API_KEY') ->setHost('https://www.mycoastalpay.com/api/v1/'); ``` Here’s an example of how to get a list of leads using an SDK. Swagger\\Client\\Api\\LeadsApi it's a SDK Class for Lead endpoints. ```php $apiInstance = new LeadsApi(null, $config);  $page        = 1; // int | Page number $sort_by     = \"created\"; // string | Sorting of leads by the field value $sort_dir    = \"asc\"; // string | Direction of sorting $group       = 2; // int | Filter leads by a group id $campaign    = 3; // int | Filter leads by a campaign id $source      = 4; // int | Filter leads by a source id $status      = 1; // int | Filter leads by a status id $category    = 1; // int | Filter leads by a status category id $user        = 12; // int | Filter leads by a user id $date_filter = \"created\"; // string | Filtering leads by a date range depends on this filter $start_date  = new \\DateTime(\"2018-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $end_date    = new \\DateTime(\"2019-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $email       = \"test@mail.com\"; // string | Filter leads by a email try {     $result = $apiInstance->leadsGet($page, $sort_by, $sort_dir, $group, $campaign, $source, $status, $category, $user, $date_filter, $start_date, $end_date, $email);     print_r($result); } catch (Exception $e) {     echo 'Exception when calling LeadsApi->leadsGet: ' . $e->getMessage() . PHP_EOL; } ``` All parameters for leadsGet method is optional and can be skipped.  If you want skip some parameters - you need to set parameter to `null`  All available classes and methods you can get in \"API Endpoints\" section below. ### API Endpoints All URIs are relative to *https://www.mycoastalpay.com/api/v1*  Class | Method | HTTP Request | Description ------------ | ------------- | ------------- | ------------- *LeadsApi* | **leadsApplicationsAppIdMappingsGet** | **GET** /leads/applications/{appId}/mappings | Get a list of available application field mappings *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdDelete** | **DELETE** /leads/applications/{appId}/mappings/{mapId} | Delete an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdGet** | **GET** /leads/applications/{appId}/mappings/{mapId} | Get an application field mapping list *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdPatch** | **PATCH** /leads/applications/{appId}/mappings/{mapId} | Update an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsPost** | **POST** /leads/applications/{appId}/mappings | Create a new application field mapping *LeadsApi* | **leadsApplicationsGet** | **GET** /leads/applications | Get a list of available applications *LeadsApi* | **leadsCampaignsGet** | **GET** /leads/campaigns | Get a list of available campaigns *LeadsApi* | **leadsDynamicFieldsSchemaGet** | **GET** /leads/dynamic-fields-schema | Get a schema of lead fields *LeadsApi* | **leadsEmailsTemplatesGet** | **GET** /leads/emails/templates | Get a list of email templates *LeadsApi* | **leadsFieldsFieldIdGet** | **GET** /leads/fields/{fieldId} | Get a lead field *LeadsApi* | **leadsFieldsFieldIdOrderPatch** | **PATCH** /leads/fields/{fieldId}/order | Update a lead field order position *LeadsApi* | **leadsFieldsFieldIdPatch** | **PATCH** /leads/fields/{fieldId} | Update a lead field *LeadsApi* | **leadsFieldsGet** | **GET** /leads/fields | Get a list of available lead fields *LeadsApi* | **leadsFieldsPost** | **POST** /leads/fields | Create a new lead field *LeadsApi* | **leadsFieldsTabsGet** | **GET** /leads/fields/tabs | Get a list of all lead field tabs *LeadsApi* | **leadsFieldsTabsPost** | **POST** /leads/fields/tabs | Create a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdGet** | **GET** /leads/fields/tabs/{tabId} | Get a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdPatch** | **PATCH** /leads/fields/tabs/{tabId} | Update a lead field tab *LeadsApi* | **leadsGet** | **GET** /leads | Get a list of leads *LeadsApi* | **leadsGroupsGet** | **GET** /leads/groups | Get a list of available groups *LeadsApi* | **leadsLeadIdActivityCampaignGet** | **GET** /leads/{leadId}/activity/campaign | Get a list of all lead campaign activity *LeadsApi* | **leadsLeadIdActivityDeletionGet** | **GET** /leads/{leadId}/activity/deletion | Get a list of all lead deletion activity *LeadsApi* | **leadsLeadIdActivityDuplicatesGet** | **GET** /leads/{leadId}/activity/duplicates | Get a list of all lead duplicate activity *LeadsApi* | **leadsLeadIdActivityLinksGet** | **GET** /leads/{leadId}/activity/links | Get a list of all lead links activity *LeadsApi* | **leadsLeadIdActivitySourceGet** | **GET** /leads/{leadId}/activity/source | Get a list of all lead source activity *LeadsApi* | **leadsLeadIdActivityStatusGet** | **GET** /leads/{leadId}/activity/status | Get a list of all lead status activity *LeadsApi* | **leadsLeadIdApplicationsApplicationIdPopulatePost** | **POST** /leads/{leadId}/applications/{applicationId}/populate | Populate PDF Document *LeadsApi* | **leadsLeadIdAppointmentsGet** | **GET** /leads/{leadId}/appointments | Get lead appointments *LeadsApi* | **leadsLeadIdAppointmentsPost** | **POST** /leads/{leadId}/appointments | Create a lead appointment *LeadsApi* | **leadsLeadIdDocumentsDocumentIdGet** | **GET** /leads/{leadId}/documents/{documentId} | Download a document *LeadsApi* | **leadsLeadIdDocumentsGet** | **GET** /leads/{leadId}/documents | Get a list of available documents *LeadsApi* | **leadsLeadIdDocumentsPost** | **POST** /leads/{leadId}/documents | Upload a document *LeadsApi* | **leadsLeadIdEmailsTemplateIdPost** | **POST** /leads/{leadId}/emails/{templateId} | Send an email to lead with template *LeadsApi* | **leadsLeadIdGet** | **GET** /leads/{leadId} | Get detailed lead information *LeadsApi* | **leadsLeadIdMailboxEmailIdAttachmentAttachmentIdGet** | **GET** /leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId} | Download a mailbox email attachment *LeadsApi* | **leadsLeadIdNotesGet** | **GET** /leads/{leadId}/notes | Get lead notes *LeadsApi* | **leadsLeadIdNotesPost** | **POST** /leads/{leadId}/notes | Create a lead note *LeadsApi* | **leadsLeadIdPatch** | **PATCH** /leads/{leadId} | Update a lead *LeadsApi* | **leadsLeadIdSignaturesApplicationIdGeneratePost** | **POST** /leads/{leadId}/signatures/{applicationId}/generate | Generate an e-signature document *LeadsApi* | **leadsLeadIdSignaturesApplicationIdSendPost** | **POST** /leads/{leadId}/signatures/{applicationId}/send | Send an e-signature document *LeadsApi* | **leadsLeadIdSignaturesGet** | **GET** /leads/{leadId}/signatures | Get a list of all lead e-signatures documents *LeadsApi* | **leadsLeadIdSmsTemplateIdPost** | **POST** /leads/{leadId}/sms/{templateId} | Send an SMS to lead with selected SMS template *LeadsApi* | **leadsLeadIdTasksGet** | **POST** /leads/{leadId}/tasks | Create a lead task *LeadsApi* | **leadsLeadIdUsersGet** | **GET** /leads/{leadId}/users | Get a list of assigned users *LeadsApi* | **leadsLeadIdUsersPost** | **POST** /leads/{leadId}/users | Assign a user *LeadsApi* | **leadsLeadIdUsersUserIdDelete** | **DELETE** /leads/{leadId}/users/{userId} | Unassign a user from a lead *LeadsApi* | **leadsPost** | **POST** /leads | Create a lead *LeadsApi* | **leadsSignaturesApplicationIdDownloadGet** | **GET** /leads/signatures/{applicationId}/download | Download an e-signature document *LeadsApi* | **leadsSmsTemplatesGet** | **GET** /leads/sms/templates | Get list of SMS templates *LeadsApi* | **leadsSourcesGet** | **GET** /leads/sources | Get a list of available sources *LeadsApi* | **leadsStatusesGet** | **GET** /leads/statuses | Get a list of available statuses *LeadsApi* | **leadsUsersGet** | **GET** /leads/users | Get a list of available users *MerchantsApi* | **merchantsGet** | **GET** /merchants | Get a list of merchants *MerchantsApi* | **merchantsMerchantNumberChargebacksGet** | **GET** /merchants/{merchantNumber}/chargebacks | Get a list of chargebacks *MerchantsApi* | **merchantsMerchantNumberGet** | **GET** /merchants/{merchantNumber} | Get detailed merchant information *MerchantsApi* | **merchantsMerchantNumberPatch** | **PATCH** /merchants/{merchantNumber} | Update an existing merchant *MerchantsApi* | **merchantsMerchantNumberRetrievalsGet** | **GET** /merchants/{merchantNumber}/retrievals | Get a list of retrievals *MerchantsApi* | **merchantsMerchantNumberStatementsGet** | **GET** /merchants/{merchantNumber}/statements | Get a list of statements *MerchantsApi* | **merchantsMerchantNumberStatementsStatementIdGet** | **GET** /merchants/{merchantNumber}/statements/{statementId} | Download a statement *MerchantsApi* | **merchantsMerchantNumberTransactionsGet** | **GET** /merchants/{merchantNumber}/transactions | Get a list of batches and transactions *SubscriptionsApi* | **subscriptionsGet** | **GET** /subscriptions | Return a list of subscriptions *SubscriptionsApi* | **subscriptionsPost** | **POST** /subscriptions | Create a subscription *SubscriptionsApi* | **subscriptionsSampleApiUpdatedGet** | **GET** /subscriptions/sample/api.updated | Data sample for the \\&quot;api.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationCreatedGet** | **GET** /subscriptions/sample/turboapp.submitted | Data sample for the \\&quot;turboapp.submitted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationUpdatedGet** | **GET** /subscriptions/sample/turboapp.updated | Data sample for the \\&quot;turboapp.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadCreatedGet** | **GET** /subscriptions/sample/lead.created | Data sample for the \\&quot;lead.created\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDeletedGet** | **GET** /subscriptions/sample/lead.deleted | Data sample for the \\&quot;lead.deleted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDocumentUploadedGet** | **GET** /subscriptions/sample/lead.document.uploaded | Data sample for the \\&quot;lead.document.uploaded\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadEmailReceivedGet** | **GET** /subscriptions/sample/lead.email.received | Data sample for the \\&quot;lead.email.received\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadNoteAddedGet** | **GET** /subscriptions/sample/lead.note.added | Data sample for the \\&quot;lead.note.added\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadRestoredGet** | **GET** /subscriptions/sample/lead.restored | Data sample for the \\&quot;lead.restored\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadStatusUpdatedGet** | **GET** /subscriptions/sample/lead.status.updated | Data sample for the \\&quot;lead.status.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadUpdatedGet** | **GET** /subscriptions/sample/lead.updated | Data sample for the \\&quot;lead.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSubscriptionIdDelete** | **DELETE** /subscriptions/{subscriptionId} | Delete a subscription *SubscriptionsApi* | **subscriptionsSubscriptionIdGet** | **GET** /subscriptions/{subscriptionId} | Return a subscription by its id *SubscriptionsApi* | **subscriptionsSubscriptionIdPatch** | **PATCH** /subscriptions/{subscriptionId} | Update a subscription # Change Log   ### 1.14.0 (2022-08-23)   #### Updated:   * Added `details.fields.uid` field to the `Get detailed lead information` endpoint **Link:** [#/paths/~1leads~1{leadId}/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}/get)       ### 1.10.4 (2022-05-02)   #### Updated:   * Added a fields filter to a leads list endpoint **Link:** [#/paths/~1leads/get](https://www.mycoastalpay.com/api/#/paths/~1leads/get)       ### 1.10.3 (2022-04-29)   #### Updated:   * Added user activity indicator to the `get residuals line items` endpoint **Link:** [#/paths/~1residuals~1lineitems~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1residuals~1lineitems~1{year}~1{month}/get)       ### 1.10.2 (2022-04-29)   #### Updated:   * Updated endpoint Create Lead, added an users_emails field. **Link:** [#/paths/~1leads/post](https://www.mycoastalpay.com/api/#/paths/~1leads/post)       ### 1.10.1 (2022-04-29)   #### Updated:   * Updated endpoint Assign a user to a lead by email **Link:** [#/paths/~1leads~1{leadId}~1users/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1users/post)       ### 1.10.0 (2022-04-06)   #### Created:   * Added an endpoint for merchant creation and assigning users. **Link:** [#/paths/~1merchants/post](https://www.mycoastalpay.com/api/#/paths/~1merchants/post)   * Added an endpoint for getting assigned users to merchant **Link:** [#/paths/~1merchants~1{merchantNumber}~1users/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1users/get)   * Added an endpoint for updating merchant details **Link:** [#/paths/~1merchants~1{merchantNumber}~1details/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1details/post)   * Added an endpoint for transactions import **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/post)   * Added an endpoint for adjustments import **Link:** [#/paths/~1merchants~1{merchantNumber}~1adjustments/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1adjustments/post)   * Added an endpoint for getting a list of batches **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/get)   * Added an endpoint for getting a list of authorizations **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get)   * Added an endpoint for batches and authorizations import **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/post)   * Added an endpoint for chargebacks import **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/post)   * Added an endpoint for retrievals import **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/post)   * Added an endpoint for merchant statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/post)   * Added an endpoint for 1099k statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post)   * Added an endpoint for memos import **Link:** [#/paths/~1merchants~1{merchantNumber}~1memos/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1memos/post)   * Added an endpoint for getting Processor and DataSource available for assigning to merchants **Link:** [#/paths/~1processors/get](https://www.mycoastalpay.com/api/#/paths/~1processors/get)       ### 1.9.0 (2022-04-06)   #### Created:   * Added endpoint to get lead details from a specific tab **Link:** [#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get)       ### 1.7.0 (2021-12-08)   #### Updated:   * Added TurboApp Equipment Created event **Link:** [#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get)       ### 1.6.10 (2021-11-24)   #### Updated:   * Updated pagination on get list of statements endpoint. **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/get)       ### 1.6.9 (2021-08-02)   #### Updated:   * Added `void_reject_chargeback` property to the batches and transactions list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.8 (2021-08-04)   #### Created:   * Added `Delete record from a lead record set` endpoint **Link:** [#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete)       ### 1.6.7 (2021-07-20)   #### Updated:   * Added `unassigned` property to the chargebacks list response. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.6.6 (2021-07-14)   #### Updated:   * Added `adjustments` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.5 (2021-07-02)   #### Updated:   * Added `type` property to the chargebacks list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.6.4 (2021-05-06)   #### Updated:   * Added `terminal_number` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.3 (2021-04-26)   #### Updated:   * Added `created_username`,`modified_username`, and `resolved_username` properties to the ticket creation endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `created_username`,`modified_username`, and `resolved_username` to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.6.2 (2021-05-31)   #### Created:   * Added `end_date` filter to deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)       ### 1.6.1 (2021-04-02)   #### Updated:   * Increased API Rate limit to 500 request per minute **Link:** [#section/Limiting](https://www.mycoastalpay.com/api/#section/Limiting)       ### 1.6.0 (2021-03-02)   #### Created:   * Added `Get pricing templates` endpoint **Link:** [#/paths/~1leads~1pricing_templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1pricing_templates/get)       ### 1.5.21 (2021-03-19)   #### Updated:   * Added new properties to the chargebacks list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added new properties to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)       ### 1.5.20 (2021-02-12)   #### Updated:   * Added `filename` property to the `lead.document.uploaded` subscription response **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)       ### 1.5.19 (2021-02-17)   #### Updated:   * Added deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)   * Added `authorization_code` property to the chargeback response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.5.18 (2021-01-14)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.5.17 (2021-03-17)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)   * Added `id` and `reply_form` properties to the chargebacks response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added the `id` property to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)     #### Created:   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get)   * Added an endpoint for Reply To Chargeback Case - Dispute Chargeback Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post)   * Added an endpoint for Reply To Chargeback Case - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Chargeback Case - Accept Chargeback **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post)   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response with Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Fulfill Retrieval Case Request **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Locate Retrieval Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post)   * Added an endpoint for Reply To Retrieval - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Retrieval Case - Imprint and Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post)   * Added an endpoint for Reply To Retrieval Case - Responding by Other Means **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post)   * Added an endpoint for Reply To Retrieval Case - Add User Notes/Images **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post)   * Added an endpoint for the file upload **Link:** [#/paths/~1merchants~1files/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1files/post)   * Added an endpoint for Download chargeback case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get)   * Added an endpoint for Download retrieval case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get)   * Added new subscription for receiving a notification when a new chargeback case created **Link:** [#/paths/~1subscriptions~1sample~1chargeback.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.added/get)   * Added new subscription for receiving a notification when chargeback case status changed **Link:** [#/paths/~1subscriptions~1sample~1chargeback.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the chargeback case due date **Link:** [#/paths/~1subscriptions~1sample~1chargeback.reminder/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.reminder/get)   * Added new subscription for receiving a notification when a new retrieval case created **Link:** [#/paths/~1subscriptions~1sample~1retrieval.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.added/get)   * Added new subscription for receiving a notification when retrieval case status changed **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the retrieval case due date **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)       ### 1.5.16 (2020-12-11)   #### Updated:   * Renamed task priority from \"Low\" to \"Normal\" **Link:** [#/paths/~1leads~1{leadId}~1tasks/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tasks/post)       ### 1.5.15 (2021-01-18)   #### Updated:   * Added `due` value for `sort_by` and `date_filter` parameters on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `only_business_days` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `only_business_days` property to the Ticket on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `only_business_days` property to the Ticket Type on the get a list of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/get)   * Added `only_business_days` parameter on the get detailed information of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `only_business_days` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `only_business_days` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `attached_files` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `attached_files` property to the Ticket Comment on the Comment create endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)       ### 1.5.14 (2020-11-26)   #### Updated:   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of the ticket create response **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket details response **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket update response **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket's checklist updated subscription response **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.13 (2020-11-20)   #### Updated:   * Added `priority` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `priority` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.12 (2020-11-02)   #### Updated:   * Changed `due_date` property to the datetime format on the ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Changed `due_date` property to the datetime format on the ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.11 (2020-10-20)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.10 (2020-10-19)   #### Updated:   * Added `group_id` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `group_id` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.9 (2020-11-02)   #### Updated:   * Added `new_files` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `new_files` property for ticket type update payload. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.8 (2020-10-20)   #### Updated:   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `preview_images` property for ticket comment request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket and ticket comment properties. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.7 (2020-10-05)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.5 (2020-07-23)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1leads~1file_labels/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1file_labels/get)       ### 1.5.5 (2020-10-20)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1helpdesk~1{ticketId}~1assignments/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1assignments/get)       ### 1.5.4 (2020-07-13)   #### Updated:   * Added `files_count` property to the ticket create endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files_count` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `files_count` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files_count` property to the ticket update endpoint response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files_count` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files_count` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files_count` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files_count` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.3 (2020-07-06)   #### Updated:   * Added `search` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.5.2 (2020-07-10)   #### Updated:   * Added `due_date` property to the ticket create endpoint request and response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `due_date` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due_date` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `due_date` property to the ticket update endpoint request and response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `due_date` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `due_date` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `due_date` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `due_date` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.1 (2020-08-10)   #### Created:   * Added a Residuals API to work with your residuals reports. **Link:** [#tag/Residuals](https://www.mycoastalpay.com/api/#tag/Residuals)       ### 1.4.9 (2020-06-26)   #### Updated:   * Added `hide_resolved` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.8 (2020-06-12)   #### Updated:   * Added `set_for`, `set_at`, `set_by`, `modified`, `modified_by`, `date_end`, `confirmed_by`, `seen_by`, `rescheduled`, `rescheduled_by`, and `rescheduled_count` properties to the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added `set_for`, `set_by`, `modified_by`, `confirmed_by`, `seen_by`, `rescheduled_by`, `rescheduled_count`,  `date_filter`, `start_date`, `end_date`, and `done` filters to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added sorting to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Marked `user` property as deprecated on the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)       ### 1.4.7 (2020-05-13)   #### Updated:   * Added `old_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)   * Added `new_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)       ### 1.4.6 (2020-05-01)   #### Created:   * Added `lead.signature.generated` subscription endpoint. **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.generated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.generated/get)   * Added `lead.signature.opened` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.opened/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.opened/get)   * Added `lead.signature.signed` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.signed/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.signed/get)     #### Updated:   * Added `createdAt` and `createdBy` properties to the `lead.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.deleted` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.restored` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `createdAt` and `createdBy` properties to the `lead.status.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.4.5 (2020-04-21)   #### Updated:   * Added `files` property to the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `file` property for each checklist item in the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files` property to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property for each comment in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `file` property for each checklist item in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files` property for each comment in the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the Helpdesk ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the ticket type creation details endpoint response. **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `file` property for each checklist item on the ticket type endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `file` property for each checklist item on the ticket type update endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `files` property for ticket created subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files` property for ticket updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files` property for ticket resolved subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files` property for ticket commented subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `files` property for ticket checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `file` property for each checklist item on checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)     #### Created:   * Added endpoint for download attachments from Ticket Type **Link:** [#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get)       ### 1.4.4 (2020-04-02)   #### Updated:   * Added `resolver` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.3 (2020-04-01)   #### Updated:   * Added `status_updated` option for `date_filter` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.2 (2020-03-27)   #### Updated:   * Added `lid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `mid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.1 (2020-03-20)   #### Updated:   * Added `hash` and `url` properties to the 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.4.0 (2020-03-05)   #### Updated:   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.created/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.deleted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.restored` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.status.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.note.added` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.note.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.note.added/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.document.uploaded` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.email.received` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.email.received/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.email.received/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.resolved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.commented` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.checklist.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.submitted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.approved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.declined` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)   * Changed all subscriptions dates properties to the snake case **Link:** [#tag/Subscriptions](https://www.mycoastalpay.com/api/#tag/Subscriptions)       ### 1.3.5 (2020-02-26)   #### Created:   * Added a Helpdesk API to work with your helpdesk data. **Link:** [#tag/Helpdesk](https://www.mycoastalpay.com/api/#tag/Helpdesk)       ### 1.3.4 (2020-02-25)   #### Updated:   * Added a `lid` property to the \"turboapp.submitted\" subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)       ### 1.3.3 (2020-02-24)   #### Updated:   * Added a `salesRep` parameter to 'lead.status.updated' subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.3.2 (2019-11-21)   #### Updated:   * Added a `expire` parameter to 'Generate an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post)   * Added the ability to add multiple signers to the document and added an `expire` parameter to 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.3.1 (2019-11-18)   #### Updated:   * Rename subscriptions from \"application.created\" to \"turboapp.submitted\" and \"application.updated\" to \"turboapp.updated\". **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)     #### Created:   * Added new subscriptions for \"turboapp.approved\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added new subscriptions for \"turboapp.declined\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)       ### 1.2.2 (2019-09-03)   #### Updated:   * Added a `per_page` property to all list endpoints.       ### 1.2.1 (2019-08-26)   #### Updated:   * Added a `leads` property to merchants endpoint. **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.2.0 (2019-07-26)   #### Updated:   * The endpoint for creating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions/post](https://www.mycoastalpay.com/api/#/paths/~1subscriptions/post)   * The endpoint for updating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions~1{subscriptionId}/patch](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1{subscriptionId}/patch)       ### 1.1.0 (2019-07-24)   #### Created:   * Added an endpoint for getting SMS templates. **Link:** [#/paths/~1leads~1sms~1templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1sms~1templates/get)   * Added new subscriptions for `application.created` event **Link:** [#/paths/~1subscriptions~1sample~1application.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.created/get)   * Added new subscriptions for `application.updated` event **Link:** [#/paths/~1subscriptions~1sample~1application.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.updated/get)     #### Updated:   * Added a `sic_code` property to merchants endpoint **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.0.0 (2019-06-20)   #### Created:   * Added change log.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from iriscrm.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from iriscrm.exceptions import ApiAttributeError


def lazy_import():
    from iriscrm.model.lead_field import LeadField
    from iriscrm.model.lead_field_options import LeadFieldOptions
    from iriscrm.model.leads_fields_get_request_all_of import LeadsFieldsGetRequestAllOf
    globals()['LeadField'] = LeadField
    globals()['LeadFieldOptions'] = LeadFieldOptions
    globals()['LeadsFieldsGetRequestAllOf'] = LeadsFieldsGetRequestAllOf


class LeadsFieldsGetRequest(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('type',): {
            'DATECREATE': "DateCreate",
            'GOOGLEMAPS': "GoogleMaps",
            'JQDATE': "jQDate",
            'NUMBER': "Number",
            'TXT': "Txt",
            'TXTAREA': "TxtArea",
            'TXTDOLLAR': "TxtDollar",
            'TXTBALANCE': "TxtBalance",
            'TXTSIC': "TxtSIC",
            'TXTPERCENT': "TxtPercent",
            'TXTROUTING': "TxtRouting",
            'TXTSECURE': "TxtSecure",
            'TXTMASKED': "TxtMasked",
            'CHECKBOX': "Checkbox",
            'SELECT': "Select",
            'SELECTRED': "SelectRed",
            'LABEL': "Label",
            'PACKAGES': "Packages",
            'PHONEMASK': "PhoneMask",
            'PRFORMATS': "PrFormats",
            'QUICKEMAIL': "QuickEmail",
            'QUICKFAX': "QuickFax",
            'TIMEZONE': "TimeZone",
        },
        ('alignment',): {
            'EMPTY': "",
            'LEFT': "left",
            'MIDDLE': "middle",
            'RIGHT': "right",
            'LEFT_COLUMN': "left_column",
            'RIGHT_COLUMN': "right_column",
            'FLOAT_LEFT_WHOLE_ROW': "float_left_whole_row",
            'FLOAT_LEFT': "float_left",
            'FLOAT_MIDDLE': "float_middle",
        },
        ('searchable',): {
            '0': 0,
            '1': 1,
        },
        ('special',): {
            'EMPTY': "",
            'MID': "mid",
            'DBA': "dba",
            'SALES_NUMBER': "sales_number",
            'BUSADDRESS': "busaddress",
            'BUSCITY': "buscity",
            'BUSSTATE': "busstate",
            'BUSZIPCODE': "buszipcode",
            'BUSTYPE': "bustype",
            'BUSPRODUCTS': "busproducts",
            'BUSMARKETTYPE': "busmarkettype",
            'BUSSTARTDATE': "busstartdate",
            'SIC': "sic",
            'TAXID': "taxid",
            'PROCESSOR': "processor",
            'OWNER_FNAME': "owner_fname",
            'OWNER_LNAME': "owner_lname",
            'OWNER_TITLE': "owner_title",
            'OWNER_SSN': "owner_ssn",
            'PHONE': "phone",
            'CELLPHONE': "cellphone",
            'EMAIL': "email",
            'CONTACT': "contact",
            'CONTACT_1': "contact_1",
            'CONTACT_2': "contact_2",
            'AVGTCKT': "avgtckt",
            'VOLUME': "volume",
            'BANK_NAME_ON_ACCOUNT': "bank_name_on_account",
            'BANK_ACCOUNT_TYPE': "bank_account_type",
            'BANK_ACCOUNT_OWNER_TYPE': "bank_account_owner_type",
            'ABA_CODE': "aba_code",
            'ACCOUNT_NUMBER': "account_number",
            'BANK_NAME': "bank_name",
            'BANK_CITY': "bank_city",
            'BANK_STATE': "bank_state",
            'BANK_ZIP': "bank_zip",
            'LMS_FSCORE': "LMS_FScore",
            'LMS_REFNUM': "LMS_RefNum",
            'LR_MONTHLY_PAYMENT': "LR_MONTHLY_PAYMENT",
            'LR_EQUIPMENT': "LR_EQUIPMENT",
            'LR_WIRE_TRANFER': "LR_WIRE_TRANFER",
            'LR_PACK_FEE': "LR_PACK_FEE",
            'LR_CANCELLATION': "LR_CANCELLATION",
            'LEADID': "leadID",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'tab': (int,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'length': (int,),  # noqa: E501
            'default': (str,),  # noqa: E501
            'alignment': (str,),  # noqa: E501
            'searchable': (int,),  # noqa: E501
            'special': (str,),  # noqa: E501
            'options': (LeadFieldOptions,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'read_only': (bool,),  # noqa: E501
            'required': (bool,),  # noqa: E501
            'override': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tab': 'tab',  # noqa: E501
        'label': 'label',  # noqa: E501
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'length': 'length',  # noqa: E501
        'default': 'default',  # noqa: E501
        'alignment': 'alignment',  # noqa: E501
        'searchable': 'searchable',  # noqa: E501
        'special': 'special',  # noqa: E501
        'options': 'options',  # noqa: E501
        'order': 'order',  # noqa: E501
        'read_only': 'readOnly',  # noqa: E501
        'required': 'required',  # noqa: E501
        'override': 'override',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'order',  # noqa: E501
        'read_only',  # noqa: E501
        'required',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LeadsFieldsGetRequest - a model defined in OpenAPI

        Keyword Args:
            tab (int): Field tab Id
            label (str): Field label
            type (str): Field type
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Field Id. [optional]  # noqa: E501
            length (int): Field size. [optional]  # noqa: E501
            default (str): Field default value. [optional]  # noqa: E501
            alignment (str): Field alignment. [optional]  # noqa: E501
            searchable (int): Searchable field. [optional]  # noqa: E501
            special (str): Field special value. [optional]  # noqa: E501
            options (LeadFieldOptions): [optional]  # noqa: E501
            order (int): [optional]  # noqa: E501
            read_only (bool): Whether the field is read only. [optional]  # noqa: E501
            required (bool): Whether the field is required. [optional]  # noqa: E501
            override (bool): Flag for overriding existing special field. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """LeadsFieldsGetRequest - a model defined in OpenAPI

        Keyword Args:
            tab (int): Field tab Id
            label (str): Field label
            type (str): Field type
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Field Id. [optional]  # noqa: E501
            length (int): Field size. [optional]  # noqa: E501
            default (str): Field default value. [optional]  # noqa: E501
            alignment (str): Field alignment. [optional]  # noqa: E501
            searchable (int): Searchable field. [optional]  # noqa: E501
            special (str): Field special value. [optional]  # noqa: E501
            options (LeadFieldOptions): [optional]  # noqa: E501
            order (int): [optional]  # noqa: E501
            read_only (bool): Whether the field is read only. [optional]  # noqa: E501
            required (bool): Whether the field is required. [optional]  # noqa: E501
            override (bool): Flag for overriding existing special field. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              LeadField,
              LeadsFieldsGetRequestAllOf,
          ],
          'oneOf': [
          ],
        }

"""
    Coastal Pay API

    # Introduction Welcome to Coastal Pay’s API!  The API is organized around `REST`. All requests should be made over `SSL`.  All request and response bodies, including errors, are encoded in `JSON`. # Open API The Open API provides numerous functions to access or to update your CRM lead  and merchant  data using simple REST calls. ### You can use the E-Signature API to: - [Generate an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post) - [Send an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post) - [Download an e-signature document](https://www.mycoastalpay.com/api#/paths/~1leads~1signatures~1{applicationId}~1download/get) - [Get a list of all lead e-signatures documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1signatures/get) - [Get a list of available applications](https://www.mycoastalpay.com/api#/paths/~1leads~1applications/get) - [Create a new application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/post) - [Get a list of available application field mappings](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings/get) - [Get an application field mapping list](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/get) - [Update an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/patch) - [Delete an application field mapping](https://www.mycoastalpay.com/api#/paths/~1leads~1applications~1{appId}~1mappings~1{mapId}/delete) ### You can use the Helpdesk API to: - [Create a new ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk/post) - [Get a list of helpdesk tickets](https://www.mycoastalpay.com/api#/paths/~1helpdesk/get) - [Add a ticket comment](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1comment/post) - [Get detailed ticked information](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/get) - [Update a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/patch) - [Delete a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}/delete) - [Upload an attachment to a ticket, comment, checklist, or ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1file/post) - [Download an attachment from a ticket](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1{ticketId}~1download~1{attachmentId}/get) - [Create a new helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/post) - [Get a list of helpdesk ticket types](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types/get) - [Get details for a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/get) - [Update a helpdesk ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/patch) - [Delete a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}/delete) - [Download an attachment from a ticket type](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get) - [Get a list of available users to notify and assign](https://www.mycoastalpay.com/api#/paths/~1helpdesk~1users/get) ### You can use the Lead API to: - [Create a lead](https://www.mycoastalpay.com/api#/paths/~1leads/post) - [Get a list of leads](https://www.mycoastalpay.com/api#/paths/~1leads/get) - [Get detailed lead information](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/get) - [Update a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}/patch) - [Get lead information from a specific tab](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get) - [Create a new lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/post) - [Get a list of available lead fields](https://www.mycoastalpay.com/api#/paths/~1leads~1fields/get) - [Get a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/get) - [Update a lead field](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}/patch) - [Update a lead field order position](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1{fieldId}~1order/patch) - [Create a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/post) - [Get a list of all lead field tabs](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs/get) - [Get a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/get) - [Update a lead field tab](https://www.mycoastalpay.com/api#/paths/~1leads~1fields~1tabs~1{tabId}/patch) - [Create a lead note](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/post) - [Get lead notes](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1notes/get) - [Create a lead appointment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/post) - [Get lead appointments](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1appointments/get) - [Populate PDF Document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1applications~1{applicationId}~1populate/post) - [Create a lead task](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/post) - [Get lead tasks](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1tasks/get) - [Assign a user](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/post) - [Get a list of assigned users](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users/get) - [Unassign a user from a lead](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1users~1{userId}/delete) - [Upload a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/post) - [Get a list of available documents](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents/get) - [Get a list of available document labels](https://www.mycoastalpay.com/api#/paths/~1leads~1file_labels/get) - [Download a document](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1documents~1{documentId}/get) - [Send an email to lead with template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1emails~1{templateId}/post) - [Get a list of email templates](https://www.mycoastalpay.com/api#/paths/~1leads~1emails~1templates/get) - [Download a mailbox email attachment](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1mailbox~1{emailId}~1attachment~1{attachmentId}/get) - [Send an SMS to lead with selected SMS template](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1sms~1{templateId}/post) - [Get list of SMS templates](https://www.mycoastalpay.com/api#/paths/~1leads~1sms~1templates/get) - [Get a list of all lead campaign activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1campaign/get) - [Get a list of all lead deletion activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1deletion/get) - [Get a list of all lead duplicate activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1duplicates/get) - [Get a list of all lead links activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1links/get) - [Get a list of all lead source activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1source/get) - [Get a list of all lead status activity](https://www.mycoastalpay.com/api#/paths/~1leads~1{leadId}~1activity~1status/get) - [Get a list of available campaigns](https://www.mycoastalpay.com/api#/paths/~1leads~1campaigns/get) - [Get a list of available groups](https://www.mycoastalpay.com/api#/paths/~1leads~1groups/get) - [Get a list of available sources](https://www.mycoastalpay.com/api#/paths/~1leads~1sources/get) - [Get a list of available statuses](https://www.mycoastalpay.com/api#/paths/~1leads~1statuses/get) - [Get a list of available users](https://www.mycoastalpay.com/api#/paths/~1leads~1users/get)  ### You can use the Merchant API to: - [Get a list of merchants](https://www.mycoastalpay.com/api#/paths/~1merchants/get) - [Get detailed merchant information](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/get) - [Update an existing merchant](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}/patch) - [Get a list of batches and transactions](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1transactions/get) - [Get a list of chargebacks](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1chargebacks/get) - [Get a list of retrievals](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1retrievals/get) - [Get a list of statements](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements/get) - [Download a statement](https://www.mycoastalpay.com/api#/paths/~1merchants~1{merchantNumber}~1statements~1{statementId}/get) ### You can use the Residuals API to: - [Get residuals summary data](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1{year}~1{month}/get) - [Get residuals summary with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1summary~1rows~1{processor_id}~1{year}~1{month}/get) - [Get residuals details with merchant rows](https://www.mycoastalpay.com/api#/paths/~1residuals~1reports~1details~1{processor_id}~1{year}~1{month}/get) - [Get residuals line items](https://www.mycoastalpay.com/api#/paths/~1residuals~1lineitems~1{year}~1{month}/get) - [Get residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1/get) - [Get a list of users with assigned residuals templates](https://www.mycoastalpay.com/api#/paths/~1residuals~1templates~1assigned~1{year}~1{month}/get)   # Generate an API token When you send an API request, you will need to include an API token in your request in order to authenticate your account.  The tokens are generated in the CRM by each user individually, and each user may create one or more tokens.  To generate a new API Token, open your user settings page by clicking on your username in the top-right corner, and clicking on the ** Settings ** link or you can use the <a href=\"https://www.mycoastalpay.com/settings\">link</a>.  Then open the ** API Settings ** tab, click ** Create New API Token **, configure your token’s settings as needed, and click ** Add New Token **:  <img src='https://www.mycoastalpay.com/images/docs/mapi001.png'/>  Your new token will now be created and displayed in a popup window:  <img src='https://www.mycoastalpay.com/images/docs/mapi002.png'/>  Once the token is created, it will be shown in the list of available API Tokens where you can copy the token, update its settings, or delete it once it’s no longer needed:  <img src='https://www.mycoastalpay.com/images/docs/mapi003.png'/>  ** Note: ** The created tokens will inherit the user’s permissions to assigned merchants, leads, groups and processors. # Using the API Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code.  `curl -X GET \"https://www.mycoastalpay.com/api/v1/leads\" -H \"accept: application/json\" -H \"X-API-KEY: [YOURKEY]\"`  Note that all requests should be made over `SSL`. All request and response bodies, including errors, are encoded in JSON.  The API returns standard HTTP success or error status codes. In case of errors, additional information about what went wrong will be encoded in the response as JSON.  By default, you can make `500` requests per minute. Check the returned HTTP headers of any API request to see your current rate limit status.  Each GET \"List\" request will return 1,000 matching results.  A maximum of 500,000 results can be returned per minute using a pagination parameter in these requests. # Using the Subscription API API Subscriptions are used to send information about an event to a URL and trigger an API call. This is more efficient than doing scheduled API calls.  To create a subscription, use the API Settings page or send a request using the instructions in the Subscriptions section below.  All you need to know is the events you want to be subscribed for and the url to which the updates need to be sent.  To create subscriptions using our GUI open tab ** API Settings ** at ** https://www.mycoastalpay.com/settings **:  <img src='https://www.mycoastalpay.com/images/docs/new-subscription.png'/> # Authentication Authenticate your account by including your secret key in API requests. Do not share your secret API keys in publicly accessible areas, client-side code, and so forth. Authentication to the API is performed via `X-API-KEY` header. Requests not properly authenticated will return a `401` error code. # Errors Our API returns standard `HTTP` success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as `JSON`. # Limiting You can make `500` requests per minute. If you will reach a limit you will get a `429: Too Many Attempts.` response from the server. Check the returned `HTTP` headers of any API request to see your current rate limit status. Headers description: * `X-RateLimit-Limit` tells you the max number of requests you're allowed to make within this application's time period * `X-RateLimit-Remaining` tells you how many requests you have left within this current time period * `Retry-After` tells you how many seconds to wait until you try again. (you'll only get `Retry-After` if you've hit the limit).   # PHP SDK  ### Installation and Usage  #### Availability  The IRIS CRM PHP SDK requires PHP version 5.5 or higher and the PHP cURL extension.  #### Composer  To install the bindings via [Composer](http://getcomposer.org/), please run:  ```bash  composer require iris-crm/php-sdk      ```   In your code, configure the environment and API credentials:  ```php require_once(__DIR__ . '/vendor/autoload.php');  use Swagger\\Client\\Configuration; use Swagger\\Client\\Api\\LeadsApi;  // Configure API key authorization $config = Configuration::getDefaultConfiguration() ->setApiKey('X-API-KEY', 'YOUR_API_KEY') ->setHost('https://www.mycoastalpay.com/api/v1/'); ``` Here’s an example of how to get a list of leads using an SDK. Swagger\\Client\\Api\\LeadsApi it's a SDK Class for Lead endpoints. ```php $apiInstance = new LeadsApi(null, $config);  $page        = 1; // int | Page number $sort_by     = \"created\"; // string | Sorting of leads by the field value $sort_dir    = \"asc\"; // string | Direction of sorting $group       = 2; // int | Filter leads by a group id $campaign    = 3; // int | Filter leads by a campaign id $source      = 4; // int | Filter leads by a source id $status      = 1; // int | Filter leads by a status id $category    = 1; // int | Filter leads by a status category id $user        = 12; // int | Filter leads by a user id $date_filter = \"created\"; // string | Filtering leads by a date range depends on this filter $start_date  = new \\DateTime(\"2018-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $end_date    = new \\DateTime(\"2019-10-20T19:20:30+01:00\"); // \\DateTime | Filter leads by a date in ISO 8601 format (Y-m-d\\\\TH:i:sP) $email       = \"test@mail.com\"; // string | Filter leads by a email try {     $result = $apiInstance->leadsGet($page, $sort_by, $sort_dir, $group, $campaign, $source, $status, $category, $user, $date_filter, $start_date, $end_date, $email);     print_r($result); } catch (Exception $e) {     echo 'Exception when calling LeadsApi->leadsGet: ' . $e->getMessage() . PHP_EOL; } ``` All parameters for leadsGet method is optional and can be skipped.  If you want skip some parameters - you need to set parameter to `null`  All available classes and methods you can get in \"API Endpoints\" section below. ### API Endpoints All URIs are relative to *https://www.mycoastalpay.com/api/v1*  Class | Method | HTTP Request | Description ------------ | ------------- | ------------- | ------------- *LeadsApi* | **leadsApplicationsAppIdMappingsGet** | **GET** /leads/applications/{appId}/mappings | Get a list of available application field mappings *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdDelete** | **DELETE** /leads/applications/{appId}/mappings/{mapId} | Delete an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdGet** | **GET** /leads/applications/{appId}/mappings/{mapId} | Get an application field mapping list *LeadsApi* | **leadsApplicationsAppIdMappingsMapIdPatch** | **PATCH** /leads/applications/{appId}/mappings/{mapId} | Update an application field mapping *LeadsApi* | **leadsApplicationsAppIdMappingsPost** | **POST** /leads/applications/{appId}/mappings | Create a new application field mapping *LeadsApi* | **leadsApplicationsGet** | **GET** /leads/applications | Get a list of available applications *LeadsApi* | **leadsCampaignsGet** | **GET** /leads/campaigns | Get a list of available campaigns *LeadsApi* | **leadsDynamicFieldsSchemaGet** | **GET** /leads/dynamic-fields-schema | Get a schema of lead fields *LeadsApi* | **leadsEmailsTemplatesGet** | **GET** /leads/emails/templates | Get a list of email templates *LeadsApi* | **leadsFieldsFieldIdGet** | **GET** /leads/fields/{fieldId} | Get a lead field *LeadsApi* | **leadsFieldsFieldIdOrderPatch** | **PATCH** /leads/fields/{fieldId}/order | Update a lead field order position *LeadsApi* | **leadsFieldsFieldIdPatch** | **PATCH** /leads/fields/{fieldId} | Update a lead field *LeadsApi* | **leadsFieldsGet** | **GET** /leads/fields | Get a list of available lead fields *LeadsApi* | **leadsFieldsPost** | **POST** /leads/fields | Create a new lead field *LeadsApi* | **leadsFieldsTabsGet** | **GET** /leads/fields/tabs | Get a list of all lead field tabs *LeadsApi* | **leadsFieldsTabsPost** | **POST** /leads/fields/tabs | Create a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdGet** | **GET** /leads/fields/tabs/{tabId} | Get a lead field tab *LeadsApi* | **leadsFieldsTabsTabIdPatch** | **PATCH** /leads/fields/tabs/{tabId} | Update a lead field tab *LeadsApi* | **leadsGet** | **GET** /leads | Get a list of leads *LeadsApi* | **leadsGroupsGet** | **GET** /leads/groups | Get a list of available groups *LeadsApi* | **leadsLeadIdActivityCampaignGet** | **GET** /leads/{leadId}/activity/campaign | Get a list of all lead campaign activity *LeadsApi* | **leadsLeadIdActivityDeletionGet** | **GET** /leads/{leadId}/activity/deletion | Get a list of all lead deletion activity *LeadsApi* | **leadsLeadIdActivityDuplicatesGet** | **GET** /leads/{leadId}/activity/duplicates | Get a list of all lead duplicate activity *LeadsApi* | **leadsLeadIdActivityLinksGet** | **GET** /leads/{leadId}/activity/links | Get a list of all lead links activity *LeadsApi* | **leadsLeadIdActivitySourceGet** | **GET** /leads/{leadId}/activity/source | Get a list of all lead source activity *LeadsApi* | **leadsLeadIdActivityStatusGet** | **GET** /leads/{leadId}/activity/status | Get a list of all lead status activity *LeadsApi* | **leadsLeadIdApplicationsApplicationIdPopulatePost** | **POST** /leads/{leadId}/applications/{applicationId}/populate | Populate PDF Document *LeadsApi* | **leadsLeadIdAppointmentsGet** | **GET** /leads/{leadId}/appointments | Get lead appointments *LeadsApi* | **leadsLeadIdAppointmentsPost** | **POST** /leads/{leadId}/appointments | Create a lead appointment *LeadsApi* | **leadsLeadIdDocumentsDocumentIdGet** | **GET** /leads/{leadId}/documents/{documentId} | Download a document *LeadsApi* | **leadsLeadIdDocumentsGet** | **GET** /leads/{leadId}/documents | Get a list of available documents *LeadsApi* | **leadsLeadIdDocumentsPost** | **POST** /leads/{leadId}/documents | Upload a document *LeadsApi* | **leadsLeadIdEmailsTemplateIdPost** | **POST** /leads/{leadId}/emails/{templateId} | Send an email to lead with template *LeadsApi* | **leadsLeadIdGet** | **GET** /leads/{leadId} | Get detailed lead information *LeadsApi* | **leadsLeadIdMailboxEmailIdAttachmentAttachmentIdGet** | **GET** /leads/{leadId}/mailbox/{emailId}/attachment/{attachmentId} | Download a mailbox email attachment *LeadsApi* | **leadsLeadIdNotesGet** | **GET** /leads/{leadId}/notes | Get lead notes *LeadsApi* | **leadsLeadIdNotesPost** | **POST** /leads/{leadId}/notes | Create a lead note *LeadsApi* | **leadsLeadIdPatch** | **PATCH** /leads/{leadId} | Update a lead *LeadsApi* | **leadsLeadIdSignaturesApplicationIdGeneratePost** | **POST** /leads/{leadId}/signatures/{applicationId}/generate | Generate an e-signature document *LeadsApi* | **leadsLeadIdSignaturesApplicationIdSendPost** | **POST** /leads/{leadId}/signatures/{applicationId}/send | Send an e-signature document *LeadsApi* | **leadsLeadIdSignaturesGet** | **GET** /leads/{leadId}/signatures | Get a list of all lead e-signatures documents *LeadsApi* | **leadsLeadIdSmsTemplateIdPost** | **POST** /leads/{leadId}/sms/{templateId} | Send an SMS to lead with selected SMS template *LeadsApi* | **leadsLeadIdTasksGet** | **POST** /leads/{leadId}/tasks | Create a lead task *LeadsApi* | **leadsLeadIdUsersGet** | **GET** /leads/{leadId}/users | Get a list of assigned users *LeadsApi* | **leadsLeadIdUsersPost** | **POST** /leads/{leadId}/users | Assign a user *LeadsApi* | **leadsLeadIdUsersUserIdDelete** | **DELETE** /leads/{leadId}/users/{userId} | Unassign a user from a lead *LeadsApi* | **leadsPost** | **POST** /leads | Create a lead *LeadsApi* | **leadsSignaturesApplicationIdDownloadGet** | **GET** /leads/signatures/{applicationId}/download | Download an e-signature document *LeadsApi* | **leadsSmsTemplatesGet** | **GET** /leads/sms/templates | Get list of SMS templates *LeadsApi* | **leadsSourcesGet** | **GET** /leads/sources | Get a list of available sources *LeadsApi* | **leadsStatusesGet** | **GET** /leads/statuses | Get a list of available statuses *LeadsApi* | **leadsUsersGet** | **GET** /leads/users | Get a list of available users *MerchantsApi* | **merchantsGet** | **GET** /merchants | Get a list of merchants *MerchantsApi* | **merchantsMerchantNumberChargebacksGet** | **GET** /merchants/{merchantNumber}/chargebacks | Get a list of chargebacks *MerchantsApi* | **merchantsMerchantNumberGet** | **GET** /merchants/{merchantNumber} | Get detailed merchant information *MerchantsApi* | **merchantsMerchantNumberPatch** | **PATCH** /merchants/{merchantNumber} | Update an existing merchant *MerchantsApi* | **merchantsMerchantNumberRetrievalsGet** | **GET** /merchants/{merchantNumber}/retrievals | Get a list of retrievals *MerchantsApi* | **merchantsMerchantNumberStatementsGet** | **GET** /merchants/{merchantNumber}/statements | Get a list of statements *MerchantsApi* | **merchantsMerchantNumberStatementsStatementIdGet** | **GET** /merchants/{merchantNumber}/statements/{statementId} | Download a statement *MerchantsApi* | **merchantsMerchantNumberTransactionsGet** | **GET** /merchants/{merchantNumber}/transactions | Get a list of batches and transactions *SubscriptionsApi* | **subscriptionsGet** | **GET** /subscriptions | Return a list of subscriptions *SubscriptionsApi* | **subscriptionsPost** | **POST** /subscriptions | Create a subscription *SubscriptionsApi* | **subscriptionsSampleApiUpdatedGet** | **GET** /subscriptions/sample/api.updated | Data sample for the \\&quot;api.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationCreatedGet** | **GET** /subscriptions/sample/turboapp.submitted | Data sample for the \\&quot;turboapp.submitted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleApplicationUpdatedGet** | **GET** /subscriptions/sample/turboapp.updated | Data sample for the \\&quot;turboapp.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadCreatedGet** | **GET** /subscriptions/sample/lead.created | Data sample for the \\&quot;lead.created\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDeletedGet** | **GET** /subscriptions/sample/lead.deleted | Data sample for the \\&quot;lead.deleted\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadDocumentUploadedGet** | **GET** /subscriptions/sample/lead.document.uploaded | Data sample for the \\&quot;lead.document.uploaded\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadEmailReceivedGet** | **GET** /subscriptions/sample/lead.email.received | Data sample for the \\&quot;lead.email.received\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadNoteAddedGet** | **GET** /subscriptions/sample/lead.note.added | Data sample for the \\&quot;lead.note.added\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadRestoredGet** | **GET** /subscriptions/sample/lead.restored | Data sample for the \\&quot;lead.restored\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadStatusUpdatedGet** | **GET** /subscriptions/sample/lead.status.updated | Data sample for the \\&quot;lead.status.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSampleLeadUpdatedGet** | **GET** /subscriptions/sample/lead.updated | Data sample for the \\&quot;lead.updated\\&quot; event *SubscriptionsApi* | **subscriptionsSubscriptionIdDelete** | **DELETE** /subscriptions/{subscriptionId} | Delete a subscription *SubscriptionsApi* | **subscriptionsSubscriptionIdGet** | **GET** /subscriptions/{subscriptionId} | Return a subscription by its id *SubscriptionsApi* | **subscriptionsSubscriptionIdPatch** | **PATCH** /subscriptions/{subscriptionId} | Update a subscription # Change Log   ### 1.14.0 (2022-08-23)   #### Updated:   * Added `details.fields.uid` field to the `Get detailed lead information` endpoint **Link:** [#/paths/~1leads~1{leadId}/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}/get)       ### 1.10.4 (2022-05-02)   #### Updated:   * Added a fields filter to a leads list endpoint **Link:** [#/paths/~1leads/get](https://www.mycoastalpay.com/api/#/paths/~1leads/get)       ### 1.10.3 (2022-04-29)   #### Updated:   * Added user activity indicator to the `get residuals line items` endpoint **Link:** [#/paths/~1residuals~1lineitems~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1residuals~1lineitems~1{year}~1{month}/get)       ### 1.10.2 (2022-04-29)   #### Updated:   * Updated endpoint Create Lead, added an users_emails field. **Link:** [#/paths/~1leads/post](https://www.mycoastalpay.com/api/#/paths/~1leads/post)       ### 1.10.1 (2022-04-29)   #### Updated:   * Updated endpoint Assign a user to a lead by email **Link:** [#/paths/~1leads~1{leadId}~1users/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1users/post)       ### 1.10.0 (2022-04-06)   #### Created:   * Added an endpoint for merchant creation and assigning users. **Link:** [#/paths/~1merchants/post](https://www.mycoastalpay.com/api/#/paths/~1merchants/post)   * Added an endpoint for getting assigned users to merchant **Link:** [#/paths/~1merchants~1{merchantNumber}~1users/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1users/get)   * Added an endpoint for updating merchant details **Link:** [#/paths/~1merchants~1{merchantNumber}~1details/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1details/post)   * Added an endpoint for transactions import **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/post)   * Added an endpoint for adjustments import **Link:** [#/paths/~1merchants~1{merchantNumber}~1adjustments/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1adjustments/post)   * Added an endpoint for getting a list of batches **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/get)   * Added an endpoint for getting a list of authorizations **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations~1{batchId}~1transactions/get)   * Added an endpoint for batches and authorizations import **Link:** [#/paths/~1merchants~1{merchantNumber}~1authorizations/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1authorizations/post)   * Added an endpoint for chargebacks import **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/post)   * Added an endpoint for retrievals import **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/post)   * Added an endpoint for merchant statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/post)   * Added an endpoint for 1099k statements import **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements~11099k/post)   * Added an endpoint for memos import **Link:** [#/paths/~1merchants~1{merchantNumber}~1memos/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1memos/post)   * Added an endpoint for getting Processor and DataSource available for assigning to merchants **Link:** [#/paths/~1processors/get](https://www.mycoastalpay.com/api/#/paths/~1processors/get)       ### 1.9.0 (2022-04-06)   #### Created:   * Added endpoint to get lead details from a specific tab **Link:** [#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tabs~1{tabId}~1fields/get)       ### 1.7.0 (2021-12-08)   #### Updated:   * Added TurboApp Equipment Created event **Link:** [#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.equipment.created/get)       ### 1.6.10 (2021-11-24)   #### Updated:   * Updated pagination on get list of statements endpoint. **Link:** [#/paths/~1merchants~1{merchantNumber}~1statements/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1statements/get)       ### 1.6.9 (2021-08-02)   #### Updated:   * Added `void_reject_chargeback` property to the batches and transactions list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.8 (2021-08-04)   #### Created:   * Added `Delete record from a lead record set` endpoint **Link:** [#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1records~1{catId}~1{recordId}/delete)       ### 1.6.7 (2021-07-20)   #### Updated:   * Added `unassigned` property to the chargebacks list response. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.6.6 (2021-07-14)   #### Updated:   * Added `adjustments` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.5 (2021-07-02)   #### Updated:   * Added `type` property to the chargebacks list response. **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.6.4 (2021-05-06)   #### Updated:   * Added `terminal_number` property to the merchants list of batches and transactions. **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.6.3 (2021-04-26)   #### Updated:   * Added `created_username`,`modified_username`, and `resolved_username` properties to the ticket creation endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `created_username`,`modified_username`, and `resolved_username` properties to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `created_username`,`modified_username`, and `resolved_username` to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.6.2 (2021-05-31)   #### Created:   * Added `end_date` filter to deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)       ### 1.6.1 (2021-04-02)   #### Updated:   * Increased API Rate limit to 500 request per minute **Link:** [#section/Limiting](https://www.mycoastalpay.com/api/#section/Limiting)       ### 1.6.0 (2021-03-02)   #### Created:   * Added `Get pricing templates` endpoint **Link:** [#/paths/~1leads~1pricing_templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1pricing_templates/get)       ### 1.5.21 (2021-03-19)   #### Updated:   * Added new properties to the chargebacks list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added new properties to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)       ### 1.5.20 (2021-02-12)   #### Updated:   * Added `filename` property to the `lead.document.uploaded` subscription response **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)       ### 1.5.19 (2021-02-17)   #### Updated:   * Added deposits endpoint **Link:** [#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1deposits~1{year}~1{month}/get)   * Added `authorization_code` property to the chargeback response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)       ### 1.5.18 (2021-01-14)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)       ### 1.5.17 (2021-03-17)   #### Updated:   * Added `id` and `invoice_number` properties to the `transactions` section of the transactions response **Link:** [#/paths/~1merchants~1{merchantNumber}~1transactions/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1transactions/get)   * Added `id` and `reply_form` properties to the chargebacks response **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks/get)   * Added the `id` property to the retrievals list response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals/get)     #### Created:   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}/get)   * Added an endpoint for Reply To Chargeback Case - Dispute Chargeback Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1dispute_reverse/post)   * Added an endpoint for Reply To Chargeback Case - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Chargeback Case - Accept Chargeback **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1accept/post)   * Added an endpoint for getting detailed chargeback information **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}/get)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response/post)   * Added an endpoint for Reply To Retrieval Case - Retrieval Response with Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1response_with_signature/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Fulfill Retrieval Case Request **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_fulfill_request/post)   * Added an endpoint for Reply To Retrieval Case - Unable to Locate Retrieval Case **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1unable_to_locate_retrieval/post)   * Added an endpoint for Reply To Retrieval - Credit Issued **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1credit_issued/post)   * Added an endpoint for Reply To Retrieval Case - Imprint and Signature **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1imprint_and_signature/post)   * Added an endpoint for Reply To Retrieval Case - Responding by Other Means **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1responding_by_other_means/post)   * Added an endpoint for Reply To Retrieval Case - Add User Notes/Images **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1add_notes_images/post)   * Added an endpoint for the file upload **Link:** [#/paths/~1merchants~1files/post](https://www.mycoastalpay.com/api/#/paths/~1merchants~1files/post)   * Added an endpoint for Download chargeback case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1chargebacks~1{caseNumber}~1files~1{fileId}/get)   * Added an endpoint for Download retrieval case files **Link:** [#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get](https://www.mycoastalpay.com/api/#/paths/~1merchants~1{merchantNumber}~1retrievals~1{caseNumber}~1files~1{fileId}/get)   * Added new subscription for receiving a notification when a new chargeback case created **Link:** [#/paths/~1subscriptions~1sample~1chargeback.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.added/get)   * Added new subscription for receiving a notification when chargeback case status changed **Link:** [#/paths/~1subscriptions~1sample~1chargeback.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the chargeback case due date **Link:** [#/paths/~1subscriptions~1sample~1chargeback.reminder/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1chargeback.reminder/get)   * Added new subscription for receiving a notification when a new retrieval case created **Link:** [#/paths/~1subscriptions~1sample~1retrieval.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.added/get)   * Added new subscription for receiving a notification when retrieval case status changed **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)   * Added new subscription for receiving a notification in 7/3/1 days before the retrieval case due date **Link:** [#/paths/~1subscriptions~1sample~1retrieval.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1retrieval.updated/get)       ### 1.5.16 (2020-12-11)   #### Updated:   * Renamed task priority from \"Low\" to \"Normal\" **Link:** [#/paths/~1leads~1{leadId}~1tasks/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1tasks/post)       ### 1.5.15 (2021-01-18)   #### Updated:   * Added `due` value for `sort_by` and `date_filter` parameters on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` parameter on the get a list of Tickets endpoint **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `only_business_days` parameter on the get detailed information of Tickets endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `only_business_days` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `only_business_days` property to the Ticket on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `only_business_days` property to the Ticket Type on the get a list of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/get)   * Added `only_business_days` parameter on the get detailed information of Ticket Type endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `only_business_days` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `only_business_days` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `attached_files` property to the Ticket on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `attached_files` property to the Ticket Checklist on the Ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `attached_files` property to the Ticket Comment on the Comment create endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)       ### 1.5.14 (2020-11-26)   #### Updated:   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of the ticket create response **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket details response **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket update response **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `template_id`, `completed_by`, and `completed_at` properties to the `checklist` section of ticket's checklist updated subscription response **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.13 (2020-11-20)   #### Updated:   * Added `priority` property to the Ticket Type on the Ticket Type create endpoint **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `priority` property to the Ticket Type on the Ticket Type update endpoint **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.12 (2020-11-02)   #### Updated:   * Changed `due_date` property to the datetime format on the ticket create endpoint **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Changed `due_date` property to the datetime format on the ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.11 (2020-10-20)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.10 (2020-10-19)   #### Updated:   * Added `group_id` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `group_id` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.9 (2020-11-02)   #### Updated:   * Added `new_files` property for ticket update payload. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `new_files` property for ticket type update payload. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)       ### 1.5.8 (2020-10-20)   #### Updated:   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `preview_images` property for ticket comment request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket and ticket comment properties. **Link:** [#/paths/~1helpdesk~1{ticketId}~1comment/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1comment/post)   * Added `preview_images` property for ticket request and response data. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)       ### 1.5.7 (2020-10-05)   #### Updated:   * Added `notify_assigned_users` property for ticket creation payload. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)       ### 1.5.5 (2020-07-23)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1leads~1file_labels/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1file_labels/get)       ### 1.5.5 (2020-10-20)   #### Updated:   * Added endpoint with file labels what can be used for document upload. **Link:** [#/paths/~1helpdesk~1{ticketId}~1assignments/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}~1assignments/get)       ### 1.5.4 (2020-07-13)   #### Updated:   * Added `files_count` property to the ticket create endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files_count` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `files_count` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files_count` property to the ticket update endpoint response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files_count` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files_count` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files_count` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files_count` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.3 (2020-07-06)   #### Updated:   * Added `search` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.5.2 (2020-07-10)   #### Updated:   * Added `due_date` property to the ticket create endpoint request and response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `due_date` property to the response of ticket list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `due_date` property to the response of ticket detailed information endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `due_date` property to the ticket update endpoint request and response. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `due_date` property to the ticket.created subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `due_date` property to the ticket.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `due_date` property to the ticket.resolved subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `due_date` property to the ticket.checklist.updated subscription data. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)       ### 1.5.1 (2020-08-10)   #### Created:   * Added a Residuals API to work with your residuals reports. **Link:** [#tag/Residuals](https://www.mycoastalpay.com/api/#tag/Residuals)       ### 1.4.9 (2020-06-26)   #### Updated:   * Added `hide_resolved` filter to the tickets list endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.8 (2020-06-12)   #### Updated:   * Added `set_for`, `set_at`, `set_by`, `modified`, `modified_by`, `date_end`, `confirmed_by`, `seen_by`, `rescheduled`, `rescheduled_by`, and `rescheduled_count` properties to the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added `set_for`, `set_by`, `modified_by`, `confirmed_by`, `seen_by`, `rescheduled_by`, `rescheduled_count`,  `date_filter`, `start_date`, `end_date`, and `done` filters to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Added sorting to the lead appointments endpoint. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)   * Marked `user` property as deprecated on the lead appointments endpoint response. **Link:** [#/paths/~1leads~1{leadId}~1appointments/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1appointments/get)       ### 1.4.7 (2020-05-13)   #### Updated:   * Added `old_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)   * Added `new_status_id` to lead status activity endpoint. **Link:** [#/paths/~1leads~1{leadId}~1activity~1status/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1activity~1status/get)       ### 1.4.6 (2020-05-01)   #### Created:   * Added `lead.signature.generated` subscription endpoint. **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.generated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.generated/get)   * Added `lead.signature.opened` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.opened/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.opened/get)   * Added `lead.signature.signed` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.signature.signed/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.signature.signed/get)     #### Updated:   * Added `createdAt` and `createdBy` properties to the `lead.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.deleted` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `email`, `contact`, `phone` and `address` properties to the `lead.restored` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `createdAt` and `createdBy` properties to the `lead.status.updated` subscription endpoint **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.4.5 (2020-04-21)   #### Updated:   * Added `files` property to the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `file` property for each checklist item in the ticket creation details endpoint response. **Link:** [#/paths/~1helpdesk/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/post)   * Added `files` property to the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property for each comment in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `file` property for each checklist item in the Helpdesk tickets details endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/get)   * Added `files` property to the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `files` property for each comment in the Helpdesk ticket update endpoint. **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the Helpdesk ticket update endpoint **Link:** [#/paths/~1helpdesk~1{ticketId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1{ticketId}/patch)   * Added `file` property for each checklist item in the ticket type creation details endpoint response. **Link:** [#/paths/~1helpdesk~1types/post](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types/post)   * Added `file` property for each checklist item on the ticket type endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/get)   * Added `file` property for each checklist item on the ticket type update endpoint. **Link:** [#/paths/~1helpdesk~1types~1{typeId}/patch](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}/patch)   * Added `files` property for ticket created subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `files` property for ticket updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `files` property for ticket resolved subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `files` property for ticket commented subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `files` property for ticket checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `file` property for each checklist item on checklist updated subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)     #### Created:   * Added endpoint for download attachments from Ticket Type **Link:** [#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk~1types~1{typeId}~1download~1{attachmentId}/get)       ### 1.4.4 (2020-04-02)   #### Updated:   * Added `resolver` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.3 (2020-04-01)   #### Updated:   * Added `status_updated` option for `date_filter` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.2 (2020-03-27)   #### Updated:   * Added `lid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)   * Added `mid` filter to the Helpdesk tickets endpoint. **Link:** [#/paths/~1helpdesk/get](https://www.mycoastalpay.com/api/#/paths/~1helpdesk/get)       ### 1.4.1 (2020-03-20)   #### Updated:   * Added `hash` and `url` properties to the 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.4.0 (2020-03-05)   #### Updated:   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.created/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.deleted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.deleted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.deleted/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.restored` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.restored/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.restored/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.status.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.note.added` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.note.added/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.note.added/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.document.uploaded` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.document.uploaded/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.document.uploaded/get)   * Added `assigned_users`, `lead_url` properties to the subscriptions response for the `lead.email.received` subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.email.received/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.email.received/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.created` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.created/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.updated/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.resolved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.resolved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.resolved/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.commented` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.commented/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.commented/get)   * Added `ticket_url` and `assigned_users` properties to the subscriptions response for the `ticket.checklist.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1ticket.checklist.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.submitted` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.updated` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.updated/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.approved` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added `application_url`, `identifier` and `lid` properties to the subscriptions response for the `turboapp.declined` subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)   * Changed all subscriptions dates properties to the snake case **Link:** [#tag/Subscriptions](https://www.mycoastalpay.com/api/#tag/Subscriptions)       ### 1.3.5 (2020-02-26)   #### Created:   * Added a Helpdesk API to work with your helpdesk data. **Link:** [#tag/Helpdesk](https://www.mycoastalpay.com/api/#tag/Helpdesk)       ### 1.3.4 (2020-02-25)   #### Updated:   * Added a `lid` property to the \"turboapp.submitted\" subscription. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)       ### 1.3.3 (2020-02-24)   #### Updated:   * Added a `salesRep` parameter to 'lead.status.updated' subscription. **Link:** [#/paths/~1subscriptions~1sample~1lead.status.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1lead.status.updated/get)       ### 1.3.2 (2019-11-21)   #### Updated:   * Added a `expire` parameter to 'Generate an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1generate/post)   * Added the ability to add multiple signers to the document and added an `expire` parameter to 'Send an e-signature document' endpoint. **Link:** [#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post](https://www.mycoastalpay.com/api/#/paths/~1leads~1{leadId}~1signatures~1{applicationId}~1send/post)       ### 1.3.1 (2019-11-18)   #### Updated:   * Rename subscriptions from \"application.created\" to \"turboapp.submitted\" and \"application.updated\" to \"turboapp.updated\". **Link:** [#/paths/~1subscriptions~1sample~1turboapp.submitted/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.submitted/get)     #### Created:   * Added new subscriptions for \"turboapp.approved\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.approved/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.approved/get)   * Added new subscriptions for \"turboapp.declined\" event. **Link:** [#/paths/~1subscriptions~1sample~1turboapp.declined/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1turboapp.declined/get)       ### 1.2.2 (2019-09-03)   #### Updated:   * Added a `per_page` property to all list endpoints.       ### 1.2.1 (2019-08-26)   #### Updated:   * Added a `leads` property to merchants endpoint. **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.2.0 (2019-07-26)   #### Updated:   * The endpoint for creating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions/post](https://www.mycoastalpay.com/api/#/paths/~1subscriptions/post)   * The endpoint for updating API subscriptions has been updated. Status based options have been added to some events. **Link:** [#/paths/~1subscriptions~1{subscriptionId}/patch](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1{subscriptionId}/patch)       ### 1.1.0 (2019-07-24)   #### Created:   * Added an endpoint for getting SMS templates. **Link:** [#/paths/~1leads~1sms~1templates/get](https://www.mycoastalpay.com/api/#/paths/~1leads~1sms~1templates/get)   * Added new subscriptions for `application.created` event **Link:** [#/paths/~1subscriptions~1sample~1application.created/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.created/get)   * Added new subscriptions for `application.updated` event **Link:** [#/paths/~1subscriptions~1sample~1application.updated/get](https://www.mycoastalpay.com/api/#/paths/~1subscriptions~1sample~1application.updated/get)     #### Updated:   * Added a `sic_code` property to merchants endpoint **Link:** [#/paths/~1merchants/get](https://www.mycoastalpay.com/api/#/paths/~1merchants/get)       ### 1.0.0 (2019-06-20)   #### Created:   * Added change log.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: helpdesk@coastalpay.com
    Generated by: https://openapi-generator.tech
"""


from datetime import date, datetime  # noqa: F401
from copy import deepcopy
import inspect
import io
import os
import pprint
import re
import tempfile
import uuid

from dateutil.parser import parse

from iriscrm.exceptions import (
    ApiKeyError,
    ApiAttributeError,
    ApiTypeError,
    ApiValueError,
)

none_type = type(None)
file_type = io.IOBase


def convert_js_args_to_python_args(fn):
    from functools import wraps
    @wraps(fn)
    def wrapped_init(_self, *args, **kwargs):
        """
        An attribute named `self` received from the api will conflicts with the reserved `self`
        parameter of a class method. During generation, `self` attributes are mapped
        to `_self` in models. Here, we name `_self` instead of `self` to avoid conflicts.
        """
        spec_property_naming = kwargs.get('_spec_property_naming', False)
        if spec_property_naming:
            kwargs = change_keys_js_to_python(
                kwargs, _self if isinstance(
                    _self, type) else _self.__class__)
        return fn(_self, *args, **kwargs)
    return wrapped_init


class cached_property(object):
    # this caches the result of the function call for fn with no inputs
    # use this as a decorator on function methods that you want converted
    # into cached properties
    result_key = '_results'

    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls=None):
        if self.result_key in vars(self):
            return vars(self)[self.result_key]
        else:
            result = self._fn()
            setattr(self, self.result_key, result)
            return result


PRIMITIVE_TYPES = (list, float, int, bool, datetime, date, str, file_type)


def allows_single_value_input(cls):
    """
    This function returns True if the input composed schema model or any
    descendant model allows a value only input
    This is true for cases where oneOf contains items like:
    oneOf:
      - float
      - NumberWithValidation
      - StringEnum
      - ArrayModel
      - null
    TODO: lru_cache this
    """
    if (
        issubclass(cls, ModelSimple) or
        cls in PRIMITIVE_TYPES
    ):
        return True
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return False
        return any(allows_single_value_input(c) for c in cls._composed_schemas['oneOf'])
    return False


def composed_model_input_classes(cls):
    """
    This function returns a list of the possible models that can be accepted as
    inputs.
    TODO: lru_cache this
    """
    if issubclass(cls, ModelSimple) or cls in PRIMITIVE_TYPES:
        return [cls]
    elif issubclass(cls, ModelNormal):
        if cls.discriminator is None:
            return [cls]
        else:
            return get_discriminated_classes(cls)
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return []
        if cls.discriminator is None:
            input_classes = []
            for c in cls._composed_schemas['oneOf']:
                input_classes.extend(composed_model_input_classes(c))
            return input_classes
        else:
            return get_discriminated_classes(cls)
    return []


class OpenApiModel(object):
    """The base class for all OpenAPIModels"""

    def set_attribute(self, name, value):
        # this is only used to set properties on self

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)

        if name in self.openapi_types:
            required_types_mixed = self.openapi_types[name]
        elif self.additional_properties_type is None:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                path_to_item
            )
        elif self.additional_properties_type is not None:
            required_types_mixed = self.additional_properties_type

        if get_simple_class(name) != str:
            error_msg = type_error_message(
                var_name=name,
                var_value=name,
                valid_classes=(str,),
                key_type=True
            )
            raise ApiTypeError(
                error_msg,
                path_to_item=path_to_item,
                valid_classes=(str,),
                key_type=True
            )

        if self._check_type:
            value = validate_and_convert_types(
                value, required_types_mixed, path_to_item, self._spec_property_naming,
                self._check_type, configuration=self._configuration)
        if (name,) in self.allowed_values:
            check_allowed_values(
                self.allowed_values,
                (name,),
                value
            )
        if (name,) in self.validations:
            check_validations(
                self.validations,
                (name,),
                value,
                self._configuration
            )
        self.__dict__['_data_store'][name] = value

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def __setattr__(self, attr, value):
        """set the value of an attribute using dot notation: `instance.attr = val`"""
        self[attr] = value

    def __getattr__(self, attr):
        """get the value of an attribute using dot notation: `instance.attr`"""
        return self.__getitem__(attr)

    def __copy__(self):
        cls = self.__class__
        if self.get("_spec_property_naming", False):
            return cls._new_from_openapi_data(**self.__dict__)
        else:
            return cls.__new__(cls, **self.__dict__)

    def __deepcopy__(self, memo):
        cls = self.__class__

        if self.get("_spec_property_naming", False):
            new_inst = cls._new_from_openapi_data()
        else:
            new_inst = cls.__new__(cls, **self.__dict__)

        for k, v in self.__dict__.items():
            setattr(new_inst, k, deepcopy(v, memo))
        return new_inst


    def __new__(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return super(OpenApiModel, cls).__new__(cls)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return super(OpenApiModel, cls).__new__(cls)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = super(OpenApiModel, cls).__new__(cls)
            self_inst.__init__(*args, **kwargs)

        if kwargs.get("_spec_property_naming", False):
            # when true, implies new is from deserialization
            new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        else:
            new_inst = new_cls.__new__(new_cls, *args, **kwargs)
            new_inst.__init__(*args, **kwargs)

        return new_inst

    @classmethod
    @convert_js_args_to_python_args
    def _new_from_openapi_data(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return cls._from_openapi_data(*args, **kwargs)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return cls._from_openapi_data(*args, **kwargs)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = cls._from_openapi_data(*args, **kwargs)

        new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        return new_inst


class ModelSimple(OpenApiModel):
    """the parent class of models whose type != object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_str(self):
        """Returns the string representation of the model"""
        return str(self.value)

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        this_val = self._data_store['value']
        that_val = other._data_store['value']
        types = set()
        types.add(this_val.__class__)
        types.add(that_val.__class__)
        vals_equal = this_val == that_val
        return vals_equal


class ModelNormal(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


class ModelComposed(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi and have oneOf/allOf/anyOf

    When one sets a property we use var_name_to_model_instances to store the value in
    the correct class instances + run any type checking + validation code.
    When one gets a property we use var_name_to_model_instances to get the value
    from the correct class instances.
    This allows multiple composed schemas to contain the same property with additive
    constraints on the value.

    _composed_schemas (dict) stores the anyOf/allOf/oneOf classes
    key (str): allOf/oneOf/anyOf
    value (list): the classes in the XOf definition.
        Note: none_type can be included when the openapi document version >= 3.1.0
    _composed_instances (list): stores a list of instances of the composed schemas
    defined in _composed_schemas. When properties are accessed in the self instance,
    they are returned from the self._data_store or the data stores in the instances
    in self._composed_schemas
    _var_name_to_model_instances (dict): maps between a variable name on self and
    the composed instances (self included) which contain that data
    key (str): property name
    value (list): list of class instances, self or instances in _composed_instances
    which contain the value that the key is referring to.
    """

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        """
        Use cases:
        1. additional_properties_type is None (additionalProperties == False in spec)
            Check for property presence in self.openapi_types
            if not present then throw an error
            if present set in self, set attribute
            always set on composed schemas
        2.  additional_properties_type exists
            set attribute on self
            always set on composed schemas
        """
        if self.additional_properties_type is None:
            """
            For an attribute to exist on a composed schema it must:
            - fulfill schema_requirements in the self composed schema not considering oneOf/anyOf/allOf schemas AND
            - fulfill schema_requirements in each oneOf/anyOf/allOf schemas

            schema_requirements:
            For an attribute to exist on a schema it must:
            - be present in properties at the schema OR
            - have additionalProperties unset (defaults additionalProperties = any type) OR
            - have additionalProperties set
            """
            if name not in self.openapi_types:
                raise ApiAttributeError(
                    "{0} has no attribute '{1}'".format(
                        type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
                )
        # attribute must be set on self and composed instances
        self.set_attribute(name, value)
        for model_instance in self._composed_instances:
            setattr(model_instance, name, value)
        if name not in self._var_name_to_model_instances:
            # we assigned an additional property
            self.__dict__['_var_name_to_model_instances'][name] = self._composed_instances + [self]
        return None

    __unset_attribute_value__ = object()

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        # get the attribute from the correct instance
        model_instances = self._var_name_to_model_instances.get(name)
        values = []
        # A composed model stores self and child (oneof/anyOf/allOf) models under
        # self._var_name_to_model_instances.
        # Any property must exist in self and all model instances
        # The value stored in all model instances must be the same
        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    v = model_instance._data_store[name]
                    if v not in values:
                        values.append(v)
        len_values = len(values)
        if len_values == 0:
            return default
        elif len_values == 1:
            return values[0]
        elif len_values > 1:
            raise ApiValueError(
                "Values stored for property {0} in {1} differ when looking "
                "at self and self's composed instances. All values must be "
                "the same".format(name, type(self).__name__),
                [e for e in [self._path_to_item, name] if e]
            )

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        value = self.get(name, self.__unset_attribute_value__)
        if value is self.__unset_attribute_value__:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
            )
        return value

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""

        if name in self.required_properties:
            return name in self.__dict__

        model_instances = self._var_name_to_model_instances.get(
            name, self._additional_properties_model_instances)

        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    return True

        return False

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


COERCION_INDEX_BY_TYPE = {
    ModelComposed: 0,
    ModelNormal: 1,
    ModelSimple: 2,
    none_type: 3,    # The type of 'None'.
    list: 4,
    dict: 5,
    float: 6,
    int: 7,
    bool: 8,
    datetime: 9,
    date: 10,
    str: 11,
    file_type: 12,   # 'file_type' is an alias for the built-in 'file' or 'io.IOBase' type.
}

# these are used to limit what type conversions we try to do
# when we have a valid type already and we want to try converting
# to another type
UPCONVERSION_TYPE_PAIRS = (
    (str, datetime),
    (str, date),
    # A float may be serialized as an integer, e.g. '3' is a valid serialized float.
    (int, float),
    (list, ModelComposed),
    (dict, ModelComposed),
    (str, ModelComposed),
    (int, ModelComposed),
    (float, ModelComposed),
    (list, ModelComposed),
    (list, ModelNormal),
    (dict, ModelNormal),
    (str, ModelSimple),
    (int, ModelSimple),
    (float, ModelSimple),
    (list, ModelSimple),
)

COERCIBLE_TYPE_PAIRS = {
    False: (  # client instantiation of a model with client data
        # (dict, ModelComposed),
        # (list, ModelComposed),
        # (dict, ModelNormal),
        # (list, ModelNormal),
        # (str, ModelSimple),
        # (int, ModelSimple),
        # (float, ModelSimple),
        # (list, ModelSimple),
        # (str, int),
        # (str, float),
        # (str, datetime),
        # (str, date),
        # (int, str),
        # (float, str),
    ),
    True: (  # server -> client data
        (dict, ModelComposed),
        (list, ModelComposed),
        (dict, ModelNormal),
        (list, ModelNormal),
        (str, ModelSimple),
        (int, ModelSimple),
        (float, ModelSimple),
        (list, ModelSimple),
        # (str, int),
        # (str, float),
        (str, datetime),
        (str, date),
        # (int, str),
        # (float, str),
        (str, file_type)
    ),
}


def get_simple_class(input_value):
    """Returns an input_value's simple class that we will use for type checking
    Python2:
    float and int will return int, where int is the python3 int backport
    str and unicode will return str, where str is the python3 str backport
    Note: float and int ARE both instances of int backport
    Note: str_py2 and unicode_py2 are NOT both instances of str backport

    Args:
        input_value (class/class_instance): the item for which we will return
                                            the simple class
    """
    if isinstance(input_value, type):
        # input_value is a class
        return input_value
    elif isinstance(input_value, tuple):
        return tuple
    elif isinstance(input_value, list):
        return list
    elif isinstance(input_value, dict):
        return dict
    elif isinstance(input_value, none_type):
        return none_type
    elif isinstance(input_value, file_type):
        return file_type
    elif isinstance(input_value, bool):
        # this must be higher than the int check because
        # isinstance(True, int) == True
        return bool
    elif isinstance(input_value, int):
        return int
    elif isinstance(input_value, datetime):
        # this must be higher than the date check because
        # isinstance(datetime_instance, date) == True
        return datetime
    elif isinstance(input_value, date):
        return date
    elif isinstance(input_value, str):
        return str
    return type(input_value)


def check_allowed_values(allowed_values, input_variable_path, input_values):
    """Raises an exception if the input_values are not allowed

    Args:
        allowed_values (dict): the allowed_values dict
        input_variable_path (tuple): the path to the input variable
        input_values (list/str/int/float/date/datetime): the values that we
            are checking to see if they are in allowed_values
    """
    these_allowed_values = list(allowed_values[input_variable_path].values())
    if (isinstance(input_values, list)
            and not set(input_values).issubset(
                set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values) - set(these_allowed_values))),
        raise ApiValueError(
            "Invalid values for `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (isinstance(input_values, dict)
            and not set(
                input_values.keys()).issubset(set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values.keys()) - set(these_allowed_values)))
        raise ApiValueError(
            "Invalid keys in `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (not isinstance(input_values, (list, dict))
            and input_values not in these_allowed_values):
        raise ApiValueError(
            "Invalid value for `%s` (%s), must be one of %s" %
            (
                input_variable_path[0],
                input_values,
                these_allowed_values
            )
        )


def is_json_validation_enabled(schema_keyword, configuration=None):
    """Returns true if JSON schema validation is enabled for the specified
    validation keyword. This can be used to skip JSON schema structural validation
    as requested in the configuration.

    Args:
        schema_keyword (string): the name of a JSON schema validation keyword.
        configuration (Configuration): the configuration class.
    """

    return (configuration is None or
            not hasattr(configuration, '_disabled_client_side_validations') or
            schema_keyword not in configuration._disabled_client_side_validations)


def check_validations(
        validations, input_variable_path, input_values,
        configuration=None):
    """Raises an exception if the input_values are invalid

    Args:
        validations (dict): the validation dictionary.
        input_variable_path (tuple): the path to the input variable.
        input_values (list/str/int/float/date/datetime): the values that we
            are checking.
        configuration (Configuration): the configuration class.
    """

    if input_values is None:
        return

    current_validations = validations[input_variable_path]
    if (is_json_validation_enabled('multipleOf', configuration) and
            'multiple_of' in current_validations and
            isinstance(input_values, (int, float)) and
            not (float(input_values) / current_validations['multiple_of']).is_integer()):
        # Note 'multipleOf' will be as good as the floating point arithmetic.
        raise ApiValueError(
            "Invalid value for `%s`, value must be a multiple of "
            "`%s`" % (
                input_variable_path[0],
                current_validations['multiple_of']
            )
        )

    if (is_json_validation_enabled('maxLength', configuration) and
            'max_length' in current_validations and
            len(input_values) > current_validations['max_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['max_length']
            )
        )

    if (is_json_validation_enabled('minLength', configuration) and
            'min_length' in current_validations and
            len(input_values) < current_validations['min_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be greater than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['min_length']
            )
        )

    if (is_json_validation_enabled('maxItems', configuration) and
            'max_items' in current_validations and
            len(input_values) > current_validations['max_items']):
        raise ApiValueError(
            "Invalid value for `%s`, number of items must be less than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['max_items']
            )
        )

    if (is_json_validation_enabled('minItems', configuration) and
            'min_items' in current_validations and
            len(input_values) < current_validations['min_items']):
        raise ValueError(
            "Invalid value for `%s`, number of items must be greater than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['min_items']
            )
        )

    items = ('exclusive_maximum', 'inclusive_maximum', 'exclusive_minimum',
             'inclusive_minimum')
    if (any(item in current_validations for item in items)):
        if isinstance(input_values, list):
            max_val = max(input_values)
            min_val = min(input_values)
        elif isinstance(input_values, dict):
            max_val = max(input_values.values())
            min_val = min(input_values.values())
        else:
            max_val = input_values
            min_val = input_values

    if (is_json_validation_enabled('exclusiveMaximum', configuration) and
            'exclusive_maximum' in current_validations and
            max_val >= current_validations['exclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than `%s`" % (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('maximum', configuration) and
            'inclusive_maximum' in current_validations and
            max_val > current_validations['inclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['inclusive_maximum']
            )
        )

    if (is_json_validation_enabled('exclusiveMinimum', configuration) and
            'exclusive_minimum' in current_validations and
            min_val <= current_validations['exclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than `%s`" %
            (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('minimum', configuration) and
            'inclusive_minimum' in current_validations and
            min_val < current_validations['inclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than or equal "
            "to `%s`" % (
                input_variable_path[0],
                current_validations['inclusive_minimum']
            )
        )
    flags = current_validations.get('regex', {}).get('flags', 0)
    if (is_json_validation_enabled('pattern', configuration) and
            'regex' in current_validations and
            not re.search(current_validations['regex']['pattern'],
                          input_values, flags=flags)):
        err_msg = r"Invalid value for `%s`, must match regular expression `%s`" % (
            input_variable_path[0],
            current_validations['regex']['pattern']
        )
        if flags != 0:
            # Don't print the regex flags if the flags are not
            # specified in the OAS document.
            err_msg = r"%s with flags=`%s`" % (err_msg, flags)
        raise ApiValueError(err_msg)


def order_response_types(required_types):
    """Returns the required types sorted in coercion order

    Args:
        required_types (list/tuple): collection of classes or instance of
            list or dict with class information inside it.

    Returns:
        (list): coercion order sorted collection of classes or instance
            of list or dict with class information inside it.
    """

    def index_getter(class_or_instance):
        if isinstance(class_or_instance, list):
            return COERCION_INDEX_BY_TYPE[list]
        elif isinstance(class_or_instance, dict):
            return COERCION_INDEX_BY_TYPE[dict]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelComposed)):
            return COERCION_INDEX_BY_TYPE[ModelComposed]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelNormal)):
            return COERCION_INDEX_BY_TYPE[ModelNormal]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelSimple)):
            return COERCION_INDEX_BY_TYPE[ModelSimple]
        elif class_or_instance in COERCION_INDEX_BY_TYPE:
            return COERCION_INDEX_BY_TYPE[class_or_instance]
        raise ApiValueError("Unsupported type: %s" % class_or_instance)

    sorted_types = sorted(
        required_types,
        key=lambda class_or_instance: index_getter(class_or_instance)
    )
    return sorted_types


def remove_uncoercible(required_types_classes, current_item, spec_property_naming,
                       must_convert=True):
    """Only keeps the type conversions that are possible

    Args:
        required_types_classes (tuple): tuple of classes that are required
                          these should be ordered by COERCION_INDEX_BY_TYPE
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        current_item (any): the current item (input data) to be converted

    Keyword Args:
        must_convert (bool): if True the item to convert is of the wrong
                          type and we want a big list of coercibles
                          if False, we want a limited list of coercibles

    Returns:
        (list): the remaining coercible required types, classes only
    """
    current_type_simple = get_simple_class(current_item)

    results_classes = []
    for required_type_class in required_types_classes:
        # convert our models to OpenApiModel
        required_type_class_simplified = required_type_class
        if isinstance(required_type_class_simplified, type):
            if issubclass(required_type_class_simplified, ModelComposed):
                required_type_class_simplified = ModelComposed
            elif issubclass(required_type_class_simplified, ModelNormal):
                required_type_class_simplified = ModelNormal
            elif issubclass(required_type_class_simplified, ModelSimple):
                required_type_class_simplified = ModelSimple

        if required_type_class_simplified == current_type_simple:
            # don't consider converting to one's own class
            continue

        class_pair = (current_type_simple, required_type_class_simplified)
        if must_convert and class_pair in COERCIBLE_TYPE_PAIRS[spec_property_naming]:
            results_classes.append(required_type_class)
        elif class_pair in UPCONVERSION_TYPE_PAIRS:
            results_classes.append(required_type_class)
    return results_classes


def get_discriminated_classes(cls):
    """
    Returns all the classes that a discriminator converts to
    TODO: lru_cache this
    """
    possible_classes = []
    key = list(cls.discriminator.keys())[0]
    if is_type_nullable(cls):
        possible_classes.append(cls)
    for discr_cls in cls.discriminator[key].values():
        if hasattr(discr_cls, 'discriminator') and discr_cls.discriminator is not None:
            possible_classes.extend(get_discriminated_classes(discr_cls))
        else:
            possible_classes.append(discr_cls)
    return possible_classes


def get_possible_classes(cls, from_server_context):
    # TODO: lru_cache this
    possible_classes = [cls]
    if from_server_context:
        return possible_classes
    if hasattr(cls, 'discriminator') and cls.discriminator is not None:
        possible_classes = []
        possible_classes.extend(get_discriminated_classes(cls))
    elif issubclass(cls, ModelComposed):
        possible_classes.extend(composed_model_input_classes(cls))
    return possible_classes


def get_required_type_classes(required_types_mixed, spec_property_naming):
    """Converts the tuple required_types into a tuple and a dict described
    below

    Args:
        required_types_mixed (tuple/list): will contain either classes or
            instance of list or dict
        spec_property_naming (bool): if True these values came from the
            server, and we use the data types in our endpoints.
            If False, we are client side and we need to include
            oneOf and discriminator classes inside the data types in our endpoints

    Returns:
        (valid_classes, dict_valid_class_to_child_types_mixed):
            valid_classes (tuple): the valid classes that the current item
                                   should be
            dict_valid_class_to_child_types_mixed (dict):
                valid_class (class): this is the key
                child_types_mixed (list/dict/tuple): describes the valid child
                    types
    """
    valid_classes = []
    child_req_types_by_current_type = {}
    for required_type in required_types_mixed:
        if isinstance(required_type, list):
            valid_classes.append(list)
            child_req_types_by_current_type[list] = required_type
        elif isinstance(required_type, tuple):
            valid_classes.append(tuple)
            child_req_types_by_current_type[tuple] = required_type
        elif isinstance(required_type, dict):
            valid_classes.append(dict)
            child_req_types_by_current_type[dict] = required_type[str]
        else:
            valid_classes.extend(get_possible_classes(required_type, spec_property_naming))
    return tuple(valid_classes), child_req_types_by_current_type


def change_keys_js_to_python(input_dict, model_class):
    """
    Converts from javascript_key keys in the input_dict to python_keys in
    the output dict using the mapping in model_class.
    If the input_dict contains a key which does not declared in the model_class,
    the key is added to the output dict as is. The assumption is the model_class
    may have undeclared properties (additionalProperties attribute in the OAS
    document).
    """

    if getattr(model_class, 'attribute_map', None) is None:
        return input_dict
    output_dict = {}
    reversed_attr_map = {value: key for key, value in
                         model_class.attribute_map.items()}
    for javascript_key, value in input_dict.items():
        python_key = reversed_attr_map.get(javascript_key)
        if python_key is None:
            # if the key is unknown, it is in error or it is an
            # additionalProperties variable
            python_key = javascript_key
        output_dict[python_key] = value
    return output_dict


def get_type_error(var_value, path_to_item, valid_classes, key_type=False):
    error_msg = type_error_message(
        var_name=path_to_item[-1],
        var_value=var_value,
        valid_classes=valid_classes,
        key_type=key_type
    )
    return ApiTypeError(
        error_msg,
        path_to_item=path_to_item,
        valid_classes=valid_classes,
        key_type=key_type
    )


def deserialize_primitive(data, klass, path_to_item):
    """Deserializes string to primitive type.

    :param data: str/int/float
    :param klass: str/class the class to convert to

    :return: int, float, str, bool, date, datetime
    """
    additional_message = ""
    try:
        if klass in {datetime, date}:
            additional_message = (
                "If you need your parameter to have a fallback "
                "string value, please set its type as `type: {}` in your "
                "spec. That allows the value to be any type. "
            )
            if klass == datetime:
                if len(data) < 8:
                    raise ValueError("This is not a datetime")
                # The string should be in iso8601 datetime format.
                parsed_datetime = parse(data)
                date_only = (
                    parsed_datetime.hour == 0 and
                    parsed_datetime.minute == 0 and
                    parsed_datetime.second == 0 and
                    parsed_datetime.tzinfo is None and
                    8 <= len(data) <= 10
                )
                if date_only:
                    raise ValueError("This is a date, not a datetime")
                return parsed_datetime
            elif klass == date:
                if len(data) < 8:
                    raise ValueError("This is not a date")
                return parse(data).date()
        else:
            converted_value = klass(data)
            if isinstance(data, str) and klass == float:
                if str(converted_value) != data:
                    # '7' -> 7.0 -> '7.0' != '7'
                    raise ValueError('This is not a float')
            return converted_value
    except (OverflowError, ValueError) as ex:
        # parse can raise OverflowError
        raise ApiValueError(
            "{0}Failed to parse {1} as {2}".format(
                additional_message, repr(data), klass.__name__
            ),
            path_to_item=path_to_item
        ) from ex


def get_discriminator_class(model_class,
                            discr_name,
                            discr_value, cls_visited):
    """Returns the child class specified by the discriminator.

    Args:
        model_class (OpenApiModel): the model class.
        discr_name (string): the name of the discriminator property.
        discr_value (any): the discriminator value.
        cls_visited (list): list of model classes that have been visited.
            Used to determine the discriminator class without
            visiting circular references indefinitely.

    Returns:
        used_model_class (class/None): the chosen child class that will be used
            to deserialize the data, for example dog.Dog.
            If a class is not found, None is returned.
    """

    if model_class in cls_visited:
        # The class has already been visited and no suitable class was found.
        return None
    cls_visited.append(model_class)
    used_model_class = None
    if discr_name in model_class.discriminator:
        class_name_to_discr_class = model_class.discriminator[discr_name]
        used_model_class = class_name_to_discr_class.get(discr_value)
    if used_model_class is None:
        # We didn't find a discriminated class in class_name_to_discr_class.
        # So look in the ancestor or descendant discriminators
        # The discriminator mapping may exist in a descendant (anyOf, oneOf)
        # or ancestor (allOf).
        # Ancestor example: in the GrandparentAnimal -> ParentPet -> ChildCat
        #   hierarchy, the discriminator mappings may be defined at any level
        #   in the hierarchy.
        # Descendant example:  mammal -> whale/zebra/Pig -> BasquePig/DanishPig
        #   if we try to make BasquePig from mammal, we need to travel through
        #   the oneOf descendant discriminators to find BasquePig
        descendant_classes = model_class._composed_schemas.get('oneOf', ()) + \
            model_class._composed_schemas.get('anyOf', ())
        ancestor_classes = model_class._composed_schemas.get('allOf', ())
        possible_classes = descendant_classes + ancestor_classes
        for cls in possible_classes:
            # Check if the schema has inherited discriminators.
            if hasattr(cls, 'discriminator') and cls.discriminator is not None:
                used_model_class = get_discriminator_class(
                    cls, discr_name, discr_value, cls_visited)
                if used_model_class is not None:
                    return used_model_class
    return used_model_class


def deserialize_model(model_data, model_class, path_to_item, check_type,
                      configuration, spec_property_naming):
    """Deserializes model_data to model instance.

    Args:
        model_data (int/str/float/bool/none_type/list/dict): data to instantiate the model
        model_class (OpenApiModel): the model class
        path_to_item (list): path to the model in the received data
        check_type (bool): whether to check the data tupe for the values in
            the model
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.

    Returns:
        model instance

    Raise:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """

    kw_args = dict(_check_type=check_type,
                   _path_to_item=path_to_item,
                   _configuration=configuration,
                   _spec_property_naming=spec_property_naming)

    if issubclass(model_class, ModelSimple):
        return model_class._new_from_openapi_data(model_data, **kw_args)
    elif isinstance(model_data, list):
        return model_class._new_from_openapi_data(*model_data, **kw_args)
    if isinstance(model_data, dict):
        kw_args.update(model_data)
        return model_class._new_from_openapi_data(**kw_args)
    elif isinstance(model_data, PRIMITIVE_TYPES):
        return model_class._new_from_openapi_data(model_data, **kw_args)


def deserialize_file(response_data, configuration, content_disposition=None):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    Args:
        param response_data (str):  the file data to write
        configuration (Configuration): the instance to use to convert files

    Keyword Args:
        content_disposition (str):  the value of the Content-Disposition
            header

    Returns:
        (file_type): the deserialized file which is open
            The user is responsible for closing and reading the file
    """
    fd, path = tempfile.mkstemp(dir=configuration.temp_folder_path)
    os.close(fd)
    os.remove(path)

    if content_disposition:
        filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                             content_disposition,
                             flags=re.I)
        if filename is not None:
            filename = filename.group(1)
        else:
            filename = "default_" + str(uuid.uuid4())

        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "wb") as f:
        if isinstance(response_data, str):
            # change str to bytes so we can write it
            response_data = response_data.encode('utf-8')
        f.write(response_data)

    f = open(path, "rb")
    return f


def attempt_convert_item(input_value, valid_classes, path_to_item,
                         configuration, spec_property_naming, key_type=False,
                         must_convert=False, check_type=True):
    """
    Args:
        input_value (any): the data to convert
        valid_classes (any): the classes that are valid
        path_to_item (list): the path to the item to convert
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        key_type (bool): if True we need to convert a key type (not supported)
        must_convert (bool): if True we must convert
        check_type (bool): if True we check the type or the returned data in
            ModelComposed/ModelNormal/ModelSimple instances

    Returns:
        instance (any) the fixed item

    Raises:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """
    valid_classes_ordered = order_response_types(valid_classes)
    valid_classes_coercible = remove_uncoercible(
        valid_classes_ordered, input_value, spec_property_naming)
    if not valid_classes_coercible or key_type:
        # we do not handle keytype errors, json will take care
        # of this for us
        if configuration is None or not configuration.discard_unknown_keys:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=key_type)
    for valid_class in valid_classes_coercible:
        try:
            if issubclass(valid_class, OpenApiModel):
                return deserialize_model(input_value, valid_class,
                                         path_to_item, check_type,
                                         configuration, spec_property_naming)
            elif valid_class == file_type:
                return deserialize_file(input_value, configuration)
            return deserialize_primitive(input_value, valid_class,
                                         path_to_item)
        except (ApiTypeError, ApiValueError, ApiKeyError) as conversion_exc:
            if must_convert:
                raise conversion_exc
            # if we have conversion errors when must_convert == False
            # we ignore the exception and move on to the next class
            continue
    # we were unable to convert, must_convert == False
    return input_value


def is_type_nullable(input_type):
    """
    Returns true if None is an allowed value for the specified input_type.

    A type is nullable if at least one of the following conditions is true:
    1. The OAS 'nullable' attribute has been specified,
    1. The type is the 'null' type,
    1. The type is a anyOf/oneOf composed schema, and a child schema is
       the 'null' type.
    Args:
        input_type (type): the class of the input_value that we are
            checking
    Returns:
        bool
    """
    if input_type is none_type:
        return True
    if issubclass(input_type, OpenApiModel) and input_type._nullable:
        return True
    if issubclass(input_type, ModelComposed):
        # If oneOf/anyOf, check if the 'null' type is one of the allowed types.
        for t in input_type._composed_schemas.get('oneOf', ()):
            if is_type_nullable(t):
                return True
        for t in input_type._composed_schemas.get('anyOf', ()):
            if is_type_nullable(t):
                return True
    return False


def is_valid_type(input_class_simple, valid_classes):
    """
    Args:
        input_class_simple (class): the class of the input_value that we are
            checking
        valid_classes (tuple): the valid classes that the current item
            should be
    Returns:
        bool
    """
    if issubclass(input_class_simple, OpenApiModel) and \
            valid_classes == (bool, date, datetime, dict, float, int, list, str, none_type,):
        return True
    valid_type = input_class_simple in valid_classes
    if not valid_type and (
            issubclass(input_class_simple, OpenApiModel) or
            input_class_simple is none_type):
        for valid_class in valid_classes:
            if input_class_simple is none_type and is_type_nullable(valid_class):
                # Schema is oneOf/anyOf and the 'null' type is one of the allowed types.
                return True
            if not (issubclass(valid_class, OpenApiModel) and valid_class.discriminator):
                continue
            discr_propertyname_py = list(valid_class.discriminator.keys())[0]
            discriminator_classes = (
                valid_class.discriminator[discr_propertyname_py].values()
            )
            valid_type = is_valid_type(input_class_simple, discriminator_classes)
            if valid_type:
                return True
    return valid_type


def validate_and_convert_types(input_value, required_types_mixed, path_to_item,
                               spec_property_naming, _check_type, configuration=None):
    """Raises a TypeError is there is a problem, otherwise returns value

    Args:
        input_value (any): the data to validate/convert
        required_types_mixed (list/dict/tuple): A list of
            valid classes, or a list tuples of valid classes, or a dict where
            the value is a tuple of value classes
        path_to_item: (list) the path to the data being validated
            this stores a list of keys or indices to get to the data being
            validated
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        _check_type: (boolean) if true, type will be checked and conversion
            will be attempted.
        configuration: (Configuration): the configuration class to use
            when converting file_type items.
            If passed, conversion will be attempted when possible
            If not passed, no conversions will be attempted and
            exceptions will be raised

    Returns:
        the correctly typed value

    Raises:
        ApiTypeError
    """
    results = get_required_type_classes(required_types_mixed, spec_property_naming)
    valid_classes, child_req_types_by_current_type = results

    input_class_simple = get_simple_class(input_value)
    valid_type = is_valid_type(input_class_simple, valid_classes)
    if not valid_type:
        if (configuration
                or (input_class_simple == dict
                    and dict not in valid_classes)):
            # if input_value is not valid_type try to convert it
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=True,
                check_type=_check_type
            )
            return converted_instance
        else:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=False)

    # input_value's type is in valid_classes
    if len(valid_classes) > 1 and configuration:
        # there are valid classes which are not the current class
        valid_classes_coercible = remove_uncoercible(
            valid_classes, input_value, spec_property_naming, must_convert=False)
        if valid_classes_coercible:
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes_coercible,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=False,
                check_type=_check_type
            )
            return converted_instance

    if child_req_types_by_current_type == {}:
        # all types are of the required types and there are no more inner
        # variables left to look at
        return input_value
    inner_required_types = child_req_types_by_current_type.get(
        type(input_value)
    )
    if inner_required_types is None:
        # for this type, there are not more inner variables left to look at
        return input_value
    if isinstance(input_value, list):
        if input_value == []:
            # allow an empty list
            return input_value
        for index, inner_value in enumerate(input_value):
            inner_path = list(path_to_item)
            inner_path.append(index)
            input_value[index] = validate_and_convert_types(
                inner_value,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    elif isinstance(input_value, dict):
        if input_value == {}:
            # allow an empty dict
            return input_value
        for inner_key, inner_val in input_value.items():
            inner_path = list(path_to_item)
            inner_path.append(inner_key)
            if get_simple_class(inner_key) != str:
                raise get_type_error(inner_key, inner_path, valid_classes,
                                     key_type=True)
            input_value[inner_key] = validate_and_convert_types(
                inner_val,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    return input_value


def model_to_dict(model_instance, serialize=True):
    """Returns the model properties as a dict

    Args:
        model_instance (one of your model instances): the model instance that
            will be converted to a dict.

    Keyword Args:
        serialize (bool): if True, the keys in the dict will be values from
            attribute_map
    """
    result = {}

    def extract_item(item): return (
        item[0], model_to_dict(
            item[1], serialize=serialize)) if hasattr(
        item[1], '_data_store') else item

    model_instances = [model_instance]
    if model_instance._composed_schemas:
        model_instances.extend(model_instance._composed_instances)
    seen_json_attribute_names = set()
    used_fallback_python_attribute_names = set()
    py_to_json_map = {}
    for model_instance in model_instances:
        for attr, value in model_instance._data_store.items():
            if serialize:
                # we use get here because additional property key names do not
                # exist in attribute_map
                try:
                    attr = model_instance.attribute_map[attr]
                    py_to_json_map.update(model_instance.attribute_map)
                    seen_json_attribute_names.add(attr)
                except KeyError:
                    used_fallback_python_attribute_names.add(attr)
            if isinstance(value, list):
                if not value:
                    # empty list or None
                    result[attr] = value
                else:
                    res = []
                    for v in value:
                        if isinstance(v, PRIMITIVE_TYPES) or v is None:
                            res.append(v)
                        elif isinstance(v, ModelSimple):
                            res.append(v.value)
                        elif isinstance(v, dict):
                            res.append(dict(map(
                                extract_item,
                                v.items()
                            )))
                        else:
                            res.append(model_to_dict(v, serialize=serialize))
                    result[attr] = res
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    extract_item,
                    value.items()
                ))
            elif isinstance(value, ModelSimple):
                result[attr] = value.value
            elif hasattr(value, '_data_store'):
                result[attr] = model_to_dict(value, serialize=serialize)
            else:
                result[attr] = value
    if serialize:
        for python_key in used_fallback_python_attribute_names:
            json_key = py_to_json_map.get(python_key)
            if json_key is None:
                continue
            if python_key == json_key:
                continue
            json_key_assigned_no_need_for_python_key = json_key in seen_json_attribute_names
            if json_key_assigned_no_need_for_python_key:
                del result[python_key]

    return result


def type_error_message(var_value=None, var_name=None, valid_classes=None,
                       key_type=None):
    """
    Keyword Args:
        var_value (any): the variable which has the type_error
        var_name (str): the name of the variable which has the typ error
        valid_classes (tuple): the accepted classes for current_item's
                                  value
        key_type (bool): False if our value is a value in a dict
                         True if it is a key in a dict
                         False if our item is an item in a list
    """
    key_or_value = 'value'
    if key_type:
        key_or_value = 'key'
    valid_classes_phrase = get_valid_classes_phrase(valid_classes)
    msg = (
        "Invalid type for variable '{0}'. Required {1} type {2} and "
        "passed type was {3}".format(
            var_name,
            key_or_value,
            valid_classes_phrase,
            type(var_value).__name__,
        )
    )
    return msg


def get_valid_classes_phrase(input_classes):
    """Returns a string phrase describing what types are allowed
    """
    all_classes = list(input_classes)
    all_classes = sorted(all_classes, key=lambda cls: cls.__name__)
    all_class_names = [cls.__name__ for cls in all_classes]
    if len(all_class_names) == 1:
        return 'is {0}'.format(all_class_names[0])
    return "is one of [{0}]".format(", ".join(all_class_names))


def get_allof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            used to make instances
        constant_args (dict):
            metadata arguments:
            _check_type
            _path_to_item
            _spec_property_naming
            _configuration
            _visited_composed_classes

    Returns
        composed_instances (list)
    """
    composed_instances = []
    for allof_class in self._composed_schemas['allOf']:

        try:
            if constant_args.get('_spec_property_naming'):
                allof_instance = allof_class._from_openapi_data(**model_args, **constant_args)
            else:
                allof_instance = allof_class(**model_args, **constant_args)
            composed_instances.append(allof_instance)
        except Exception as ex:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of '%s'. The "
                "input data was invalid for the allOf schema '%s' in the composed "
                "schema '%s'. Error=%s" % (
                    allof_class.__name__,
                    allof_class.__name__,
                    self.__class__.__name__,
                    str(ex)
                )
            ) from ex
    return composed_instances


def get_oneof_instance(cls, model_kwargs, constant_kwargs, model_arg=None):
    """
    Find the oneOf schema that matches the input data (e.g. payload).
    If exactly one schema matches the input data, an instance of that schema
    is returned.
    If zero or more than one schema match the input data, an exception is raised.
    In OAS 3.x, the payload MUST, by validation, match exactly one of the
    schemas described by oneOf.

    Args:
        cls: the class we are handling
        model_kwargs (dict): var_name to var_value
            The input data, e.g. the payload that must match a oneOf schema
            in the OpenAPI document.
        constant_kwargs (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Kwargs:
        model_arg: (int, float, bool, str, date, datetime, ModelSimple, None):
            the value to assign to a primitive class or ModelSimple class
            Notes:
            - this is only passed in when oneOf includes types which are not object
            - None is used to suppress handling of model_arg, nullable models are handled in __new__

    Returns
        oneof_instance (instance)
    """
    if len(cls._composed_schemas['oneOf']) == 0:
        return None

    oneof_instances = []
    # Iterate over each oneOf schema and determine if the input data
    # matches the oneOf schemas.
    for oneof_class in cls._composed_schemas['oneOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if oneof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        single_value_input = allows_single_value_input(oneof_class)

        try:
            if not single_value_input:
                if constant_kwargs.get('_spec_property_naming'):
                    oneof_instance = oneof_class._from_openapi_data(
                        **model_kwargs, **constant_kwargs)
                else:
                    oneof_instance = oneof_class(**model_kwargs, **constant_kwargs)
            else:
                if issubclass(oneof_class, ModelSimple):
                    if constant_kwargs.get('_spec_property_naming'):
                        oneof_instance = oneof_class._from_openapi_data(
                            model_arg, **constant_kwargs)
                    else:
                        oneof_instance = oneof_class(model_arg, **constant_kwargs)
                elif oneof_class in PRIMITIVE_TYPES:
                    oneof_instance = validate_and_convert_types(
                        model_arg,
                        (oneof_class,),
                        constant_kwargs['_path_to_item'],
                        constant_kwargs['_spec_property_naming'],
                        constant_kwargs['_check_type'],
                        configuration=constant_kwargs['_configuration']
                    )
            oneof_instances.append(oneof_instance)
        except Exception:
            pass
    if len(oneof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None "
            "of the oneOf schemas matched the input data." %
            cls.__name__
        )
    elif len(oneof_instances) > 1:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. Multiple "
            "oneOf schemas matched the inputs, but a max of one is allowed." %
            cls.__name__
        )
    return oneof_instances[0]


def get_anyof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            The input data, e.g. the payload that must match at least one
            anyOf child schema in the OpenAPI document.
        constant_args (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Returns
        anyof_instances (list)
    """
    anyof_instances = []
    if len(self._composed_schemas['anyOf']) == 0:
        return anyof_instances

    for anyof_class in self._composed_schemas['anyOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if anyof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        try:
            if constant_args.get('_spec_property_naming'):
                anyof_instance = anyof_class._from_openapi_data(**model_args, **constant_args)
            else:
                anyof_instance = anyof_class(**model_args, **constant_args)
            anyof_instances.append(anyof_instance)
        except Exception:
            pass
    if len(anyof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None of the "
            "anyOf schemas matched the inputs." %
            self.__class__.__name__
        )
    return anyof_instances


def get_discarded_args(self, composed_instances, model_args):
    """
    Gathers the args that were discarded by configuration.discard_unknown_keys
    """
    model_arg_keys = model_args.keys()
    discarded_args = set()
    # arguments passed to self were already converted to python names
    # before __init__ was called
    for instance in composed_instances:
        if instance.__class__ in self._composed_schemas['allOf']:
            try:
                keys = instance.to_dict().keys()
                discarded_keys = model_args - keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
        else:
            try:
                all_keys = set(model_to_dict(instance, serialize=False).keys())
                js_keys = model_to_dict(instance, serialize=True).keys()
                all_keys.update(js_keys)
                discarded_keys = model_arg_keys - all_keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
    return discarded_args


def validate_get_composed_info(constant_args, model_args, self):
    """
    For composed schemas, generate schema instances for
    all schemas in the oneOf/anyOf/allOf definition. If additional
    properties are allowed, also assign those properties on
    all matched schemas that contain additionalProperties.
    Openapi schemas are python classes.

    Exceptions are raised if:
    - 0 or > 1 oneOf schema matches the model_args input data
    - no anyOf schema matches the model_args input data
    - any of the allOf schemas do not match the model_args input data

    Args:
        constant_args (dict): these are the args that every model requires
        model_args (dict): these are the required and optional spec args that
            were passed in to make this model
        self (class): the class that we are instantiating
            This class contains self._composed_schemas

    Returns:
        composed_info (list): length three
            composed_instances (list): the composed instances which are not
                self
            var_name_to_model_instances (dict): a dict going from var_name
                to the model_instance which holds that var_name
                the model_instance may be self or an instance of one of the
                classes in self.composed_instances()
            additional_properties_model_instances (list): a list of the
                model instances which have the property
                additional_properties_type. This list can include self
    """
    # create composed_instances
    composed_instances = []
    allof_instances = get_allof_instances(self, model_args, constant_args)
    composed_instances.extend(allof_instances)
    oneof_instance = get_oneof_instance(self.__class__, model_args, constant_args)
    if oneof_instance is not None:
        composed_instances.append(oneof_instance)
    anyof_instances = get_anyof_instances(self, model_args, constant_args)
    composed_instances.extend(anyof_instances)
    """
    set additional_properties_model_instances
    additional properties must be evaluated at the schema level
    so self's additional properties are most important
    If self is a composed schema with:
    - no properties defined in self
    - additionalProperties: False
    Then for object payloads every property is an additional property
    and they are not allowed, so only empty dict is allowed

    Properties must be set on all matching schemas
    so when a property is assigned toa composed instance, it must be set on all
    composed instances regardless of additionalProperties presence
    keeping it to prevent breaking changes in v5.0.1
    TODO remove cls._additional_properties_model_instances in 6.0.0
    """
    additional_properties_model_instances = []
    if self.additional_properties_type is not None:
        additional_properties_model_instances = [self]

    """
    no need to set properties on self in here, they will be set in __init__
    By here all composed schema oneOf/anyOf/allOf instances have their properties set using
    model_args
    """
    discarded_args = get_discarded_args(self, composed_instances, model_args)

    # map variable names to composed_instances
    var_name_to_model_instances = {}
    for prop_name in model_args:
        if prop_name not in discarded_args:
            var_name_to_model_instances[prop_name] = [self] + list(
                filter(
                    lambda x: prop_name in x.openapi_types, composed_instances))

    return [
        composed_instances,
        var_name_to_model_instances,
        additional_properties_model_instances,
        discarded_args
    ]

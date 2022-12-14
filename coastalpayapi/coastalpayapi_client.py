# -*- coding: utf-8 -*-

"""
coastalpayapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from coastalpayapi.decorators import lazy_property
from coastalpayapi.configuration import Configuration
from coastalpayapi.configuration import Environment
from coastalpayapi.http.auth.custom_header_authentication import CustomHeaderAuthentication
from coastalpayapi.controllers.e_signature_controller\
    import ESignatureController
from coastalpayapi.controllers.leads_controller import LeadsController


class CoastalpayapiClient(object):

    @lazy_property
    def e_signature(self):
        return ESignatureController(self.config, self.auth_managers)

    @lazy_property
    def leads(self):
        return LeadsController(self.config, self.auth_managers)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION, x_api_key='TODO: Replace',
                 config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         x_api_key=x_api_key)
        else:
            self.config = config
        self.initialize_auth_managers(self.config)

    def initialize_auth_managers(self, config):
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = CustomHeaderAuthentication(config.x_api_key)
        return self.auth_managers

#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from java.util import Collections
from java.nio.charset import StandardCharsets
from com.google.api.client.googleapis.auth.oauth2 import GoogleCredential
from com.google.api.client.googleapis.javanet import GoogleNetHttpTransport
from com.google.api.client.json.jackson2 import JacksonFactory
from com.google.api.services.androidpublisher import AndroidPublisher, AndroidPublisherScopes

from org.apache.commons.io import IOUtils

class AndroidPublisherHelper(object):
    # Global instance of the JSON factory.
    JSON_FACTORY = JacksonFactory.getDefaultInstance()
    HTTP_TRANSPORT = GoogleNetHttpTransport.newTrustedTransport()

    @staticmethod
    def create_client(application_name, service_account_json):
        credential = AndroidPublisherHelper.__authorize_with_service_account(service_account_json)

        # Set up and return API client.
        return AndroidPublisher.Builder(AndroidPublisherHelper.HTTP_TRANSPORT, AndroidPublisherHelper.JSON_FACTORY,
                                        credential).setApplicationName(application_name).build()

    @staticmethod
    def __authorize_with_service_account(service_account_json):
        credential = GoogleCredential.fromStream(IOUtils.toInputStream(service_account_json, StandardCharsets.UTF_8)).createScoped(Collections.singleton(AndroidPublisherScopes.ANDROIDPUBLISHER))
        return credential

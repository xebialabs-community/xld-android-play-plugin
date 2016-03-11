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
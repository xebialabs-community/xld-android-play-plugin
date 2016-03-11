#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.io import File

from com.google.api.client.http import FileContent
from com.google.api.client.repackaged.com.google.common.base import Preconditions, Strings
from com.google.api.services.androidpublisher.model import Track
from androidplay.AndroidPublisherHelper import AndroidPublisherHelper

import sys

class AndroidPublisherClient(object):

    MIME_TYPE_APK = "application/vnd.android.package-archive"

    def __init__(self, service_account_json):
        self._service_account_json = service_account_json

    @staticmethod
    def create_client(service_account_json):
        return AndroidPublisherClient(service_account_json)

    def upload_apk(self, package_name, application_name, apk_path, track):
        try:
            Preconditions.checkArgument( not Strings.isNullOrEmpty(package_name), "PACKAGE_NAME cannot be null or empty!")

            # Create the API service.
            service = AndroidPublisherHelper.create_client(application_name, self._service_account_json)
            edits = service.edits()

            # Create a new edit to make changes to your listing.
            edit_request = edits.insert(package_name, None)
            edit = edit_request.execute()
            edit_id = edit.getId()
            print "Created edit with id: [%s]" % edit_id

            # Upload new apk to developer console
            apk_file = FileContent(self.MIME_TYPE_APK, File(apk_path))
            upload_request = edits.apks().upload(package_name,edit_id,apk_file)
            apk = upload_request.execute()
            print "Version code [%s] has been uploaded" % apk.getVersionCode()

            # Assign apk to alpha track.
            apk_version_codes = [apk.getVersionCode()]
            update_track_request = edits.tracks().update(package_name, edit_id,track,Track().setVersionCodes(apk_version_codes))
            updated_track = update_track_request.execute()
            print "Track [%s] has been updated." % updated_track.getTrack()

            # Commit changes for edit.
            commit_request = edits.commit(package_name, edit_id)
            app_edit = commit_request.execute()
            print "App edit with id [%s] has been comitted" % app_edit.getId()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def create_application(self, application_name):
        try:
            Preconditions.checkArgument( not Strings.isNullOrEmpty(application_name), "Application name cannot be null or empty!")
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
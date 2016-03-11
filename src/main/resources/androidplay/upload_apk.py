#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from androidplay.AndroidPublisherClient import AndroidPublisherClient

client = AndroidPublisherClient.create_client(deployed.container.serviceAccountJson)
client.upload_apk(deployed.packageName, deployed.applicationName, deployed.file.path, deployed.track)

from androidplay.AndroidPublisherClient import AndroidPublisherClient

client = AndroidPublisherClient.create_client(deployed.container.serviceAccountJson)
client.upload_apk(deployed.packageName, deployed.applicationName, deployed.file.path, deployed.track)

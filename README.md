# Preface #

[![Build Status](https://travis-ci.org/xebialabs-community/xld-android-play-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xld-android-play-plugin)

This document describes the functionality provided by the XLD Android Play plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The Android Play plugin is a XL Deploy plugin that adds capability for deploying mobile applications to the Android Play Store.

# Requirements #

* **Requirements**
	* **XL Deploy** 5.1.0+

# Installation #

Place the plugin xldp file into your `SERVER_HOME/plugins` directory.

# Supported vs Not Supported #

* Uploading apk files is supported, including different tracks.
* Undeploying apk files is not supported.
* Optional signing of the apk file is not supported.
* Creating listings isn't supported yet.
* Creation of an application name and package name isn't supported. You'll have to use the developer console for this.

# Usage #

1. Go to `Repository - Infrastructure`, create a new `play.Store`. You'll need to enter the json string received when creating a Service Account:
   [Create a Service Account](https://developers.google.com/android-publisher/getting_started#setting_up_api_access_clients)
2. Create an environment under `Repository - Environments` and add the created `play.Store` to the environment. 
3. Create an application with a `play.Apk` as deployable.
4. Start deploying

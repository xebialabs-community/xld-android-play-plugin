# XL Deploy Android Play plugin

[![Build Status][xld-android-play-plugin-travis-image]][xld-android-play-plugin-travis-url]
[![License: MIT][xld-android-play-plugin-license-image]][xld-android-play-plugin-license-url]
![Github All Releases][xld-android-play-plugin-downloads-image]

[xld-android-play-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-android-play-plugin.svg?branch=master
[xld-android-play-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-android-play-plugin
[xld-android-play-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-android-play-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-android-play-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-android-play-plugin/total.svg


## Preface

This document describes the functionality provided by the XLD Android Play plugin.

See the [XL Deploy reference manual](https://docs.xebialabs.com/xl-deploy) for background information on XL Deploy and deployment automation concepts.  

## Overview

The Android Play plugin is a XL Deploy plugin that adds capability for deploying mobile applications to the Android Play Store.

## Requirements

* **Requirements**
	* **XL Deploy** 5.5+

## Installation #

* Copy the latest XLDP file from the [releases page](https://github.com/xebialabs-community/xld-android-play-plugin/releases) into the `XL_DEPLOY_SERVER/plugins` directory.
* Restart the XL Deploy server.

## Supported vs Not Supported #

* Uploading apk files is supported, including different tracks.
* Undeploying apk files is not supported.
* Optional signing of the apk file is not supported.
* Creating listings isn't supported yet.
* Creation of an application name and package name isn't supported. You'll have to use the developer console for this.

## Usage

1. Go to `Repository - Infrastructure`, create a new `play.Store`. You'll need to enter the json string received when creating a Service Account:
   [Create a Service Account](https://developers.google.com/android-publisher/getting_started#setting_up_api_access_clients)
2. Create an environment under `Repository - Environments` and add the created `play.Store` to the environment. 
3. Create an application with a `play.Apk` as deployable.
4. Start deploying

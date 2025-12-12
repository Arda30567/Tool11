[app]

# Title of your application
title = Python Toolbox

# Package name
package.name = pythontoolbox

# Package domain (needed for android/ios packaging)
package.domain = com.pythontoolbox

# Source code where the main.py live
source.dir = ../src

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Application versioning
version = 2.0.0

# Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,Pillow==10.0.0,qrcode==7.4.2,requests==2.31.0,speedtest-cli==2.1.3

# Supported orientation
orientation = portrait

# Android specific

# Presplash background color
android.presplash_color = #FFFFFF

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Target Android API
android.api = 33

# Minimum API
android.minapi = 21

# Android SDK
android.sdk = 33

# Android NDK
android.ndk = 25b

# Android NDK API
android.ndk_api = 21

# Private storage
android.private_storage = True

# Application should be fullscreen?
fullscreen = 0

# Android logcat filters
android.logcat_filters = *:S python:D

# Android archs
android.archs = arm64-v8a,armeabi-v7a

# Build mode (0 = debug, 1 = release)
android.build_mode = 0

# The package name of the android app
android.package = com.pythontoolbox.app

# Python for android fork
p4a.fork = kivy/python-for-android

# Python for android branch
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section] key=value or [section] key=value1,value2
#
#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#    [app@demo]
#    title = My Application (demo)
#
#    [app:source.exclude_patterns@demo]
#    images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#    buildozer --profile demo android debug
[app]
title = Health Record
package.name = healthrecord
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 34.0.0
android.arch = arm64-v8a
p4a.source_dir =
p4a.bootstrap = sdl2
p4a.extra_args = --add-source=org.kivy.android
# Permissions - add camera for photos
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
# Launch mode
android.launch_mode = singleTask

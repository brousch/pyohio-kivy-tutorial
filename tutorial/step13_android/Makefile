# Project settings
PY := python
WD := /home/kivy/pyohio-kivy-tutorial
PROJECT_DIR := $(WD)/tutorial/step13_android

# Python for Android settings
PY4A := /home/kivy/python-for-android
PY4A_PACKAGE := $(PY4A)/dist/default
PY4A_MODULES := "kivy"

# Android settings
APK_PACKAGE := com.example.pkt
APP_NAME := "PyOhio Kivy Tutorial"
APK_NAME := PyOhioKivyTutorial
APK_VERSION := 0.1
APK_ORIENTATION := sensor
APK_ICON := $(PROJECT_DIR)/resources/icon.png
APK_PRESPLASH := $(PROJECT_DIR)/resources/presplash.jpg
APK_DEBUG := $(PY4A_PACKAGE)/bin/$(APK_NAME)-$(APK_VERSION)-debug.apk

# Run
.PHONY: run
run:
	cd $(PROJECT_DIR); \
	$(PY) main.py

.PHONY: inspect
inspect:
	cd $(PROJECT_DIR); \
	$(PY) main.py -m inspector

.PHONY: monitor
monitor:
	cd $(PROJECT_DIR); \
	$(PY) main.py -m monitor

# Initialize python-for-android
.PHONY: create_python_for_android_distribution
create_python_for_android_distribution:
	rm -rf $(PY4A)/dist
	cd $(PY4A); \
	./distribute.sh -m $(PY4A_MODULES)

# Android commands
.PHONY: package_android
package_android:
	cd $(PY4A_PACKAGE); \
	$(PY) ./build.py --package $(APK_PACKAGE) --name $(APP_NAME) --version $(APK_VERSION) --orientation $(APK_ORIENTATION) --icon $(APK_ICON) --presplash $(APK_PRESPLASH) --dir $(PROJECT_DIR) debug
	mkdir -p $(WD)/binaries
	cp $(APK_DEBUG) $(WD)/binaries/

# Upload and install runables
.PHONY: install_android
install_android:
	adb install -r $(APK_DEBUG)


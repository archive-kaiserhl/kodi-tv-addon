NAME := kodi-tv-addon
PLUGIN_NAME := plugin.video.${NAME}

.PHONY: package
package:
	zip -r ${PLUGIN_NAME}.zip src

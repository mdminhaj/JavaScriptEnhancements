import platform
import os

NODE_JS_VERSION = "v6.10.1"
NODE_JS_BINARIES_FOLDER_NAME = "node_binaries"
NODE_JS_VERSION_URL_LIST_ONLINE = "https://nodejs.org/dist/index.json"
NODE_JS_BINARIES_FOLDER = os.path.join(PACKAGE_PATH, NODE_JS_BINARIES_FOLDER_NAME)
NODE_JS_OS = os_switcher.get(sublime.platform())
NODE_JS_BINARIES_FOLDER_PLATFORM = os.path.join(NODE_JS_BINARIES_FOLDER, NODE_JS_OS + "-" + PLATFORM_ARCHITECTURE)
NODE_JS_ARCHITECTURE = "x64" if PLATFORM_ARCHITECTURE == "64bit" else "x86"
NODE_JS_BINARY_NAME = "node" if NODE_JS_OS != 'win' else "node.exe"

NODE_MODULES_FOLDER_NAME = "node_modules"
NODE_MODULES_PATH = os.path.join(PACKAGE_PATH, NODE_MODULES_FOLDER_NAME)
NODE_MODULES_BIN_PATH = os.path.join(NODE_MODULES_PATH, ".bin")

NODE_JS_PATH_EXECUTABLE = os.path.join(NODE_JS_BINARIES_FOLDER_PLATFORM, "bin", NODE_JS_BINARY_NAME) if NODE_JS_OS != 'win' else os.path.join(NODE_JS_BINARIES_FOLDER_PLATFORM, NODE_JS_BINARY_NAME)

NPM_NAME = "npm" if NODE_JS_OS != 'win' else "npm.cmd"
NPM_PATH_EXECUTABLE = os.path.join(NODE_JS_BINARIES_FOLDER_PLATFORM, "bin", NPM_NAME) if NODE_JS_OS != 'win' else os.path.join(NODE_JS_BINARIES_FOLDER_PLATFORM, NPM_NAME)

YARN_NAME = "yarn" if NODE_JS_OS != 'win' else "yarn.cmd"
YARN_PATH_EXECUTABLE = os.path.join(NODE_MODULES_BIN_PATH, YARN_NAME)


from logHandler import log
import globalPluginHandler
import addonHandler
import ui
import win32clipboard
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_clearClipboard(self, gesture):
		_("""Clear your clipboard content.""")
		try:
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.CloseClipboard()
			ui.message(_("Clipboard cleared."))
			log.info("Clipboard cleared")
			return None
		except Exception as Error:
			log.error("Cannot clear clipboard")
			ui.message(_("Clipboard clear failed."))
			return None
	__gestures = {
		"kb:Alt+Delete": "clearClipboard"
	}
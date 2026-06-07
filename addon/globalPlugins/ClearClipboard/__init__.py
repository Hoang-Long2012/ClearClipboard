from logHandler import log
import globalPluginHandler
import addonHandler
import ui
import ctypes
addonHandler.initTranslation()
User32 = ctypes.windll.user32
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_clearClipboard(self, gesture):
		_("""Clear your clipboard content.""")
		try:
			User32.OpenClipboard(0)
			User32.EmptyClipboard()
			ui.message(_("Clipboard cleared."))
			log.info("Clipboard cleared")
		except Exception as Error:
			log.exception(f"Cannot clear clipboard\n{str(Error)}")
			ui.message(_("Clipboard clear failed."))
		finally:
			try:
				User32.CloseClipboard()
				return None
			except Exception:
				return None
	__gestures = {
		"kb:Alt+Delete": "clearClipboard"
	}
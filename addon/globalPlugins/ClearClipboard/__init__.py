from logHandler import log
from scriptHandler import script
import globalPluginHandler
import addonHandler
import ui
import ctypes
addonHandler.initTranslation()
User32 = ctypes.windll.user32
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Clear clipboard")
	@script(description=_("Clear your clipboard content."), category=scriptCategory)
	def script_clearClipboard(self, gesture):
		Opened = False
		try:
			if not User32.OpenClipboard(0):
				raise ctypes.WinError()
			Opened = True
			if not User32.EmptyClipboard():
				raise ctypes.WinError()
			ui.message(_("Clipboard cleared."))
			log.info("Clipboard cleared")
		except Exception:
			log.exception("Cannot clear clipboard")
			ui.message(_("Clipboard clear failed."))
		finally:
			if Opened:
				try:
					User32.CloseClipboard()
				except Exception:
					pass
	__gestures = {
		"kb:Alt+Delete": "clearClipboard"
	}
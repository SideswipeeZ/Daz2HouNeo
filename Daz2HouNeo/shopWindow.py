import os, base64, hou, re
from Qt import QtCore, QtWidgets, QtCompat, QtGui
from Qt.QtWidgets import QFileDialog
from PIL import Image
sessID = ''
#Global Vars
txDirList = []
shopList = []
shopPaths = []
##Labels
label_shop = ["Name","Connected Input","Filename","Connected Node" ]
label_tx = ["Preview","FileName","Path"]

#Table Vars
shaderSel = -1
rootP = ""
class shopWindow(QtWidgets.QMainWindow):
	def __init__(self, rootPath, sessID,parent=None):
		super(shopWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
		global sessID1, rootP
		sessID1 = sessID
		rootP = rootPath

		gwUi = os.path.join(rootPath + "\Assets\shopWindow.ui")
		self.mw = QtCompat.loadUi(gwUi)
		self.setCentralWidget(self.mw)
		self.setWindowTitle("Shader - Menu")

		self.changeIndex(0)

		########################################
		#                 PIXMAP               #
		########################################
		#Header Image Main (Base64) 'data:image/png;base64,'
		header64M = "iVBORw0KGgoAAAANSUhEUgAAAWkAAAA9CAQAAADFGlCQAAAACXBIWXMAAAsTAAALEwEAmpwYAAAK+2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIiB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA5LTA2VDE3OjU5OjM0KzAxOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIwLTA5LTA3VDEzOjM5OjQ5KzAxOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wOS0wN1QxMzozOTo0OSswMTowMCIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMSIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NjhiZjMzOGMtZGJmNi0yNjQzLTlhM2UtOWZmOTM2NmVjNDdiIiB4bXBNTTpEb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6MTNkYmJkYmUtZmM4Yi0yNDQwLWIyODMtNTcwZDE2Y2ZiNjU5IiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NTA0Y2RmMjAtNTQ1NS1jOTRiLTliZDItMmJmNTg0Y2Q0NmUxIiB0aWZmOk9yaWVudGF0aW9uPSIxIiB0aWZmOlhSZXNvbHV0aW9uPSI3MjAwMDAvMTAwMDAiIHRpZmY6WVJlc29sdXRpb249IjcyMDAwMC8xMDAwMCIgdGlmZjpSZXNvbHV0aW9uVW5pdD0iMiIgZXhpZjpDb2xvclNwYWNlPSI2NTUzNSIgZXhpZjpQaXhlbFhEaW1lbnNpb249IjM2MSIgZXhpZjpQaXhlbFlEaW1lbnNpb249IjYxIj4gPHBob3Rvc2hvcDpUZXh0TGF5ZXJzPiA8cmRmOkJhZz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJOYW1lPSJTSEFERVIiIHBob3Rvc2hvcDpMYXllclRleHQ9IlNIQURFUiIvPiA8L3JkZjpCYWc+IDwvcGhvdG9zaG9wOlRleHRMYXllcnM+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NTA0Y2RmMjAtNTQ1NS1jOTRiLTliZDItMmJmNTg0Y2Q0NmUxIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTA2VDE3OjU5OjM0KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjA4MjNhYWFjLTAyNTMtYTA0ZS04OGI3LWJhYjVhZGMyNmE5NiIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0wNlQyMzo0MzowMyswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo2YjcyZGY2OC01ZGE2LTkyNDItYTQ2Zi1lODM2YzU2M2Q5MTgiIHN0RXZ0OndoZW49IjIwMjAtMDktMDdUMTM6Mzk6NDkrMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY29udmVydGVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJmcm9tIGFwcGxpY2F0aW9uL3ZuZC5hZG9iZS5waG90b3Nob3AgdG8gaW1hZ2UvcG5nIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJkZXJpdmVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJjb252ZXJ0ZWQgZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NjhiZjMzOGMtZGJmNi0yNjQzLTlhM2UtOWZmOTM2NmVjNDdiIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTA3VDEzOjM5OjQ5KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjZiNzJkZjY4LTVkYTYtOTI0Mi1hNDZmLWU4MzZjNTYzZDkxOCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo1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"
		header_dataM = base64.b64decode(header64M)
		header_pixmapM = QtGui.QPixmap()
		header_pixmapM.loadFromData(header_dataM)
		#Assign to Label
		self.mw.lbl_header_main.setPixmap(header_pixmapM)

		#Init Console Label
		self.mw.lbl_console.setText("...")

		########################################
		#              Button                  #
		########################################
		# Arnold Button
		ar64 = 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGymlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA5LTIxVDE4OjAzOjUwKzAxOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIwLTA5LTIxVDE4OjA0OjU4KzAxOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wOS0yMVQxODowNDo1OCswMTowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2YjRlYjA0YS0wOGQ5LWY0NGItYWY2OS1lM2JlOGQ3NTNhY2MiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDpmYWZmYjlhMC1mNTdhLTA2NDMtYmE0Zi1kYmM5NGRjMWVjYjEiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDoyYzg4ZDJlZi1mMmMxLWQ0NGYtYTJjNC03MDA5ZTJiMzE1M2UiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiBwaG90b3Nob3A6SUNDUHJvZmlsZT0ic1JHQiBJRUM2MTk2Ni0yLjEiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjJjODhkMmVmLWYyYzEtZDQ0Zi1hMmM0LTcwMDllMmIzMTUzZSIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0yMVQxODowMzo1MCswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo2MTBhZGRiMy1mZDI1LTgyNGUtOTAwYy02YmE2Y2I3Njc4NTIiIHN0RXZ0OndoZW49IjIwMjAtMDktMjFUMTg6MDM6NTArMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NmI0ZWIwNGEtMDhkOS1mNDRiLWFmNjktZTNiZThkNzUzYWNjIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTIxVDE4OjA0OjU4KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+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'
		ar64_Data = base64.b64decode(ar64)
		arPixmap = QtGui.QPixmap()
		arPixmap.loadFromData(ar64_Data)
		self.mw.bttn_Arnold.setIcon(arPixmap)
		self.mw.bttn_Arnold.setIconSize(QtCore.QSize(32,32))
		self.mw.bttn_Arnold.clicked.connect(lambda: self.changeIndex(1))

		#######

		self.mw.bttn_1.setIcon(arPixmap)
		self.mw.bttn_1.setIconSize(QtCore.QSize(32,32))
		self.mw.bttn_1.clicked.connect(self.conMat)

		self.mw.bttn_2.setIcon(arPixmap)
		self.mw.bttn_2.setIconSize(QtCore.QSize(32,32))
		self.mw.bttn_2.clicked.connect(self.createOccluWireframe)

		self.mw.bttn_3.setIcon(arPixmap)
		self.mw.bttn_3.setIconSize(QtCore.QSize(32,32))
		self.mw.bttn_3.clicked.connect(self.createArnoldHair)

		self.mw.bttn_4.setIcon(arPixmap)
		self.mw.bttn_4.setIconSize(QtCore.QSize(32,32))
		self.mw.bttn_4.clicked.connect(self.createArnoldSkin)

		# Button for Texture Map Assignment Menu
		self.mw.bttn_texAssignArnold.clicked.connect(lambda: self.changeIndex(2))


		############################# TABLE BUTTONS #################################
		### Select Arnold Shader Button
		self.mw.bttn_select_shader.clicked.connect(self.loadShaderNodes)
		# Select Texture Directory Button
		self.mw.bttn_select_txdir.clicked.connect(self.loadTxDir)
		##Reset Buttons
		self.mw.bttn_reset_shadersel.clicked.connect(self.loadShaderTable)
		self.mw.bttn_reset_txDir.clicked.connect(self.loadTxTable)
		##Disable Buttons for clarity
		self.mw.bttn_reset_shadersel.setDisabled(True)
		self.mw.bttn_reset_txDir.setDisabled(True)
		## Clear Fields Button
		self.mw.bttn_clearfields.clicked.connect(self.clearFields)

		##Table Events
		self.mw.table_shader.clicked.connect(self.shopTableSel)
		self.mw.table_texture.doubleClicked.connect(self.txTableSel)






		#Back to Menu Button
		## Back Button Base64
		back64 = 'iVBORw0KGgoAAAANSUhEUgAAAWkAAAA9CAYAAABvE5gbAAAACXBIWXMAAAsTAAALEwEAmpwYAAAHTmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA5LTA2VDAwOjA2OjAzKzAxOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIwLTA5LTA2VDIzOjI2OjQ4KzAxOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wOS0wNlQyMzoyNjo0OCswMTowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpiNzcxNDM0NS0yNWU2LWE2NGMtYWYyYi1iMmQ2YTBmNjEyZmEiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDoxYjdiNmY4YS04ZTUzLThiNDUtODJhZC1iMzJhMzEyYzQ3MzkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpmYjI1ZmI0NC1iN2U3LTUzNDItOTJlNy02ZTcyZjI2ODQ3YWEiIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmZiMjVmYjQ0LWI3ZTctNTM0Mi05MmU3LTZlNzJmMjY4NDdhYSIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0wNlQwMDowNjowMyswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDplMDQ4YzdhMS01NTExLTU0NGItYWMzOS0wNzgyNGVkNWU0NmIiIHN0RXZ0OndoZW49IjIwMjAtMDktMDZUMDA6MDY6MDMrMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Yjc3MTQzNDUtMjVlNi1hNjRjLWFmMmItYjJkNmEwZjYxMmZhIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTA2VDIzOjI2OjQ4KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDxwaG90b3Nob3A6VGV4dExheWVycz4gPHJkZjpCYWc+IDxyZGY6bGkgcGhvdG9zaG9wOkxheWVyTmFtZT0i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'
		back64_Data = base64.b64decode(back64)
		backPixmap = QtGui.QPixmap()
		backPixmap.loadFromData(back64_Data)
		##
		self.mw.bttn_backfooter.setIcon(backPixmap)
		self.mw.bttn_backfooter.setIconSize(QtCore.QSize(361,61 ))
		self.mw.bttn_backfooter.clicked.connect(lambda: self.changeIndex(0))


		#Show Form
		self.show()


	#########################################
	#                 Functions             #
	#########################################

	## CONSOLE UPDATER
	def consoleOut(self,message):
		#Set Console Message
		self.mw.lbl_console.setText(message)

	## Change Index of Stacked Widget
	def changeIndex(self,indx):
		self.consoleOut("...")
		self.mw.stackedWidget.setCurrentIndex(indx)
		if indx == 0:
			self.resize(361,520)
		elif indx == 2:
			self.resize(720,720)

	## Handle Material Convertion
	def conMat(self):
		try:
			nodeToSend = hou.selectedNodes()[0]
			#print(nodeToSend.type())
		except IndexError:
			self.consoleOut('MAT_ERROR: Select a Valid Node!')
		#Check if Node is selected before continuing.
		if nodeToSend:
			if nodeToSend.type().name() == 'material':
				self.convertToArnold(nodeToSend)
			elif nodeToSend.type().name() == 'geo':
				# If type is Geo Loop all material nodes if found.
				mat_nodes = [node for node in nodeToSend.children() if node.type().name() == 'material']
				for each in mat_nodes:
					self.convertToArnold(each)
			elif nodeToSend.type().name() == 'subnet':
				## Find all geo nodes and then find all materials if exists obv
				geo_nodes = [node for node in nodeToSend.children() if node.type().name() == 'geo']
				for each in geo_nodes:
					mat_nodes = [node for node in each.children() if node.type().name() == 'material']
					for nodE in mat_nodes:
						self.convertToArnold(nodE)
			else: # else error as no node type is compatible
				self.consoleOut("ERROR Select a Material Node or its Nested Parent.")

	## Convert Material here ARNOLD. Called by other functions not directly from a button unless specific.
	def convertToArnold(self, node):
		SHOP = hou.node('/shop/')
		#Get Number of materials to create
		nMats = node.parm('num_materials').eval()
		# Create Boxnetwork
		netBox = SHOP.createNetworkBox()
		netBox.setComment('Daz2Hou NEO Arnold NetworkBox')
		#Loop for each material creating a new arnold one.
		for i in range(1,nMats+1):
			#Get Group Name of current loop.
			grp = "Ai_"+(node.parm('group'+str(i)).eval())
			#Check if Shader Exists
			if hou.node("/"+SHOP.name()+"/"+grp) is None:
				#Create Arnold VOP in Root location
				arnoldNode = SHOP.createNode('arnold_vopnet', run_init_scripts = True)
				arnoldNode.setName(grp,unique_name=True)
				arnoldNode.moveToGoodPosition()
				#Add Node to Network Box
				netBox.addItem(arnoldNode)
				#Create Shader inside
				#Create 'Smart' type indicator
				Mtype = 'Surface'
				if Mtype == 'Surface':
					surfNode = arnoldNode.createNode('arnold::standard_surface')
					#create image nodes for surface shading
					surfaceType = 1
					if surfaceType == 1:
						
						######################################################
						## Base Colour Node
						baseNode = arnoldNode.createNode('arnold::image')
						baseNode.setName('base')
						# Set Base Colour
						surfNode.setInput(1,baseNode)
						#Set Subsurface Colour
						surfNode.setInput(18,baseNode)
						baseNode.moveToGoodPosition()

						## Specular Colour Set
						specNode = arnoldNode.createNode('arnold::image')
						specNode.setName('specular')
						# Set Specular Input
						surfNode.setInput(4,specNode)
						# Set Sheen Input
						surfNode.setInput(33,specNode)
						specNode.moveToGoodPosition()

						## Sub-Surface Scatter
						sssNode = arnoldNode.createNode('arnold::image')
						sssNode.setName('sss')
						# Set SSS Input
						surfNode.setInput(17,sssNode)
						sssNode.moveToGoodPosition()

						##Normal Input
						NNode = arnoldNode.createNode('arnold::image')
						NNode.setName('normal')
						#Set Normal Input
						surfNode.setInput(39,NNode)
						NNode.moveToGoodPosition()
						######################################################

				elif Mtype == 'Hair':
					surfNode = arnoldNode.createNode('arnold::standard_hair')
				surfNode.moveToGoodPosition()
				outNode = hou.node(SHOP.name()+ "/" + arnoldNode.name()+"/"+"OUT_material")
				outNode.setInput(0,surfNode)
			#Assign Material to Material Group.
			node.parm("shop_materialpath"+str(i)).set("/"+SHOP.name()+"/"+grp)
		netBox.fitAroundContents()
		self.consoleOut('Converted to Arnold Materials')

	## Create Hair Shader Arnold
	def createArnoldHair(self):
		SHOP = hou.node('/shop/')
		#Create Arnold Node in SHOP var level
		arnoldNode = SHOP.createNode('arnold_vopnet', run_init_scripts = True)
		arnoldNode.setName("Ai_Hair_DZ",unique_name=True)
		arnoldNode.moveToGoodPosition()
		#Create Hair Node
		hairNode = arnoldNode.createNode('arnold::standard_hair')
		hairNode.moveToGoodPosition()
		#Out Node
		outNode = hou.node(SHOP.name()+ "/" + arnoldNode.name()+"/"+"OUT_material")
		outNode.setInput(0,hairNode)

	## Create Skin Shader
	def createArnoldSkin(self):
		SHOP = hou.node('/shop/')
		#Create Arnold Node in SHOP var level
		arnoldNode = SHOP.createNode('arnold_vopnet', run_init_scripts = True)
		arnoldNode.setName("Ai_Skin_DZ",unique_name=True)
		arnoldNode.moveToGoodPosition()	
		#Create Surface Node
		surfNode = arnoldNode.createNode('arnold::standard_surface')
		surfNode.moveToGoodPosition()
		#Out Node
		outNode = hou.node(SHOP.name()+ "/" + arnoldNode.name() + "/" + "OUT_material")
		outNode.setInput(0,surfNode)

		##Change surface node parameters
		# SSS Type=Diffusion, Radius=1,0.35,0.2, Scale=0.05
		surfNode.parm('subsurface_type').set('diffusion')
		surfNode.parm('subsurface').set(0.8)
		surfNode.parmTuple('subsurface_radius').set((1.0,0.35,0.2))
		surfNode.parm('subsurface_scale').set(0.05)
		###########################################################

	##Create Occlusion Wireframe Shader
	def createOccluWireframe(self):
		SHOP = hou.node('/shop/')
		#Create Arnold Node in SHOP var level
		arnoldNode = SHOP.createNode('arnold_vopnet', run_init_scripts = True)
		arnoldNode.setName("Ai_WireFrameOcclusion_DZ",unique_name=True)
		arnoldNode.moveToGoodPosition()	
		#Create Multiply Node
		multNode = arnoldNode.createNode('arnold::multiply')
		#Create Wireframe Node
		wireframeNode = arnoldNode.createNode('arnold::wireframe')
		#change Edge Type to Poly & Create a 
		wireframeNode.parm('edge_type').set('polygons')
		wireframeNode.parm('line_width').set(0.5)
		wireframeNode.moveToGoodPosition()
		#Create Ambient Occlusion Node
		occNode = arnoldNode.createNode('arnold::ambient_occlusion')
		occNode.moveToGoodPosition()
		#Connect Wire and Occlusion Nodes
		multNode.setInput(0,wireframeNode)
		multNode.setInput(1,occNode)
		multNode.moveToGoodPosition()
		#Out Node
		outNode = hou.node(SHOP.name()+ "/" + arnoldNode.name() + "/" + "OUT_material")
		outNode.setInput(0,multNode)
		outNode.moveToGoodPosition()

	## Table Functions.
	#Clear Fields in Texture Assign Page.
	def clearFields(self):
		self.consoleOut("...")
		self.mw.lbl_tx_shader.setText("Arnold Shadernet Nodes")
		self.mw.lbl_tx_dir.setText("Loaded: From Directory")
		#Button Disabled
		self.mw.bttn_reset_shadersel.setDisabled(True)
		self.mw.bttn_reset_txDir.setDisabled(True)
		#Clear Tables
		self.mw.table_texture.setRowCount(0)
		self.mw.table_texture.setColumnCount(0)
		self.mw.table_shader.setRowCount(0)
		self.mw.table_shader.setColumnCount(0)
		global txDirList, shopList, shopPaths, shaderSel
		txDirList = []
		shopList = []
		shopPaths = []
		shaderSel = -1

	#Load Shader Nodes
	def loadShaderNodes(self):
		#Get shaders inside valid shadernet (arnold atm)
		target_node = hou.selectedItems()[0]
		#Check if Node is Arnold Vopnet
		if target_node.type().name() == 'arnold_vopnet':
			#Get all Image Nodes inside if exist
			imgNodes = [node for node in target_node.children() if node.type().name() == 'arnold::image']
			#Check if more than one exists
			if len(imgNodes) > 0:
				#Print on label out
				self.mw.lbl_tx_shader.setText("Arnold Shadernet: " + target_node.name())
				#Create List for Tuples to be sent to Populate Table with
				global shopPaths
				shopPaths = []
				nodeToTableList = []
				#for each item inside the list, get parms and add to table.
				for node in imgNodes:
					#Get filename parameter and eval to see if it exists.
					global shopPaths, shaderSel, shopList
					#shopList = []
					#shaderSel = -1
					#shopPaths = []
					shopPaths.append(node.path())
					parameter = node.parm('filename').eval()
					#Get Name of Node
					nodeName = node.name()
					if len(parameter) <= 0:
						parameter = 'None'
					#Outputs of Node
					outs = node.outputConnectors()[0] # Get the RGBA output.
					if len(outs) <= 0:
						#outs = 'Not Connected'
						connectedNodeStr = "None"
					else:
						#Parse Connection.
						#Get Connected Node name from RGBA
						outStr = str(outs)
						splitOut = outStr.split(" ")
						# Get Node Name
						connectedNodeStr = splitOut[6]
						connectedNodeIndex = int(re.sub('\D', '', splitOut[8]))
						
						#Get Connections from Node inside Shader Node (Surface).
						conNode = hou.node(target_node.path() + '/' + connectedNodeStr)
						inputList = conNode.inputNames()
						#Create Dictionary for Values in Inputlist
						connection_Dict = {}
						keys = range(len(inputList))
						#Populate Dictionary
						for i in keys:
							connection_Dict[i] = inputList[i]
						
						# Get Data using get method of dict
						#print(connection_Dict)
						paramTarget = connection_Dict.get(connectedNodeIndex, 'Invalid')
							
					if not paramTarget:
						paramTarget = 'Invalid'
					if not connectedNodeStr:
						connectedNodeStr = 'None'
					if connectedNodeStr == 'None':
						paramTarget = "None"
					#Append Tuple to List.[name,targetparamter,fileParamter,nodeConnName]
					datatoappend = (nodeName,paramTarget,parameter,connectedNodeStr)
					nodeToTableList.append(datatoappend)
				#print(nodeToTableList)
				#Call Load Shader Table
				if len(nodeToTableList) > 0:
					global shopList
					shopList = nodeToTableList
					self.loadShaderTable()
				else:
					self.consoleOut("No Image Nodes Detected.")

	#Load Shaders Nodes in Table
	def loadShaderTable(self):
		#Init Table Widget
		self.mw.table_shader.setRowCount(0)
		self.mw.table_shader.setColumnCount(0)
		#Data should have a set number of items which contain tuples.
		#Images take 1 column to show. (Set it usually on first column)
		global shopList, label_shop
		data = shopList
		rvLabels = label_shop
		#Set Column Count
		self.mw.table_shader.setColumnCount(len(data[0]))
		#Set Header Labels
		for i in range(len(rvLabels)):
			itemA = QtWidgets.QTableWidgetItem(rvLabels[i])
			#itemA.setBackground(QtGui.QColor(255, 0, 0))
			self.mw.table_shader.setHorizontalHeaderItem(i,itemA)
		
		#print(len(data[0]))
		#print(data)
		#Populate Table
		for i in range(len(data)):
			rowPosition = self.mw.table_shader.rowCount()
			self.mw.table_shader.insertRow(rowPosition)
			#Populate Columns in Current Row
			#Create list from tuples
			toLst = data[i]
			counter = 0
			for each in toLst:
				self.mw.table_shader.setItem(rowPosition , counter, QtWidgets.QTableWidgetItem(each)) 
				counter = counter + 1
		#Lastly open button to reset.
		self.mw.bttn_reset_shadersel.setDisabled(False)

	# Load Texture Directory.
	def loadTxDir(self):
		try:
			txdirpath = str(QFileDialog.getExistingDirectory(self, "Select DAZ Texture Directory","C:\Users\Public\Documents\My DAZ 3D Library\Runtime\Textures"))
		except:
			txdirpath = str(QFileDialog.getExistingDirectory(self, "Select DAZ Texture Directory"))
		#print(txdirpath)
		#If path exists
		if txdirpath:
			self.mw.lbl_tx_dir.setText("Loaded: " + txdirpath )
			global txDirList
			txDirList = []
			#Get all Compatible Files inside
			valid_images = [".jpg",".png",".bmp"]
			for file in os.listdir(txdirpath):
				#print(file)
				ext = os.path.splitext(file)[1]
				name = os.path.splitext(file)[0]
				if ext.lower() in valid_images:
					#add item to list (filePath,Name)
					tup = ((os.path.join(txdirpath,file)),name)
					txDirList.append(tup)
			if txDirList:
				self.loadTxTable() # Load TX Table with data processed.
		else:
			self.consoleOut("NO Valid Texture Maps Found in Directory.")

	# Load Texture Data to Table
	def loadTxTable(self):
		global txDirList
		#print(txDirList)
		#Init Table Widget
		self.mw.table_texture.setRowCount(0)
		self.mw.table_texture.setColumnCount(0)
		#Set Column count to len of data set
		self.mw.table_texture.setColumnCount(len(txDirList[0])+1)#+1 for image preview.
		#Set column names.
		global label_tx
		headlabels = label_tx
		for i in range(len(headlabels)):
			itemA = QtWidgets.QTableWidgetItem(headlabels[i])
			self.mw.table_texture.setHorizontalHeaderItem(i,itemA)
		#Loop to populate table.
		for i in range(len(txDirList)):
			rowPosition = self.mw.table_texture.rowCount()
			self.mw.table_texture.insertRow(rowPosition)
			#Get Path and Name Vars
			pixpath, itemName = txDirList[i]
			
			#Create Pixmap for Preview
			#pixa = QtGui.QPixmap(pixpath)
			pixData = self.genThumbnail(pixpath)
			pixa = QtGui.QPixmap(pixData)
			#print(pixData)
			imgPreview = QtWidgets.QTableWidgetItem(pixa,"")
			self.mw.table_texture.setItem(rowPosition , 0, imgPreview)
			self.mw.table_texture.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(itemName))
			self.mw.table_texture.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(pixpath))
		#Activate Button.
		self.mw.bttn_reset_txDir.setDisabled(False)

	# Generate Thumbnail for Texture Table
	def genThumbnail(self,targetPath):
		imgLoad = Image.open(targetPath)
		sizeImg = 150
		imgLoad.thumbnail((sizeImg,sizeImg))
		global rootP
		tempDir = rootP + "\\temp\\thumbs"
		savename = tempDir + "\\" + "thumb.png"
		imgLoad.save(savename)
		return savename

	#Handle Shader Table Click Event
	def shopTableSel(self,indx):
		global shaderSel
		row = indx.row()
		shaderSel = row

	#Handle Texture Table Double-Click Event
	def txTableSel(self,indx):
		global shopPaths, shaderSel, txDirList
		row = indx.row()
		target = shopPaths[shaderSel] #Target Image Node Path
		#print(target)
		texmap = txDirList[row][0]
		#Apply the Tex map to Target Node
		tarNode = hou.node(target)
		tarNode.parm('filename').set(texmap)
		#ReScan and Update Table.
		self.loadShaderNodes()


	###########################################################################

	## CLOSE EVENT OF WINDOW
	def closeEvent(self,event):
		print("Daz to Houdini NEO: closing Shader Window (shopWindow) "+ sessID1 + '.')
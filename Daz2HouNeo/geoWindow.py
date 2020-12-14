import os, base64, hou
from Qt import QtCore, QtWidgets, QtCompat, QtGui
from Qt.QtWidgets import QFileDialog
sessID1 = ''
class geoWindow(QtWidgets.QMainWindow):
	def __init__(self, rootPath, sessID,parent=None):
		super(geoWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)

		self.closed = QtCore.Signal(int)
		global sessID1
		sessID1 = sessID

		gwUi = os.path.join(rootPath + "\Assets\geoWindow.ui")
		self.mw = QtCompat.loadUi(gwUi)
		self.setCentralWidget(self.mw)
		self.setWindowTitle("Geometry - Menu")

		########################################
		#                 PIXMAP               #
		########################################
		#Header Image Main (Base64)
		header64M = "iVBORw0KGgoAAAANSUhEUgAAAWkAAAA9CAQAAADFGlCQAAAACXBIWXMAAAsTAAALEwEAmpwYAAAK/2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIiB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA5LTA2VDE3OjU5OjM0KzAxOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIwLTA5LTA2VDIzOjQzOjE4KzAxOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wOS0wNlQyMzo0MzoxOCswMTowMCIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMSIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ODliYmE4MTYtN2U3Ni1hMDQ3LWJjYzctNmFkNjczNzM1ODljIiB4bXBNTTpEb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6M2FlNWY3OWUtNGQ0ZC1jMTQ4LTlmZDctZGUxNDAzZDU0ZTIwIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NTA0Y2RmMjAtNTQ1NS1jOTRiLTliZDItMmJmNTg0Y2Q0NmUxIiB0aWZmOk9yaWVudGF0aW9uPSIxIiB0aWZmOlhSZXNvbHV0aW9uPSI3MjAwMDAvMTAwMDAiIHRpZmY6WVJlc29sdXRpb249IjcyMDAwMC8xMDAwMCIgdGlmZjpSZXNvbHV0aW9uVW5pdD0iMiIgZXhpZjpDb2xvclNwYWNlPSI2NTUzNSIgZXhpZjpQaXhlbFhEaW1lbnNpb249IjM2MSIgZXhpZjpQaXhlbFlEaW1lbnNpb249IjYxIj4gPHBob3Rvc2hvcDpUZXh0TGF5ZXJzPiA8cmRmOkJhZz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJOYW1lPSJHRU9NRVRSWSIgcGhvdG9zaG9wOkxheWVyVGV4dD0iR0VPTUVUUlkiLz4gPC9yZGY6QmFnPiA8L3Bob3Rvc2hvcDpUZXh0TGF5ZXJzPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjUwNGNkZjIwLTU0NTUtYzk0Yi05YmQyLTJiZjU4NGNkNDZlMSIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0wNlQxNzo1OTozNCswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDowODIzYWFhYy0wMjUzLWEwNGUtODhiNy1iYWI1YWRjMjZhOTYiIHN0RXZ0OndoZW49IjIwMjAtMDktMDZUMjM6NDM6MDMrMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6MWUzMmYwZTctNTI4OS1lNDRiLTkyYzYtYjEwMzEzZGRjYjBhIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTA2VDIzOjQzOjE4KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNvbnZlcnRlZCIgc3RFdnQ6cGFyYW1ldGVycz0iZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iZGVyaXZlZCIgc3RFdnQ6cGFyYW1ldGVycz0iY29udmVydGVkIGZyb20gYXBwbGljYXRpb24vdm5kLmFkb2JlLnBob3Rvc2hvcCB0byBpbWFnZS9wbmciLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjg5YmJhODE2LTdlNzYtYTA0Ny1iY2M3LTZhZDY3MzczNTg5YyIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0wNlQyMzo0MzoxOCswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4gPC94bXBNTTpIaXN0b3J5PiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoxZTMyZjBlNy01Mjg5LWU0NGItOTJjNi1iMTAzMTNkZGNiMGEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5k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"
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

		########################################
		#              MENU BUTTONS         
		########################################
		self.mw.bttn_1.clicked.connect(self.importFbx)

		self.mw.bttn_2.clicked.connect(self.subnetToGeo)

		self.mw.bttn_3.clicked.connect(lambda: self.changeIndex(1))

		self.mw.bttn_100.clicked.connect(lambda: self.setScale(1))
		self.mw.bttn_010.clicked.connect(lambda: self.setScale(0.1))
		self.mw.bttn_001.clicked.connect(lambda: self.setScale(0.01))

		self.mw.bttn_4.clicked.connect(lambda: self.changeIndex(2))

		## Back Button Base64
		back64 = 'iVBORw0KGgoAAAANSUhEUgAAAWkAAAA9CAYAAABvE5gbAAAACXBIWXMAAAsTAAALEwEAmpwYAAAHTmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIwLTA5LTA2VDAwOjA2OjAzKzAxOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDIwLTA5LTA2VDIzOjI2OjQ4KzAxOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wOS0wNlQyMzoyNjo0OCswMTowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpiNzcxNDM0NS0yNWU2LWE2NGMtYWYyYi1iMmQ2YTBmNjEyZmEiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDoxYjdiNmY4YS04ZTUzLThiNDUtODJhZC1iMzJhMzEyYzQ3MzkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpmYjI1ZmI0NC1iN2U3LTUzNDItOTJlNy02ZTcyZjI2ODQ3YWEiIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmZiMjVmYjQ0LWI3ZTctNTM0Mi05MmU3LTZlNzJmMjY4NDdhYSIgc3RFdnQ6d2hlbj0iMjAyMC0wOS0wNlQwMDowNjowMyswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDplMDQ4YzdhMS01NTExLTU0NGItYWMzOS0wNzgyNGVkNWU0NmIiIHN0RXZ0OndoZW49IjIwMjAtMDktMDZUMDA6MDY6MDMrMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Yjc3MTQzNDUtMjVlNi1hNjRjLWFmMmItYjJkNmEwZjYxMmZhIiBzdEV2dDp3aGVuPSIyMDIwLTA5LTA2VDIzOjI2OjQ4KzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDxwaG90b3Nob3A6VGV4dExheWVycz4gPHJkZjpCYWc+IDxyZGY6bGkgcGhvdG9zaG9wOkxheWVyTmFtZT0i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'
		back64_Data = base64.b64decode(back64)
		backPixmap = QtGui.QPixmap()
		backPixmap.loadFromData(back64_Data)
		##
		self.mw.bttn_backfooter.setIcon(backPixmap)
		self.mw.bttn_backfooter.setIconSize(QtCore.QSize(361,61 ))
		self.mw.bttn_backfooter.clicked.connect(lambda: self.changeIndex(0))

		########################################
		#              SUBNET PAGE
		########################################
		self.mw.bttn_PreviewSubnet.clicked.connect(self.previewSubnet)
		self.mw.bttn_clearList.clicked.connect(self.clearList)

		########################################
		#             Extra Page
		########################################
		self.mw.hairGeo1.clicked.connect(self.hairGroomGeo)
		self.mw.lockGeo1.clicked.connect(self.lockObjMergeNodes)
		self.mw.kinefx1.clicked.connect(self.kinefxSubnet)


		#Show Form at end.
		self.show()

	###########################################################################
	#########################################
	#                 Functions             #
	#########################################

	## CONSOLE UPDATER
	def consoleOut(self,message):
		#Out message to Console Label.
		self.mw.lbl_console.setText(message)

	## Change Stacked Widget Index
	def changeIndex(self,indx):
		self.consoleOut("...")
		self.mw.stackedWidget.setCurrentIndex(indx)

	#Clear List
	def clearList(self):
		#Clear List
		self.mw.lst_preview.clear()

	## FBX IMPORTER
	def importFbx(self):
		#Opens File Dialog
		self.consoleOut("Opening File Prompt...")
		options = QFileDialog.Options()
		#options |= QFileDialog.DontUseNativeDialog
		fbx_fileName, _ = QFileDialog.getOpenFileName(self,"Select FBX File.", "","Filmbox FBX (*fbx);;All Files (*)", options=options)

		if fbx_fileName:
			#Debug Line
			print(fbx_fileName)
			#Try importing FBX
			try:
				print("Importing FBX...")
				self.consoleOut("Importing FBX...")
				fbx = hou.hipFile.importFBX(fbx_fileName)
				print("Imported Complete.")
				self.consoleOut("Importing Complete.")
			except:
				print("ERROR_IMPORTING_FBX 001")
				self.consoleOut("ERROR_IMPORTING_FBX_001")

	## SCALE BUTTONS
	def setScale(self,value):
		node = hou.selectedNodes()[0]
		if node.type().name() == 'subnet':
			node.parm('scale').set(value)
			self.consoleOut("Subnet Scaling {0}".format(str(value)))
		elif node.type().name() == 'geo':
			node.parm('scale').set(value)
			self.consoleOut("GEO Scaling {0}".format(str(value)))             
		else:
			print("ERROR Please select a subnet or geo node.")
			self.consoleOut("ERROR Scaling, Select Subnet or GEO node first.")

	## PREVIEW SUBNET
	def previewSubnet(self):
		self.mw.lst_preview.clear()
		FBX = hou.selectedNodes()[0]
		if FBX.type().name() == "subnet":
			geometry_FBX = [node for node in FBX.children() if node.type().name() == 'geo']
			for geo in geometry_FBX:
				self.mw.lst_preview.addItem(geo.name())
		else:
			self.consoleOut("ERROR, No Subnet Selected.")
			print("ERROR, No Subnet Selected.")

	## Convert Subnet to GEO OBJ MERGE
	def subnetToGeo(self):
		FBX = hou.selectedNodes()[0]
		#Root Location
		OBJ = hou.node('/obj/')

		#If Node Exists
		if not FBX:
			#Error no node selected
			self.consoleOut('SUBNET CONVERT ERROR: Select Subnet Node First.')
		elif FBX.type().name() == "subnet":
			# Process FBX Subnet for GEO
			# Add Selection for Version
			#Version 1 (Original From Tool)
			self.consoleOut('SUBNET CONVERT: Ver 1 Selected.')
			self.subGeoVersion1(FBX,OBJ)
		else:
			self.consoleOut('SUBNET CONVERT ERROR: Select Subnet Node ONLY.')

	## Convert Geo Methods
	def subGeoVersion1(self,FBX,OBJ):
		# Create Geometry node to store FBX parts
		geometry = OBJ.createNode('geo', run_init_scripts = False)
		geometry.setName('GEO_{}'.format(FBX.name()),unique_name=True)
		geometry.moveToGoodPosition()
		# Get all parts inside FBX container
		geometry_FBX = [node for node in FBX.children() if node.type().name() == 'geo']

		# Create merge node for parts
		merge = geometry.createNode('merge')
		merge.setName('master_merge')

		#Create Null Object at the end
		oNull = geometry.createNode('null')
		oNull.setName('OUT_DAZ')
		#Link MergeOut to NullIn
		oNull.setInput(0, merge)

		####
		for geo in geometry_FBX:
			# Create Object Merge node
			objectMerge = geometry.createNode('object_merge')
			objectMerge.setName(geo.name())

			# Set path to FBX part object
			objectMerge.parm('objpath1').set(geo.path())
			objectMerge.parm('xformtype').set(1)

			## MATERIAL HANDLING
			matName = hou.node("obj/" + FBX.name() + "/" + geo.name() + "/" + geo.name() + "_material")
			if matName is not None:
				parentH = hou.node("obj/" + geometry.name())
				hou.copyNodesTo([matName], parentH)
				material = hou.node("obj/" + geometry.name() + "/" + geo.name() + "_material")

				############------------############
				#Call process to convert materials.
				#From Older Version Un-Implemented
				############------------############
			else:
				# Create Material node if none exist. No materials are added if none are detected.
				material = geometry.createNode('material')
				material.setName('MAT_{}'.format(geo.name()))

			# LINK NODES

			# Link Material to Object MergeName
			material.setNextInput(objectMerge)
			# Link part to Merge
			merge.setNextInput(material)

		# Set Null Node flags to Render
		oNull.setDisplayFlag(1)
		oNull.setRenderFlag(1)
		 # Layout geometry content in Network View 
		geometry.layoutChildren()

		####
		# Set Null Node flags to Render
		oNull.setDisplayFlag(1)
		oNull.setRenderFlag(1)

		# Layout geometry content in Network View
		geometry.layoutChildren()

	## Create Hair GEO (Groom with VDB Node)
	def hairGroomGeo(Self):
		node = hou.selectedNodes()[0]
		if node:
			OBJ = hou.node('/obj/')
			if node.type().name() == 'geo':

				#Create Geo in OBJ level.
				geometry = OBJ.createNode('geo', run_init_scripts = False)
				geometry.setName('Hair_GEO_{}'.format(node.name()),unique_name=True)
				geometry.moveToGoodPosition()

				#Obj Merge
				objectMerge = geometry.createNode('object_merge')
				objectMerge.setName(node.name())
				objectMerge.parm('objpath1').set(node.path())

				#Transform
				xform = geometry.createNode('xform')
				xform.setInput(0,objectMerge)

				#Delete
				delnode = geometry.createNode('delete')
				delnode.setInput(0,xform)

				#Null Out_Char
				nullChar = geometry.createNode('null')
				nullChar.setName('OUT_CHAR')
				nullChar.setInput(0,delnode)

				#AttrbPaint
				try:
					attribpaint = geometry.createNode('attribpaint')
					attribpaint.setInput(0,nullChar)
					#Set AttrbPaint Density parameter
					attribpaint.parm('attribname1').set('density')
				except:
					 paintNode = geometry.createNode('paint')
					 paintNode.setInput(0,nullChar)

				#Null Out_Density
				nullDen = geometry.createNode('null')
				nullDen.setName('OUT_DENSITY')
				nullDen.setInput(0,attribpaint)

				#VDB from Polygons
				vdbN = geometry.createNode('vdbfrompolygons')
				vdbN.setInput(0,attribpaint)

				#Null Out_VDB
				nullVDB = geometry.createNode('null')
				nullVDB.setInput(0,vdbN)
				nullVDB.setName('OUT_VDB')

				#Set Render Flags
				nullChar.setDisplayFlag(1)
				nullChar.setRenderFlag(1)

				#Layout Geo
				geometry.layoutChildren()
			else:
				self.consoleOut('GROOM GEO ERROR: Select a GEO node.')
		else:
			self.consoleOut('GROOM GEO ERROR: Select a Node First.')

	## Lock Geo OBJ MERGE
	def lockObjMergeNodes(self):
		nodeS = hou.selectedNodes()[0]
		obj_merges = [node for node in nodeS.children() if node.type().name() == 'object_merge']
		for each in obj_merges:
			each.setHardLocked(1)

	##Check Houdini Version for KineFx
	def kinefxnow(self):
		var1 = hou.applicationVersionString().split(".")
		floatvar = float(var1[0]+"."+var1[1])
		if floatvar >= 18.5:
			return True
		else:
			return False
		'''	
		if int(var1[0]) > 17:
			if int(var1[0]) == 18:
				if int(var1[1]) == 5:
					return True
				else:
					return False
			else:
				return True
		else:
			return False
		'''

	## KineFx from Subnet V1.
	def kinefxSubnet(self):
		#Check if KineFx is avilable.
		if self.kinefxnow() == True:
			#Get Selected Subnet.
			targetNode = hou.selectedNodes()[0]
			if targetNode.type().name() == 'subnet':
				OBJ = hou.node('/obj/')
				geonode = OBJ.createNode('geo', run_init_scripts = False)
				geonode.setName('Daz_kfx_subnet',unique_name=True)
				geonode.moveToGoodPosition()
				# Create Nodes
				kineType = 1
				if kineType == 1:
					#Scene Import Node.
					sceneimport = geonode.createNode('kinefx::scenecharacterimport')
					#Set subnet path param
					sceneimport.parm('objsubnet').set(targetNode.path())
					sceneimport.moveToGoodPosition()

					# FBX Animation Import
					fbxanimimport = geonode.createNode('kinefx::fbxanimimport')
					fbxanimimport.moveToGoodPosition()

					#Rig Match Pose
					rigmatchpose = geonode.createNode('kinefx::rigmatchpose')
					rigmatchpose.setInput(0,sceneimport,2)
					rigmatchpose.setInput(1,fbxanimimport,0)
					rigmatchpose.moveToGoodPosition()

					# Map Points
					mapppoints = geonode.createNode('kinefx::mappoints')
					mapppoints.setInput(0,rigmatchpose,0)
					mapppoints.setInput(1,rigmatchpose,1)
					mapppoints.moveToGoodPosition()

					# Full body ik
					fullikbody = geonode.createNode('kinefx::fullbodyik')
					fullikbody.setInput(0,mapppoints,0)
					fullikbody.setInput(1,mapppoints,1)
					fullikbody.moveToGoodPosition()

					#bone deform
					bonedeform = geonode.createNode('bonedeform')
					bonedeform.setInput(0,sceneimport,0)
					bonedeform.setInput(1,sceneimport,1)
					bonedeform.setInput(2,fullikbody,0)
					bonedeform.moveToGoodPosition()

					#Out Null
					outNull = geonode.createNode('null')
					outNull.setInput(0,bonedeform)
					outNull.moveToGoodPosition()
			else:
				self.consoleOut("ERROR: Please Select a Valid Subnet.")
		else:
			self.consoleOut("ERROR:KinefX Hou Version is Lower than 18.5.")

	###########################################################################

	## CLOSE EVENT OF WINDOW
	def closeEvent(self,event):
		print("Daz to Houdini NEO: closing Geometry Window (geoWindow) " + sessID1 + '.')
		#self.closed.emit(1)
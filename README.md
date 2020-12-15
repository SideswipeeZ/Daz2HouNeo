# Daz Studio to Houdini Processing Tools
![DazHouHeader](https://github.com/SideswipeeZ/Daz2HouNeo/blob/main/git/github_header.png)

## Overview
The **Daz2Houdini Neo** Processing Tool is made to help Import Daz3D FBX exports, into Houdini and to prepare shaders/rops/lights/animation. (As Of **VER:01.00**: Only Supports Arnold for Shaders and ROPs.)


# Contents
 [Installation](#installation)
 * [Node Shape Install](#install-the-node-shape-optional)

 [Requirements](#requirements)
* [Application Functions](#functions)

	* [Geometry Menu](#geometry)
	* [Shader Menu](#shader)
	* [Render Menu](#render)
	* [Debug Info](#debug)

[Showcase](#showcase)
	
[Licence](#licence)

## Requirements
VER:01.00 Modules:
*	[**Qt**](https://github.com/mottosso/Qt.py)
*	**PIL**

This Python Tool was written for use with Python 2.7 in Houdini however it should be Python 3 safe.
# Installation
Tested on Windows OS.
## Manual Install
Copy the Folder ***Daz2HouNeo*** to **/Documents/Houdini{Houdini_Version}/python2.7libs**. Please also place Qt Module here.
Change Path in **mainWindow.py** to the root of the ***Daz2HouNeo*** Folder.
In Houdini, Create a New Shelf Tool with the following code in the script section.
```
from Daz2HouNeo import mainWindow

mainWin = mainWindow.H2Dz()
mainWin.resize(361,520)
mainWin.show()
 ```
## Windows OS Easy Installer.
Use the Provided Program to allow the program to auto install the files to local system. Please Follow the instruction on the Program.
## Install the Node Shape. *(optional)*
Please Copy the ***Daz3DLogo.json*** file to **{HOUDINI_INSTALL_LOCATION}\houdini\config\NodeShapes** This is optional to get the Daz Logo nodeshape for easy location of networks create by the tool.
![NodeShapePreview](https://github.com/SideswipeeZ/Daz2HouNeo/blob/main/git/nodeshapes.PNG)
Preview of Nodeshapes in Houdini.

# Functions
**The majority of the tool works by first Selecting a Node from the Network View and then, Interacting with the UI Window.**

![DazUIWindow](https://github.com/SideswipeeZ/Daz2HouNeo/blob/main/git/mainmenuui.png)

The Main Menu Window 'floats' in a smaller version while a child window is spawned. To open the Main Menu Window again to its larger size, there is a Expand menu bar that is visible on mouse over. Please note that you can open all three working windows at once and that **Closing the Main menu will also close all child windows.**

All Child Windows are configured to be resizeable with minumum size contraints the only limiting factor.

## Geometry

*  **Import FBX** 
		* Import an FBX to Subnet into OBJ Level.
*  **Create GEO from Subnet**
		* Creates a new GEO Node into OBJ Level from the Subnet Selected.
		* **Node Structure:**
		*  - OBJ MERGE  (Per Geo Object in Subnet)
		* - MATERIAL SOP (Per Geo Object in Subnet)
		* - MERGE (Master Merge)
		* - NULL (OUTPUT_NULL)
*  **Scale Geometry/Subnet**
		*  **1.0** - Set Uniform Scale of SOP to this Value 
		* **0.1** - Set Uniform Scale of SOP to this Value 
		*  **0.01** - Set Uniform Scale of SOP to this Value 

* **Preview Subnet** *(Ui Change Occurs)*
		* Switches to another page on UI.
		*  Shows All geometry nodes inside of a Subnet selected.

*	**Experimental Tools** *(Ui Change Occurs)*
*	**Create Hair Groom Geo (VDB+Density)***
		*	Creates a New GEO Node in OBJ Level from Selected Geometry node.
		*	Node Creates a setup for hair with a VDB Output and Density Output that are to be configured by the artist.
	*	**Lock Obj Merge Nodes in GEO**
			*	 Sets the Lock flag on all OBJ Merge Nodes inside of a Selected GEO node if found.
	* **KineFx from Subnet***
		* Only Works in Houdini 18.5 and up, as KineFx was introduced in this release.
		* Creates a Network from Selected Subnet Node for Animation Re-target. (Requires Setup by Artist for full control.)

*(  * Asterisk Objects are Experimental)*

## Shader
* **Convert to Arnold Material**
	* Selectable Nodes Include: Subnet, Geometry, Material SOP.
	* Converts the Selected Node to check for materials SOPs inside and convert them to Arnold Materials in SHOP level.
* **Create Arnold Shaders**
	* Create Arnold **Wireframe/Occlusion** Material in SHOP.
	* Create Arnold **Hair** Material in SHOP.
	* Create Arnold **Skin** Material in SHOP.
	
* **Texture Map Menu** *(Ui Change Occurs)*
	* *This Is a Tool that allows the quick assignment to Image Node inside of an Arnold Shader.*
	* 
	* **Select Arnold Shader:**
		* The Selected Arnold Shader If contains an Image Node, Will load all found Image Nodes into the Table.
	* **Load Directory Textures:**
		* Prompts User to Locate Folder for Texture Maps. Supported Formats *[.jpg, .png, .bmp]*
		* Loads Texture Maps Details and Preview into Table.

	* **Usage:**
		*	Load a Shader with Image Nodes and Load Texture Directory.
		*	Double Click the Image Node from the Left Table.
		*	Double Click the Texture Map from the Right Table to Assign Map to Image Node.
		*	*NOTE: Paths are **NOT** relative as of VER:01.00*

##  Render
### Create Lights
*	**Create Arnold Lights Menu:** *(Ui Change Occurs)*
	*	Each Button Creates an Arnold Light at OBJ Level with a unqiue name based on the Light Type shown on the Button.
*	**Arnold Light Tool V2.1 [BETA]** *(Ui Change Occurs)*
	*	This is an Implementation of the Arnold Light Tool With Improvements to code.
	*	This Tool allows the selection of Multiple Arnold Light Objects and the ability to batch affect thier Values for Colour, Intensity, Exposure, AOV Light Group and Target Object. *(Features a Colour Preview.)*

### Create ROPs
* **Create Arnold ROP (Default)**
	* By Default, a Standard Arnold ROP will be created in OUT with a unique name to differentiate that it was made by this tool.

* **Advanced ROP** *(Ui Change Occurs)*
	* **AOV Groups**
		* These are Checkboxes that allow the addition of AOVs to a Selected Arnold ROP. *(Note: it will skip any AOVs that are already present on the ROP)*
		* **Create Arnold ROP with AOVs**: Creates a New ROP in OUT with a unique name and the selected AOVs from the checkboxes ticked.
		* **Apply AOVs to Selected Arnold ROP**: Create AOV Entries for the Selected Arnold ROP.

## #Debug
This Menu was used to Test various Items of Code and UI Elements, Not Intended to be Used outside of Development.

# Showcase

![ShowcaseImage](https://github.com/SideswipeeZ/Daz2HouNeo/blob/main/git/Compliation_Pei_4k.png)

# Licence
MIT

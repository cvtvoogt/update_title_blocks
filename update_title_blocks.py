import wx
import pcbnew

class UpdateTitleBlocksPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Update Title Blocks"
        self.category = "Update Title Blocks"
        self.description = "Simple Hello World plugin for KiCad 10 schematic"
        self.show_toolbar_button = True
        self.icon_file_name = "hello_icon.png"

    def Run(self):
        wx.MessageBox("Hello World from Update Title Blocks!", "Update Title Blocks")


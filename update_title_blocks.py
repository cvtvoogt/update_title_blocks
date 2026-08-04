import wx
import pcbnew

class HelloWorldPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Hello World"
        self.category = "Hello World"
        self.description = "Simple Hello World plugin for KiCad 10 schematic"
        self.show_toolbar_button = True
        self.icon_file_name = "update_title_blocks.png"

    def Run(self):
        wx.MessageBox("Hello World from KiCad 10 Schematic Plugin!", "Hello World")
